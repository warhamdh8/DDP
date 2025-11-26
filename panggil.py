import bangunRuang as br
import bangundatar as bd

print("~~~~ BANGUN RUANG ~~~~")
print(f"Volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4, 5, 2)}")
print(f"Volum prisma segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum tabung adalah {br.tabung(7, 10)}")
print(f"Volum kerucut adalah {br.kerucut(5, 12)}")

print("~~~~ BANGUN DATAR ~~~~~")
print(f"Luas persegi adalah {bd.persegi(5)}")
print(f"Luas persegi panjang adalah {bd.persegi_panjang(8,5)}")
print(f"Luas segitiga adalah {bd.segitiga(3,4)}")
print(f"Luas lingkaran adalah {bd.lingkaran(5)}")
print(f"Luas jajarGenjang adalah {bd.jajarGenjang(4,7)}")