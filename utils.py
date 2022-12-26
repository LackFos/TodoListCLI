import os
def tampilkanKegiatan():
    file = open("kegiatan.txt", "r")
    listKegiatan = file.readlines()

    if(listKegiatan): # Cek apakah listKegiatan memiliki isi
        print("List Kegiatan")
        print("-------------")
        for i in range(len(listKegiatan)):
            print(i + 1, end=". ") # Untuk print nomor, misalnya: 1. 2. 3.
            print(listKegiatan[i], end="")
    else:
        print("================================")
        print("| Anda tidak memiliki kegiatan |")
        print("================================")

def tambahKegiatan():
    file = open("kegiatan.txt", "a+")
    kegiatan = input("Masukkan kegiatan anda : ")
    file.write(kegiatan + "\n")

def hapusKegiatan():
    try:
        nomorKegiatan = int(input("Masukkan nomor kegiatan yang akan dihapus : "))
        file = open("kegiatan.txt", "r")
        listKegiatan = file.readlines()
        if(nomorKegiatan <= len(listKegiatan)): # Cek apakah nomor yang diinput user ada di listKegiatan
            del listKegiatan[nomorKegiatan - 1] # -1 supaya kegiatan yang hapus sesuai dengan nomor kegiatan yang di input
            file = open("kegiatan.txt", "w+")
            file.write("".join(listKegiatan))
        else:
            # Print Error
            print("================================================")
            print("| Nomor kegiatan yang anda berikan tidak valid |")
            print("================================================")
    except:
            # Print Error
            print("==========================================")
            print("| Silahkan memberikan input berupa angka |")
            print("==========================================")


def enterKey():
    input("Enter untuk melanjutkan...\n")

def setup():
    path = os.getcwd() + "/kegiatan.txt"
    if(os.path.isfile(path) == False):
        file = open("kegiatan.txt", "w+")
        file.close()
