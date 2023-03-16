print("hello world")


baslik = "İstiklal Marşı"
print(baslik)

# yorum satırı -

baslik = "Mehmet Akif Ersoy"
print(baslik)
#string = metinsel ifade 
#int = integer = tam sayı ifadesi


vade = 36
ekVade = 6
vde2 = "36"

# float, decimal , double
aylikOdeme = 200.50

#bool .boolen =>true veya false
yukselisteMi = True

# matematiksel operatörler
print(5  + 5)
print( vade + 12)
print (vade + ekVade)

print (5-5)
print (vade -12)
print (vade - ekVade)
print(36 - 5)

print(5*5)
print(vade * ekVade)
print(vade * 5)

print(20/5)
print (vade /2)
print(vade / ekVade)


yeniVade = vade /2
fiayt = 100 
indiriöliFiyat = fiayt /10
print(indiriöliFiyat)

# % =>mode (kalanı veriyor)
print(10 % 2)
print(vade % 5)
print(vade  % ekVade)
print (30 % 10)

# mamtıksal operöterler
print(1 == 1) # her iki taraf birbirine eşit mi ? ( doğruysa true yanlış ise false döngsü döner)
print (2 == 1)

print (1>2) # 1 , 2 den büyük mü ? ( doğruysa true yanlış ise false döngsü döner)
print(2>1)
print(1<= 1) # bük eşittir 

# or => veya  and 
print(1>2 or 5>2) # sadece bir tanesini doğru olması yeterli
print(1>2 and 5 >2 ) # her ikisi de doğru olmak zorunda
print( 1>2 or 5>2 and 3>2 ) # soldan sağa okunur 
print(1>2 and 5>3 and 3>2 )#  ik noktada yanlışı gördüğünde yanlış die cevap verecektir
print("--------------")
# karar yapıları 
# if alse

sayi1 =10
sayi2 =15

if sayi1 > sayi2 :
    print("sayi1 sayi2 den büyüktür")
elif sayi1 < sayi2 :
    print( "sayi2 sayi1 den büyüktür" )
else: 
   print(" her iki sayi birbirine eşittir")






#    python main.py