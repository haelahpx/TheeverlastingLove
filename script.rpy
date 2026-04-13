default luna_hearts = 0
default nara_hearts = 0

default unlocked_luna = False
default unlocked_nara = False
default unlocked_diego = False
default unlocked_mila = False
default unlocked_tiffany = False
default unlocked_arga = False

define npc = Character("Orang Tua")  # Just in case it was missing

# Define custom screen positions
define centerleft = Position(xalign=0.25)
define centerright = Position(xalign=0.75)

# Screens
screen character_card(char_name, char_desc, char_image):
    modal True
    window:
        style "gm_root"
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15 xalign 0.5

            text "KARAKTER BARU TERBUKA" size 40 xalign 0.5
            add char_image xalign 0.5
            text char_name size 35 xalign 0.5
            text char_desc size 25 xalign 0.5

            textbutton "Lanjutkan" action Return() xalign 0.5

screen stats_display():
    vbox:
        xalign 0.98 yalign 0.02 spacing 5
        text "Hubungan:" size 22
        text "Luna: [luna_hearts] ♥" size 20
        text "Nara: [nara_hearts] ♥" size 20

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    use stats_display

# Images
image auditorium = im.Scale("bg/auditorium.jpg", 1920, 1080)
image bg_kantin_gate = im.Scale("bg/bg_kantin_gate.jpg", 1920, 1080)
image bg_kantin_table = im.Scale("bg/bg_kantin_gate.jpg", 1920, 1080)

# Transforms
transform left_terang:
    xpos 0.09
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 1.0
    linear 0.2 alpha 1.0

transform left_redup:
    xpos 0.09
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 0.4
    linear 0.2 alpha 0.4

transform right_terang:
    xpos 0.89
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 1.0
    linear 0.2 alpha 1.0

transform right_redup:
    xpos 0.89
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 0.4
    linear 0.2 alpha 0.4

transform center_terang:
    xpos 0.5
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 1.0
    linear 0.2 alpha 1.0

transform center_redup:
    xpos 0.5
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    alpha 0.4
    linear 0.2 alpha 0.4

define Z = Character("Diego & Mila", color="#7FB2B2")

default temp_name = "Raka"
default mc_name = "Raka"

screen name_input_screen():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)  # ✅ FIXED
        vbox:
            spacing 20
            text "Masukkan nama kamu:" size 30
            input value VariableInputValue("temp_name") length 32
            textbutton "Lanjut" action [SetVariable("mc_name", temp_name), Jump("after_name_input")]

label name_input:
    call screen name_input_screen
    return

label after_name_input:
    if mc_name.strip() == "":
        $ mc_name = "Raka"
    $ r = Character(mc_name)
    return

# --- Full Chat UI Component ---
# Letakkan kode ini di dalam file screens.rpy atau gui.rpy

# 1. Style dasar untuk window dan teks chat
style chat_window is empty:
    # Window utama dibuat transparan karena gelembung chat sudah memiliki background sendiri.
    background None

style chat_what is text:
    # Style untuk teks pesan di dalam gelembung.
    color "#000000" # Warna teks hitam agar mudah dibaca di bubble terang.
    size 22
    layout "subtitle"

style chat_who is text:
    # Style untuk nama pengirim di atas pesan.
    color "#3a76c6" # Warna nama biru khas aplikasi chat.
    size 24
    bold True

# 2. Style untuk gelembung chat kiri dan kanan
style chat_bubble_left is empty:
    # Menggunakan file SVG atau PNG yang sudah Anda simpan.
    # Pastikan file ini ada di folder /gui proyek Anda.
    background Frame("gui/chat_bubble_left.svg", 15, 15)
    xalign 0.05 # Posisi gelembung di sisi kiri layar.
    padding (15, 15, 15, 15) # Jarak antara teks dan tepi gelembung.
    xmaximum 600 # Lebar maksimum gelembung agar tidak terlalu memanjang.

style chat_bubble_right is empty:
    # Menggunakan file SVG atau PNG yang sudah Anda simpan.
    # Pastikan file ini ada di folder /gui proyek Anda.
    background Frame("gui/chat_bubble_right.svg", 15, 15)
    xalign 0.95 # Posisi gelembung di sisi kanan layar.
    padding (15, 15, 15, 15)
    xmaximum 600

# 3. Screen utama yang berfungsi sebagai komponen UI chat
screen group_chat_ui(messages):
    # 'tag' digunakan agar kita bisa dengan mudah menyembunyikan screen ini dengan 'hide chat'.
    tag chat

    # Latar belakang untuk UI Chat. Pilih salah satu dari opsi di bawah.
    # Opsi 1: Background gambar (pastikan file ada di folder /gui).
    add "gui/chat_background.svg"
    # Opsi 2: Latar belakang warna solid.
    # window:
    #     style "game_menu_background"
    # Opsi 3: Latar belakang buram (memerlukan transform 'blur_background').
    # add "bg [current_background]" at blur_background

    # Viewport memungkinkan konten untuk di-scroll jika lebih panjang dari layar.
    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        yinitial 1.0 # Otomatis scroll ke pesan terbaru di bagian bawah.

        # Vbox menumpuk elemen (gelembung chat) secara vertikal.
        vbox:
            style_group "chat"
            spacing 10 # Jarak vertikal antar gelembung chat.

            # Loop 'for' untuk menampilkan setiap pesan dari daftar 'messages' yang diberikan.
            for who, what, side in messages:
                # Frame berfungsi sebagai kontainer untuk setiap gelembung.
                frame:
                    # 'if' statement untuk memilih style gelembung berdasarkan 'side'.
                    if side == "right":
                        style "chat_bubble_right"
                    else:
                        style "chat_bubble_left"

                    # Vbox di dalam frame untuk menumpuk nama pengirim dan isi pesannya.
                    vbox:
                        spacing 5
                        text who style "chat_who"
                        text what

define r_chat = Character("[mc_name]", ctc=None, what_style="chat_what", window_style="chat_window")
define m_chat = Character("Mila", ctc=None, what_style="chat_what", window_style="chat_window")
define d_chat = Character("Diego", ctc=None, what_style="chat_what", window_style="chat_window")

# Store character profiles
label profile:
    $ profile_raka = store.character_profiles["Raka"]
    $ profile_luna = store.character_profiles["Luna"]
    $ profile_nara = store.character_profiles["Nara"]
    $ profile_Tiffany = store.character_profiles["Tiffany"]
    $ profile_Diego = store.character_profiles["Diego"]
    $ profile_Arga = store.character_profiles["Arga"]
    $ profile_Mila = store.character_profiles["Mila"]
    $ profile_Ben = store.character_profiles["Ben"]
    $ profile_Rilandy = store.character_profiles["Rilandy"]
    $ profile_npc = store.character_profiles["npc"]
    return

label unlock_character(char_name, char_desc, char_image):
    call screen character_card(char_name, char_desc, char_image)
    return


label start:
    call name_input
    jump scene_1
label scene_1:
    scene auditorium
    with fade

    play music "bgm/outsideclass.mp3" fadein 1.0

    "Hari pertama masuk SMA, bagi [mc_name] ini adalah awalan dari hidupnya yang sudah lama berhenti sejenak."
    "Semua orang mengatakan ini adalah waktu yang tepat untuk aku menghabiskan masa mudaku. Sepertinya Aku akan mencoba mendengarkan apa kata mereka, melakukan hal yang seharusnya aku lakukan sebagai remaja umum selayaknya siswa SMA."
    "Aku berharap semuanya akan berjalan dengan baik dan sesuai dengan apa yang aku inginkan."

    show raka normal mirror at left_terang
    with dissolve
    r "Permisi pak, mau tanya. Ruang auditorium dimana ya.."

    show raka normal mirror at left_redup
    show npc at right_terang
    npc "Disana dek."

    show raka normal mirror at left_terang
    show npc at right_redup
    r "Terimakasih pak"

    hide raka normal mirror
    hide npc


    "[mc_name] berjalan menuju ruang auditorium."

    show raka normal mirror at left_terang
    r "Hari pertama ini sangat menegangkan ya…"
    r "Aku kepikiran deh, aku bisa ga ya cepat beradaptasi dan dapat teman baru?"
    r "Hmmm..." # play sfx langkah kaki
    r "Loh? Kok aku jadi deg-deg an ya…" #play sfx detak jantung
    hide raka normal mirror

    "Luna datang menghampiri raka"

    show luna normal at right_terang
    l "Hai!"

    show raka kaget mirror at left_terang
    show luna normal at right_redup
    r "...."

    hide raka kaget mirror
    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "{i}Wah! Dia siapa? Cantik banget…{/i}" #dialog dalam hati
    r "{i}Aku gabisa berhenti menatapnya… dia…Ceria, penuh semangat, dan ramah banget…{/i}" #dialog dalam hati
    r "oh! hai?"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Boleh kenalan ga? Nama kamu siapa?"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Eh- boleh… aku [mc_name]"
    r "Kalau nama kamu?"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Luna! Namaku Luna…"

    #play sfx testing mic

    hide raka normal mirror
    hide luna normal
    show nara normal at right_terang
    n "Halo semuanya, nama saya Nara sebagai perwakilan dari OSIS."
    n "Ada pemberitahuan, bagi peserta didik baru SMA Harapan Bangsa,"
    n " di mohon untuk mencatat informasi yang tertera di mading sekolah sebagai arahan mengenai kegiatan MPLS sekolah kami."

    #play sfx kericuhan anak-anak

    hide nara normal
    show raka normal mirror at left_terang
    r "{i}Eh? Dia liat ke arahku kah? Dia ngeliatin aku bukan? Apa aku terlalu percaya diri? Ahh ga mungkin lah!{/i}"
    r "{i}Tapi- dia ga berhenti menatap ke arahku…{/i}"

    hide raka normal mirror
    show nara normal at right_terang
    n "Baik, itu saja informasi yang harus saya sampaikan. Terimakasih."

    hide nara normal
    show raka normal mirror at left_terang
    r "{i}Oh, ternyata benar, dia tidak melihat ke arahku. Haha, aku ini terlalu pede.{/i}"
    r "{i}Tapi- kalau dilihat-lihat, kakak itu menarik sih. Cantik juga…{/i}"
    hide raka normal mirror
        #stop music fadeout 1.0
    if not unlocked_nara:
        $ unlocked_nara = True
        call unlock_character("Nara", "Anggota OSIS yang kalem dan berwibawa.", "card nara")
    if not unlocked_luna:
        $ unlocked_luna = True
        call unlock_character("Luna", "Gadis ceria dan penuh semangat.", "card luna")

    jump scene_2

label scene_2:
    scene bg_kantin_gate with fade

    play music "bgm/friendstheme.mp3" fadein 1.0

    "[mc_name] berjalan menuju arah kantin sekolahnya dan mencari kedua sahabatnya yang selalu bersama dengannya sejak SMP hingga saat ini."
    "Kedua sahabat nya ini adalah sepasang kekasih yang sudah menjalin hubungan asmara sejak SMP hingga saat ini."
    "Bagi [mc_name], kedua sahabatnya ini bagaikan rumah yang utuh dan selalu melindunginya. [mc_name] sangat menyayangi kedua sahabatnya itu."
    
    play sound "shout.ogg"

    show diego normal at right_terang
    d "[mc_name]!!!"

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Siniiii!"

    hide diego normal
    hide mila normal mirror

    "[mc_name] menghampiri Diego dan Mila"

    show raka normal mirror at left_terang
    r "Eh- itu mereka"
    r "Diegoo! Milaa!"
    hide raka normal mirror

    scene bg_kantin_table with fade
    "Diego dan Mila sudah berada di kantin, menunggu [mc_name] agar dapat makan siang bersama-sama."
    "[mc_name] berlari menghampiri kedua sahabatnya yang berdiri di depan meja makan kantin dan menunggunya tiba."
    "[mc_name], Diego dan Mila duduk di meja makan kantin dan berbincang satu sama lain."

    show mila normal at right_terang
    m "Gimana hari pertama kamu [mc_name]?"

    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Biasa aja sih, gaada yang seru."

    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Ah iya? Kok gitu sih…"

    hide raka normal mirror
    show diego normal mirror at left_terang
    show mila normal at right_redup
    d "Masa sih? Ga ada ketemu cewek gitu?"

    show mila normal at right_terang
    show diego normal mirror at left_redup
    m "Diego! Apaansih." #pake emote sebel

    hide diego normal mirror
    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Eh- hehehe… Ada sih…"

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Hah? Serius? Siapa?!"

    menu:
        "Ceritain Luna":
            jump scene_2luna
        "Ceritain Nara":
            jump scene_2nara
        "Gak cerita":
            jump scene_2rahasia  

label scene_2luna:

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Tadi ada cewe rambutnya pirang, cantik banget deh…"
    r "Terus dia ramah dan ceria gitu orangnya, seolah-olah punya banyak energi seharian."

    hide diego normal
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Oh iya? Kayaknya tadi aku lihat deh, emang cantik banget tuh.."

    hide raka normal mirror
    show diego normal mirror at left_terang
    show mila normal at right_redup
    d "Eh- emang ada? Kok aku ga liat sih" #pake emote kecewa

    show mila normal at right_terang
    show diego normal mirror at left_redup
    m "Kenapa kecewa gitu mukanya?! dih cantik dikit langsung gitu" #pake nada kesal atau emote masih kecewa

    hide diego normal mirror
    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Siapa namanya?"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Kenapa harus ditanya?" #pake emote sinis

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Namanya luna"

    hide mila normal mirror
    show diego normal mirror at left_terang
    show raka normal at right_redup
    d "Namanya cantik deh…"

    hide raka normal
    show mila normal at right_terang
    show diego normal mirror at left_redup
    m "Ribut yuk?" #pake muka jengkel

    hide diego normal mirror
    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Ah sudahlah..."

    hide raka normal mirror
    hide mila normal

    "[mc_name] meninggalkan Diego dan Mila di kantin" #play suara langkah kaki
    if not unlocked_diego:
        $ unlocked_nara = True
        call unlock_character("Diego", "(deskripsi diego)", "card diego")
    if not unlocked_mila:
        $ unlocked_luna = True
        call unlock_character("MIla", "(deskripsi mila)", "card mila")
    jump scene_3

label scene_2nara:

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Kalian lihat ga sih cewe yang kasih pengumuman di auditorium tadi?"

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Oh... itu! aku merhatiin dia tadi, yang tinggi dan cantik itu kan?"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Merhatiin banget nih, kayakya sampai detail begitu" #pake emote sinis

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Oh ya.. jelas! dia cantik banget sih emang…"

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Terserah deh." #masih pake emote sinis

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Siapa namanya?"

    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Aku gatau sih belum kenalan…"

    hide mila normal mirror
    show diego normal mirror at left_terang
    show raka normal at right_redup
    d "Masa gatau sih.. Nama dia Nara, perwakilan dari osis."

    hide raka normal
    show mila normal at right_terang
    show diego normal mirror at left_redup 
    m "Kok kamu tau sih?! [mc_name] aja gatau, kok kamu bisa tahu?!"

    show diego normal mirror at left_terang
    show mila normal at right_redup
    d "Kan tadi dia ngasih tau di depan. Gimana sih?"

    show mila normal at right_terang
    show diego normal mirror at left_redup 
    m "Oh iya, kan kamu merhatiin dia banget. Si paling perhatian." #pake muka sarkas

    hide diego normal mirror
    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Ah sudahlah.."
    hide raka normal mirror
    hide mila normal

    "[mc_name] meninggalkan Diego dan Mila di kantin"#play suara langkah kaki
    if not unlocked_diego:
        $ unlocked_nara = True
        call unlock_character("Diego", "(deskripsi diego)", "card diego")
    if not unlocked_mila:
        $ unlocked_luna = True
        call unlock_character("MIla", "(deskripsi mila)", "card mila")
    jump scene_3

label scene_2rahasia:

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Rahasia!."

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Yah kenapa? Kasih tau dong!" #pake emote kecewa

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Diego apaansi. Itukan privasi dia, biarin aja. Lagi pula, kenapa sih pengen tau banget?" #pake emote bete

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Aku penasaran siapa ceweknya."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Giliran cewek aja cepet."

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Ah sudahlah.."
    hide raka normal
    hide mila normal mirror

    "[mc_name] meninggalkan Diego dan Mila di kantin" #play suara langkah kaki

    if not unlocked_diego:
        $ unlocked_nara = True
        call unlock_character("Diego", "(deskripsi diego)", "card diego")
    if not unlocked_mila:
        $ unlocked_luna = True
        call unlock_character("MIla", "(deskripsi mila)", "card mila")
    jump scene_3

label scene_3:
    scene bg class with fade  # <- Ganti ini jika punya background kelas, misal: "bg_class.jpg"

    play music "bgm/onlyclass.mp3" fadein 1.0

    "Hari demi hari telah berlalu, [mc_name] menjalani kegiatan awal SMA nya bersama dengan Diego dan Mila yang sudah menjadi sahabatnya selama ini."
    "[mc_name] berusaha beradaptasi sebisanya, hingga pada akhirnya masa MPLS telah usai."
    "Peserta didik sudah memulai aktivitas sekolah seperti biasa. Kelas akan segera dimulai."

    show raka normal mirror at left_terang
    with dissolve
    r "{i}ini gurunya mana sih kok gaada? Telat kali ya…{/i}"

    hide raka normal mirror with fade
    show luna normal at left_terang
    "Luna berbincang dengan temannya" #tambah sfx percakapan

    hide luna normal with fade
    show raka kaget mirror at left_terang
    r "{i}Eh- itu luna bukan ya?{/i}"

    hide raka kaget mirror
    show raka normal mirror at left_terang
    r "{i}Ternyata kita sekelas ya, hmm.{/i}"

    menu:
        "panggil luna":
            jump scene_3a
        "ga panggil luna":
            jump scene_3b


label scene_3a:
    show raka normal mirror at left_terang
    r "Luna..."

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Eh- iya kenapa [mc_name]?"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "{i}Aduh aku harus ngomong apa ya?{/i}" 
    r "{i}Aku tanya sekolah lamanya aja kali ya? Eh jangan. Makanan kesukaannya? Jangan. Film kesukaannya? Jangan juga. Apa dong?{/i}" 

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "[mc_name]? Kok bengong?" 

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Eh- Gapapa sih, panggil aja."

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Eh? Gitu doang...? Hehe, kirain kenapa."
    l "{i}[mc_name] kenapa ya? Tiba-tiba manggil…{/i}" 

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Oh iya! Luna!"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Iya [mc_name]? Kenapa nih? Panggil doang?"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Hahaha, engga kok!"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Lalu? Kenapa [mc_name]? Ada yang bisa Luna bantu?"

    show raka smile mirror at left_terang 
    show luna normal at right_redup
    r "Aku cuma mau bilang kamu cantik Luna."

    show luna shock at right_terang 
    show raka smile mirror at left_redup
    l "Eh?"
    
    show luna malu at right_terang 
    l "Ma- Makasih ya [mc_name]...."

    show raka smile mirror at left_terang
    show luna malu at right_redup
    r "Kenapa makasih Luna?"

    show luna shock at right_terang
    show raka smile mirror at left_redup
    l "Karena kamu memuji aku?"

    show raka smile mirror at left_terang
    show luna shock at right_redup
    r "Aku tidak memuji kamu Luna, memang faktanya kalau kamu cantik. Semua orang tidak bisa berhenti memandang kamu."

    show luna shock at right_terang
    show raka smile mirror at left_redup
    l "*gasp*"
    l "[mc_name]?"

    show raka smile mirror at left_terang
    show luna shock at right_redup
    r "Iya Luna?"

    "Luna mengeluarkan tiga bungkus permen manis yang tersimpan di dalam tempat pensil mungil berwarna pink nya itu."

    show luna smile at right_terang 
    show raka smile mirror at left_redup
    l "Ini permen buat kamu."

    show raka shock mirror at left_terang 
    show luna smile at right_redup
    r "Wah! Ini buat aku? Kenapa?"

    show luna smile at right_terang
    show raka shock mirror at left_redup
    l "Karena kamu udah bikin aku senang hari ini. Makasih ya [mc_name]!"

    show raka shock mirror at left_terang
    # play sound "suara_deg_degan.ogg" 
    "Deg"
    
    # play music "lagu_lovely.ogg" with fadeout 1.0 fadein 1.0
    show raka shy mirror at left_terang with dissolve 
    show luna smile at right_redup

    show luna smile at right_terang
    show raka shy mirror at left_redup
    l "Aku senang bisa berkenalan dengan kamu [mc_name]!"

    hide luna
    hide raka
    with dissolve
    
    show tiffany normal at center 
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."
    
    hide tiffany normal
    
    $ luna_hearts += 1

    if not unlocked_tiffany:
        $ unlocked_tiffany = True
        call unlock_character("Tiffany", "(deskripsi tiffany)", "card tiffany")

    jump scene_4

label scene_3b:
    show raka normal mirror at left_terang
    r "{i}Kenapa ga aku panggil aja ya tadi? Siapa tau dia notice aku.{/i}" 
    r "{i}Mungkin belum saatnya. Semoga nanti masih ada kesempatan ngobrol.{/i}" 

    hide raka normal mirror
    with dissolve

    show tiffany normal at center
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."
    t "Apa kalian semua sudah tau, ibu disini mengajar mata pelajaran apa?"

    "Seluruh kelas terdengar bergumam, lalu satu suara terdengar."
    "???" "Bahasa!" 

    show tiffany normal at center
    t "Tidak tepat!"
    t "Ada lagi yang mau tebak?"

    show luna normal at right_terang 
    show tiffany normal at left_terang 
    l "Matematika?"

    show tiffany normal at left_terang
    show luna normal at right_redup
    t "Tidak tepat. Apa kalian semua tidak melihat jadwal? Bagaimana kalian akan melanjutkan pelajaran jika tidak melihat jadwal?!"

    show luna normal at right_terang
    show tiffany normal at left_redup
    l "Oh benar juga!"
    
    "Luna mengeluarkan selembar kertas yang berisikan jadwal mata pelajaran kelasnya."
    l "Kimia!"

    show tiffany smile at left_terang 
    show luna normal at right_redup
    t "Tepat sekali! Siapa namamu?"

    show luna normal at right_terang
    show tiffany smile at left_redup
    l "Luna!"

    show tiffany smile at left_terang
    show luna normal at right_redup
    t "Baik Luna, Karena kamu sudah menjawab pertanyaannya, bagaimana kalau kamu jadi ketua kelas ini? Apa yang lain setuju?"
    
    "???" "Setuju!"

    "Luna berdiri dari kursi kelasnya, lalu membungkukkan badannya."
    show luna smile at right_terang
    show tiffany smile at left_redup
    l "Baik, mohon kerjasamanya ya, semuanya!"
    
    hide luna
    hide tiffany
    
    show raka normal mirror at center
    r "{i}Luna lucu banget…{/i}" 
    hide raka

    show tiffany normal at center
    t "Sekarang, siapa yang mau jadi wakil ketua kelas?"

    "Kelas seketika menjadi hening."
    "..."
    "Tidak ada satupun yang berani mengajukan dirinya untuk menjadi wakil ketua kelas dan berpartner dengan Luna."

    show luna normal at right_terang
    show tiffany normal at left_terang
    t "Kalau tidak ada yang mau mengajukan diri, ibu akan minta Luna untuk menunjuk salah satu dari kalian sebagai wakil bagi Luna!"
    
    "Tiffany menunjuk Luna, memberikan sinyal kepada Luna untuk segera memilih salah satu anak murid lainnya yang akan menjadi partnernya sebagai wakil ketua kelas."
    
    show luna normal at right_terang
    show tiffany normal at left_redup
    l "Luna pilih…"

    "Tatapan mata Luna langsung tertuju kepada [mc_name] yang duduk di belakang kelas seolah-olah sudah menargetkan bahwa [mc_name] lah yang akan menjadi partner nya sebagai wakil ketua kelas."
    l "[mc_name]! Luna pilih [mc_name] untuk jadi wakil ketua kelas!"
    
    show raka shock mirror at left_terang
    show luna normal at right_redup
    show tiffany normal at center 
    r "*gasp*"

    show tiffany smile at center
    show raka shock mirror at left_redup
    show luna normal at right_redup
    t "Baik Luna, terimakasih atas pilihannya."
    t "Mari kita berikan tepuk tangan dulu untuk teman kita Luna dan [mc_name] yang sekarang secara resmi sudah menjadi ketua kelas dan wakil ketua kelas."

    "Seluruh kelas bertepuk tangan."
    "Luna kembali duduk di kursinya dan menatap ke arah [mc_name] lalu tersenyum kepada [mc_name]."
    
    show luna smile at right_terang
    show raka normal mirror at left_redup
    
    show raka smile mirror at left_terang
    show luna smile at right_redup

    hide raka
    hide luna
    hide tiffany
    with dissolve
    
    if not unlocked_tiffany:
        $ unlocked_tiffany = True
        call unlock_character("Tiffany", "(deskripsi tiffany)", "card tiffany")

    jump scene_4


label scene_4:
    "Jam istirahat telah tiba. Bel sekolah berbunyi nyaring, menandakan waktunya siswa beristirahat sejenak dari rutinitas belajar yang padat."
    "[mc_name] berdiri dari kursinya, merapikan buku-bukunya, lalu berjalan keluar kelas."
    
    scene lorong 
    with fade
    
    show raka normal mirror at center
    
    "Dalam perjalanannya menuju kantin, [mc_name] melewati ruang perpustakaan yang terletak di sisi kanan lorong."
    "Pandangannya sempat tertuju pada rak-rak buku yang tampak rapi dari balik kaca jendela besar."
    
    show nara normal at right with easeinright
    show raka normal mirror at left
    
    "Di depan pintu, terdapat Nara yang sedang berjalan menuju perpustakaan tersebut."

    r "{i}Hm… udah istirahat nih, pengen ke kantin sih.. Tapi belum ada teman, aku sama Diego dan Mila aja deh..{/i}"
    r "{i}Eh- itu bukannya kakak kelas yang tadi ya?.. Siapa namanya.. Oh iya Nara! Aku sapa ga ya?{/i}"

    menu:
        "Sapa Nara":
            jump scene_4a
        "Gak Sapa":
            jump scene_4_tidak_sapa

label scene_4_tidak_sapa:
    r "{i}Ah, sudahlah. Jangan ganggu, mending langsung ke kantin aja.{/i}"
    hide nara with easeoutright
    "[mc_name] memutuskan untuk tidak menyapa dan langsung melanjutkan perjalanannya."
    jump scene_4_ke_kantin_versi_buruk 

label scene_4a:
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Halo… kak Nara ya? Yang tadi di auditorium."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Iya. Kenapa ya?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Kenalin kak, Aku [mc_name] dari kelas 10 MIPA 5. Kalau kakak kelas apa?"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh, aku 11 MIPA 5."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Wah! sama dong, kakak lagi apa disini?"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh, aku cuman mau baca novel sih."

    menu:
        "Wah! Kakak suka baca novel juga?":
            jump scene_4_novel_convo
        "Aku fikir kaka mau rapat":
            jump scene_4_rapat_convo
        "Sama siapa?":
            jump scene_4_siapa_convo

label scene_4_novel_convo:
    # Giliran Raka berbicara.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Wah! Kakak suka baca novel juga?"

    # Giliran Nara berbicara.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Iya, kamu baca novel?"

    # Giliran Raka berbicara.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Baru-baru ini sih kak, Ada rekomendasi ga ka?"

    # Giliran Nara berbicara.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Kamu sukanya genre apa?"

    # ... dan seterusnya, polanya sama untuk setiap dialog.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Biasanya baca nya romance sih kak."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh aku tahu yang bagus nih, Love in Bekasi."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oh iya, aku juga pernah denger juga."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Nah itu, seru! Cobain deh.."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Kalau kakak sukanya genre apa?"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Aku sukanya fantasy."
    n "Tapi kadang juga baca self development sih."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Wah! fantasy pasti kakaknya baca series Pluto dari Tiro Lio."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Iya! Kamu bener."
    n "Aku koleksi semua seriesnya!"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "{i}Padahal aku asal sebut judul novel yang Mila punya.{/i}"
    r "Wah! aku baru sampai buku pertama boleh pinjam buku keduanya ga?"
    r "Aku masih penasaran banget soalnya."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Boleh, tapi aku ga bawa bukunya. Gimana kalau nanti kamu ke kelas aku aja sepulang sekolah?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Boleh banget tuh kak!"
    r "Oke kak, aku duluan ya.. Udah ditunggu teman soalnya."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Aku tunggu ya..."

    $ nara_hearts += 1

    "Setelah berbincang dengan Nara, [mc_name] bergegas menuju kantin."
    hide nara
    hide raka
    with fade
    jump scene_4_ke_kantin_versi_baik

label scene_4_rapat_convo:
    # Raka yang bertanya.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Aku fikir kaka mau rapat."

    # Nara menjawab.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Engga sih."
    n "Aku duluan ya."

    hide nara with easeoutright

    # Raka merespon dalam hati, jadi dia tetap terang.
    show raka normal mirror at left_terang
    r "Oke kak."
    "Percakapan berakhir dengan canggung, dan [mc_name] melanjutkan perjalanannya ke kantin."
    jump scene_4_ke_kantin_versi_buruk

label scene_4_siapa_convo:
    # Raka yang bertanya.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Sama siapa?"

    # Nara menjawab dengan ketus.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Sama siapapun itu, bukan urusan kamu!"

    # Raka merespon.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oh iya kak maaf."

    $ nara_hearts -= 1

    "Nara pergi tanpa berkata-kata lagi, meninggalkan [mc_name] yang kebingungan."
    hide nara with easeoutright
    "[mc_name] merasa sedikit menyesal dan melanjutkan perjalanan ke kantin."
    jump scene_4_ke_kantin_versi_buruk

label scene_4_ke_kantin_versi_baik:
    scene kantin
    with fade

    # Menampilkan semua karakter, awalnya semua bisa dibuat redup.
    show diego normal at left_redup
    show mila normal at right_redup
    show raka normal at center_redup

    # Saatnya Diego bicara, jadi buat dia terang, yang lain redup.
    show diego at left_terang
    d "Kok lama banget sih keluarnya?"

    # Raka menjawab. Raka terang, lainnya redup.
    show raka normal at center_terang
    show diego normal at left_redup
    show mila normal at right_redup
    r "Hehe, soalnya…"

    menu:
        "Ceritakan ketemu Nara":
            jump scene_4_cerita_nara
        "Gak usah cerita":
            jump scene_4_gak_cerita_nara

label scene_4_cerita_nara:
    # Raka berbicara.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Tadi aku ketemu seseorang."

    # Diego merespon.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Siapa lagi.. Tuh?"

    # Mila merespon.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Coba cerita."

    # Raka melanjutkan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Jadi aku ketemu Nara yang anggota OSIS itu loh.."

    # Diego dan Mila merespon bersamaan, kita buat keduanya terang.
    show diego at left_terang
    show mila at right_terang
    show raka at center_redup
    d "Oh.. Kak Nara.."
    m "Oh.. Kak Nara.."

    # Mila bertanya.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Kak Nara Kenapa?"

    # Raka menjawab.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Kayaknya aku tertarik deh, sama kak Nara."

    # Diego dan Mila kaget bersamaan.
    show diego at left_terang
    show mila at right_terang
    show raka at center_redup
    d "Hah!.. Serius?!.."
    m "Hah!.. Serius?!.."

    # Raka meyakinkan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Iya serius!... Ternyata kak Nara orangnya suka baca novel, bantuin aku dong.."

    # Diego bertanya.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Bantuin gimana tuh?"

    # Mila menyahut.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Bantuin deketin lah, gimana sih kamu!"

    # Diego merespon.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Hehehe."

    # Raka bertanya.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Nanti aku mau ke kelas Kak Nara untuk pinjam bukunya. Kira-kira aku harus apa lagi ya?"

    # Diego memberi saran.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Menurutku ya, setelah kamu baca bukunya, coba deh kamu ceritakan secara berkala ke Kak Nara. Supaya, Kak Nara tahu kalau kamu benar-benar baca buku dia."

    # Mila menimpali.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Aku setuju sama Diego, tapi, jangan terlalu gegabah. Ga semua cewek suka langsung di deketin secara berkala."

    # Diego setuju.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Hm.. bener juga."

    # Mila bertanya.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Emang buku apa yang dibaca sama kak Nara?"

    # Raka menjawab.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Nah! Bukunya itu yang sama persis kayak yang kamu baca Mil…"

    # Mila bingung.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Hah? Yang mana? Banyak loh buku yang ku baca.."

    # Raka mencoba menjelaskan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Yang kayak nama planet itu loh Mil…"

    # Diego menebak.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Pluto ga sih Mil? Yang kamu pajang itu."

    # Mila teringat.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Oh astaga! Yang itu."

    # Raka memastikan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Nah! Pokoknya itu lah. Ceritain dong Mil itu kayak gimana…"

    # Diego protes.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Ih, waktu itu aku tanya ceritanya malah disuruh baca sendiri. Curang!"

    # Mila menyuruh Diego diam.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Diem dulu deh kamu Diego! Ini lagi serius!"
    # Mila mulai bercerita.
    m "Jadi, ceritanya tentang seorang character yang punya kekuatan super, tepatnya kekuatan menghilang. Tapi, dia sembunyikan kekuatan itu dari semua orang termasuk orang tuanya sendiri."
    m "Lalu, di suatu hari, ada temen sekelasnya yang bisa dibilang paling pintar diantara yang lain. Dia mulai curiga dengan si karakter utama ini, kalau karakter ini punya kekuatan."
    m "Nah! Di buku edisi pertama ini, akan menceritakan hal tadi dan ternyata di dunia mereka, ga hanya pemeran utamanya yang punya kekuatan super."

    # Raka merespon cerita Mila.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Menarik ya… pantesan aja Kak Nara suka."
    r "Siapa nama karakter utamanya Mil?"

    # Mila mau menjawab, tapi dipotong Diego.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Nam-"

    # Diego memotong.
    show diego at left_terang
    show mila at right_redup
    show raka at center_redup
    d "Namanya Raya."

    # Mila melengkapi.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Dan nama karakter pintar tadi adalah Alri."

    # Raka bertanya lagi.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Terus, selanjutnya aku harus apa?"

    # Mila memberi saran.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Nanti kamu ke kelas dia sepulang sekolah kan?"

    # Raka mengiyakan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Iya…"

    # Mila memberi saran terakhir.
    show mila at right_terang
    show diego at left_redup
    show raka at center_redup
    m "Nanti ajak pulang bareng aja..."

    # Diego setuju.
    show diego at left_terang
    show raka at center_redup
    show mila at right_redup
    d "Setuju!"

    "Bel masuk pun berbunyi, mengakhiri waktu istirahat mereka."
    jump scene_5

label scene_4_gak_cerita_nara:
    # Raka berbicara.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Aku tadi ke toilet dulu."

    # Mila merespon.
    show mila at right_terang
    show raka at center_redup
    show diego at left_redup
    m "Yaudah kalian mau pesen apa?"

    # Diego menjawab.
    show diego at left_terang
    show mila at right_redup
    show raka at center_redup
    d "Aku ayam geprek."

    # Raka menjawab.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Aku samain aja deh."

    # Mila berkomentar.
    show mila at right_terang
    show raka at center_redup
    show diego at left_redup
    m "Kebiasaan."

    "Mereka pun makan bersama hingga bel masuk kembali berbunyi."
    jump end_of_day

label scene_4_ke_kantin_versi_buruk:
    scene kantin
    with fade

    # Menampilkan karakter. Diego akan bicara pertama, jadi dia dibuat terang.
    show diego at left_terang
    show mila at right_redup
    show raka at center_redup

    d "Kok lama banget sih keluarnya?"

    # Raka menjawab.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Aku tadi ke toilet dulu."

    # Mila bertanya.
    show mila at right_terang
    show raka at center_redup
    show diego at left_redup
    m "Yaudah kalian mau pesen apa?"

    # Diego memesan.
    show diego at left_terang
    show mila at right_redup
    show raka at center_redup
    d "Aku ayam geprek."

    # Raka memesan.
    show raka at center_terang
    show diego at left_redup
    show mila at right_redup
    r "Aku samain aja deh."

    # Mila berkomentar.
    show mila at right_terang
    show raka at center_redup
    show diego at left_redup
    m "Kebiasaan."

    "Mereka pun makan bersama hingga bel masuk kembali berbunyi."
    jump end_of_day

label scene_5:
    scene kelas_nara
    with fade

    "Bel sekolah telah berbunyi, menandakan sudah tiba saatnya pulang sekolah."
    "Sebelum bergegas pulang ke rumah, [mc_name] menyempatkan diri mengunjungi kelas Nara untuk meminjam buku novelnya yang sudah dijanjikan."

    # Nara dan Arga sudah ada di scene, kita buat mereka redup karena belum ada dialog.
    show nara normal at right_redup
    show arga normal at center_redup

    r "{i}(Hatiku berdegup kencang, aku pun melihat jendela kelas kak Nara namun, disana aku melihat dia sedang berbicara akrab dengan satu cowo.){/i}"
    r "{i}Itu siapanya kak nara ya?{/i}"

    # Raka masuk dan memulai percakapan.
    show raka normal mirror at left_terang
    r "Halo. Kak Nara."

    # Nara merespon.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    show arga normal at center_redup
    n "Eh- halo."

    # Raka berbicara.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    show arga normal at center_redup
    r "Aku mau ambil buku yang tadi kakak pinjamkan…"

    # Nara menjawab.
    show nara normal at right_terang
    show raka normal mirror at left_redup
    show arga normal at center_redup
    n "Oh iya, Ini bukunya.. Jangan lupa dibaca ya…"

    # Raka merespon.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    show arga normal at center_redup
    r "Pasti dong kak!"

    # Arga bertanya pada Nara.
    show arga normal at center_terang
    show nara normal at right_redup
    show raka normal mirror at left_redup
    a "Siapa dia, Ra?"

    # Nara menjelaskan ke Arga.
    show nara normal at right_terang
    show arga normal at center_redup
    show raka normal mirror at left_redup
    n "Oh ini teman baruku. Adik kelas kita, tadi ketemu di perpustakaan."

    # Arga merespon.
    show arga normal at center_terang
    show nara normal at right_redup
    show raka normal mirror at left_redup
    a "Oh temen doang."

    play sound "suara_deg.ogg"
    # Monolog Raka, jadi Raka tetap terang.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    show arga normal at center_redup
    r "{i}Hah? Mereka pacaran?!{/i}"

    # Nara berbicara lagi.
    show nara normal at right_terang
    show arga normal at center_redup
    show raka normal mirror at left_redup
    n "Oh iya, [mc_name]. Kenalin ini temen aku, dia namanya Arga…"

    # Arga memperkenalkan diri.
    show arga normal at center_terang
    show nara normal at right_redup
    show raka normal mirror at left_redup
    a "Iya kenalin aku Arga. Ketua OSIS di sekolah ini."

    # Monolog Raka, lalu dia merespon Arga.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    show arga normal at center_redup
    r "{i}Ternyata hanya teman. Tapi kok deket banget ya? Apa jangan-jangan si Arga ini juga suka sama Kak Nara?{/i}"
    r "Halo kak, aku [mc_name] dari 10 MIPA 5. Salam kenal ya!"

    # Raka mencoba bicara, tapi dipotong.
    r "Oh iya kak mau ke toko buk-"

    # Arga memotong, mengajak Nara.
    show arga normal at center_terang
    show nara normal at right_redup
    show raka normal mirror at left_redup
    a "Ra, jadi kan kita makan bareng?"

    # Nara menjawab Arga.
    show nara normal at right_terang
    show arga normal at center_redup
    show raka normal mirror at left_redup
    n "Jadi dong.. Kan udah janji."
    # Nara bertanya pada Raka.
    n "Tadi kenapa [mc_name]?"

    # Raka merespon.
    show raka normal mirror at left_terang
    show nara normal at right_redup
    show arga normal at center_redup
    r "Oh gapapa kak, gajadi."

    # Arga mengajak berangkat.
    show arga normal at center_terang
    show nara normal at right_redup
    show raka normal mirror at left_redup
    a "Yuk berangkat sekarang, nanti takutnya penuh."

    # Nara setuju dan pamit.
    show nara normal at right_terang
    show arga normal at center_redup
    show raka normal mirror at left_redup
    n "Yuk! Duluan ya [mc_name]."

    hide arga with easeoutright
    hide nara with easeoutright

    # Raka merespon sendiri.
    show raka normal mirror at left_terang
    r "Iya kak. Hati-hati ya.. Oh iya, makasih juga bukunya."

    # Catatan: Nara sudah hilang dari layar, tapi dia bicara.
    # Agar logis, kita bisa tampilkan dia sebentar lalu hilangkan lagi.
    show nara normal at right_terang
    n "Oh, tenang aja!"
    hide nara

    # Monolog Raka.
    show raka normal mirror at left_terang
    r "{i}Yah, padahal tadi seru kalau pergi bareng sambil ngobrolin novel Pluto nya Mila.{/i}"

    hide raka
    with fade


    scene bus
    play music "lagu_sedih.ogg" # Ganti dengan nama file musik yang melankolis
    with fade

    "Di dalam bus perjalanan pulang sekolah, [mc_name] duduk pada kursi belakang bus dan menyandarkan kepalanya ke kaca bus."
    "Hujan turun dan cuaca diluar sedang tidak cerah. [mc_name] merenung dan memikirkan apa yang ia lihat di kelas 11 MIPA 5 tadi."
    # ... (Tidak ada perubahan di bagian monolog dan narasi)
    # ...

    stop music fadeout 2.0
    scene apartemen_raka # Ganti dengan nama background apartemen Raka
    with fade

    # ... (Tidak ada perubahan di bagian narasi)
    # ...

    r "(menghela nafas) Huft, tadi cara bikin soto ayam gimana ya? Dulu mama gimana ya buatnya? Males banget harus nanya lagi."
    r "Ah iya! Minta Mila dan Diego aja kesini, Diego kan jago masak! Eh- masakannya Mila kan juga enak banget! Wah beruntung banget sih aku punya mereka!"

    "[mc_name] mengambil telepon genggamnya dan memanggil Diego dan Mila secara online melalui group chat yang mereka bertiga miliki."
    # ... (Dialog chat tidak perlu transform karena karakter belum muncul di layar)
    # ...
    r "Mila! Datang ke rumahku ya! Aku Lapar!"
    m "Kasian nya, haha. Baiklah, aku kesana ya, tunggu aku!"
    d "Manggil Mila, tapi tetap saja aku yang masak. Menyebalkan."
    # ... dst

    "Diego dan Mila berangkat bersama menuju apartemen [mc_name]."
    "Sesampainya di apartemen [mc_name], Diego bergegas memasak dengan bahan makanan yang sudah dibawa oleh Mila."
    "Diego dan Mila memasak bersama, sedangkan [mc_name] hanya disana menyaksikan kedua sahabatnya yang sudah ia anggap sebagai kakanya itu memasak makan malam untuknya."

    # Karakter muncul. Diego akan bicara pertama, jadi dia yang terang.
    show diego senang at left_terang
    show mila smile at right_redup
    show raka normal at center_redup

    d "Sudah! Mari kita makan!"

    # Mila berbicara.
    show mila smile at right_terang
    show diego senang at left_redup
    show raka normal at center_redup
    m "[mc_name], tolong siapkan alat makannya ya."

    # Raka merespon dengan sprite berbeda.
    show raka senyum at center_terang
    show diego senang at left_redup
    show mila smile at right_redup
    r "Siap kakakku tercinta!"

    # Diego merespon dengan sprite berbeda.
    show diego kesal at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Kamu ga manggil aku kakak juga [mc_name]?! Aku kan kakakmu!!!"

    # Raka menjawab.
    show raka senyum at center_terang
    show diego kesal at left_redup
    show mila smile at right_redup
    r "Tidak! Tidak mau!"

    # Diego merespon dengan sprite berbeda.
    show diego smirk at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Aku sudah memasak makan malam untuk mu loh! Berterimakasihlah pada kakakmu ini!"

    # Raka menjawab.
    show raka senyum at center_terang
    show diego smirk at left_redup
    show mila smile at right_redup
    r "Hanya Mila yang ku anggap kakak! Terimakasih Mila! Kamu bukan kakakku Diego, kamu menggelikan!"

    # Diego merespon.
    show diego smirk at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Oh kamu begitu ya! Gausah makan!"

    "Diego memukul tangan [mc_name] yang hendak mengambil makanan di atas meja."

    # Raka merespon dengan sprite berbeda.
    show raka sad at center_terang
    show diego smirk at left_redup
    show mila smile at right_redup
    r "Mila tolong aku!"

    # Mila merespon.
    show mila smile at right_terang
    show raka sad at center_redup
    show diego smirk at left_redup
    m "Sama-sama [mc_name]! Kamu memang adikku yang terbaik!"

    # Diego merespon.
    show diego smirk at left_terang
    show raka sad at center_redup
    show mila smile at right_redup
    d "Tidak adil! Aku juga mau jadi kakak mu!"

    # Mila menengahi.
    show mila smile at right_terang
    show raka sad at center_redup
    show diego smirk at left_redup
    m "Sudah-sudah! Kita harus makan sekarang sebelum makanannya dingin. Kalian kakak adik termenyebalkan yang pernah ku lihat."


    # Akhir dari Scene 5
    hide raka
    hide diego
    hide mila
    with fade

    jump scene_6

label end_of_day:
    "Waktu di sekolah pun berakhir, dan [mc_name] pulang ke rumah seperti biasa."
    "Di dalam bus perjalanan pulang sekolah, [mc_name] duduk pada kursi belakang bus dan menyandarkan kepalanya ke kaca bus."
    "Bus telah sampai pada halte yang dituju oleh [mc_name]. [mc_name] melanjutkan perjalanan nya ke apartemen nya dengan berjalan kaki sambil mendengarkan lagu menggunakan earphone kabel yang selalu menemaninya dari SMP"
    "Setelah sampai di apartemennya, [mc_name] melanjutkan aktivitas kesehariannya seperti membersihkan rumah, masak, belajar dan lain sebagainya."
    "Namun, di tengah kegiatan memasaknya, [mc_name] merasa kesepian karena orang tua nya yang sudah tidak lagi bersama dan mereka sudah memiliki kehidupan masing-masing"

    r "(menghela nafas) Huft, tadi cara bikin soto ayam gimana ya? Dulu mama gimana ya buatnya? Males banget harus nanya lagi."
    r "Ah iya! Minta Mila dan Diego aja kesini, Diego kan jago masak! Eh- masakannya Mila kan juga enak banget! Wah beruntung banget sih aku punya mereka!"

    "[mc_name] mengambil telepon genggamnya dan berbicara Diego dan Mila secara online melalui group chat yang mereka bertiga miliki."

    window hide
    $ messages = []

    show screen group_chat_ui(messages)
    pause 1.0 

    $ messages.append(("[mc_name]", "Mila! Datang ke rumahku ya! Aku Lapar!", "right"))
    show screen group_chat_ui(messages)
    pause 1.0

    $ messages.append(("Mila", "Kasian nya, haha. Baiklah, aku kesana ya, tunggu aku!", "left"))
    show screen group_chat_ui(messages)
    pause 1.2

    $ messages.append(("Diego", "Manggil Mila, tapi tetap saja aku yang masak. Menyebalkan.", "left"))
    show screen group_chat_ui(messages)
    pause 1.0

    $ messages.append(("[mc_name]", "Hahaha, ayolah Diego. Aku sudah sangat lapar nih.", "right"))
    show screen group_chat_ui(messages)
    pause 1.0

    $ messages.append(("Diego", "Bilang dulu dengan lembut ke aku seperti kamu bilang ke Mila!", "left"))
    show screen group_chat_ui(messages)
    pause 1.5

    $ messages.append(("[mc_name]", "Gamau! Kenapa aku harus berbicara lembut kepadamu? Menggelikan!", "right"))
    show screen group_chat_ui(messages)
    pause 1.0

    $ messages.append(("Diego", "Aku kan kakak laki-lakimu!", "left"))
    show screen group_chat_ui(messages)
    pause 1.0

    $ messages.append(("[mc_name]", "SEJAK KAPAN KAMU JADI KAKAKKU?!", "right"))
    show screen group_chat_ui(messages)
    pause 1.2

    $ messages.append(("Diego", "KAMU SUDAH TIDAK SAYANG AKU LAGI?!", "left"))
    show screen group_chat_ui(messages)
    pause 1.2

    $ messages.append(("[mc_name]", "HANYA MILA YANG KU ANGGAP KAKAK! KAMU MENGGELIKAN DIEGO!", "right"))
    show screen group_chat_ui(messages)
    pause 1.5

    $ messages.append(("Diego", "AWAS KAMU YA! AKU KESANA SEKARANG!", "left"))
    show screen group_chat_ui(messages)
    pause 2.0 

    hide screen group_chat_ui

    window show

    "Diego dan Mila berangkat bersama menuju apartemen [mc_name]."
    "Sesampainya di apartemen [mc_name], Diego bergegas memasak dengan bahan makanan yang sudah dibawa oleh Mila."
    "Diego dan Mila memasak bersama, sedangkan [mc_name] hanya disana menyaksikan kedua sahabatnya yang sudah ia anggap sebagai kakanya itu memasak makan malam untuknya."

    show diego senang at left_terang
    show mila smile at right_redup
    show raka normal at center_redup
    d "Sudah! Mari kita makan!"

    show mila smile at right_terang
    show diego senang at left_redup
    show raka normal at center_redup
    m "[mc_name], tolong siapkan alat makannya ya."

    show raka senyum at center_terang
    show diego senang at left_redup
    show mila smile at right_redup
    r "Siap kakakku tercinta!"

    show diego kesal at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Kamu ga manggil aku kakak juga [mc_name]?! Aku kan kakakmu!!!"

    show raka senyum at center_terang
    show diego kesal at left_redup
    show mila smile at right_redup
    r "Tidak! Tidak mau!"

    show diego smirk at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Aku sudah memasak makan malam untuk mu loh! Berterimakasihlah pada kakakmu ini!"

    show raka senyum at center_terang
    show diego smirk at left_redup
    show mila smile at right_redup
    r "Hanya Mila yang ku anggap kakak! Terimakasih Mila! Kamu bukan kakakku Diego, kamu menggelikan!"

    # Diego merespon.
    show diego smirk at left_terang
    show raka senyum at center_redup
    show mila smile at right_redup
    d "Oh kamu begitu ya! Gausah makan!"

    "Diego memukul tangan [mc_name] yang hendak mengambil makanan di atas meja."

    # Raka merespon (dengan sprite baru).
    show raka sad at center_terang
    show diego smirk at left_redup
    show mila smile at right_redup
    r "Mila tolong aku!"

    # Mila menjawab.
    show mila smile at right_terang
    show raka sad at center_redup
    show diego smirk at left_redup
    m "Sama-sama [mc_name]! Kamu memang adikku yang terbaik!"

    # Diego merespon.
    show diego smirk at left_terang
    show raka sad at center_redup
    show mila smile at right_redup
    d "Tidak adil! Aku juga mau jadi kakak mu!"

    # Mila menengahi.
    show mila smile at right_terang
    show raka sad at center_redup
    show diego smirk at left_redup
    m "Sudah-sudah! Kita harus makan sekarang sebelum makanannya dingin. Kalian kakak adik termenyebalkan yang pernah ku lihat."

    # Akhir adegan
    hide raka
    hide diego
    hide mila
    with fade

    jump scene_6


label scene_6:
    scene gerbang_sekolah with fade
    "Matahari terbit kembali, hari telah berganti. [mc_name] melakukan kegiatannya seperti biasa. Namun, hari ini [mc_name] datang terlambat ke sekolahnya."

    show raka normal at center_terang with easeinbottom
    r "Pak tunggu! Jangan ditutup gerbangnya!"

    show raka normal at center_redup
    npc "Yah kamu telat! Sudah tidak bisa."

    show raka normal at center_terang
    r "Hanya telat dua menit pak, please…"

    show raka normal at center_redup
    npc "Gabisa, sudah peraturannya begitu."

    show raka normal at center_terang
    r "{i}Hm… gimana ya caranya?{/i}"
    r "{i}apa aku coba manjat yah?{/i}"
    r "{i}([mc_name] sedang mencari jalan){/i}"
    hide raka with easeoutleft

    "Saat [mc_name] mencari jalan, [mc_name] melihat Luna duduk di pojok tembok."
    show luna normal at right_redup with easeinright
    show raka normal at left_terang with easeinleft
    r "Eh- Luna! Ngapain?"

    show luna normal at right_terang
    show raka normal at left_redup
    l "Hi [mc_name], kamu telat juga?"

    menu:
        "Menurut Kamu?":
            jump scene_6a
        "Hehehe, telat sih… Tapi cuma sedikit.":
            jump scene_6b

label scene_6a:
    # Luna merespon, jadi dia menjadi terang dan Raka redup.
    show luna normal at right_terang
    show raka normal at left_redup
    l "haha iya juga ya. Gimana sih aku."

    $ luna_hearts -= 1
    play sound "audio/suara_jatuh.ogg"
    "Tiba-tiba terdengar suara jatuh."
    "Luna dan [mc_name] terkejut dan langsung mencari tahu dimana sumber suara jatuh yang baru saja mereka dengar."

    # Ben muncul. Luna langsung berbicara padanya.
    # Fokus pada Luna, yang lain redup.
    show ben normal at center_redup with popin
    show luna normal at right_terang
    show raka normal at left_redup
    l "Ben! Kamu ngapain? Kamu jatuh kah? Sakit ga?"

    # Ben menjawab, fokus pindah padanya.
    show ben kaget at center_terang with dissolve
    show luna normal at right_redup
    show raka normal at left_redup
    b "Eh?! Luna!! Kamu ngapain disini??"
    b "Kamu juga sekolah disini??"

    # Monolog Raka, fokus padanya.
    show raka normal at left_terang
    show ben kaget at center_redup
    show luna normal at right_redup
    r "{i}(Terkejut saat melihat ada seseorang yang menyapa Luna dengan sangat akrab.){/i}"

    # Luna berbicara pada Ben.
    show luna normal at right_terang
    show ben kaget at center_redup
    show raka normal at left_redup
    l "Aku sekolah disini, tapi tadi aku telat hehe."
    l "Kok aku ga pernah liat kamu sih di sekolah?"

    # Ben menjawab.
    show ben normal at center_terang with dissolve
    show luna normal at right_redup
    show raka normal at left_redup
    b "Hehehe, iya. Aku selalu bolos dari awal masuk. Sekarang-pun aku niatnya mau bolos. Tapi malah ketemu kalian di sini."

    # Luna merespon.
    show luna normal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Ben nakal ya! Aku bilangin mamih kamu nanti ya!"

    # Ben menjawab.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Eh?! Jangan Luna!"

    # Luna merespon.
    show luna normal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Hahaha! Lagian sih nakal."

    # Ben menjawab.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Hehehe, makasih Luna cantik!"

    # Luna merespon (dengan sprite baru).
    show luna ngeledek at right_terang with dissolve
    show ben normal at center_redup
    show raka normal at left_redup
    l "Aku terima ga ya ucapan terimakasih-nya?"

    # Ben menjawab.
    show ben normal at center_terang
    show luna ngeledek at right_redup
    show raka normal at left_redup
    b "Terima! Nanti aku kasih hadiah!"

    # Luna memperkenalkan Raka.
    show luna normal at right_terang with dissolve
    show ben normal at center_redup
    show raka normal at left_redup
    l "Benar ya? Oh iya Ben, aku hampir lupa. Kenalin, ini temanku namanya [mc_name]."

    # Ben menyapa Raka.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Hai! Aku Ben, semoga kita akrab ya."

    # Monolog Raka.
    show raka normal at left_terang
    show ben normal at center_redup
    show luna normal at right_redup
    r "{i}(Tersentak seketika disaat Ben dengan sangat mudah dan ramah mengajaknya berkenalan.){/i}"

    # Raka menjawab Ben.
    r "Oh, aku [mc_name]. Salam kenal ya."

    # Ben bertanya.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Wah! Kalian kelas berapa?"

    # Luna menjawab.
    show luna normal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Kita dari kelas 10 MIPA 5. Kalau kamu?"

    # Ben merespon.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Jadi kalian berdua sekelas ya?"

    # Luna mengiyakan.
    show luna normal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Iya! Kita berdua sekelas."

    # Ben merespon.
    show ben normal at center_terang
    show luna normal at right_redup
    show raka normal at left_redup
    b "Bagus kalau gitu! Karena kalian sekelas, aku bisa main ke kelas kalian sekaligus. Tanpa harus datang ke dua kelas bergantian!"

    # Monolog Raka.
    show raka normal at left_terang
    show ben normal at center_redup
    show luna normal at right_redup
    r "{i}(Ngapain sih dia? Menyebalkan.){/i}"

    # Luna merespon Ben (dengan sprite baru).
    show luna tengil at right_terang with dissolve
    show ben normal at center_redup
    show raka normal at left_redup
    l "Ben! Jangan usil ya tapi?"

    # Ben menjawab.
    show ben normal at center_terang
    show luna tengil at right_redup
    show raka normal at left_redup
    b "Usil ga ya… "

    # Luna merespon (dengan sprite baru).
    show luna kesal at right_terang with dissolve
    show ben normal at center_redup
    show raka normal at left_redup
    l "Ben! Jangan usil!"

    # Ben menjawab.
    show ben normal at center_terang
    show luna kesal at right_redup
    show raka normal at left_redup
    b "Ga usil? Ga asik!"
    
    # Luna memanggil Ben.
    show luna kesal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Ben!"

    "Luna memukul pundak Ben."
    play sound "audio/gedebuk.ogg"

    # Ben pamit.
    show ben normal at center_terang
    show luna kesal at right_redup
    show raka normal at left_redup
    b "Aku pergi duluan ya Luna, [mc_name]."

    # Luna bertanya.
    show luna kesal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Loh kamu mau kemana?! Kamu mau bolos yah!!"

    # Ben menjawab.
    show ben normal at center_terang
    show luna kesal at right_redup
    show raka normal at left_redup
    b "Hehe iya, aku ada janji diluar"
    
    # Luna mengancam.
    show luna kesal at right_terang
    show ben normal at center_redup
    show raka normal at left_redup
    l "Awas ya nanti aku bilangin mamih kamu loh."

    # Ben memohon (dengan sprite baru).
    show ben sedih at center_terang with dissolve
    show luna kesal at right_redup
    show raka normal at left_redup
    b "Untuk hari ini aja kok luna, besok besok aku pasti masuk sekolah."

    # Luna merespon (dengan sprite baru).
    show luna marah at right_terang with dissolve
    show ben sedih at center_redup
    show raka normal at left_redup
    l "Oke, awas ya! Kalau besok aku ga lihat kamu, nanti aku kasih tau mamih kamu pokoknya."

    # Ben merespon.
    show ben normal at center_terang with dissolve
    show luna marah at right_redup
    show raka normal at left_redup
    b "Siap, pasti kok aku pasti masuk sekolah soalnya ada kamu."

    hide ben with easeoutright
    "Ben pergi dan meninggalkan Luna dan [mc_name]."
    "Suasana jadi canggung dan hening."
    "..."
    "Pikiran [mc_name] dipenuhi rasa penasaran terhadap anak tadi yang berbicara dengan Luna."

    # Monolog Raka, fokus padanya. Luna menjadi redup.
    show raka normal at left_terang
    show luna marah at right_redup
    r "{i}Apa aku tanya saja ya itu siapa?{/i}"
    r "{i}Jangan deh, sepertinya Luna kesal denganku karena jawaban ku tadi yang terdengar kasar…{/i}"
    r "{i}Tapi aku penasaran. Tanya saja deh.{/i}"
    # Raka bertanya pada Luna.
    r "Tadi itu siapa kamu Luna?"

    # Luna menjawab.
    show luna marah at right_terang
    show raka normal at left_redup
    l "Itu temanku, dari kecil."

    # Raka merespon.
    show raka normal at left_terang
    show luna marah at right_redup
    r "Oh pantas saja, kalian terlihat sangat akrab."

    # Luna menjawab singkat.
    show luna marah at right_terang
    show raka normal at left_redup
    l "Iya."

    # Monolog Raka.
    show raka normal at left_terang
    show luna marah at right_redup
    r "{i}Sepertinya Luna benar-benar marah denganku.{/i}"

    "Gerbang sekolah seketika terbuka lebar."
    "Penjaga sekolah keluar dan memanggil semua anak-anak yang terlambat masuk sekolah."
    $ unlocked_ben = True
    call unlock_character("Ben", "Teman masa kecil Luna yang usil dan ceria.", "card ben")
    return

label scene_6b:
    # Luna merespon, jadi dia menjadi terang dan Raka redup.
    show luna normal at right_terang
    show raka normal at left_redup
    l "Hahaha, bagus deh! Aku jadi ada teman telat bersama!"

    # Raka bertanya, fokus berpindah padanya.
    show raka normal at left_terang
    show luna normal at right_redup
    r "Kamu kenapa telat?"

    # Luna menjawab.
    show luna normal at right_terang
    show raka normal at left_redup
    l "Tadi supir aku telat datangnya.."
    l "Kalau kamu kenapa?"

    # Raka menjawab, lalu berpikir. Dia tetap menjadi fokus.
    show raka normal at left_terang
    show luna normal at right_redup
    r "Alarm aku rusak, jadi kesiangan deh."
    r "{i}Hm.. kira-kira..{/i}"

    menu:
        "Ajak jalan keluar.":
            jump scene_6b_ajak_jalan
        "Cari jalan masuk sekolah.":
            jump scene_6b_cari_jalan
            
label scene_6b_ajak_jalan:
    r "Kamu udah sarapan belum?"
    l "Belum, ada apa [mc_name]?"
    show luna shy at right with dissolve
    l "[mc_name] mau ajak Luna jajan bareng?"
    r "Boleh, asal sama Luna."
    l "..."
    "Luna terdiam sebentar."
    l "Ah.. Eh? Tadi apa? Aku ga dengar…"
    show luna normal at right with dissolve
    r "Luna mau jajan kan?"
    l "Oh iya, aku mau jajan…"
    l "Eh- maksudnya kita jajan…"
    r "{i}Emang dia seimut ini ya..{/i}"
    r "Kamu jajan apa?"
    l "Aku…"
    l "Aku gatau tempat jajan disini ada dimana.."
    r "Kamu biasanya jajan dimana?"
    l "Aku selama ini ga pernah jajan, [mc_name]."
    r "Kalau gitu, aku mau nunjukin jajanan tradisional enak! aku yakin kamu suka!"
    l "Boleh.. Yuk!!!"
    
    hide raka with easeoutleft
    hide luna with easeoutright
    
    scene jalanan with fade
    "[mc_name] dan Luna berjalan bersama menuju toko jajanan tradisional yang disarankan oleh [mc_name] langsung kepada Luna."
    "Mereka berdua berbincang dan tertawa bersama, sesekali berlari saat menuju toko kue tradisional."

    scene toko_kue with fade
    show raka normal at left with easeinleft
    show luna normal at right with easeinright
    "[mc_name] dan Luna memasuki toko kue tradisional."
    "Saat [mc_name] membuka pintu toko, harum dari dapur toko kue menyebar keseluruh ruangan toko. Harum manis, gurih, dan harum butter yang sangat kuat, membuat keduanya semakin lapar."
    r "Permisi bu, ini [mc_name] kembali."
    npc "Halo [mc_name]! Sudah lama kamu tidak kesini. Ibu ada banyak kue tradisional varian baru loh!"
    r "Wah, iya bu. Belakangan ini saya sibuk mengurus awalan masuk sekolah, jadi tidak sempat mampir."
    npc "Ini siapa [mc_name]? Teman [mc_name] ya?"
    r "Oh iya bu, kenalin ini teman [mc_name] namanya Luna!"
    npc "Halo Luna! Wah, kamu anak yang cantik ya!"
    l "Halo bu, aku Luna! Salam kenal ya!"
    npc "Semoga Luna suka ya kue-kue buatan Ibu!"
    l "Luna pasti suka! Karena harum kue nya saja sudah sangat enak! Pasti kuenya sangat lezat!"
    npc "Wah! [mc_name] hebat bisa berteman dengan anak sebaik kamu Luna!"
    r "Ibu bisa saja."
    npc "([mc_name] dan Luna mau pesan apa?)"
    r "saya mau pesan onde-onde nya 5 ya.."
    npc "Siap! Ditunggu sebentar ya..."
    "Sambil menunggu kue siap, [mc_name] dan Luna melihat sekeliling etalase kue-kue yang sangat harum itu"
    l "[mc_name]! Harum banget tokonya! Aku semakin lapar dan ingin cepat makan deh!"
    r "Benar Luna! Setiap kali aku kesini, aku juga tidak bisa menahan perutku karena harum yang dikeluarkan dari dalam dapur kue ini!"
    l "Seharusnya aku tahu toko kue ini dari dulu! Aku pasti sering beli disini deh."
    r "Coba saja kita sudah kenal dari lama ya! Pasti aku akan memberitahu kamu tentang tempat ini dari dulu Luna!"
    l "Wah! Pasti sangat menyenangkan jika kita bisa kenal dari dulu ya!"
    npc "Ini [mc_name], Luna, kue pesanannya."
    "Penjaga toko kue memberikan sebungkus kertas kue yang berisikan lima kue onde-onde pesanan [mc_name] dan Luna."
    npc "Semoga kalian suka ya!"
    r "Makasih bu!"
    l "Terimakasih banyak bu!"
    npc "Sama-sama! Ibu harap Luna bisa kembali kesini lagi ya bersama [mc_name]!"
    l "Luna pasti kesini lagi kok sama [mc_name]!"
    npc "Ajak Luna selalu ya [mc_name]!"
    r "Siap bu!"

    hide raka with easeoutleft
    hide luna with easeoutright
    scene taman with fade
    "[mc_name] dan Luna meninggalkan toko kue, lalu pergi ke taman yang terletak tidak jauh dari toko kue tradisional ini."
    "[mc_name] membuka bungkus kue, dan mengambilkan satu potong kue tersebut lalu memberikannya kepada Luna untuk dapat dicoba lebih dulu."
    show raka normal at left with easeinleft
    show luna normal at right with easeinright
    r "Nih, kue nya!"
    "Luna mengambil kue onde-onde yang diberikan oleh [mc_name], lalu memakan kue onde-onde tersebut."
    show luna kaget at right with dissolve
    l "Wah!!! Ini apa?! Enak banget!"
    show luna normal at right with dissolve
    r "Hahaha, iya memang!"
    l "Aku jadi semakin menyesal tidak mengetahui tempat ini dari awal."
    
    b "”Luna?! Kamu ngapain disini?”"
    "Seseorang dari belakang memanggil Luna dengan kencang."
    show ben normal at truecenter with easeinright
    "[mc_name] terkejut saat melihat ada seseorang yang menyapa Luna dengan sangat akrab."
    r "{i}Dia siapa?{/i}"
    l "Ben?! Eh- aku- aku lagi jajan…"
    "Ben melihat seragam yang dikenakan oleh Luna."
    b "Kamu sekolah di SMA Harapan Bangsa juga?"
    l "Iya. Kamu juga Ben? Kok aku ga pernah lihat kamu ya dari awal masuk."
    b "Hehe… aku memang belum pernah masuk. Setelah sampai depan gerbang, aku selalu pergi, karena itu bukan sekolah yang aku mau!"
    l "Ben nakal ya! Aku bilangin mamih kamu nanti ya!"
    b "Eh?! Jangan Luna!"
    l "Hahaha! Lagian sih nakal."
    b "Hehehe, makasih Luna cantik!"
    show luna ngeledek at right with dissolve
    l "Aku terima ga ya ucapan terimakasih-nya?"
    b "Terima! Nanti aku kasih hadiah!"
    show luna normal at right with dissolve
    l "Benar ya? Oh iya Ben, aku hampir lupa. Kenalin, ini temanku namanya [mc_name]."
    b "Hai! Aku Ben, semoga kita akrab ya."

    r "{i}Tersontak seketika disaat Ben dengan sangat mudah dan ramah mengajaknya berkenalan.{/i}"
    r "Oh, aku [mc_name]. Salam kenal ya."
    b "Wah! Kalian kelas berapa?"
    l "Kita dari kelas 10 MIPA 5. Kalau kamu?"
    b "Jadi kalian berdua sekelas ya?"
    l "Iya! Kita berdua sangat akrab!!"
    show raka malu at left with dissolve
    "[mc_name] merasa malu saat Luna menganggapnya sebagai teman akrabnya."
    r "Eh- iya.. Kita berdua sangat akrab."
    show raka normal at left with dissolve
    b "Bagus kalau gitu! Karena kalian sekelas, aku bisa main ke kelas kalian sekaligus. Tanpa harus datang ke dua kelas bergantian!"
    r "{i}Ngapain sih dia? Menyebalkan.{/i}"
    show luna tengil at right with dissolve
    l "Ben! Jangan usil ya tapi?"
    b "Usil ga ya… "
    show luna kesal at right with dissolve
    l "Ben! Jangan usil!"
    b "Ga usil? Ga asik!"
    l "Ben!"
    "Luna memukul pundak Ben."
    play sound "audio/gedebuk.ogg"
    
    b "Aku pergi duluan ya Luna, [mc_name]."
    show luna sedih at right with dissolve
    l "Secepat itu?"
    show ben normal at truecenter with dissolve
    b "Iya! Aku ada urusan hehe."
    show luna normal at right with dissolve
    l "Baiklah. Hati-hati ya!"
    r "Hati-hati ya."
    b "Sampai jumpa di sekolah semuanya!"

    hide ben with easeoutright
    "Ben pergi dan meninggalkan Luna dan [mc_name] di taman."
    r "Tadi itu siapa kamu Luna?"
    l "Itu teman kecilku. Kita selalu bersama dari usia tiga tahun."
    r "Kalian bertemu dimana?"
    l "Kebetulan orang tua kami berteman, dan kami tinggal di komplek yang sama. Lalu kami juga selalu pergi ke sekolah yang sama."
    l "Tapi, disaat masuk SMA ini aku ga tahu kabar Ben sekolah dimana. Dan ternyata kita satu sekolah lagi."
    show luna kesal at right with dissolve
    l "Sebuah kebetulan yang sangat menyebalkan!"
    show raka bingung at left with dissolve
    r "Kok kamu terlihat kesal Luna?"
    l "Kamu memangnya tidak lihat dia tadi? Ben itu sangat menyebalkan!"
    show raka tertawa at left with dissolve
    r "Eh- iya sih. Hahaha"
    show raka normal at left with dissolve
    show luna normal at right with dissolve
    $ luna_hearts += 1
    $ unlocked_ben = True
    call unlock_character("Ben", "Teman masa kecil Luna yang usil dan ceria.", "card ben")
    jump scene_7

label scene_6b_cari_jalan:
    "[mc_name] dan Luna berpencar mencari celah di tembok belakang sekolah"
    l "[mc_name]! Sini… aku ketemu jalan masuk."
    r "Dimana tuh?"
    # Delay + Sound effect annoying
    r "Luna.. Luna.. ini mah gabisa."
    r "Hm.."
    r "Coba deh... kamu injak kakiku, terus naik ke dindingnya. Kayaknya bisa deh dari sini."
    l "Yakin kamu kuat?"
    r "Iya, yaudah cepetan sebelum ada yang lihat!"

    "Luna naik pelan-pelan sambil pegangan ke tembok"
    l "Awas aja ya kalo aku jatuh…"
    r "Tenang aja, aku tahan. Udah bisa, belum?"
    l "Dikit lagi... nah, udah! Aku di atas!"
    r "Oke, sekarang bantu aku naik juga!"
    
    "Luna gemetar dan dari atas tembok ia melihat ke arah bawah"
    l "[mc_name], ini tinggi juga sih… Aku ga yakin kalau aku bisa."
    
    "[mc_name] dengan sigap melihat ke arah atas tembok untuk memastikan Luna, lalu [mc_name] lanjut berpikir."
    r "Iya juga ya... tunggu disini ya Luna.., di situ ada pipa tuh tapi agak berkarat sih,"
    l "Gapapa, asal bisa bantu turun. Kamu bisa turunin tangan juga gak? Biar aku pegangan."
    r "Oke, sini, injek tong sampah itu dulu, yang ada di bawah. Terus loncat, aku tarik!"
    "Luna menginjak tong sampah, loncat sambil tangannya menggapai tangan [mc_name]. Luna turun dengan susah payah."
    l "Huhh… berhasil juga… gila... deg-degan banget!"
    r "Wah! Ternyata kamu bisa juga Luna. yuk, lanjut sebelum kita ketahuan."
    
    hide luna with easeoutright
    "[mc_name] dan Luna bergegas menuju kelas dengan mengendap-ngendap."
    show ben kaget at right with easeinright
    b "Eh?! Luna!! Kamu ngapain disini??"
    b "Kamu juga sekolah disini??"
    show luna normal at left with easeinleft
    l "Eh?! Ben! Kamu juga ngapain disini?"
    
    show raka normal at center with easeinbottom
    r "{i}Terkejut saat melihat ada seseorang yang menyapa Luna dengan sangat akrab.{/i}"

    l "Aku sekolah disini, tapi tadi aku telat hehe, untung ada [mc_name] jadi aku bisa manjat."
    l "Kok aku ga pernah liat kamu sih di sekolah?"
    show ben normal at right with dissolve
    b "Hehehe, iya. Aku selalu bolos dari awal masuk. Sekarang-pun aku niatnya mau bolos. Tapi malah ketemu kalian di sini."
    l "Ben nakal ya! Aku bilangin mamih kamu nanti ya!"
    b "Eh?! Jangan Luna!"
    l "Hahaha! Lagian sih nakal."
    b "Hehehe, makasih Luna cantik!"
    show luna ngeledek at left with dissolve
    l "Aku terima ga ya ucapan terimakasih-nya?"
    b "Terima! Nanti aku kasih hadiah!"
    show luna normal at left with dissolve
    l "Benar ya? Oh iya Ben, aku hampir lupa. Kenalin, ini temanku namanya [mc_name]."
    b "Hai! Aku Ben, semoga kita akrab ya."
    r "{i}Tersentak seketika disaat Ben dengan sangat mudah dan ramah mengajaknya berkenalan.{/i}"
    r "Oh, aku [mc_name]. Salam kenal ya."
    b "Wah! Kalian kelas berapa?"
    l "Kita dari kelas 10 MIPA 5. Kalau kamu?"
    b "Jadi kalian berdua sekelas ya?"
    l "Iya! Kita berdua sekelas."
    b "Bagus kalau gitu! Karena kalian sekelas, aku bisa main ke kelas kalian sekaligus. Tanpa harus datang ke dua kelas bergantian!"
    r "{i}Ngapain sih dia? Menyebalkan.{/i}"
    show luna tengil at left with dissolve
    l "Ben! Jangan usil ya tapi?"
    b "Usil ga ya… "
    show luna kesal at left with dissolve
    l "Ben! Jangan usil!"
    b "Ga usil? Ga asik!"
    l "Ben!"
    "Luna memukul pundak Ben."
    
    b "Aku pergi duluan ya Luna, [mc_name]."
    l "Loh kamu mau kemana?! Kamu mau bolos yah!!"
    b "Hehe iya, aku ada janji diluar"
    l "Awas ya nanti aku bilangin mamih kamu loh."
    show ben sedih at right with dissolve
    b "Untuk hari ini aja kok luna, besok besok aku pasti masuk sekolah."
    show luna marah at left with dissolve
    l "Oke, awas ya! Kalau besok aku ga lihat kamu, nanti aku kasih tau mamih kamu pokoknya."
    show ben normal at right with dissolve
    b "Siap, pasti kok aku pasti masuk sekolah soalnya ada kamu."

    hide ben with easeoutright
    "Ben meninggalkan Luna dan [mc_name] di belakang sekolah."
    r "Tadi itu siapa kamu Luna?"
    l "Itu teman kecilku. Kita selalu bersama dari usia tiga tahun."
    r "Kalian bertemu dimana?"
    l "Kebetulan orang tua kami berteman, dan kami tinggal di komplek yang sama. Lalu kami juga selalu pergi ke sekolah yang sama."
    l "Tapi, disaat masuk SMA ini aku ga tahu kabar Ben sekolah dimana. Dan ternyata kita satu sekolah lagi."
    $ unlocked_ben = True
    call unlock_character("Ben", "Teman masa kecil Luna yang usil dan ceria.", "card ben")
    jump scene_7

label scene_7:
    scene koridor_sekolah with fade
    
    play sound "audio/peluit.ogg"
    "Prittttttt…"
    rl "Semua anak 10 MIPA 5 diharap pergi kelapangan dan memakai seragam olahraga."

    show raka normal at center with easeinbottom
    r "Tunggu pak!"
    r "{i}Susah banget sih pakai sepatu ini.{/i}"

    show luna normal at right with easeinright
    l "Ayo [mc_name]!"
    r "Luna tunggu!"

    hide luna with easeoutright
    "Luna berhenti dari larinya dan terkejut mendengar panggilan [mc_name]."
    "Luna kembali berlari balik kearah gedung sekolah dan menghampiri [mc_name]."
    show luna normal at right with moveinright
    
    l "Aku tungguin, ya."
    r "Terimakasih ya Luna."
    l "Tenang saja [mc_name]. Aku akan selalu disini kok sama kamu."
    
    "[mc_name] melanjutkan mengikat tali sepatu olahraganya yang belum tersimpul rapi itu."
    r "Sudah!"
    l "Yuk!"

    "Saat Luna hendak berlari lebih dulu, [mc_name] menarik lengan Luna dan menahannya pergi."
    "Luna mendadak berhenti dan terkejut."
    show luna shock at right with hpunch
    l "Ada apa [mc_name]? Apa tali sepatu mu belum selesai?"
    show raka smile at center with dissolve
    r "Tidak, aku hanya ingin menarikmu agar kita bisa berlari bersama menuju lapangan."
    show luna shy at right with dissolve
    "Luna terdiam dan wajahnya tersipu malu."
    r "Yuk?"
    l "Yuk!"

    hide raka with easeoutleft
    hide luna with easeoutright

    scene lapangan_sekolah with fade
    "Mereka berdua kembali berlari bersama menuju lapangan sekolah dengan [mc_name] yang menarik lengan Luna."

    show raka normal at centerleft with easeinleft
    show luna normal at centerright with easeinright
    show rl normal at right with easeinright
    
    rl "Kalian telat!"
    rl "Kalian lari ya, keliling lapangan."
    l "Yah pak! Kan cuma selisih sedikit… "
    l "Ayolah pak.."
    rl "Gimana ya… hm."
    rl "Gaboleh! Lari dua puluh kali."
    l "Yah pak, capek dong?"
    r "Iya pak, kasian tuh Luna nanti kecapekan."
    show rl tertawa at right with dissolve
    rl "Kalian ini bisa aja ya nawarnya."
    show luna sedih at centerright with dissolve
    l "Iya pak, nanti kaki saya sakit gimana?"
    show rl normal at right with dissolve
    rl "Yaudah, lima belas kali deh."
    r "Masih banyak tuh pak, sepuluh aja gimana?"
    show luna sedih at centerright with dissolve
    l "Iya pak, sepuluh deh gapapa. Please…"
    rl "Yaudah iya, iya. Sepuluh kali keliling. Cepat sana."
    
    l "Siap!"
    r "Siap!"
    l "Makasih bapak Rilandy yang sangat tampan. Bapak baik banget deh!"
    r "Makasih pak!"
    rl "Ah, bisa aja kalian ini."

    hide rl with easeoutright
    
    "[mc_name] dan Luna memulai hukuman lari mereka bersama."
    r "Luna, aku minta maaf ya. Karena kamu nungguin aku, kamu jadi ikut dihukum juga."
    l "Ihh.. Gapapa [mc_name], kan aku yang mau sendiri buat nungguin kamu."
    r "Tapi aku jadi merasa bersalah karena kamu ikut dihukum juga."
    l "Gapapa kok [mc_name], Kamu ga salah kok."
    r "Jangan gitu Luna."
    r "Gimana nanti kalau istirahat aku traktir."
    l "Gausah [mc_name]. Aku gapapa kok."
    show raka tengil at centerleft with dissolve
    r "Gapapa kok, kan ini aku juga yang mau."
    show luna normal at centerright with dissolve
    l "Hahaha, yaudah deh kalau kamu maksa."
    l "Makasih ya [mc_name]."
    r "Sama-sama, Luna."

    "[mc_name] dan Luna menyelesaikan hukuman yang mereka dapatkan."
    show rl normal at right with easeinright
    r "Pak, kita berdua sudah selesai lari nya."
    rl "Wih, hebat kalian. Yasudah, sana kalian istirahat atau beraktivitas bebas lainnya."
    r "Oke pak, makasih ya."
    l "Oke pak, makasih ya."
    hide rl with easeoutright
    
    npc "[mc_name]! Ayok main basket bareng!"
    r "Duluan! Nanti nyusul!"
    r "Luna, aku main basket dulu ya."
    l "Oke, semangat ya!"
    hide luna with easeoutleft

    "[mc_name] melanjutkan kegiatan bermain bola basket bersama teman sekelasnya."
    play sound "audio/bola_jatuh.ogg"
    "Bola yang [mc_name] lempar tidak sengaja mengenai seseorang yang sedang lewat di samping lapangan."
    
    show nara hurt at center with hpunch
    npc "Kak Nara!"
    show raka shock at left with dissolve
    r "Kak Nara?! Itu Kak Nara?!"

    "Seseorang yang terjatuh itu ternyata adalah Nara."
    "Semua orang disekitar menghampiri Nara yang tejatuh."
    "[mc_name] mencoba menghampiri Nara yang terjatuh, namun terhalang oleh banyaknya orang yang berada di sekitar Nara."
    
    show rl normal at right with easeinright
    rl "Nara kamu gapapa?"
    n "Ga- gapapa pak."
    rl "Bisa berdiri ga?"
    n "Bisa pak."
    
    "Nara mencoba berdiri…"
    play sound "audio/jatuh_gedebuk.ogg"
    "Nara terjatuh dan tidak bisa berdiri."
    show nara sedih at center with dissolve
    n "Aw!"
    rl "Udah gausah berdiri."

    "Pak Rilandy bergegas membawa Nara ke ruang UKS."
    hide nara with easeoutbottom
    hide rl with easeoutright
    
    play sound "audio/bel_sekolah.ogg"
    "Bel istirahat berbunyi."

    show raka normal at center
    r "{i}Duh… sekarang jam istirahat.{/i}"
    r "{i}Tadi aku udah janji buat traktir Luna… tapi aku juga yang bikin Kak Nara jatuh.{/i}"
    r "{i}Gimana ya? Kalau aku tinggalin Luna, nanti dia mikir aku ngelupain janji.{/i}"
    r "{i}Tapi Kak Nara juga pasti sakit banget… dan itu salahku, aku harus minta maaf.{/i}"
    r "{i}Aku harus gimana? Aduh…{/i}"
    r "{i}Kalau aku pergi ke UKS, Luna gimana?{/i}"
    r "{i}Tapi kalau aku pergi ke Luna, Kak Nara gimana?{/i}"

    menu:
        "Temui Luna (Tepati Janji).":
            jump menemui_luna_scene7
        "Temui Nara (Minta Maaf).":
            jump menemui_nara_scene7

label menemui_luna_scene7:
    "Setelah mempertimbangkan banyak hal di dalam pikirannya, Raka akhirnya memilih untuk menepati janji-nya kepada Luna saat ini juga."
    "Raka bergegas pergi menuju kantin, dimana itulah tempat janji temu bersama Luna."

   
    r "Hai Luna, udah nunggu lama ya?"
    l "Hai Raka, engga kok. Aku belum lama disini."
    r "Kamu udah pesan?"
    l "Belum, aku nungguin kamu."
    r "Aku pesenin ya?"
    l "Boleh."
    r "Luna, coba tebak aku mau pesen apa di antara menu ini?" 
    l "Hm… Nasi goreng?"
    r "Betul!"
    r "{i} Padahal sebenarnya aku gatau mau pesan apa. {/i}"

    show luna smirk
    l "Haha, sudah kutebak pasti kamu mau pilih nasi goreng, aku kan pintar."
    r "Sebentar ya, aku pesan dulu."
    l "Iya, Raka."

    "Raka pergi menuju meja pemesanan makanan kantin untuk memesan menu makanan yang sudah dipilih oleh Luna dan dirinya di kantin makanan utama."
    "Setelah makanannya sudah siap, Raka membawanya sendiri untuk langsung di berikan kepada Luna."

    
    r "Ini dia makanannya tuan putri Luna!"
    l "Hahaha, bisa aja kamu Raka, Makasih ya!, Aku jadi nggak enak nih."
    r "Tenang aja Luna, anggap aja ini hadiah buat kamu yang udah mau nungguin aku tadi. Dan jadi teman dihukum lari bareng, hehe."

    show raka smile 
    r "Anggap aja ini permintaan maaf. Tapi kalau boleh jujur, aku nggak nyesel dihukum hari ini."

    "Luna menghentikan suapannya, sedikit bingung"
    l "Lho, kok gitu? Capek tahu lari keliling lapangan."
    r "Iya capek, tapi jadi punya alasan buat ngobrol berdua sama kamu kayak sekarang. Kalau nggak dihukum, mana mungkin bisa?"

    "Raka menatap Luna sekilas, lalu kembali fokus ke makanannya, sedikit salah tingkah dengan ucapannya sendiri"

    show luna smile
    l "jadi itu rencananya? Pinter juga."

    "Luna melanjurkan makannya kembali."
    l "Aku kira kamu bakal ngejauhin aku karena udah bawa sial."
    r "Justru sebaliknya. Dibanding cuma ngobrol di kelas, kayak gini lebih seru. Aku jadi tahu kalau kamu orangnya asyik, nggak jaim."
    l "Kamu juga, kok. Kirain pendiam, ternyata bisa ngobrol juga."

    "Luna tertawa kecil"
    l "Biasanya kan nempel terus sama dua sahabatmu itu."

    show raka smile
    r "Diego sama Mila? Iya, mereka paket lengkap dari SMP. Nanti aku kenalin, tapi siap-siap aja, mereka suka interogasi orang yang lagi deket sama aku.."

    show luna shock 
    show luna smile                           
    l "Oh ya? Aku tunggu deh interogasinya.” (Luna menatap Raka)."
    l "Tapi aku penasaran, kenapa kamu kelihatannya canggung gitu di kelas?"
    r "Eh? Masa? Aku… mungkin emang nggak terlalu jago basa-basi di depan banyak orang. Lebih nyaman ngobrol personal kayak gini."

    show luna smile
    l "Baguslah, berarti aku orang yang spesial, dong?"

    "Raka berusaha untuk memberanikan dirinya menatap kedua mata Luna."
    show raka smile
    r "Menurut kamu?" 
    r "Makanya, hukuman dan nasi goreng ini harus sering-sering diulang kayaknya, biar ngobrolnya makin lancar."

    show luna smile
    l " Hahaha. Dasar, ada maunya."
    r "Eh, kamu suka yang manis-manis nggak?"
    l "Hah? Makanan manis? Ada apa Raka tiba-tiba?"
    r "Itu lho, di kantin katanya ada ice cream. Tadi rame banget. Kamu mau ga?"

    show luna smile
    l "“Wah, serius? boleh."
    r "Oke, sebentar ya, aku beli dulu kamu tunggu disini aja."

    "Raka menuju kantin yang menjual es krim."
    "Di sebelah kantin es krim terdapat kantin makanan berat yang mayoritas menunya untuk menu sarapan."

    r "{i}Eh...{/i}"
    r "{I}Itu bukannya kak arga ya?.. Kok dia beli bubur jam segini.{/i}"
    r "Kak Arga?"

    "Arga menoleh ke arah Raka yang berdiri tepat di belakangnya. Tatapannya yang dingin dan sadis, seolah-olah menyerang Raka dengan bilah yang tajam."

    a "Raka."

    "Suara Arga yang dingin dan tajam memanggil nama Raka, membuat Raka semakin takut akan keberadaan Arga disaat ini."

    r "Iya kak. Kakak beli bubur? Buat kak Nara ya? Gimana keadaan dia, kak?"

    "Senyuman tipis yang memilki arti tajam di dalamnya, dilemparkan langsung oleh Arga kepada Raka."
    
    show arga mad
    a "Oh, lu masih inget Nara ternyata. Kirain udah lupa."

    show raka shock
    r "Maksudnya, kak?"

    "Arga melirik sekilas ke arah meja Luna, lalu kembali menatap Raka dengan ekspresi yang berkata bahwa Raka menjijikan."

    show arga sinis
    a "Enggak. Gua cuma heran aja. Bisa secepat itu ganti prioritas."

    show raka sad
    r "Aku tadi mau ke UKS untuk jenguk Nara dan minta maaf secara langsung, tapi…"

    show arga mad
    a "Tapi ada janji yang lebih penting, kan?” (Arga memotong ucapan Raka)."
    a "Nara di UKS, Katanya kena bola kenceng banget. Aneh ya, pemainnya bisa seceroboh itu."

    show raka sad
    r "Itu aku kak, aku bener-bener gak sengaja... Aku mau minta maaf."

    show arga sad
    a "Minta maaf ke gua? Nggak salah nih? Harusnya lu di sana, bukan di sini makan sama orang lain."

    "Nada bicara Arga yang sangat tenang namun tersimpan amarah yang sangat mendalam pada setiap kata yang ia keluarkan."

    a "Nara itu orangnya nggak suka ngeluh. Walaupun sakit, dia pasti bilang ‘nggak apa-apa’. Tapi orang yang peduli beneran, pasti tahu kalau dia lagi nggak baik-baik aja tanpa harus dia ngomong."

    "Raka merasa sangat bersalah dan menyesali apa yang telah dia perbuat."

    show raka sad
    r "Aku…"
    a "Udahlah, gua duluan ya. Ada yang harus diurus. Lebih penting dibandingkan melanjutkan percakapan ga jelas ini."

    "Arga berjalan melewati Raka, berhenti sejenak di sampingnya, lalu membalikkan tubuh menghadap Raka."

    a "Lain kali, kalau mau sok peduli, pastiin topengmu lebih meyakinkan."

    jump end_chapter1



label menemui_nara_scene7:
    "Di sore hari ini, dimana hampir seluruh siswa sudah tidak ada lagi di sekolah. Pintu UKS sedikit terbuka. Raka melihat Nara duduk di tepi kasur."
    "Wajah Nara pucat pasi, tubuhnya terlihat sangat lemas dan lemah. Sementara seorang petugas PMR baru saja selesai mengompres perut Nara."

    "*tok tok tok*"
    "Raka mengetuk pintu ruang UKS. "

    r "Permisi…"

    "Nara mendengar suara ketukan pintu langsung melihat kearah pintu dan menunggu siapa yang hendak datang ke UKS di jam sore ini."

    n "Raka? Kamu ngapain di sini?"

    n "Raka berjalan menghampiri kasur UKS dimana Nara terbaring di atasnya."

    r "Itu… Kak, aku mau minta maaf. Soal bola basket tadi. Itu salahku, aku bener-bener tidak sengaja. Maaf, ya."

    show nara normal
    n "*menghela napas*"

    "Nara tersenyum tipis setelah mendengar pengakuan dari Raka."

    n "“Aku gapapa. Namanya juga kecelakaan. Aku juga salah, jalan di pinggir lapangan tapi nggak merhatiin."

    r "Tapi perut kakak jadi sakit gitu. Pasti sakit banget, ya? Muka kakak pucat."
    
    "Raka menunjuk ke arah perut Nara dengan tatapan dan nadanya tulus dipenuhi rasa khawatir."

    "Nara terkejut dengan pernyataan Raka. Raka menunjukan sisi perhatiannya yang membuat Nara menjadi lebih luluh terhadap Raka."

    show nara shock
    n "Heh… kelihatan banget, ya? Cuma nyeri sedikit, kok. Nggak usah khawatir."
    r "Jangan bilang nggak apa-apa. Aku jadi makin merasa bersalah."

    "Nara terdiam sejenak dan terkejut menatap Raka yang terlihat tulus ."

    show nara shy
    n "Yaudah, iya, ini nyeri. Puas?"

    "Nara berbicara dengan nada datar, tapi ada sedikit senyum tipis di bibirnya."
    "Raka merasa sedikit lebih lega karena Nara yang mau berbicara jujur kepadanya."

    r "Nah, gitu. Kakak butuh sesuatu? Mau aku beliin minuman hangat atau roti? Biar ada tenaga."
    n "Nggak usah, nanti malah merepotkan."
    r "“Nggak ada yang direpotin, kak. Anggap aja ini bagian dari permintaan maafku."

    "Tatapan Nara seketika terpaku kepada wajah Raka dan menatap kedua matanya dengan lekat."

    n "Yaudah. Air mineral aja cukup."
    r "“Oke, siap! Tunggu sebentar, ya, kak!"
    
    "Raka bergegas keluar untuk membeli air mineral dan kembali dalam beberapa menit."
    "Raka memberikan air mineral yang tadi ia beli kepada Nara."

    r "Ini, kak."
    n "Terimakasih banyak ya Raka, aku jadi ngerepotin kamu."

    show raka sad
    r "Jangan berterima kasih sama aku kak, ini memang seharusnya aku lakukan, bahkan ini tidak bisa mengembalikan kondisi kaka ke awal kan?"
    n "Kenapa kamu berpikir begitu?"
    r "Aku cuma mau Kak Nara baik-baik saja… aku jadi sedih kalau Kak Nara kenapa-kenapa."
    n "Hahaha, kamu lucu banget Raka! Makasih banyak ya! Aku jadi bisa ketawa lagi."
    r "Sama-sama, kak! Aku senang deh lihat Kak Nara bisa ketawa lagi."

    "Suasana hening seketika, Nara memberhentikan percakapannya kepada Raka."
    "Raka mencoba mencari topik lain untuk dibicarakan bersama Nara agar suasana tidak menjadi canggung dan kembali cair."

    r "Oh iya, kak…"
    n "Hm?"
    r "Soal novel Pluto yang kakak bilang di perpustakaan waktu itu…"

    show nara confuse
    n "Kenapa dengan novel itu?"
    r "Aku… semalam udah baca sebagian. Ternyata seru banget. Tentang cewek bernama Raya yang punya kekuatan menghilang itu, kan?"

    show nara smile
    n "Wah, kamu beneran baca? Aku kira kamu cuma basa-basi waktu itu."

    "Raka merasa sangat senang dan lega melihat Kak Nara yang semakin terbuka dan dekat dengannya."
    "Raka tidak tahu harus berkata apa dan bagaimana cara mengekspresikan perasaan bahagianya ini. Ia tetap melanjutkan percakapannya dengan Nara."

    show raka smile
    r "Beneran, kak. Aku jadi penasaran, gimana si Alri, cowok pintar itu, bisa curiga sama kekuatannya Raya?"
    n "Nah, itu bagian menariknya! Alri itu tipe pengamat. Dia peka sama detail-detail kecil yang sering dilewatkan orang lain. Dia sadar kalau Raya sering ‘hilang’ di momen-momen krusial. Buat dia, itu bukan kebetulan."
    r "Wah… keren. Berarti dia karakter yang cerdas banget, ya."
    n "Iya! Sangat cerdas! Makanya aku suka. Karakternya tidak dangkal. Kamu harus baca sampai akhir buku pertama, ada plot twist yang bagus."
    r "Serius, Kak? Jadi makin penasaran! Nanti aku lanjutin, deh."
    n "Ohiya, panggil aku Nara aja!"
    r "gapapa nih kak?"
    n "Ya, tentu saja! Aku dengan senang hati!"

    "Raka dan Nara terus berbincang tentang novel itu."
    "Raka begitu terhanyut melihat sisi lain Nara yang bersemangat dan terbuka, sementara Nara senang menemukan teman bicara yang nyambung dan menyenangkan. Keduanya benar-benar lupa waktu dan situasi yang ada. "

    # ganti background ke lorong sekolah

    "Dengan senyum yang masih tersisa di wajahnya, Raka melangkah keluar dari ruang UKS. Langkahnya ringan, seolah beban yang tadi sempat menghimpit dadanya perlahan mulai menguap. Udara sore terasa lebih hangat dari biasanya, dan cahaya matahari yang menembus sela-sela daun tampak lebih bersahabat."

    "Pikirannya masih dipenuhi oleh percakapan serunya dengan Nara tawa mereka yang spontan, tatapan mata Nara yang sesekali mencuri perhatiannya, dan caranya berbicara yang terasa begitu dekat, begitu tulus. Entah mengapa, semua itu meninggalkan jejak yang sulit diabaikan."

    r "{i}Wah, Nara ternyata asyik banget kalau diajak ngobrolin novel. Senyumnya juga… manis banget. Aku harus cepat-cepat selesaikan baca novelnya biar bisa ngobrol lagi sama dia.{/i}"
    r "Aku masih tidak sangka bisa jadi sedekat ini dengan Nara…"

    "Raka berjalan santai di koridor yang mulai sepi karena jam istirahat akan segera berakhir. Tiba-tiba, langkahnya terhenti saat seseorang muncul dari balik pilar dan berdiri tepat di hadapannya."

    show raka kaget
    r "Ben? Lo ngapain di sini?"

    show ben mad 
    b "Nungguin lo."

    show raka confuse
    r "Nungguin gue? Kenapa? Ada perlu?"

    "Senyum Ben yang mengerenyit tipis seperti mengetahui hal buruk apa yang sudah terjadi di depan matanya."

    show ben mad
    b "Seneng banget kelihatannya muka lo. Lancar urusannya di dalam ruang UKS itu?"

    show raka confuse
    r "Maksud lo? Gue dari UKS. Nemenin Kak Nara, tadi ada kecelakaan."

    show ben mad
    b "Oh, gue tahu. Lo nemenin Kak Nara."
    b "Pasti penting banget, ya, urusannya? Sampai ada orang lain yang lo lupain gitu aja."

    "Kata-kata terakhir Ben terasa seperti tamparan. Pikiran Raka yang tadinya dipenuhi Nara, seketika kosong, lalu sebuah nama dan sebuah janji muncul dengan kilatan rasa ngeri."

    show raka kaget
    r "Luna…"

    "Suara Raka terhentak perlahan dan nyaris tidak terdengar."
    "Raka terkejut dengan apa yang barus aja dia ingat dalam pikirannya, yaitu Luna."

    show ben mad
    b "Nah, akhirnya lo inget juga. Gue kira kapasitas otak lo cuma cukup buat satu cewek."

    "Nada bicara Ben penuh dengan hinaan."

    show raka sad
    r "Di… di mana dia sekarang? Dia di mana, Ben?"

    show ben kaget
    b "Nyariin dia sekarang? Terlambat."
    b "Dia udah pulang."

    show raka kaget
    r "Pulang?!"

    show ben mad
    b "Iya. Setelah nungguin lo di kantin sendirian lebih dari setengah jam."
    b "Gue lihat dia di sana, duduk sambil ngeliatin jalan masuk kantin. Gue ajak makan, dia nolak. Katanya, ‘Aku udah janji sama Raka"

    "Setiap kalimat yang keluar dari mulut Ben terasa seperti tusukan bilah tajam yang menghantam hati Raka disaat yang bersamaan."

    show raka sad
    r "Aku… aku bener-bener lupa, Ben…"

    show ben mad
    b "Tentu aja lo lupa."
    b "Dia nunggu sampai bel mau bunyi, sampai akhirnya dia sadar kalau orang yang dia tunggu nggak akan pernah datang. Lo tahu gimana ekspresi kecewanya? Gue yakin lo nggak akan mau lihat."
    b "Dia pergi sambil nunduk. Dan itu semua gara-gara lo."

    # *deg* (bgm panik/takut and deg deg an)

    show raka sad
    r "Terus, gimana caranya gua minta maaf ke dia? Gua harus minta maaf…"

    show ben mad
    b "Nggak usah!"

    "Ben memotong ucapan Raka dengan nadanya yang tinggi itu."

    show ben mad
    b "Gua yang nungguin lo disini cuma mau bilang satu hal. Jauhin Luna! Apapun alasannya!"


    show raka kaget
    r "Apa?!"

    show ben mad
    b "Dia cewek yang terlalu baik buat dijadikan pilihan kedua sama orang plin-plan kayak lo. Hari ini lo udah buktiin kalau janji lo itu nggak ada harganya."

    "Ben menatap Raka lurus ke mata, tatapannya penuh peringatan."

    b "Jadi, dengerin gue baik-baik. Sekali lagi lo bikin dia kecewa, yang lo hadapin bukan lagi cuma kata-kata dari gue."

    "Setelah mengatakan itu, Ben dengan sengaja menabrak bahu Raka cukup keras saat ia berjalan melewatinya. Ia pergi tanpa menoleh lagi."

    "Raka terdiam mematung di tengah koridor yang sepi. Tidak ada Luna untuk dimintai maaf. Tidak ada siapa-siapa. Hanya ada dirinya dan rasa bersalah yang begitu besar, membayangkan kekecewaan Luna yang bahkan tidak sempat ia lihat dengan mata kepalanya sendiri."

    jump end_chapter1


label end_chapter1: 
    "Raka terdiam dan merenung. Ia tidak tahu lagi harus melakukan apa. Dalam kebingungannya, Raka berpikir untuk menghubungi Diego dan Mila untuk meminta saran dan solusi."
    
    "Namun, terbesit di pikirannya sebuah rasa ragu karena ia merasa seperti anak kecil yang selalu bergantung pada kedua kakaknya setiap kali keadaan menjadi sulit. Sebuah perasaan malu perlahan menyelip di dadanya."

    "Ia menatap layar ponselnya yang masih menyala, nama Diego dan Mila terpampang jelas di daftar kontak. Jari-jarinya sempat bergerak, tapi berhenti di tengah jalan."

    show raka sad
    r "Sampai kapan aku akan begini terus?"

    show raka mad
    r "Aku harus menyelesaikan masalah ini sendiri! Ini masalah yang kuperbuat sendiri, jadi harus aku yang menyelesaikannya sendiri"

    show raka sad
    r "Aku sangat membutuhkan Diego dan Mila, tapi… kali ini akan aku hadapi sendiri."

    show raka confuse
    r "Nara atau Luna? Itu adalah pilihanku sendiri, tanpa campur tangan siapa pun, bahkan jika itu adalah Mila dan Diego."

    show raka mad
    r "“Siapa dan bagaimana akhirnya, akan aku tentukan sendiri, nanti…"

    "Perasaan Raka bercampur menjadi satu dan tidak karuan. Tak ada satupun orang yang dapat membantu permasalahan Raka saat ini."

    "Raka menginjakan telapak kakinya dan melangkah perlahan keluar sekolah."

    "*dug!*" #(bgm suara jatuh)

    show raka confuse
    r "Eh? Suara apa itu?" #ganti lagu jadi lagu romantis
    c "Raka! Aku di sebelah sini"

    "Raka melihat sekeliling mencari sumber suara yang memanggil namanya itu."

    c "Raka! Ini aku! Tidakkah kamu ingat?"

    "Raka menoleh kearah kanan dari jalan yang sedang ia lewati. Lalu-"

    "*dug*" # (bgm suara dentuman ringan)
    "Dengan cepat Callista berlari dan memeluk Raka dengan sangat erat."


    c "Aku sangat merindukan kamu Raka! Kamu kemana saja?"
    b "Cal- Callista?!"

    "Raka terpaku. Tubuhnya seolah membeku dalam pelukan yang lama dirindukan, tapi tak pernah ia duga akan terjadi hari ini."

    show raka shock
    r "Ca- Callista…?!"

    show callista sad
    c "Sudah dua tahun… dan kamu sama sekali tidak berubah."

    "Pelukan itu begitu hangat. Terlalu familiar. Tapi justru karena itu, Raka merasa hatinya kacau."

    show raka sad
    r "{i}…kenapa sekarang? Saat aku justru sedang mencoba mengenal Nara… dan Luna… {/i}"

    show raka confuse
    r "{i}Perasaan ini… kenapa seperti ditarik kembali ke masa lalu?{/i}"

    "Callista melepaskan pelukannya perlahan, mendengak keatas dan menatap wajah Raka dengan senyum tipis yang penuh rindu."

    show callista salting
    c "Maaf, kalau aku tiba-tiba muncul seperti ini. Aku tahu, mungkin waktunya tidak tepat."

    "Raka menunduk. Suaranya tercekat. Ia ingin bicara, tapi hatinya menolak memilih kata."

    show raka nervous
    r "Tidak… aku cuma... kaget."

    show callista sad
    c "Boleh aku ikut jalan sebentar? Seperti dulu… saat kita pulang bareng dari sekolah."

    "Raka mengangguk pelan. Keduanya berjalan menyusuri jalan kecil yang mulai sepi, langkah mereka lambat dan ragu."

    show bg sunset_road with fade

    show raka sad
    r "{i}Kenapa hati ini terasa asing... padahal orang di sebelahku begitu akrab?{/i}"

    show raka sad
    r "{i}Nara yang selalu membuatku tertantang... Luna yang hangat dan mengerti semua sisi diriku... dan sekarang Callista... yang datang dengan kenangan tak tergantikan.{/i}"

    show callista smile
    c "Kamu masih suka diam sambil mikir sendiri, ya?"

    show raka salting
    r "Hah… iya. Maaf. Banyak yang ada di kepala."

    show callista shy
    c "Boleh aku tahu… apakah di antara semua itu… ada aku?"

    "Raka terdiam. Pertanyaan itu sederhana, tapi menohok. Ia menatap langit yang mulai gelap."

    show raka normal
    r "Callista… kehadiranmu sekarang membangunkan sesuatu yang sudah lama aku coba hilangkan. Tapi aku juga sedang… mencoba mengenal orang lain."

    show callista sad
    c "Ah.. siapa orang beruntung itu?"

    show raka surprise
    r "Kamu tidak perlu tahu?"

    show callista sad
    c "Aku bodoh! Kau benar Raka, untuk apa aku tahu bukan? memangnya aku siapa kamu?" 

    "Raka menelan ludah. Ada desir sakit di dadanya, bukan karena kehadiran Callista… tapi karena ia tak bisa menjawabnya dengan jujur, bahkan pada dirinya sendiri."

    show raka sad
    r "Aku… belum tahu, Callista. Aku benar-benar bingung."

    show callista smile
    c "Kalau begitu… aku akan sabar menunggu. Bukan sebagai masa lalu… tapi sebagai kemungkinan."

    "Keduanya berhenti melangkah. Angin sore menyapu wajah mereka."
    
    "Raka mengalihkan wajahnya dan menatap Callista."

    "Mata Callista yang berbinar indah, seperti memberikan harapan baru bagi mereka untuk bisa memulai semuanya dari awal. Namun-"

    "Raka tersadar, semuanya tak lagi sama... Kehadiran Nara dan Luna lah yang sekarang membuat hidupnya menjadi lebih berwarna."

    "Apakah Callista juga akan menambahkan warna baru di dalam hidup Raka?"
