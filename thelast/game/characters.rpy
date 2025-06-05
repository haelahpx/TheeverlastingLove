define R = Character("Raka", color="#3399FF")
define D = Character("Diego", color="#00CCCC")
define A = Character("Arga", color="#336600")

define L = Character("Luna", color="#FF66CC")
define M = Character("Mila", color="#FF9999")
define T = Character("Tiffany", color="#FF3399")

define N = Character("Nara", color="#CC6600")
define B = Character("Ben", color="#993300")
define RL = Character("Rilandy", color="#6666FF")

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

# Image declarations (default 'normal' expression)
image raka normal = im.Scale("characters/Raka_Normal.png", 420, 420)
image raka kaget = "images/characters/Raka_Kaget.png"

image luna normal = im.Scale("characters/Luna_Normal.png", 420, 420)
image nara normal = "images/characters/Nara_Normal.png"

image diego normal = "images/characters/Diego.png"
image arga normal = "images/characters/Arga.png"
image mila normal = "images/characters/Mila.png"
image tiffany normal = "images/characters/Tiffany.png"
image ben normal = "images/characters/Ben.png"
image rilandy normal = "images/characters/Rilandy.png"
