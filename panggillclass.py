from file import JsonKu

file_name = "file.json"
json_ku = JsonKu(file_name)

print("1. Baca file")
print("2. Tulis file")
print("3. Update file")
print("4. Hapus data dari file")
pilihan = input("Pilih opsi (1/2/3/4): ")

if pilihan == "1":
    json_ku.baca()
elif pilihan == "2":
    json_ku.tulis()
elif pilihan == "3":
    json_ku.update()
elif pilihan == "4":
    json_ku.hapus()
else:
    print("Pilihan tidak valid.")