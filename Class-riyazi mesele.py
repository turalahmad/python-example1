class Riyaziyyat:
    def __init__(self,sayi1,sayi2):

        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        return self.sayi1+self.sayi2

    def cixma(self):
        return self.sayi1-self.sayi2

    def vurma(self):
        return self.sayi1*self.sayi2

    def bolme(self):
        return self.sayi1/self.sayi2

riyaziyyat1 = Riyaziyyat(2,9)

print(str(riyaziyyat1.toplama()))
