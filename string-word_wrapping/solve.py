class word_wrapper:
    def __init__(self, row_length):
        self.limit = row_length

    def wrapIt(self, src):
        if len(src) < self.limit: return src

        wrapped = []
        while len(src) > self.limit:
            src = src.strip()
            wrapped.append(src[:self.limit])
            src = src[self.limit:]
        if src: wrapped.append(src)
        return wrapped
