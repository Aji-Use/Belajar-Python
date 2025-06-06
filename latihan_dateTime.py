# Latihan dengan library date time
import datetime as dt


tgl_lahir = int(input("Masukkan tanggal lahir anda \t= "))
bln_lahir = int(input("Masukkan bulan lahir anda \t= "))
thn_lahir = int(input("Masukkan tahun lahir anda \t= "))

lahir = dt.date(thn_lahir, bln_lahir, tgl_lahir)
hari_ini = dt.date.today()

jml_hari = hari_ini - lahir
umur = jml_hari.days // 360

print(f"anda hidup selama {jml_hari.days} hari")
print(f"Umur anda adalah {umur} tahun")
print(f"Anda lahir pada hari = {lahir:%A}")
