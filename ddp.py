list_kendaraan=["motor","sport","950cc","hitam","roda2"]
list_kendaraan.append("125.000.000")
list_kendaraan.append("kopling")
list_kendaraan.insert(2,"kawasaki")

print(list_kendaraan)



bangun_datar=int(input("masukan jenis bangun datar:"))
match bangun_datar :
    case 1: 
        print("s x s")
        s1 = float(input("Sisi 1 :"))
        s2 = float(input("Sisi 2 :"))
        hasil= s1 * s2
        print("hasilnnya adalah:", hasil)
    case 2 : 
        print("3,14 * r * r")
        r1 = float(input("r1 :"))
        r2 = float(input("r2 :"))
        hasil= 3.14 * r1 * r2
        print("hasilnya adaalah", hasil)
    case 3 :
        print("1/2 x alas x tinggi")
        alas = float(input("alas :"))
        tinggi = float(input("tingi :"))
        hasil = 0.5 * alas * tinggi
        print("hasilnya adalah :", hasil)


    