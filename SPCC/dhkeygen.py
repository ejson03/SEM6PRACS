class DH:
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def keygenStage1(self, secret):
        return (self.g ** secret) % self.p

    def keygenStage2(self, ctext, secret):
        return (ctext ** secret) % self.p