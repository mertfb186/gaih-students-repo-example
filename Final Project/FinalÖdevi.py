#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("********10 Soruluk Bilgi Yarışmasına Hoşgeldiniz******** \nUYARI:Soruları cevaplarken yazım yanlışı yapmamaya dikkat ediniz.\nBirinci soru ile başlıyoruz")
puan=0
a1=input("Güneş sisteminde yer alan en büyük gezegenin ismi nedir?").lower()
if(a1==("jüpiter")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Jüpiter olacaktı")
print("\n2. ile devam ediyoruz")
a2=input("Periyodik cetveli kim bulmuştur?").lower()
if(a2==("dmitri mendeleyev") or a2==("dimitri mendeleyev")):
   print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
   puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Dmitri Mendeleyev(Dimitri Mendeleyev) olacaktı")
print("3.Soru")
a3=input("1994 yılında yayımlanmış, Tom Hanks’in başrolünde oynadığı düşük iq sahibi birisinin yaşadıklarını anlatan dram filminin ismi nedir?").lower()
if(a3==("forrest gump")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Forrest Gump olacaktı")
print("4.Soru")
a4=input("Magna Carta hangi ülkenin kralıyla yapılmış bir sözleşmedir?").lower()
if(a4==("ingiltere") or a4==("i̇ngiltere")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:İngiltere olacaktı")
print("5.Soru")
a5=input("Hababam sınıfı kitabının yazarı kimdir?").lower()
if(a5==("rıfat ılgaz")or a5==("rıfat ilgaz")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Rıfat Ilgaz olacaktı")
print("6.Soru")
a6=input("Özel Görelilik Teorisi kime aittir?").lower()
if(a6==("albert einstein")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Albert Einstein olacaktı")
print("7.Soru")
a7=input("Fatih Sultan Mehmet’in babası kimdir?").lower()
if(a7==("2.murad") or a7==("2.murat") or a7==("ikinci murad") or a7==("ikinci murat")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:2.murad(2.murat) olacaktı")
print("8.Soru")
a8=input("Türk sanat müziğinin önde gelen üstadlarından biri 600’ü aşkın plağı ve kasedi olan ve herkes tarafindan “Sanat Güneşi” diye adlandırılan,\n 1996 yılında kendisi için düzenlenen bir ödül töreninide kalp krizi geçirirerek hayatını kaybeden sanatçımız kimdir?").lower()
if(a8==("zeki müren")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Zeki Müren olacaktı")
print("9.Soru")
a9=input("Dünyaca ünlü Da Vinci Şifresi kitabının yazarı kimdir?").lower()
if(a9==("dan brown")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:Dan Brown olacaktı")
print("10.Soru yani yarışmamızın son sorusu geliyor")
a10=input("Bir basketbol maçında bir takımda kaç kişi bulunur?").lower()
if(a10==("5") or a10==("beş")):
    print("Cevabınız Doğru Tebrikler.10 Puan kazandınız")
    puan=puan+10
else:
    print("Cevabınız Yanlış.Doğru Cevap:beş(5) olacaktı")
str(puan)
print("Puanınız:", puan)
if (puan<=50):
  print("Başarısız oldunuz!")
else:
  print("Tebrikler!Yarışmayı başarıyla tamamladınız.")


# In[ ]:




