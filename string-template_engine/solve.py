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
    pat_key = r'{\$(?P<key>.+?)}'
    keys = []

    @classmethod
    def find_keys(cls, src):
        for mo in re.finditer(cls.pat_key, src):
            cls.keys.append(mo.group('key'))
        print(cls.keys)

    @classmethod
    def evaluate(cls, src, mov):
        template_engine.find_keys(src)
        for key in cls.keys:
            val = map_of_vars.get(key)
            src = re.sub('{\$' + key + '}', val, src)
        return src
