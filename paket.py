#Nama file : paket.py
#mengimpor modul geometri2D
#yang berada di dalam paket matematika
import matematika.geometri2D

def main():
    #bujur sangkar
    s = 5

    luas = matematika.geometri2D.luasBujursangkar(s)

    print("BUJURSANGKAR")
    print("Panjang sisi\t: ", s)
    print("Luas\t\t= ", luas)

if __name__ == "__main__":
    main()