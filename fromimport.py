#Nama file : fromimport.py
#mengimpor fungsi luasPersegiPanjang
#dari modul geometri2D

from matematika.geometri2D import luasPersegiPanjang

#persegi panjang
p=10
l= 8
luas=luasPersegiPanjang(p,l)

print("persegi panjang")
print("Panjang\t:",p)
print("lebar\t:",l)
print("luas\t:",luas)