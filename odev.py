# değişken veri tipleri

ogretmenAd1 ="Halit Kalaycı"
ogretmenAd2 ="Engin Demiroğ"

kursAdi1="java Kamp"
kursAdi2 ="javascript"
kursAdi3 ="python" 

ogrenci1="hanife Altıntaş"
ogrenci2 = "Belimay Ay"

# alınan kurs adları ve öğrenci öğretmen adları 
print((kursAdi1)+ "="+(ogretmenAd1)+ "="+(ogrenci1) +"   "+ (ogrenci2))


# şart blokları ===> öğrencilerin kursa kayıt yapıp yamadıları ile ilgili birdizi kod yazacağım

sonuc1="kayıt yapıldı"
sonuc2="kayıt yapılmadı"

if kursAdi2 + ogrenci1:
    print(sonuc1)
elif kursAdi2 :
    print(sonuc2)


# ödev 2 diziler ile ilgili bireysel çalışma

courses=[" java  ", " python " , " javascript ", " C++ ", " C# "]
teachers =[" Engin demiroğ " , " Halit Kalaycı "]
students= [" Hanife  Altintaş ", " Belinay Ay ", " Yasemin Min "]
records=["kayıt tamamlandı " , " kayıt edilemedi "] # kayıt 
print(courses[1] + teachers[1] + students [2] )


