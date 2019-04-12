# Ededlerin sade ve murekkeb olmasinin teyini
sayac = 0
sayi = input('Sayı: ')
for i in range(2, int(sayi)):
      if (int(sayi) % i == 0):
            sayac += 1
            break
if (sayac != 0):
      print("murekkeb")
else:
      print("sade")

