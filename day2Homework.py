ogrenciler=[" Hanife Atıntaş "," Dilara Çalışkan "," Ali Kılınç " ," Saliha Özdemir "," Züleyha Kundak "]
print(ogrenciler)


ogrenciler.append(" Halit kalaycı ") # listeye öğrenci  ekledi
print(ogrenciler)

print("--------------------------")


ogrenciler.remove(" Züleyha Kundak ")  # değer ile çalışarak isimi isler
print(ogrenciler)

print("--------------------------")


ogrenciler.extend([" Engin Demiroğ "," Cemile Tınas " , " Sultan Karatepe "]) # birden fazla ekleme yapar
print(ogrenciler)


print("--------------------------")


print(ogrenciler[1]) # listedeki index numarasına göre öğrenci çağırıyor


print("--------------------------")


for ogrenci in ogrenciler:  # liste üzerindeki bütün öğrencileri tek tek yazdırıyor
    print(ogrenci)

print("--------------------------")    

while True:
    print(ogrenciler)
    break

print("--------------------------")













