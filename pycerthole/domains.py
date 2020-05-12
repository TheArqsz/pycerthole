# -*- coding: utf-8 -*-

__author__ = 'Arqsz'

from datetime import datetime

class Domain:
    def __init__(self, raw_object=None, raw_type='json', domain_address=None, insert_date=None, delete_date=None):
        self.raw_object = raw_object
        self.raw_type = raw_type
        self.domain_address = domain_address
        self.insert_date = insert_date
        self.delete_date = delete_date
        self.is_blocked = False
        if raw_object:
            self._parse_raw_object()

    def __repr__(self):
        if self.is_blocked:
            return 'Domain(' + str({
                'domain_address': self.domain_address,
                'insert_date': self.insert_date,
                'delete_date': self.delete_date,
                'is_blocked': self.is_blocked
            }) + ')'
        else:
            return 'Domain(' + str({
                'domain_address': self.domain_address,
                'insert_date': self.insert_date,
                'is_blocked': self.is_blocked
            }) + ')'

    def _parse_raw_object(self):
        if self.raw_type == 'json':
            self.domain_address = self.raw_object.get('DomainAddress')
            self.insert_date = self._parse_date(
                self.raw_object.get('InsertDate')
            )
            self.delete_date = self._parse_date(
                self.raw_object.get('DeleteDate')
            )
            if self.delete_date:
                self.is_blocked = True
        elif self.raw_type == 'txt':
            self.domain_address = self.raw_object
        elif self.raw_type == 'csv':
            self.domain_address = self.raw_object[1]
            self.insert_date = self._parse_date(
                self.raw_object[2]
            )
            if len(self.raw_object) > 3:
                self.delete_date = self._parse_date(
                    self.raw_object[3]
                )
                self.is_blocked = True
        elif self.raw_type == 'xml':
            self.domain_address = self.raw_object.adresdomeny.next_element
            self.insert_date = self._parse_date(
                self.raw_object.datawpisu.next_element
            )

    def _parse_date(self, raw_date):
        if not raw_date:
            return None
        else:
            return datetime.strptime(
                raw_date,
                "%Y-%m-%dT%H:%M:%S"
            )