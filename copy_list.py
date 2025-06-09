# Belajar copy list


# ======== Hal yang wajar ========
# Merubah data list 2 sama dengan merubah data list 1
print("====Merubah data list 2 sama dengan merubah data list 1====")

pirates = ["shanks", "gaban", "raileight", "joyboy"]
copy_pirates = pirates

print(f"Data 1 : {pirates}")
print((f"Data 2 : {copy_pirates}"))

print("Percobaan update data")
copy_pirates[0] = "roger"

print(f"Data 1 : {pirates}")
print((f"Data 2 : {copy_pirates}"))


# Cara (melakukan copy list) agar ketika data copy dirubah, data utama tidak ikut dirubah
print("\n====(melakukan copy list) agar ketika data copy dirubah, data utama tidak ikut dirubah====")


print(f"Data utama \t\t\t: {pirates}")
print(f"Copy data tanpa (.copy()) \t: {copy_pirates}")
print("\n")
copy_data = pirates.copy()
print(f"Copy data dengan (.copy()) \t\t\t: {copy_pirates}")

copy_data[0] = "mihawk"
print(f"Merubah copy data tanpa merubah data utama \t: {copy_data}")

