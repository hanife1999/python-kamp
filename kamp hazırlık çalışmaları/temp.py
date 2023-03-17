# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# ----- DEĞİŞKENLER----------
print ("HELLO WORLD")

int  = 10 #integger sayısal bir değişken
x ="10" #metinsel bir değişken = string 

print(int + 15)


name = "hanife "
surname= "altıntaş"

print(name + surname)

mesaj ="merhaba dünya"
print(mesaj [2:5]) #2 den 5 e kadar

#---------LOWER UPPER--------

mesaj1 = "bu gün eve gelme"
print(mesaj1.lower()) # düşük ( harfleri küçük yazar)
print(mesaj1.upper()) # üst (harfleri büyük yazar)
print( mesaj1.replace("ü", "u")) # değiştirme (harfi ü den u ya çevirdi)
print(mesaj1.split()) # cümle içersinde yakaladığı boşluklardaki kelimeleri dizi haline getiriyor

#------------WORKSHOPS-------------
A = 10
B = 20 

A,B =B,A
 
# temp =10 #  temp = geçici 
# A=B
# B =temp

print( "A = " + str(A)) # str = string = metin
print("B = "  + str(B))

#;-------------- LİSTELER-------------


# ogrenci1="hanife "
# ogrenci2="yasemin"
# ogrenci3="belinay"
#  print(ogrenci1)


ogrenciler=["hanife","yasemin","belinay"]
print(ogrenciler[1])
ogrenciler.append("sevilay") #listeye yeni biri ekleniyor
print(ogrenciler[3])
print(len(ogrenciler)) # len kaç elemandan oluştuğunu söyler

#list constructor
sehirler= list(("Ankara", "Afyon"))
print(sehirler)
#print(sehirler.clear())# listeyi temizler

print("Ankara sayısı = " + str(sehirler.count("Ankara"))) # kaç kana ankara kelimesi var onu hesaplıyor
print("Ankara indexi  = " + str(sehirler.index("Ankara"))) #bulunduğu yerde kesiyor
sehirler.pop(1) # pop ediyor yani listeden çıkarıyor
sehirler.insert(0, "Eskişehir") # listeye yerleştirme yaptı
print(sehirler )

#------TUPLE-------
tupleListe = (2,4,6,"Aydın") 
liste =  [2,4,6,"Aydın"]
print(type(tupleListe)) # tuple demet demek
print(type(liste))
print(tupleListe)
print(liste)
     

# -------SET -----------
setA = {1,2,3,4,5,6}
setB = {1,3,4,6,7,8}

print(setA  | setB)  # orta olanları tekrar yazdırmadan listeliyor
print(setA.union(setB)) # orta olanları tekrar yazdırmadan listeliyor

print(setA & setB) # ortak olanlar listelendi
print(setA.intersection(setB)) # ortak olanlar listelendi

print(setA - setB)  # farklı olanları listeliyor
print(setA.difference(setB)) # farklı olanları listeliyor

print(setA ^ setB) # otakları almadan her iki kümeyi ayırdı
print(setA.symmetric_difference(setB))# otakları almadan her iki kümeyi ayırdı

sozluk = {"kitap" : "book", "masa" : "table", "kalem" : "pencil"}

print(sozluk)

#---------- İF---------------
int1 =100
int2 = 200
if int1>int2:
    print("sayı 1 büyüktür")
print("sayı 1 küçüktür")



lights = ["red", "yellow", "green"]
currentLight = lights[2]
print(currentLight)

if currentLight == "red":
    print("STOP")
if currentLight == "green":
    print("GO")
if currentLight == "yellow":
    print("READY")
    
    
# -----------ELİF & ELSE----------


lights = ["red", "yellow", "green"]
currentLight = lights[2]
print(currentLight)

if currentLight == "red":
    print("STOP")
elif currentLight == "green":
    print("GO")
elif currentLight == "yellow":
    print("READY")
    
    
  #----  workshop-------
  
# sayii = float(input("sayı giriniz : ")) 
# if sayii > 0:
#     print("sayı pozitiftir")
# elif sayii==0:
#     print("sayı sıfırdır")
# else:    
#     print("sayı negatiftir")
    
 #------------- workshop 2---------
 
 
ssayi1 = int (input("1. Sayı : "))   
ssayi2 = int (input("2. Sayı : "))   
ssayi3 = int (input("3. Sayı : "))   

if (ssayi1>=ssayi2)and (ssayi1>=ssayi3):
    enBuyuk = ssayi1

elif (ssayi2>=ssayi1) and (ssayi2>=ssayi3):
    enBuyuk= ssayi2

else:
    enBuyuk = ssayi3

print("En Büyük Sayı : "+ enBuyuk)    

