#!/usr/bin/env python
# coding: utf-8

# In[2]:


arasınav1=int(input("Ali'nin arasınav notunu giriniz:"))
proje1=int(input("Ali'nin proje notunu giriniz:"))
final1=int(input("Ali'nin final notunu giriniz:"))
geçmenotu1=arasınav1*0.3+proje1*0.3+final1*0.4
print("Ali'nin geçme notu:",geçmenotu1)
arasınav2=int(input("Mehmet'in arasınav notunu giriniz:"))
proje2=int(input("Mehmet'in proje notunu giriniz:"))
final2=int(input("Mehmet'in final notunu giriniz:"))
geçmenotu2=arasınav2*0.3+proje2*0.3+final2*0.4
print("Mehmet'in geçme notu:",geçmenotu2)
arasınav3=int(input("Ayşe'nin arasınav notunu giriniz:"))
proje3=int(input("Ayşe'nin proje notunu giriniz:"))
final3=int(input("Ayşe'nin final notunu giriniz:"))
geçmenotu3=arasınav3*0.3+proje3*0.3+final3*0.4
print("Ayşe'nin geçme notu:",geçmenotu3)
arasınav4=int(input("Zeynep'in arasınav notunu giriniz:"))
proje4=int(input("Zeynep'in proje notunu giriniz:"))
final4=int(input("Zeynep'in final notunu giriniz:"))
geçmenotu4=arasınav4*0.3+proje4*0.3+final4*0.4
print("Zeynep'in geçme notu:",geçmenotu4)
arasınav5=int(input("Ahmet'in arasınav notunu giriniz:"))
proje5=int(input("Ahmet'in proje notunu giriniz:"))
final5=int(input("Ahmet'in final notunu giriniz:"))
geçmenotu5=arasınav5*0.3+proje5*0.3+final5*0.4
print("Ahmet'in geçme notu:",geçmenotu5)
öğrenci_bilgileri={"Ali'nin ara sınavı":arasınav1,
                   "Ali'nin proje notu":proje1,
                   "Ali'nin final sınavı":final1,
                   "Mehmet'in ara sınavı":arasınav2,
                   "Mehmet'in proje notu":proje2,
                   "Mehmet'in final sınavı":final2,
                   "Ayşe'nin ara sınavı":arasınav3,
                   "Ayşe'nin proje notu":proje3,
                   "Ayşe'nin final sınavı":final3,
                   "Zeynep'in ara sınavı":arasınav4,
                   "Zeynep'in proje notu":proje4,
                   "Zeynep'in final sınavı":final4,
                   "Ahmet'in ara sınavı":arasınav5,
                   "Ahmet'in proje notu":proje5,
                   "Ahmet'in final sınavı":final5,
                  }
liste1=[{'isim':'Ali','geçmenotu':geçmenotu1},
        {'isim':'Mehmet','geçmenotu':geçmenotu2},
        {'isim':'Ayşe','geçmenotu':geçmenotu3},
        {'isim':'Zeynep','geçmenotu':geçmenotu4},
        {'isim':'Ahmet','geçmenotu':geçmenotu5}]
sorted(liste1, key = lambda x: x["geçmenotu"], reverse=True)

