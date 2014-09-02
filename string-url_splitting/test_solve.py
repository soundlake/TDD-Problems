import unittest
from solve import url_parser

class test_url_parser(unittest.TestCase):
    def test_protocol_http(self):
        protocol = url_parser('http://some.thing').protocol
        self.assertEqual(protocol, 'http')

    def test_protocol_ftp(self):
        protocol = url_parser('ftp://a.large.site').protocol
        self.assertEqual(protocol, 'ftp')

    def test_domain_simple(self):
        domain = url_parser('ftp://a.large.site').domain
        self.assertEqual(domain, 'a.large.site')

    def test_domain_with_path(self):
        domain = url_parser('http://a.site.with/a-path').domain
        self.assertEqual(domain, 'a.site.with')

    def test_path_empty(self):
        path = url_parser('http://www.google.se').path
        self.assertEqual(path, '')

if __name__ == '__main__':
    unittest.main()
