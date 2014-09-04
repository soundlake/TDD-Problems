import re



class MissingValueError(Exception):
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return repr('There is no value with the key <' + self.value + '>')



class map_of_vars:
    dictionary = dict()

    @classmethod
    def init(cls):
        cls.dictionary = dict()

    @classmethod
    def put(cls, key, value):
        cls.dictionary[key] = value

    @classmethod
    def get(cls, key):
        if key in cls.dictionary: return cls.dictionary[key]
        else: raise MissingValueError(key)



class template_engine:
    pat_key = r'{\$(?P<key>.+?)}'

    @classmethod
    def find_keys(cls, src):
        keys = []
        for mo in re.finditer(cls.pat_key, src):
            keys.append(mo.group('key'))
        print(keys)
        return keys

    @classmethod
    def evaluate(cls, src, mov):
        keys = template_engine.find_keys(src)
        for key in keys:
            val = map_of_vars.get(key)
            src = re.sub('{\$' + key + '}', val, src)
        return src
