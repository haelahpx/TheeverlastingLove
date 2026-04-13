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


image raka normal = im.Scale("images/characters/MC/Raka_Normal.png", 420, 420)
image raka normal mirror = im.Scale("images/characters/MC/Raka_Normal_Mirror.png", 420, 420)
image raka kaget = im.Scale("images/characters/MC/Raka_Kaget.png", 420, 420)
image raka kaget mirror = im.Scale("images/characters/MC/Raka_Kaget_Mirror.png", 420, 420)
image raka sad = im.Scale("images/characters/MC/Raka_Kaget_Mirror.png", 420, 420)
image raka mikir = "images/characters/MC/raka_mikir.png"

image luna normal = im.Scale("characters/Luna/Luna_Normal.png", 420, 420)
image luna kaget = "images/characters/Luna/luna_kaget.png"
image luna malu = "images/characters/Luna/luna_malu.png"

image nara normal = im.Scale("images/characters/Nara/Nara_Normal.png", 420, 420)
image nara normal mirror = im.Scale("images/characters/Nara/Nara_Normal_Mirror.png", 420, 420)
image nara sinis = "images/characters/Nara/nara_sinis.png"

image diego normal = im.Scale("images/characters/Diego/Diego.png", 420, 420)
image diego normal mirror = im.Scale("images/characters/Diego/Diego_Mirror.png", 420, 420)
image diego senang = im.Scale("images/characters/Diego/Diego_Mirror.png", 420, 420)
image diego smirk = im.Scale("images/characters/Diego/Diego_Mirror.png", 420, 420)
image diego kesal = im.Scale("images/characters/Diego/Diego_Mirror.png", 420, 420)
image diego kecewa = "images/characters/Diego/diego_kecewa.png"

image arga normal = im.Scale("images/characters/Arga/Arga.png", 420, 420)
image arga normal mirror = im.Scale("images/characters/Arga/Arga_Mirror.png", 420, 420)

image mila normal = im.Scale("images/characters//Mila/Mila.png", 420, 420)
image mila normal mirror = im.Scale("images/characters/Mila/Mila_Mirror.png", 420, 420)
image mila smile = im.Scale("images/characters/Mila/Mila_Mirror.png", 420, 420)
image mila sinis = "images/characters/Mila/mila_sinis.png"

image tiffany normal = im.Scale("images/characters/Tiffany/Tiffany.png", 420, 420)
image tiffany smile = im.Scale("images/characters/Tiffany/Tiffany.png", 420, 420)

image ben normal = im.Scale("images/characters/Ben/Ben.png", 420, 420)
image ben kaget = im.Scale("images/characters/Ben/Ben.png", 420, 420)
image ben sedih = im.Scale("images/characters/Ben/Ben.png", 420, 420)

image rilandy normal = im.Scale("images/characters/Rilandy/Rilandy.png", 420, 420)




image card luna = im.Scale("images/cards/luna_card.jpg", 420, 420)
image card nara = im.Scale("images/cards/nara_card.jpg", 420, 420)
image card diego = "images/cards/diego_card.png"
image card mila = "images/cards/mila_card.png"
image card tiffany = "images/cards/tiffany_card.png"
image card arga = "images/cards/arga_card.png"
image card ben = "images/cards/arga_card.png"