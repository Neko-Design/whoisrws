import requests
import logging
from murl import Url
from IPy import IP

class webservice():
    def __init__(self):
        self.webservice_hostname = 'whois.arin.net'
        self.webservice_protocol = 'http'
        self.webservice_path = '/rest'
        self.webservice_format = 'json'
        self.webservice_endpoints = [
            'orgs',
            'customers',
            'pocs',
            'asns',
            'nets',
            'rdns',
            'ip'
        ]

    def _make_api_call(self, api, resource, parameters, headers):
        if api not in self.webservice_endpoints:
            logging.error("Requested API '{}' is not Supported.".format(api))
            return false

        api_url        = Url('')
        api_url.host   = self.webservice_hostname
        api_url.scheme = self.webservice_protocol
        api_url.path   = "{}/{}/{}.{}".format(self.webservice_path, api, resource, self.webservice_format)
        
        response = requests.get(api_url.url)
        if response.status_code != 200:
            return False
        if self.webservice_format == 'json':
            return response.json()
        return response.text

    def ip(self, ip_address):
        try:
            IP(ip_address)
        except ValueError:
            logging.error('Requested IP Address {} is not Valid'.format(ip_address))
            return false
        return self._make_api_call('ip', ip_address, None, None)