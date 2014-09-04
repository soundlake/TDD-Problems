import re



class map_of_vars:
    dictionary = dict()

    @classmethod
    def put(cls, key, value):
        cls.dictionary[key] = value

    @classmethod
    def get(cls, key):
        return cls.dictionary[key]



class template_engine:
    pat_key = r'{\$(?P<key>.+)}'

    @classmethod
    def find_keys(cls, src):
        mo = re.search(cls.pat_key, 'Hello {$name}')
        print(mo.groups())
        return mo.group('key')

    @classmethod
    def evaluate(cls, src, mov):
        key = template_engine.find_keys(src)
        val = map_of_vars.get(key)
        return re.sub('{\$' + key + '}', val, src)
