tahun=input("Masukkan Tahun: ")                                 #Untuk pengguna memasukkan tahun yang ingin diketahui

if (int(tahun)%4) == 0:                                       #Tahun yang habis dibagi dengan angka 4 merupakan tahun kabisat, parameter tahun diubah menjadi integer karena input merupakan string
    if (int(tahun)%100) == 0:                                 #Jika input habis dibagi dengan angka 4 dan juga habis dibagi dengan angka 100, maka tahun tersebut bukan tahun kabisat
        if (int(tahun)%400) == 0:                             #Jika input habis dibagi dengan angka 100 dan 400 maka input termasuk tahun kabisat
            print("Tahun", tahun, "adalah tahun kabisat")
        else:
            print("Tahun", tahun, "bukan tahun kabisat")
    else:
        print("Tahun", tahun, "adalah tahun kabisat")
else:
    print("Tahun", tahun, "bukan tahun kabisat")                #Jika input tidak memenuhi semua kondisi yang ditentukan maka input bukan tahun kabisat

