from utils import setup, enterKey, tampilkanKegiatan, tambahKegiatan, hapusKegiatan

setup()
while True:
    tampilkanKegiatan() # Print Isi List dari "listKegiatan"
    print("\nOpsi pilihan program TodoList :","\n1. Tambahkan kegiatan", "\n2. Hapus kegiatan", "\n3. Exit") # Print Opsi yang dapat user pilih
    
    opsiTerpilih =  input("\nSilahkan masukkan pilihan anda : ")
    if opsiTerpilih == "1":
        tambahKegiatan()
        enterKey()
    elif opsiTerpilih == "2":
        hapusKegiatan()
        enterKey()
    elif opsiTerpilih == "3":
        exit()
    else:
        # Print Error
        print("============================")
        print("| Pilihan anda tidak valid |")
        print("============================")
    