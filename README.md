# ARIN WHOIS Webservice Client
A Python library for interacting with the ARIN WHOIS REST service.

## Installation
To install, simply run `pip install whoisrws`

## Usage
To perform a lookup, first create an instance of the webservice, then call one of the available methods:

```
from whoisrws import webservice
whois = webservice()
# Perform a Lookup for one of GitHub's IP Addresses
whois.ip('192.30.255.113')
>>> <dictionary>
```
