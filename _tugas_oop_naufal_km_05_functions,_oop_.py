# -*- coding: utf-8 -*-
""".Tugas OOP  Naufal KM-05: Functions, OOP .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gPTlZYabyEbj4WAGJ653Ki5l1hqm_XTn

# **Fungsi**
"""

# Deklarasi Fungsi
def cetak(x):
  print(x)

# Memanggil Fungsi
cetak("wokee")

# Latihan
# Deklarasi Fungsi
def cetak(z):
  print(z)

# Memanggil Fungsi
cetak("Hallo!")

# Deklarasi Fungsi dengan pengembalian
def tambah(a, b):
  return a + b;

# Memanggil Fungsi
print(tambah(2, 3))

# Latihan
# Deklarasi Fungsi dengan pengembalian
def tambahan(a, b, c):
  return a + b + c;

# Memanggil Fungsi
print(tambahan(2, 3, 4))

def nama_fungsi(arg1, arg2, arg3):
  # isi fungsi

def fungsi_dengan_pengembalian(arg1, arg2, arg3):
  # isi fungsi
  return 'sesuatu'

# Latihan
def nama_fungsi(arg1, arg2, arg3):
  # isi fungsi

def fungsi_dengan_pengembalian(arg1, arg2, arg3:
  # isi fungsi
  return 'sesuatu'

"""# **Method**"""

class NamaClass:
  def nama_method(arg1, arg2, ...):
    # isi method

class PersegiPanjang:
  def __init__(self,panjang,lebar):
    self.panjang = panjang
    self.lebar = lebar
  
  def keliling(self):
    return 2 * (self.panjang + self.lebar)
  def luas(self):
    return self.panjang * self.lebar

# Deklarasi Object (Class)
class Kucing(object):
  def meong(self):
    print("meeooong")

# Memanggil method
cat = Kucing()
cat.meong()

# Latihan 
# Deklarasi Object (Class)
class singa(object):
  def roar(self):
    print("Rooaarrr")

# Memanggil method
lion = singa()
lion.roar()

"""# **Lambda Expression**"""

# Lambda expression
tambah = lambda a, b: (a + b)
print(tambah(2, 3))

# Latihan
# Lambda expression
kurang = lambda a, b: (a - b)
print(kurang(5, 3))

"""# **Object Oriented Programming**

## **Encapsulation**
"""

nama = "cemong"
usia = 1
warna = "putih coklat muda"
jenis = "anggora"

def meongg():
  print("meeeoonnggg... ")

def info_kucing(nama, usia, warna, jenis):
  print(f"nama: {nama}, usia: {usia}, warna: {warna}, jenis: {jenis}")

info_kucing(nama, usia, warna, jenis)


class Kucing:
  def __init__(self, nama, usia, warna, jenis):
    self.nama = nama
    self.usia = usia
    self.warna = warna
    self.jenis = jenis

  def myfunc(self):
    print("Hello my name is " + self.nama)
  
  def meong(self):
    print("meeeoonnggg... ")

  def info(self):
    print(f"nama: {self.nama}, usia: {self.usia}, warna: {self.warna}, jenis: {self.jenis}")


kucing1 = Kucing("cemong", 1, "putih coklat muda", "anggora")

kucing1.info()

# LATIHAN
motor = "vario"
warna = "putih"
jenis = "matic"

def ngengg():
  print("ngengggg... ")

def info_motor(motor, warna, jenis):
  print(f"motor: {motor},  warna: {warna}, jenis: {jenis}")

info_motor(motor, warna, jenis)


class Motor:
  def __init__(self,motor,  warna, jenis):
    self.motor = motor
    self.warna = warna
    self.jenis = jenis

  def myfunc(self):
    print("motornya adalah " + self.motor)
  
  def ngeng(self):
    print("ngengggggg... ")

  def info(self):
    print(f"motor: {self.motor},  warna: {self.warna}, jenis: {self.jenis}")


motor1 = Motor("vario",  "putih", "matic")

motor1.info()

"""## **Abstraction**"""

# Memanggil method dari objek tanpa harus mengetahui cara kerja method
motor1.myfunc()

"""## **Inheritence**"""

class Binatang(object):
  def __init__(self, nama, usia, jenis, mamalia):
    self.nama = nama
    self.usia = usia
    self.jenis = jenis
    self.mamalia = mamalia

  def tidur(self, durasi):
    for x in range(durasi):
      print("ddrrr... ddrrr... ")

  def info(self):
    print(f"nama: {self.nama}, usia: {self.usia}, jenis: {self.jenis}, mamalia: {self.mamalia}")


animal1 = Binatang("cemong", 1, "omnivora", True)

animal1.info()

class Kucing(Binatang):
  def __init__(self,  nama, usia, jenis, mamalia, warna, jenis_kucing):
    super().__init__(nama, usia, jenis, mamalia)
    self.warna = warna
    self.jenis_kucing = jenis_kucing
  
  def meong(self):
    print("meeeonnggg")

  def info_kucing(self):
    print(f"warna: {self.warna}, jenis kucing: {self.jenis_kucing}")

cat1 = Kucing("cemong", 1, "omnivora", True, "putih coklat muda", "anggora")

cat1.info()
cat1.info_kucing()

# Latihan
class Kendaraan(object):
  def __init__(self, motor, warna, jenis, bahan_bakar):
    self.motor = motor
    self.warna = warna
    self.jenis = jenis
    self.bahan_bakar = bahan_bakar

  def manasin(self, durasi):
    for x in range(durasi):
      print("ddrrr... ddrrr... ")

  def info(self):
    print(f"motor: {self.motor}, warna: {self.warna}, jenis: {self.jenis}, bahan_bakar: {self.bahan_bakar}")


vehicle = Kendaraan("vario", "putih", "matic", "pertamax" )

vehicle.info()

class Motor(Kendaraan):
  def __init__(self,  motor, warna, jenis, pertamax,jenis_bahan_bakar):
    super().__init__(motor, warna, jenis, pertamax)
    self.warna = warna
    self.jenis_bahan_bakar = jenis_bahan_bakar
  
  def ngeng(self):
    print("ngengggg....")

  def info_motor(self):
    print(f"warna: {self.warna}, jenis bahan bakar: {self.jenis_bahan_bakar}")

motorbike1 = Motor("vario", "putih", "matic", True, "pertamax")

motorbike1.info()
motorbike1.info_motor()



"""## **Polymorphism**"""

class Ikan(Binatang):
  def __init__(self,  nama, usia, jenis, mamalia, warna, jenis_air, jenis_ikan):
    super().__init__(nama, usia, jenis, mamalia)
    self.warna = warna
    self.jenis_air = jenis_air
    self.jenis_ikan = jenis_ikan
  
  def berenang(self, durasi):
    print("wushh... wush... ")

  def info_ikan(self):
    print(f"warna: {self.warna}, jenis ikan: {self.jenis_ikan}, jenis air: {self.jenis_air}")

fish1 = Ikan("Jago", 2, "omnivora", False, "Merah Putih", "Tawar", "Cupang")

fish1.info()
fish1.info_ikan()
fish1.tidur(5)

# LATIHAN
class Motor(Kendaraan):
  def __init__(self,  motor, warna, matic, bahan_bakar):
    super().__init__(motor, warna, matic, bahan_bakar)
    self.warna = warna
    self.bahan_bakar = bahan_bakar
  
  def berjalan(self, durasi):
    print("ngengg... wush... ")

  def info_motor(self):
    print(f"warna: {self.warna}, bahan bakar: {self.bahan_bakar}")

motorbike1 = Motor("Jago", "Putih", "Matic","Pertamax")

motorbike1.info()
motorbike1.info_motor()
motorbike1.manasin(5)
motorbike1.berjalan(5)