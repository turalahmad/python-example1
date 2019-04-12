class Qus:
    nov_adi=""
    qus_adi=""

    def adYaz(self):
        print("Novun adi:",self.nov_adi)
        print("Qusun adi:",self.qus_adi)

class Yirtici(Qus):
    qanat_uzunlugu="0"
    agirliq="0"
    def adYaz1(self):
        print("Qusun qanat uzunlugu",self.qanat_uzunlugu)
        print("Qusun agirligi", self.agirliq)

class Qartal(Yirtici):
    alt_nov="0"

    def adYaz2(self):
        print("Qusun alt novu", self.alt_nov)


qarabag_qartali=Qartal()

qarabag_qartali.qus_adi="Azerian eagle"
qarabag_qartali.nov_adi="Qara Qartalli"
qarabag_qartali.agirliq="10kg"
qarabag_qartali.qanat_uzunlugu="1m"
qarabag_qartali.alt_nov="middle east asia"
qarabag_qartali.adYaz()
qarabag_qartali.adYaz1()
qarabag_qartali.adYaz2()
