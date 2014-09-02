class check_amount:
    def __init__(self, amount):
        self.raw = amount

    def __str__(self):
        if not self.raw:
            return 'Zero dollar'
        if self.raw == 0.01:
            return '01/100 dollar'
        if self.raw == 1:
            return 'One dollar'
        result = 'dollars'
        if self.cents:
            result = '%02d/100 ' % (self.cents * 100) + result

        return result.capitalize()

    @property
    def cents(self):
        return self.raw % 1.0
    @property
    def one(self):
        return int(self.raw) % 10
