class check_amount:
    def __init__(self, amount):
        self.raw = amount
        self.ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.decs = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    def str_cents(self):
        if self.cents: return '%02d/100 ' % round(self.cents * 100)
        else: return ''

    def str_dec(self):
        part = ''
        if self.one or self.dec:
            if self.dec == 1:
                part = self.tens[self.one] + ' '
            else:
                if self.dec > 1:
                    part = self.decs[self.dec]
                    if self.one:
                        part += '-'
                part += self.ones[self.one] + ' '
            if self.cents: part += 'and '
        return part

    def __str__(self):
        # simple ones
        if not self.raw:
            return 'Zero dollar'
        if self.raw == 0.01:
            return '01/100 dollar'
        if self.raw == 1:
            return 'One dollar'

        # complex
        result = 'dollars'
        result = self.str_cents() + result
        result = self.str_dec() + result

        return result.capitalize()

    @property
    def cents(self):
        return self.raw % 1.0
    @property
    def one(self):
        return int(self.raw) % 10
    @property
    def dec(self):
        return int(self.raw / 10) % 10
