faiz = 1.59
vade = "36"
krediAdi= "İhtiyaç krdisi"

# print(vade+ 12)

print(type (faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
# print(int(krediAdi) + 12)

faiz = str (faiz)
print(type(faiz))


# vade = input ("Lütfen istediğiniz vade sayısını giriniz :  ")      # her ikisi de aynı işlevi görür
# print(type (vade))
# print (int (vade )+ 12)

# vade =int (input ("Lütfen istediğiniz vade sayısını giriniz :  "))         
# print(type (vade))
# print ( (vade )+ 12)

# string interpolation 
# seçtiğinşz vade sonucu ortaya çıkan vade 
print("seçtiğiniz vade sonucu ortaya çıkanvade  = " + str (vade))
print("seçtiğiniz vade sonucu ortaya çıkanvade  = {vadeSayisi}".format(vadeSayisi = vade) )
print( f"seçtiğiniz vade sonucu ortaya çıkan vade : {vade} ")


isim="Halit"
metin = "merhaba {name}".format(name="Samet")
print(metin)


# f-string
metin= f"Hoşgeldiniz {1+1}"
print(metin)


# listeler 
# döngüler

krediler= ["İhtiyaç Kredisi", "Taşıt kredisi","konut Kredisi"]
print(type (krediler))
print(krediler[0])
#len --> length  kaç tane üeün olduğunu gösteririr
print(len(krediler))


krediler.append("özel kredi") # diziye ekleme yapar
krediler.pop() #pop sistedeki son ürünü siler eğer içine rakam yazarsan onu siler  (indexle çalışır )
krediler.pop(0)
krediler.remove("Taşıt kredisi") #(değer le çalışır) siler
krediler.extend(["emeklilik kredisi", "ev kredisi"]) # ekleme yapar
print(krediler)


# for döngüsü
for i in range(10): #10 a kadar tek tek yazacak
    print(i)
print("----------------")
for i in range(5,10):
    print(i)

print("----------------")
for i in range(0,51,10):
    print(i)



krediler= ["İhtiyaç Kredisi", "Taşıt kredisi","konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("----------------")    
for i in range(len(krediler)):
    print(krediler[i])

print("---------------------------")    

# while
i=0
while i<10:
    print("x")
    i+=1  # i yi 10 a kadar bir bir arttır demek

print("---------------------------")    

while True:
    print("X")
    break # döngüyü krıyor kesiyor


print("---------------------------")    

i=0
while i< len(krediler):
    print(krediler[i]) # eğer i ti i+=1 yapmassa 0. elaman sonsuz döngüye girer 
    i+=1

# fonsiyonlar

fiyat =100
indirim= 20

# dedinition
def calculate ():
    print(100- 80)

def calculateWhithParams(fiyat, indirim):
    print(fiyat-indirim)    


calculate()
calculate()
calculateWhithParams(100,30)

print("---------------------------")    

def sayHello (name):
    print(f"merhaba {name}")

sayHello("hanife")
sayHello("belinay")

print("---------------------------")    
def calculateAnReturn (fiyat,indirim):
    return fiyat-indirim

yenFiyat = calculateAnReturn(200,50)
print (yenFiyat)








