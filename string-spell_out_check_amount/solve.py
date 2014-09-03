class check_amount:
    def __init__(self, amount):
        self.raw = amount
        self.ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    def __str__(self):
        if not self.raw:
            return 'Zero dollar'
        if self.raw == 0.01:
            return '01/100 dollar'
        if self.raw == 1:
            return 'One dollar'
        result = 'dollars'
        if self.cents:
            result = '%02d/100 ' % round(self.cents * 100) + result
        if self.one:
            if self.dec == 1:
                part = self.tens[self.one] + ' '
            else:
                part = self.ones[self.one] + ' '
            if len(result) > len('dollars'):
                part += 'and '
            result = part + result
        if self.dec == 1 and not self.one:
            part = 'Ten '
            if len(result) > len('dollars'):
                part += 'and '
            result = part + result

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
