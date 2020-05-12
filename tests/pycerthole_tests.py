# -*- coding: utf-8 -*-

__author__ = 'Arqsz'

import unittest

from pycerthole import CertHole, CertHoleConnectionException, CertHoleTypeException, Domain
from bs4.element import Tag

class TestCertHole(unittest.TestCase):

    def test_init(self):
        ch = CertHole()
        self.assertIsNotNone(ch)

    def test_wrong_url(self):
        ch = CertHole(base_url='http://hole.cert.pl/dommmmmains')
        self.assertRaises(CertHoleConnectionException, ch.get_raw_data)

    def test_get_domain_json(self):
        ch = CertHole()
        domains = ch.get_data(default_type='json')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNotNone(domains[0].insert_date)
        self.assertIn(domains[0].is_blocked, [True, False])

    def test_get_domain_csv(self):
        ch = CertHole()
        domains = ch.get_data(default_type='csv')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNotNone(domains[0].insert_date)
        self.assertIn(domains[0].is_blocked, [True, False])

    def test_get_domain_xml(self):
        ch = CertHole()
        domains = ch.get_data(default_type='xml')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNotNone(domains[0].insert_date)
        self.assertIsNone(domains[0].delete_date)

    def test_get_domain_txt(self):
        ch = CertHole()
        domains = ch.get_data(default_type='txt')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNone(domains[0].insert_date)
        self.assertIsNone(domains[0].delete_date)

    def test_get_domain_wrong_type(self):
        ch = CertHole()
        self.assertRaises(CertHoleTypeException, ch.get_data, 'rar')

    def test_get_domain_blocked_json(self):
        ch = CertHole()
        domains = ch.get_data_blocked(default_type='json')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNotNone(domains[0].insert_date)
        self.assertIsNotNone(domains[0].delete_date)

    def test_get_domain_blocked_csv(self):
        ch = CertHole()
        domains = ch.get_data_blocked(default_type='csv')
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Domain)
        self.assertIsNotNone(domains[0].domain_address)
        self.assertIsNotNone(domains[0].insert_date)
        self.assertIsNotNone(domains[0].delete_date)

    def test_get_domain_blocked_xml(self):
        ch = CertHole()
        self.assertRaises(CertHoleTypeException, ch.get_data_blocked, 'xml')

    def test_get_domain_blocked_txt(self):
        ch = CertHole()
        self.assertRaises(CertHoleTypeException, ch.get_data_blocked, 'txt')

    def test_get_domain_raw_data_json(self):
        ch = CertHole()
        domains = ch.get_raw_data(default_type='json')
        self.assertIsInstance(domains, list)
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], dict)

    def test_get_domain_raw_data_csv(self):
        ch = CertHole()
        domains = ch.get_raw_data(default_type='csv')
        self.assertIsInstance(domains, list)
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], list)

    def test_get_domain_raw_data_txt(self):
        ch = CertHole()
        domains = ch.get_raw_data(default_type='txt')
        self.assertIsInstance(domains, list)
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], str)

    def test_get_domain_raw_data_xml(self):
        ch = CertHole()
        domains = ch.get_raw_data(default_type='xml')
        self.assertIsInstance(domains, list)
        self.assertGreater(len(domains), 0)
        self.assertIsInstance(domains[0], Tag)

    def test_get_domain_raw_data_wrong_type(self):
        ch = CertHole()
        self.assertRaises(CertHoleTypeException, ch.get_raw_data, 'rar')


if __name__ == '__main__':
    unittest.main()