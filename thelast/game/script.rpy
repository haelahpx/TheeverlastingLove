default luna_hearts = 0
default nara_hearts = 0

default unlocked_luna = False
default unlocked_nara = False
default unlocked_diego = False
default unlocked_mila = False
default unlocked_tiffany = False
default unlocked_arga = False


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

image auditorium = im.Scale("bg/auditorium.jpg", 1920, 1080)
image bg_kantin_gate = im.Scale("bg/bg_kantin_gate.jpg", 1920, 1080)
image bg_kantin_table = im.Scale("bg/bg_kantin_gate.jpg", 1920, 1080)

# Transformasi untuk karakter kiri (pojok kiri atas dialog box)
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

# Transformasi untuk karakter kanan (pojok kanan atas dialog box)
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

define Z = Character("Diego & Mila", color="#7FB2B2")

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

label unlock_character(char_name, char_desc, char_image):
    call screen character_card(char_name, char_desc, char_image)
    return
label start:
    scene auditorium
    with fade

    play music "bgm/videoplayback.m4a"

    show raka normal mirror at left_terang
    with dissolve
    r "Hari ini adalah hari pertamaku masuk SMA."
    r "Aku kepikiran deh, aku bisa ga ya cepat beradaptasi dan dapat teman baru? Hm…"

    play sound "footstep.ogg"

    show luna normal at right with moveinright
    show raka normal mirror at left_redup
    l "Hai!"

    hide raka normal mirror at left
    show raka kaget mirror at left_terang
    show luna normal at right_redup
    r "(kaget)"
    r "(dalam hati) Wah! Dia siapa? Cantik banget… Ceria, penuh semangat dan ramah banget…"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Oh! Hai?"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Boleh kenalan ga? Nama kamu siapa?"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Eh- boleh… aku Raka."
    r "Kalau nama kamu?"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Luna! Namaku Luna…"

    play sound "mic_test.ogg"

    show nara normal at right
    hide raka normal at left
    hide luna normal at right 
    n "Test, test, test…"
    n "Halo semuanya, nama saya Nara sebagai perwakilan dari OSIS."
    n "Ada pemberitahuan, bagi peserta didik baru SMA Harapan Bangsa, di mohon untuk mencatat informasi yang tertera di mading sekolah sebagai arahan mengenai kegiatan MPLS sekolah kami."

    show raka normal mirror at left_terang
    hide nara normal at right
    r "(dalam hati) Wah, kakak itu... bisa banget bawa diri. Udah keren, kalem, cantik pula. Komplit banget sih."
    if not unlocked_nara:
        $ unlocked_nara = True
        call unlock_character("Nara", "Anggota OSIS yang kalem dan berwibawa.", "card nara")
    if not unlocked_luna:
        $ unlocked_luna = True
        call unlock_character("Luna", "Gadis ceria dan penuh semangat.", "card luna")

    jump scene_2

label scene_2:
    scene bg_kantin_gate with fade

    "Raka berjalan menuju arah kantin sekolahnya dan mencari kedua sahabatnya yang selalu bersama sejak SMP hingga saat ini."
    "Kedua sahabatnya ini sudah menjalin hubungan asmara bersama sejak SMP hingga saat ini."
    
    play sound "shout.ogg"

    show diego normal at right_terang
    d "Rakaaa!"

    show mila normal at right_terang
    hide diego normal at right
    m "Siniiii!"

    show raka normal mirror at left_terang
    hide diego normal at right
    hide mila normal at right
    r "Eh- itu mereka."
    r "Diegoo! Milaa!"

    jump scene_2a

label scene_2a:
    scene bg_kantin_table with fade

    "Raka, Diego dan Mila berjalan menuju meja makan kantin untuk melanjutkan percakapan mereka."

    show mila normal at right_terang
    m "Gimana hari pertama kamu Raka?"

    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Biasa aja sih, gaada yang seru."

    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Ah iya? Kok gitu sih…"

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Masa sih? Ga ada ketemu cewek gitu?"

    hide diego normal
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Diego! Apaansih."
    hide mila normal
    show raka normal mirror at left_terang
    r "Eh- hehehe… Ada sih…"

    hide raka normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Hah? Serius? Siapa?!"

    menu:
        "Ceritain Luna":
            jump scene_2b_luna
        "Ceritain Nara":
            jump scene_2b_nara
        "Gak cerita":
            jump scene_2b_rahasia

label scene_2b_luna:
    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Tadi ada cewe rambutnya pirang, cantik banget… ramah dan ceria gitu orangnya, seolah-olah punya banyak energi seharian."
    
    hide diego normal 
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Oh iya? Kayaknya tadi aku lihat deh, emang cantik banget tuh.."

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Eh- emang ada? Kok aku ga liat sih..." 

    "Diego tampak agak sedikit kecewa."

    hide diego normal 
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Kenapa kecewa gitu mukanya?! Dih cantik dikit langsung gitu." 

    hide mila normal 
    show raka normal mirror at left_terang
    r "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Siapa namanya?"

    hide diego normal 
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Kenapa harus ditanya?" 
    "Mila menatap Diego dengan sinis."

    hide mila normal
    show raka normal mirror at left_terang
    r "Namanya Luna."

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Namanya cantik deh…"

    hide raka normal mirror
    show diego normal at right_redup
    show mila normal mirror at left_terang
    m "Ribut yuk?"
    
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Ah sudahlah..."
    jump scene_2c

label scene_2b_nara:

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Kalian lihat ga sih cewe yang kasih pengumuman di auditorium tadi?"

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Oh... itu! aku merhatiin dia tadi, yang tinggi dan cantik itu kan?"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Merhatiin banget nih, kayakya sampai detail begitu."

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Oh ya.. jelas! dia cantik banget sih emang…"

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Terserah deh." 
    "Mila menatap Diego dengan sinis."

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

    hide raka normal
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Masa gatau sih... Nama dia Nara, perwakilan dari OSIS."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Kok kamu tau sih?! Raka aja gatau, kok kamu bisa tahu?!"

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Kan tadi dia ngasih tau di depan. Gimana sih?"

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Oh iya, kan kamu merhatiin dia banget. Si paling perhatian." 

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Ah sudahlah..."
    jump scene_2c

label scene_2b_rahasia:
    
    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Rahasia!."

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Yah kenapa? Kasih tau dong!"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Diego apaansi. Itukan privasi dia, biarin aja. Lagi pula, kenapa sih pengen tau banget?"

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Aku penasaran siapa ceweknya."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Giliran cewek aja cepet."

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Ah sudahlah..."
    jump scene_2c

label scene_2c:
    hide raka
    hide diego
    hide mila

    "Raka meninggalkan Diego dan Mila di kantin."

    jump scene_3

label scene_3:
    scene bg class with fade  # <- Ganti ini jika punya background kelas, misal: "bg_class.jpg"

    "MPLS sudah selesai. Peserta didik sudah memulai aktivitas sekolah seperti biasa. Kelas akan segera dimulai."

    show raka normal mirror at left_terang
    r "ini gurunya mana sih kok gaada? Telat kali ya…"

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "(Luna berbincang dengan temannya dan ada sound effect suara percakapan)"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Eh- itu luna bukan ya?"

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
    l "Eh- iya kenapa raka?"

    show raka normal mirror at left_terang
    show luna normal at right_redup
    r "Gapapa sih, manggil aja."

    show luna normal at right_terang
    show raka normal mirror at left_redup
    l "Eh? Gitu doang...? Hehe, kirain kenapa."
    l "Raka kenapa ya? Tiba-tiba manggil…"

    hide raka normal mirror
    hide luna normal
    show tiffany normal at right_terang
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide tiffany normal
    jump scene_4

label scene_3b:
    show raka normal mirror at left_terang
    r "Kenapa ga aku panggil aja ya tadi? Siapa tau dia notice aku."
    r "Mungkin belum saatnya. Semoga nanti masih ada kesempatan ngobrol."

    show tiffany normal at right_terang
    show raka normal mirror at left_redup
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide raka normal mirror
    hide tiffany normal

    jump scene_4

label scene_4:
    "Jam istirahat telah tiba, Raka berjalan menuju kantin dan melalui ruang perpustakaan."

    show raka normal mirror at left_terang
    r "hm… udah istirahat nih, pengen ke kantin sih.. Tapi belum ada teman, aku sama Diego dan Mila aja deh.."
    r "Eh- itu bukannya kakak kelas yang tadi ya?.. Siapa namanya.. Oh iya Nara! Aku sapa ga ya?"

    menu:
        "sapa nara":
            jump scene_4a_sapa
        "ga sapa":
            jump scene_4a_gasapa

label scene_4a_sapa:

    show raka normal mirror at left_terang
    r "Halo… kak Nara ya? Yang tadi di auditorium."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Iya. Kenapa ya?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Kenalin kak, Aku Raka dari kelas 10 MIPA 5. Kalau kakak kelas apa?"

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
        "Wah! kaka suka baca novel juga?":
            jump scene_4a_sapa_v1
        "Aku fikir kaka mau rapat":
            jump scene_4a_sapa_v2
        "Sama siapa?":
            jump scene_4a_sapa_v3

label scene_4a_sapa_v1:

    show nara normal at right_terang
    n "iya, kamu baca novel?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Baru-baru ini sih kak, Ada rekomendasi ga ka?"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Kamu sukanya genre apa?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Biasanya baca nya romance sih kak."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh aku tahu yang bagus nih, love in bekasi"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oh iya, aku juga pernah denger juga"

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
    r "Wah! fantasy pasti kakaknya baca series Pluto dari Tiro Lio"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Iya! Kamu bener."
    n "Aku koleksi semua seriesnya!"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Aku masih penasaran banget soalnya."

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "boleh tapi aku ga bawa bukunya, gimana kalau nanti kamu ke kelas aku aja sepulang sekolah?"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "boleh banget tuh kak!"
    r "Oke kak, aku duluan ya.. Udah ditunggu temen soalnya"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Aku tunggu ya..."

    hide nara normal
    hide raka normal mirror

    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."

    show diego normal at right_terang
    d "kok lama banget sih keluarnya?"

    menu:
        "cerita ketemu nara":
            jump scene_4a_sapa_v1_cerita
        "ga cerita":
            jump scene_4a_sapa_v1_gacerita

label scene_4a_sapa_v1_cerita:

    show raka normal mirror at left_terang
    r "Tadi aku ketemu seseorang."

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Siapa lagi.. Tuh?"

    hide diego normal
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Coba cerita"

    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Jadi aku ketemu Nara yang anggota OSIS itu loh.."
    
    hide raka normal mirror
    show diego normal mirror at left_terang
    show mila normal at right_terang
    z "Oh.. Kak Nara.." #diego sama mila

    hide diego normal mirror
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "kak Nara Kenapa ?"

    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "kayaknya aku tertarik deh, sama kak nara"
    z "hah!.. Serius?!.." #diego sama mila

    show raka normal mirror at left_terang
    show mila normal at right_redup
    r "Iya serius!... Ternyata kak nara orangnya suka baca novel, bantuin aku dong.."
    
    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Bantuin gimana tuh?"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Bantuin deketin lah, gimana sih kamu!"

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Hehehe."

    hide mila normal mirror
    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "Nanti aku mau ke kelas Kak Nara untuk pinjam bukunya. Kira-kira aku harus apa lagi ya?"

    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Menurutku ya, setelah kamu baca bukunya, coba deh kamu ceritakan secara berkala ke Kak Nara. supaya, Kak Nara tahu kalau kamu benar-benar baca buku dia."
    
    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Aku setuju sama Diego, tapi, jangan terlalu gegabah. Ga semua cewek suka langsung di deketin secara berkala."
    
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Hm.. bener juga."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Emang buku apa yang dibaca sama kak Nara?"
    
    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Nah! Bukunya itu yang sama persis kayak yang kamu baca Mil…"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Hah? Yang mana? Banyak loh buku yang ku baca.."
    
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Yang kayak nama planet itu loh Mil…"

    hide raka normal
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Pluto ga sih Mil? Yang kamu pajang itu."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Oh astaga! Yang itu."

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Nah! Pokoknya itu lah. Ceritain dong Mil itu kayak gimana…"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Jadi-"

    hide raka normal
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Ih, waktu itu aku tanya ceritanya malah disuruh baca sendiri. Curang!"

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Diem dulu deh kamu Diego! Ini lagi serius!"
    m "Jadi, ceritanya tentang seorang character yang punya kekuatan super, tepatnya kekuatan menghilang. Tapi, dia sembunyikan kekuatan itu dari semua orang termasuk orang tuanya sendiri."
    m "Lalu, di suatu hari, ada temen sekelasnya yang bisa dibilang paling pintar diantara yang lain. Dia mulai curiga dengan si karakter utama ini, kalau Karakter ini punya kekuatan."
    m "Nah! dibuku edisi pertama ini, akan menceritakan hal tadi dan ternyata di dunia mereka, ga hanya pemeran utamanya yang punya kekuatan super."
    
    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Menarik ya… pantesan aja Kak Nara suka."
    r "Siapa nama karakter utamanya Mil?"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Nam-"

    hide raka normal
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Namanya Raya."

    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Dan nama karakter pintar tadi adalah Alri"

    hide diego normal
    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Terus, selanjutnya aku harus apa?"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Nanti kamu ke-kelas dia sepulang sekolah kan?"

    show raka normal at right_terang
    show mila normal mirror at left_redup
    r "Iya…"

    show mila normal mirror at left_terang
    show raka normal at right_redup
    m "Nanti ajak pulang bareng aja.."

    hide raka normal
    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "setuju!"

    hide diego normal
    hide mila normal mirror

    jump scene_5

label scene_4a_sapa_v1_gacerita:
    show raka normal mirror at left_terang
    r "aku tadi ke toilet dulu"

    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Yaudah kalian mau pesen apa?"

    hide mila normal
    show diego normal at right_terang
    show raka normal mirror at left_redup
    d "Aku ayam geprek"

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "aku samain aja deh"

    hide diego normal
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Kebiasaan."
    
    hide raka normal mirror
    hide diego normal
    hide mila normal

    jump scene_5
    
label scene_4a_sapa_v2:

    show nara normal at right_terang
    n "Engga sih."
    n "Aku duluan ya."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oke kak."

    hide raka normal mirror
    hide nara normal

    jump scene_4b  

label scene_4a_sapa_v3:

    show nara normal at right_terang
    n "Sama siapapun itu, bukan urusan kamu!"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oh iya kak maaf."
    
    hide nara normal
    n "(pergi tanpa kata kata)"
    $ nara_hearts+=-1
    
    hide raka normal mirror

    jump scene_4b

label scene_4b:
    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."

    show diego normal at right_terang
    d "kok lama banget sih keluarnya?"

    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "aku tadi ke toilet dulu"

    hide raka normal mirror
    show mila normal mirror at left_terang
    show diego normal at right_redup
    m "Yaudah kalian mau pesen apa?"

    show diego normal at right_terang
    show mila normal mirror at left_redup
    d "Aku ayam geprek"

    hide mila normal mirror
    show raka normal mirror at left_terang
    show diego normal at right_redup
    r "aku samain aja deh"

    hide diego normal
    show mila normal at right_terang
    show raka normal mirror at left_redup
    m "Kebiasaan."

    hide diego normal
    hide raka normal mirror
    hide mila normal

    jump scene_6

label scene_5:
    "Bell sekolah telah berbunyi, menandakan sudah tiba saatnya pulang sekolah. Sebelum bergegas pulang ke rumah, Raka menyempatkan diri mengunjungi kelas Nara untuk meminjam buku novelnya yang sudah dijanjikan."
    show raka normal mirror at left_terang
    r "(Hatiku berdegup kencang, aku pun melihat jendela kelas kak Nara namun, disana aku melihat dia sedang berbicara akrab dengan satu cowo.)"
    r "itu siapanya kak nara ya?” (Khawatir)"    
    r "Halo. Kak Nara"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Eh- halo."

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Aku mau ambil buku yang tadi kakak pinjamkan…"

    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh iya, Ini bukunya.. Jangan lupa dibaca ya…"

    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Pasti dong kak!"

    hide nara normal
    show arga normal at right_terang
    show raka normal mirror at left_redup
    a "Siapa dia Ra?"

    hide raka normal mirror
    show nara normal mirror at left_terang
    show arga normal at right_redup
    n "Oh ini temen baruku. adik kelas kita, tadi ketemu di perpustakaan."

    show arga normal at right_terang
    show nara normal mirror at left_redup
    a "Oh temen doang."

    hide nara normal mirror
    show raka normal mirror at left_terang
    show arga normal at right_redup
    r "(Hah? Mereka pacaran?!)"

    hide arga normal
    show nara normal at right_terang
    show raka normal mirror at left_redup
    n "Oh iya, Raka. Kenalin ini temen aku, dia namanya Arga…"

    hide raka normal mirror
    show arga normal mirror at left_terang
    show nara normal at right_redup
    a "Iya kenalin aku Arga. Ketua OSIS di sekolah ini."

    hide nara normal
    show raka normal at right_terang
    show arga normal mirror at left_redup
    r "(Ternyata hanya teman. Tapi kok deket banget ya? Apa jangan-jangan si Arga ini juga suka sama Kak Nara?)"
    r "Halo kak, aku Raka dari 10 MIPA 5. Salam kenal ya!"
    r "Oh iya kak mau ke toko buk—"

    show arga normal mirror at left_terang
    show raka normal at right_redup
    a "Ra, jadi kan kita makan bareng?"

    hide raka normal
    show nara normal at right_terang
    show arga normal mirror at left_redup
    n "Jadi dong.. Kan udah janji"
    n "Tadi kenapa Raka?"
    
    hide arga normal mirror
    show raka normal mirror at left_terang
    show nara normal at right_redup
    r "Oh gapapa kak, gajadi"

    hide nara normal
    show arga normal at right_terang
    show raka normal mirror at left_redup
    a "Yuk berangkat sekarang, nanti takuntya penuh"

    hide raka normal mirror
    show nara normal mirror at left_terang
    show arga normal at right_redup
    n "Yuk! Duluan ya raka"

    hide arga normal
    show raka normal at right_terang
    show nara normal mirror at left_redup
    r "iya kak. hati hati ya.. Oh iya, makasih juga bukunya."

    show nara normal mirror at left_terang
    show raka normal at right_redup
    n "Oh, tenang aja!"

    show raka normal at right_terang
    show nara normal mirror at left_redup
    r "(Yah, padahal tadi seru kalau pergi bareng sambil ngobrolin novel plutonya Mila.)"

    hide arga normal
    hide raka normal
    hide nara normal mirror

label scene_6:
    r "Pak tunggu! Jangan ditutup gerbangnya!"
    npc "Yah kamu telat! Sudah tidak bisa."
    r "Hanya telat dua menit pak, please…"
    npc "Gabisa, sudah peraturannya begitu."
    r "Hm… gimana ya caranya?"
    r "apa aku coba manjat yah?"
    r "(raka sedang mencari jalan)"
    "Saat Raka mencari jalan, Raka melihat Luna duduk di pojok tembok."
    r "Eh- Luna! Ngapain?"
    l "Hi Raka, kamu telat juga?"
    
    menu:
        "Menurut Kamu?":
            jump scene_6a
        "Hehehe, telat sih… Tapi cuma sedikit.":
            jump scene_6b
    
label scene_6a:
    l "haha iya juga ya. Gimana sih aku."
    $ luna_hearts+=-1

label scene_6b:
    l "Hahaha, bagus deh! Aku jadi ada teman telat bersama!"
    r "Kamu kenapa telat?"
    l "Tadi supir aku telat datangnya.."
    l "Kalau kamu kenapa?"
    r "Alarm aku rusak, jadi kesiangan deh."
    r "(Hm.. kira-kira..?)"
    menu:
        "Ajak jalan keluar.":
            jump scene_6b_ajak_jalan
        "Cari jalan masuk sekolah.":
            jump scene_6b_cari_jalan

label scene_6b_ajak_jalan:
    r "kamu udah sarapan belum?"
    l "belum, kenapa mau jajan bareng?"
    r "boleh, asal sama kamu."
    # (gambar luna kaget tersipu malu)
    l "Ah.. Eh? Tadi apa? Aku ga dengar…"
    r "Mau jajan kan?"
    l "Oh iya, aku mau jajan…"
    l "Eh- maksudnya kita jajan…"
    r "(emang dia seimut ini ya..?)"
    r "kamu jajan apa?"
    l "Aku.. aku gatau tempat jajan disini dimana.."
    r "Kamu biasanya jajan dimana?"
    l "Aku selama ini ga pernah jajan"
    r "Kalau gitu, aku mau nunjukin jajanan tradisional enak! aku yakin kamu suka!"
    l "Boleh.. Yuk!!!"
    "Raka dan Luna berjalan menuju toko jajanan tradisional, sambil berbincang dan tertawa bersama."
    r "Permisi bu, saya mau pesan onde-onde nya 5 ya.."
    npc "Siap dek, ditunggu ya.."
    "Sambil menunggu kue siap, Raka dan Luna melihat sekeliling etalase kue-kue."
    npc "ini dek, kue-nya."
    r "Makasih bu!"
    "Raka dan Luna meninggalkan toko kue, lalu pergi ke taman."
    r "Nih, kue nya!"
    "Luna mengambil kue onde-onde yang diberikan oleh Raka, lalu memakan kue onde-onde tersebut."
    l "Wah!!! Ini apa?! Enak banget!"
    r "Hahaha, iya memang!"
    $ luna_hearts += 1
    b "Luna?! Kamu ngapain disini?"
    "Raka terkejut saat melihat ada seseorang yang menyapa Luna dengan sangat akrab."
    r "(Dia siapa?)"
    l "Ben?! Eh- aku- aku lagi jajan…"
    "Ben melihat seragam yang di kenakan oleh Luna."
    b "Kamu sekolah di SMA Harapan Bangsa juga?"
    l "Iya. Kamu juga Ben? Kok aku gapernah lihat kamu ya dari awal masuk."
    b "Hehe… aku memang belum pernah masuk. Setelah sampai depan gerbang, aku selalu pergi, karena itu bukan sekolah yang aku mau!"
    l "Ben nakal ya! Aku bilangin mamih kamu nanti ya!"
    b "Eh?! Jangan Luna!"
    l "Hahaha! Lagian sih nakal."
    b "Hehehe, makasih Luna cantik!"
    l "Aku terima ga ya ucapan terimakasih-nya?"
    b "Terima! Nanti aku kasih hadiah!"
    l "Benar ya? Oh iya Ben, aku hampir lupa. Kenalin, ini temanku namanya Raka."
    b "Hai! Aku Ben, semoga kita akrab ya."
    "Raka tersontak seketika disaat Ben dengan sangat mudah dan ramah mengajaknya  berkenalan."
    r "Oh, aku Raka. Salam kenal ya."
    b "Wah! Kalian kelas berapa?"
    l "Kita dari kelas 10 MIPA 5. Kalau kamu?"
    b "Jadi kalian berdua sekelas ya?"
    l "Iya! Kita berdua sangat akrab!!"
    "Raka merasa malu saat Luna menganggapnya sebagai teman akrabnya."
    r "Eh- iya.. Kita berdua sangat akrab."
    b "Bagus kalau gitu! Karena kalian sekelas, aku bisa main ke kelas kalian sekaligus. Tanpa harus datang ke dua kelas bergantian!"
    r "(Ngapain sih dia? Menyebalkan.)"
    l "Ben! Jangan usil ya tapi?"
    b "Usil ga ya… "
    l "Ben! Jangan usil!"
    b "Ga usil? Ga asik!"
    l "Ben!"
    "Luna memukul pundak Ben."
    # (sound effect gedebuk)
    b "Aku pergi duluan ya Luna, Raka."
    l "Secepat itu?"
    b "Iya! Aku ada urusan hehe."
    l "Baiklah. Hati-hati ya!"
    r "Hati-hati ya."
    b "Sampai jumpa di sekolah semuanya!"
    "Ben meninggalkan Luna dan Raka di taman."
    r "Tadi itu siapa kamu Luna?"
    l "Itu teman kecilku. Kita selalu bersama dari usia tiga tahun."
    r "Kalian bertemu dimana?"
    l "Kebetulan orang tua kami berteman, dan kami tinggal di komplek yang sama. Lalu kami juga selalu pergi ke sekolah yang sama."
    l "Tapi, disaat masuk SMA ini aku ga tahu kabar Ben sekolah dimana. Dan ternyata kita satu sekolah lagi."
    r "Sebuah kebetulan yang sangat menyebalkan!"
    $ unlocked_ben = True
    call unlock_character("Ben", "Teman masa kecil Luna yang usil dan ceria.", "card ben")
    return

label scene_6b_cari_jalan:
    "Raka dan Luna berpencar mencari celah di tembok belakang sekolah."
    l "Rakaa! Sini… aku ketemu jalan masuk."
    r "Dimana tuh?"
    # (Delay + Sound effect annoying)
    r "Luna.. Luna.. ini mah gabisa."
    r "Hm.."
    r "Coba deh... kamu injak kakiku, terus naik ke dindingnya. Kayaknya bisa deh dari sini."
    l "Yakin kamu kuat?"
    r "Iya, yaudah cepetan sebelum ada yang lihat!"
    "Luna naik pelan-pelan sambil pegangan ke tembok."
    l "Awas aja ya kalo aku jatuh…"
    r "Tenang aja, aku tahan. Udah bisa, belum?"
    l "Dikit lagi... nah, udah! Aku di atas!"
    r "Oke, sekarang bantu aku naik juga!"
    "Luna dari atas tembok, nengok ke bawah."
    l "Raka, ini tinggi juga sih… Aku ga yakin kalau aku bisa."
    "Raka ngeliat ke atas, mikir sebentar."
    r "Iya juga ya... tunggu disini ya Luna.., di situ ada pipa tuh tapi agak berkarat sih."
    l "Gapapa, asal bisa bantu turun. Kamu bisa turunin tangan juga gak? Biar aku pegangan."
    r "Oke, sini, injek tong sampah itu dulu, yang ada dibawah. Terus loncat, aku tarik!"
    "Luna injak tong sampah, loncat sambil tangannya ngegapai tangan Raka. Luna turun dengan susah payah."
    l "Hahh… berhasil juga… gila... deg-degan banget!"
    r "Wah! Ternyata kamu bisa juga Luna. yuk, lanjut sebelum kita ketahuan."
    "Raka dan Luna bergegas menuju kelas dengan mengendap-ngendap."
    b "Eh?! Luna!! Kamu ngapain disini??"
    b "Kamu juga sekolah disini??"
    l "Eh?! Ben! Kamu juga ngapain disini?"
    "Raka terkejut saat melihat ada seseorang yang menyapa Luna dengan sangat akrab."
    l "Aku sekolah disini, tapi tadi aku telat hehe, untung ada Raka jadi aku bisa manjat."
    l "Kok aku gapernah liat kamu sih disekolah?"
    b "Hehehe, iya. Aku selalu bolos dari awal masuk. Sekarang-pun aku niatnya mau bolos. Tapi malah ketemu kalian di sini."
    l "Ben nakal ya! Aku bilangin mamih kamu nanti ya."
    b "Eh?! Jangan Luna!"
    l "Hahaha! Lagian sih nakal."
    b "Hehehe, makasih Luna cantik!"
    l "Aku terima ga ya ucapan terimakasih-nya?"
    b "Terima! Nanti aku kasih hadiah!"
    l "Benar ya? Oh iya Ben, aku hampir lupa. Kenalin, ini temanku namanya Raka."
    b "Hai! Aku Ben, semoga kita akrab ya."
    "Raka tersentak seketika disaat Ben dengan sangat mudah dan ramah mengajaknya  berkenalan."
    r "Oh, aku Raka. Salam kenal ya."
    b "Wah! Kalian kelas berapa?"
    l "Kita dari kelas 10 MIPA 5. Kalau kamu?"
    b "Jadi kalian berdua sekelas ya?"
    l "Iya! Kita berdua sekelas."
    b "Bagus kalau gitu! Karena kalian sekelas, aku bisa main ke kelas kalian sekaligus. Tanpa harus datang ke dua kelas bergantian!"
    r "(Ngapain sih dia? Menyebalkan.)"
    l "Ben! Jangan usil ya tapi?"
    b "Usil ga ya… "
    l "Ben! Jangan usil!"
    b "Ga usil? Ga asik!"
    l "Ben!"
    "Luna memukul pundak Ben."
    b "Aku pergi duluan ya Luna, Raka."
    l "Loh kamu mau kemana?! Kamu mau bolos yah!!"
    b "Hehe iya, aku ada janji diluar"
    l "Awas ya nanti aku bilangin mamih kamu loh."
    b "Untuk hari ini aja kok luna, besok besok aku pasti masuk sekolah."
    l "Oke, awas ya! Kalau besok aku ga lihat kamu, nanti aku kasih tau mamih kamu pokoknya."
    b "Siap, pasti kok aku pasti masuk sekolah soalnya ada kamu."
    "Ben meninggalkan Luna dan Raka di belakang sekolah."
    r "Tadi itu siapa kamu Luna?"
    l "Itu teman kecilku. Kita selalu bersama dari usia tiga tahun."
    r "Kalian bertemu dimana?"
    l "Kebetulan orang tua kami berteman, dan kami tinggal di komplek yang sama. Lalu kami juga selalu pergi ke sekolah yang sama."
    l "Tapi, disaat masuk SMA ini aku ga tahu kabar Ben sekolah dimana. Dan ternyata kita satu sekolah lagi."
    $ unlocked_ben = True
    call unlock_character("Ben", "Teman masa kecil Luna yang usil dan ceria.", "card ben")

label scene_7:
    rl "(Sound effect peluit) prittttttt… semua anak 10 MIPA 5 diharap pergi kelapangan dan memakai seragam olahraga"
    r "Tunggu pak!"
    r "(Susah banget sih pakai sepatu ini)"
    l "Ayo Raka!"
    r "Luna tunggu!"
    "Luna kembali berlari kearah gedung sekolah menghampiri Raka."
    l "Aku tungguin, ya."
    r "Sudah!"
    "Setelah Raka selesai mengikat sepatunya, mereka berdua kembali berlari menuju lapangan sekolah."
    rl "Kalian telat!"
    rl "Kalian lari ya, keliling lapangan."
    l "Yah pak! Kan cuma selisih dikit… "
    l "Ayolah pak.."
    rl "Gimana ya… gaboleh! Lari dua puluh kali."
    l "Yah pak, capek dong?"
    r "Iya pak, kasian tuh Luna nanti kecapekan."
    rl "Kalian ini bisa aja ya nawarnya."
    l "Iya pak, nanti kaki saya sakit gimana?"
    rl "Yaudah, lima belas kali deh."
    r "Masih banyak tuh pak, sepuluh aja gimana?"
    l "Iya pak, sepuluh deh gapapa. Please…"
    rl "Yaudah iya, iya. Sepuluh kali keliling. Cepat sana."
    l "Siap!"
    r "Siap!"
    l "Makasih bapak Rilandy yang sangat tampan. Bapak baik banget deh!"
    r "Makasih pak!"
    rl "Ah, bisa aja kalian ini."
    "Raka dan Luna memulai hukuman lari mereka bersama."
    r "Luna, aku minta maaf  ya. Karena kamu nungguin aku, kamu jadi ikut dihukum juga."
    l "Ihh.. Gapapa Raka, kan aku yang mau sendiri buat nungguin kamu."
    r "Tapi aku jadi merasa bersalah karena kamu ikut dihukum juga."
    l "Gapapa kok Raka, Kamu ga salah kok."
    r "Jangan gitu Luna."
    r "Gimana nanti kalau istirahat aku traktir"
    l "Gausah Raka. Aku gapapa kok. "
    r "Gapapa kok, kan ini aku juga yang mau."
    l "Hahaha,Yaudah deh kalau kamu maksa."
    l "Makasih ya Raka."
    r "Sama-sama, Luna."
    "Raka dan Luna menyelesaikan hukuman yang mereka dapatkan."
    r "Pak, kita berdua sudah selesai lari nya."
    rl "Wih, hebat kalian. Yasudah, sana kalian istirahat atau beraktivitas bebas lainnya."
    r "Oke pak, makasih ya."
    l "Oke pak, makasih ya."
    npc "Rakaa! Ayok main basket bareng!"
    r "Duluan! Nanti nyusul!"
    r "Luna, aku main basket dulu ya."
    l "Oke, semangat ya!"
    "Raka melanjutkan kegiatan bermain bola basket bersama teman sekelasnya."
    # (Sound Effect bola jatuh)
    "Bola yang Raka lempar tidak sengaja mengenai Nara yang sedang lewat di samping lapangan."
    npc "Kak Nara!"
    r "Kak Nara!"
    "Semua orang disekitar menghampiri Nara yang tejatuh."
    "Raka mencoba menghampiri Nara yang terjatuh, namun terhalang oleh banyaknya orang yang berada di sekitar Nara."
    rl "Nara kamu gapapa?"
    n "Ga- gapapa pak."
    rl "Bisa berdiri ga?"
    n "Bisa pak."
    "Nara mencoba berdiri…"
    # (Sound effect jatuh)
    "Nara terjatuh dan tidak bisa berdiri."
    n "Aw."
    rl "Udah gausah berdiri."
    "Pak Rilandy bergegas membawa Nara ke ruang UKS."
    # (Bel istirahat berbunyi)
    r "(Duh… sekarang jam istirahat.)"
    r "(Tadi aku udah janji buat traktir Luna… tapi aku juga yang bikin Kak Nara jatuh.)"
    r "(Gimana ya? Kalau aku tinggalin Luna, nanti dia mikir aku ngelupain janji.)"
    r "(Tapi Kak Nara juga pasti sakit banget… dan itu salahku, aku harus minta maaf.)"
    r "(Aku harus gimana? Aduh…)"
    r "(Kalau aku pergi ke UKS Luna gimana?)"
    r "(Tapi kalau aku pergi ke Luna, Kak Nara gimana?)"
    menu:
        "Temui Luna":
            jump scene_7_luna
        "Temui Nara":
            jump scene_7_nara

label scene_7_luna:
    "Raka akhirnya memilih menepati janji-nya kepada Luna."
    r "Hai Luna, udah nunggu lama ya?"
    l "Hai Raka, engga kok. Aku belum lama disini."
    r "Kamu udah pesan?"
    l "Belum, aku nungguin kamu."
    r "Aku pesenin ya?"
    l "Boleh."
    r "Luna, coba tebak aku mau pesen apa di antara menu ini?"
    l "Hm… Nasi goreng?"
    r "Betul!"
    r "(Padahal sebenarnya aku gatau mau pesan apa.)"
    l "Haha sudah kutebak pasti kamu mau pilih nasi goreng, aku kan pintar."
    r "Sebentar ya, aku pesan dulu."
    l "Iya, Raka."

    return



