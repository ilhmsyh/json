import json

class JsonKu:
    def __init__(self, file_name):
        self.file_name = file_name

    def baca(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file) #json.load() adalah fungsi yang digunakan untuk membaca file JSON dan mengembalikan data dalam bentuk dictionary.
                print(json.dumps(data, indent=4)) #json.dumps() adalah fungsi yang digunakan untuk mengubah data dictionary menjadi string JSON.
                                                  #indent=4 adalah parameter yang digunakan untuk menambahkan indentasi ke dalam data JSON.
        except Exception as e:
            print(f"Error: {e}")

    def tulis(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            if not isinstance(data, list):
                data = [data]
            else:
                print("Data saat ini:")
                print(json.dumps(data, indent=4))
    
            judul = input("Masukkan judul: ")
            pengarang = input("Masukkan pengarang: ")
            tahun_terbit = int(input("Masukkan tahun terbit (angka): "))
    
            data.append({"judul": judul, "pengarang": pengarang, "tahun_terbit": tahun_terbit})
    
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print("Data berhasil ditulis.")
        except Exception as e:
            print(f"Error: {e}")

    def update(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                print("Data saat ini:")
                print(json.dumps(data, indent=4))
    
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return
    
            index = int(input("Masukkan indeks baris yang ingin diperbarui (mulai dari 0):"))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return
    
            print("Pilih opsi:")
            print("1. Perbarui field yang ada")
            print("2. Buat field baru")
    
            opsi = input("Masukkan pilihan (1/2): ")
    
            if opsi == "1":
                key_to_update = input("Masukkan kunci yang ingin diperbarui Contoh (judul/pengarang/tahun_terbit): ")
                if key_to_update in data[index]:
                    if isinstance(data[index].get(key_to_update), list):
                        print(f"Field {key_to_update} saat ini:")
                        print(data[index].get(key_to_update))
                        new_values = []
                        while True:
                            new_value = input(f"Masukkan nilai baru untuk field {key_to_update} (atau ketik 'selesai' untuk berhenti): ")
                            if new_value.lower() == 'selesai':
                                break
                            new_values.append(new_value)
                        data[index][key_to_update].extend(new_values)
                    else:
                        print("Apakah ingin menambahkan nilai baru sebagai array?")
                        print("1. Ya")
                        print("2. Tidak")
                        pilihan = input("Masukkan pilihan (1/2): ")
                        if pilihan == "1":
                            new_value = input(f"Masukkan nilai baru untuk field {key_to_update}: ")
                            data[index][key_to_update] = [new_value]
                        elif pilihan == "2":
                            print("Pilih tipe data:")
                            print("1. Integer")
                            print("2. String")
                            tipe_data = input("Masukkan pilihan (1/2): ")
                            if tipe_data == "1":
                                new_value = int(input(f"Masukkan nilai baru untuk field {key_to_update}: "))
                                data[index][key_to_update] = new_value
                            elif tipe_data == "2":
                                new_value = input(f"Masukkan nilai baru untuk field {key_to_update}: ")
                                data[index][key_to_update] = new_value
                            else:
                                print("Pilihan tidak valid.")
                else:
                    print("Kunci tidak ada.")
                    return
            elif opsi == "2":
                new_key = input("Masukkan nama field baru: ")
                print("Apakah ingin menambahkan nilai baru sebagai array?")
                print("1. Ya")
                print("2. Tidak")
                pilihan = input("Masukkan pilihan (1/2): ")
                if pilihan == "1":
                    new_value = input(f"Masukkan nilai baru untuk field {new_key}: ")
                    data[index][new_key] = [new_value]
                elif pilihan == "2":
                    print("Pilih tipe data:")
                    print("1. Integer")
                    print("2. String")
                    tipe_data = input("Masukkan pilihan (1/2): ")
                    if tipe_data == "1":
                        new_value = int(input(f"Masukkan nilai baru untuk field {new_key}: "))
                        data[index][new_key] = new_value
                    elif tipe_data == "2":
                        new_value = input(f"Masukkan nilai baru untuk field {new_key}: ")
                        data[index][new_key] = new_value
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print("Pilihan tidak valid.")
                    return
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Field berhasil diperbarui.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                print("Data saat ini:")
                print(json.dumps(data, indent=4))
                
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return

            index = int(input("Masukkan indeks baris yang ingin dihapus (mulai dari 0): "))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return

            del data[index]
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data pada baris {index} berhasil dihapus.")
        except Exception as e:
            print(f"Error: {e}")