# ==========Belajar Dictionary=========
print("\n==========Belajar Dictionary=========")

data_list = [1,2,3,4,"otong"]

""" 
    dictionary => associative array
    pengambilan data dengan identifier(key)

"""
data_dic = {
    'nama' : 'umar',
    'umur' : 20,
    'alamat' : 'konoha',
    'list' : data_list
}

print(f"Data Dictionary : {data_dic}")
print(f"Memanggil satu data dic : {data_dic['nama']}")
print(f"Memanggil data list pada dic : {data_dic['list']}")