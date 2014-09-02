import re

class url_parser:
    def __init__(self, url):
        substrings = re.split('://|/', url, 2)
        if len(substrings) < 3:
            substrings.append('')
        protocol, domain, path = substrings
        self.protocol = protocol
        self.domain = domain
        self.path = path
