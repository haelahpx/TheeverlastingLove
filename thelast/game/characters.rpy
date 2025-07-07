define r = Character("Raka", color="#3399FF")
define d = Character("Diego", color="#00CCCC")
define a = Character("Arga", color="#336600")

define l = Character("Luna", color="#FF66CC")
define m = Character("Mila", color="#FF9999")
define t = Character("Tiffany", color="#FF3399")

define n = Character("Nara", color="#CC6600")
define b = Character("Ben", color="#993300")
define rl = Character("Rilandy", color="#6666FF")
define npc = Character("npc", color="#6666FF")

define z = Character("Diego & Mila", color="#FFCC00")


init python:
    store.character_profiles = {
        "Raka": {
            "nama": "Raka Pratama",
            "umur": 16,
            "hobi": "Bermain basket",
            "kepribadian": "Pemalu tapi perhatian"
        },
        "Luna": {
            "nama": "Luna Ayudia",
            "umur": 16,
            "hobi": "Membaca novel",
            "kepribadian": "Ceria dan ramah"
        },
        "Nara": {
            "nama": "Nara Anindya",
            "umur": 17,
            "hobi": "Public speaking",
            "kepribadian": "Kalem dan dewasa"
        },
        "Diego": {
            "nama": "Diego Fernando",
            "umur": 17,
            "hobi": "Bermain gitar",
            "kepribadian": "Santai dan karismatik"
        },
        "Arga": {
            "nama": "Arga Mahendra",
            "umur": 16,
            "hobi": "Coding",
            "kepribadian": "Pendiam dan cerdas"
        },
        "Mila": {
            "nama": "Mila Safira",
            "umur": 16,
            "hobi": "Menari",
            "kepribadian": "Penuh semangat dan percaya diri"
        },
        "Tiffany": {
            "nama": "Tiffany Elvira",
            "umur": 16,
            "hobi": "Fashion design",
            "kepribadian": "Stylish dan perfeksionis"
        },
        "Ben": {
            "nama": "Ben Hartono",
            "umur": 17,
            "hobi": "Menulis puisi",
            "kepribadian": "Misterius dan puitis"
        },
        "Rilandy": {
            "nama": "Rilandy Septian",
            "umur": 17,
            "hobi": "Fotografi",
            "kepribadian": "Tenang dan pengamat"
        }
    }


image raka normal = im.Scale("characters/Raka_Normal.png", 420, 420)
image raka normal mirror = im.Scale("characters/Raka_Normal_Mirror.png", 420, 420)
image raka kaget = im.Scale("characters/Raka_Kaget.png", 420, 420)
image raka kaget mirror = im.Scale("characters/Raka_Kaget_Mirror.png", 420, 420)
image raka mikir = "images/characters/raka_mikir.png"

image luna normal = im.Scale("characters/Luna_Normal.png", 420, 420)
image luna kaget = "images/characters/luna_kaget.png"
image luna malu = "images/characters/luna_malu.png"

image nara normal = im.Scale("characters/Nara_Normal.png", 420, 420)
image nara normal mirror = im.Scale("characters/Nara_Normal_Mirror.png", 420, 420)
image nara sinis = "images/characters/nara_sinis.png"

image diego normal = im.Scale("characters/Diego.png", 420, 420)
image diego normal mirror = im.Scale("characters/Diego_Mirror.png", 420, 420)
image diego kecewa = "images/characters/diego_kecewa.png"

image arga normal = im.Scale("characters/Arga.png", 420, 420)
image arga normal mirror = im.Scale("characters/Arga_Mirror.png", 420, 420)

image mila normal = im.Scale("characters/Mila.png", 420, 420)
image mila normal mirror = im.Scale("characters/Mila_Mirror.png", 420, 420)
image mila sinis = "images/characters/mila_sinis.png"

image tiffany normal = im.Scale("characters/Tiffany.png", 420, 420)

image ben normal = im.Scale("characters/Ben.png", 420, 420)

image rilandy normal = im.Scale("characters/Rilandy.png", 420, 420)




image card luna = "images/cards/luna_card.png"
image card nara = "images/cards/nara_card.png"
image card diego = "images/cards/diego_card.png"
image card mila = "images/cards/mila_card.png"
image card tiffany = "images/cards/tiffany_card.png"
image card arga = "images/cards/arga_card.png"