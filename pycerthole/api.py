# -*- coding: utf-8 -*-

__author__ = 'Arqsz'

import requests
import csv
import json
from io import StringIO

from bs4 import BeautifulSoup
from pycerthole.domains import Domain

class CertHoleException(Exception):
    def __init__(self, message='Basic CertHole exception'):
        self.message = message

class CertHoleTypeException(CertHoleException):
    def __init__(self, message='Type not supported'):
        self.message = message

class CertHoleConnectionException(CertHoleException):
    def __init__(self, message='Cannot connect to hole.cert'):
        self.message = message

class CertHole:
    
    def __init__(self, base_url="https://hole.cert.pl/domains", json_endpoint="domains.json", 
        txt_endpoint="domains.txt", csv_endpoint="domains.csv", xml_endpoint="domains.xml"):
        self.base_url = base_url
        self.json_endpoint = json_endpoint
        self.txt_endpoint = txt_endpoint
        self.csv_endpoint = csv_endpoint
        self.xml_endpoint = xml_endpoint
        self.accepted_types = ['json', 'txt', 'csv', 'xml']
    
    def get_data(self, default_type='json'):
        if default_type not in self.accepted_types:
            raise CertHoleTypeException

        raw_data = self.get_raw_data(default_type=default_type)
        return [Domain(raw_object=raw_object, raw_type=default_type) for raw_object in raw_data]

    def get_data_blocked(self, default_type='json'):
        if default_type not in self.accepted_types:
            raise CertHoleTypeException
        elif default_type in ['xml', 'txt']:
            raise CertHoleTypeException('Those types return only domains that are not blocked')

        raw_data = self.get_raw_data(default_type=default_type)
        l = list()
        temp = [Domain(raw_object=raw_object, raw_type=default_type) for raw_object in raw_data]
        for d in temp:
            if d.is_blocked:
                l.append(d)
                    
        return l


    def get_raw_data(self, default_type='json'):
        if default_type not in self.accepted_types:
            raise CertHoleTypeException
        
        url = "{}/{}".format(self.base_url, self._get_endpoint_by_type(default_type))
        r = requests.get(url)
        if r.status_code != 200:
            raise CertHoleConnectionException
        else:
            return self._get_content_by_type(default_type=default_type, response=r)

    def _get_endpoint_by_type(self, default_type='json'):
        if default_type == 'json':
            return self.json_endpoint
        elif default_type == 'csv':
            return self.csv_endpoint
        elif default_type == 'xml':
            return self.xml_endpoint
        elif default_type == 'txt':
            return self.txt_endpoint

    def _get_content_by_type(self, default_type='json', response=None):
        if not response:
            raise CertHoleException('Empty response')

        if default_type == 'json':
            return response.json()
        elif default_type == 'csv':
            i = StringIO(response.text)
            r = csv.reader(i, delimiter=',')
            # Skip header
            next(r)
            return [''.join(row).strip().split('\t') for row in r]
        elif default_type == 'xml':
            b = BeautifulSoup(response.text, "html.parser")
            return b.find_all('pozycjarejestru')
        elif default_type == 'txt':
            return response.text.split('\n')
