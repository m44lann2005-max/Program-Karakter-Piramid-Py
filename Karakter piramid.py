def buat_piramida(karakter, tinggi):
    for i in range(1, tinggi + 1):
        # Spasi untuk pusatkan piramida
        spasi = ' ' * (tinggi - i)
        # Karakter untuk baris tersebut
        bintang = karakter * (2 * i - 1)
        print(spasi + bintang)

# Contoh penggunaan
karakter = input("Masukkan karakter: ")
tinggi = int(input("Masukkan tinggi piramida: "))
buat_piramida(karakter, tinggi)