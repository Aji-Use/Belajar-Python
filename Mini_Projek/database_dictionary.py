# Latihan membuat database sederhana dengan dictionary

import datetime


user1  = {
    "id" : "PR001",
    "name" : "Roronoa Zoro",
    "born" : datetime.datetime(1999,4,1),
    "address" : "tanjung pinang",
    "status" : "pirate"
}
user2  = {
    "id" : "PR002",
    "name" : "Monkey D. Luffy",
    "born" : datetime.datetime(2000,6,12),
    "address" : "tanjung priok",
    "status" : "pirate"
}
user3  = {
    "id" : "MR001",
    "name" : "Monkey D. Garp",
    "born" : datetime.datetime(1945,2,5),
    "address" : "tanjung priok",
    "status" : "marine"
}
user4  = {
    "id" : "MR002",
    "name" : "Sakazuki Akainu",
    "born" : datetime.datetime(1950,4,1),
    "address" : "tanjung priok",
    "status" : "marine"
}
user5  = {
    "id" : "MR003",
    "name" : "Borsalino Kizaru",
    "born" : datetime.datetime(1948,10,21),
    "address" : "gresik",
    "status" : "marine"
}
user6  = {
    "id" : "PR003",
    "name" : "God D. Usop",
    "born" : datetime.datetime(2000,7,8),
    "address" : "padang",
    "status" : "pirate"
}

# nested list
database = {
    "PR001" : user1,
    "PR002" : user2,
    "PR003" : user6,
    "MR001" : user3,
    "MR002" : user4,
    "MR003" : user5
}

# dump database
print(f"{'ID':<6} {'NAME':<20} {'BORN':<8} {'ADDRESS':<20} {'STATUS':<10}")
print("="*65)

for key in database:
    KEY = key
    
    ID = database[KEY]['id']
    NAME = database[KEY]['name']
    BORN = database[KEY]['born'].strftime("%x")
    ADDRESS = database[KEY]['address']
    STATUS = database[KEY]['status']
    
    print(f"{ID:<6} {NAME:<20} {BORN:<8} {ADDRESS:<20} {STATUS:<10}")
   
    