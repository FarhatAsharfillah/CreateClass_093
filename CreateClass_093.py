#Membuat class untuk memasukkan objek persegi panjang yang memiliki
#panjang dan lebar juga sebagai metode untuk menghitung 
class PersegiPanjang:
    #init sebagai konstruktor dengan parameter self
    def __init__(self, Panjang, Lebar):
        #penetapan nilai panjang dan lebar
        self.Panjang = Panjang
        self.Lebar = Lebar
    #metode hitung_keliling untuk menghitung keliling dengan mengakses self panjang dan lebar
    def hitung_keliling(self):
        return 2 * (self.Panjang + self.Lebar)
    #metode hitung_luas untuk menghitung luas dengan mengakses self panjang dan lebar
    def hitung_luas(self):
        return self.Panjang * self.Lebar
    #metode yang mengembalikan string dari objek saat dipanggil oleh print atau str
    def __str__(self):
        #f"Persegi panjang, panjang" untuk memasukkan nilai variabel ke dalam string
        return f"Persegi panjang, panjang {self.Panjang} cm, dan lebar {self.Lebar} cm"

#
def main():
    try:
        Panjang=float(input("Masukkan Panjangnya ="))
        Lebar=float(input("Masukkan Lebarnya ="))
        if Panjang <=0 or Lebar <=0:
            print("")
            return
        PP=PersegiPanjang(Panjang,Lebar)
        print(PP)
        print("Keliling: ", PP.hitung_keliling())
        print("Luas: ", PP.hitung_luas())
    except ValueError:
        print("Nilai Harus Sesuai")
main()
