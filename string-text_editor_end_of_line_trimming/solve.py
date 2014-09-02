import re

def trimmer(src):
    src = re.sub('[ \t]+$', '', src)
    src = re.sub('\n +', '\n', src)
    return src
