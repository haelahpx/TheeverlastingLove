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
    xpos 0.0
    ypos 0.7
    xanchor 0.06
    yanchor 0.9
    alpha 1.0
    linear 0.2 alpha 1.0

transform left_redup:
    xpos 0.0
    ypos 0.7
    xanchor 0.06
    yanchor 0.9
    alpha 0.4
    linear 0.2 alpha 0.4

# Transformasi untuk karakter kanan (pojok kanan atas dialog box)
transform right_terang:
    xpos 1.0
    ypos 0.3
    xanchor 0.95
    yanchor 0.22
    alpha 1.0
    linear 0.2 alpha 1.0

transform right_redup:
    xpos 1.0
    ypos 0.3
    xanchor 0.95
    yanchor 0.22
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

label unlock_character(char_name, char_desc, char_image):
    call screen character_card(char_name, char_desc, char_image)
    return
label start:
    scene auditorium
    with fade

    play music "bgm/videoplayback.m4a"

    show raka normal at left_terang
    with dissolve
    r "Hari ini adalah hari pertamaku masuk SMA."
    r "Aku kepikiran deh, aku bisa ga ya cepat beradaptasi dan dapat teman baru? Hm…"

    play sound "footstep.ogg"

    show luna normal at right with moveinright
    l "Hai!"

    show raka kaget at center
    r "(kaget)"
    r "(dalam hati) Wah! Dia siapa? Cantik banget… Ceria, penuh semangat dan ramah banget…"
    show raka normal at center
    r "Oh! Hai?"

    l "Boleh kenalan ga? Nama kamu siapa?"
    r "Eh- boleh… aku Raka."
    r "Kalau nama kamu?"
    l "Luna! Namaku Luna…"

    play sound "mic_test.ogg"

    show nara normal at right
    n "Test, test, test…"
    n "Halo semuanya, nama saya Nara sebagai perwakilan dari OSIS. Ada pemberitahuan, bagi peserta didik baru SMA Harapan Bangsa, di mohon untuk mencatat informasi yang tertera di mading sekolah sebagai arahan mengenai kegiatan MPLS sekolah kami."

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
    show raka normal at left
    play sound "shout.ogg"
    d "Rakaaa!"
    m "Siniiii!"
    r "Eh- itu mereka."

    show raka normal at left
    show diego normal at center
    show mila normal at right

    r "Diegoo! Milaa!"

    jump scene_2a

label scene_2a:
    scene bg_kantin_table with fade

    "Raka, Diego dan Mila berjalan menuju meja makan kantin untuk melanjutkan percakapan mereka."
    show mila normal at left
    m "Gimana hari pertama kamu Raka?"
    hide mila normal
    show raka normal at left
    r "Biasa aja sih, gaada yang seru."
    hide raka normal
    show mila normal at left
    m "Ah iya? Kok gitu sih…"
    hide mila normal
    show diego normal at left
    d "Masa sih? Ga ada ketemu cewek gitu?"
    hide diego normal
    show mila normal at left
    m "Diego! Apaansih."
    hide mila normal
    show raka normal at left
    r "Eh- hehehe… Ada sih…"
    hide raka normal
    show diego normal at left
    d "Hah? Serius? Siapa?!"

    menu:
        "Ceritain Luna":
            jump scene_2b_luna
        "Ceritain Nara":
            jump scene_2b_nara
        "Gak cerita":
            jump scene_2b_rahasia

label scene_2b_luna:
    show diego normal at left 
    r "Tadi ada cewe rambutnya pirang, cantik banget… ramah dan ceria gitu orangnya, seolah-olah punya banyak energi seharian."
    show mila normal at left
    m "Oh iya? Kayaknya tadi aku lihat deh, emang cantik banget tuh.."
    d "Eh- emang ada? Kok aku ga liat sih..." 
    "Diego tampak agak sedikit kecewa."
    m "Kenapa kecewa gitu mukanya?! Dih cantik dikit langsung gitu." 
    r "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"
    d "Siapa namanya?"
    m "Kenapa harus ditanya?" 
    "Mila menatap Diego dengan sinis."
    r "Namanya Luna."
    d "Namanya cantik deh…"
    m "Ribut yuk?"
    r "Ah sudahlah..."
    jump scene_2c

label scene_2b_nara:
    r "Kalian lihat ga sih cewe yang kasih pengumuman di auditorium tadi?"
    d "Oh... itu! aku merhatiin dia tadi, yang tinggi dan cantik itu kan?"
    m "Merhatiin banget nih, kayakya sampai detail begitu."
    d "Oh ya.. jelas! dia cantik banget sih emang…"
    m "Terserah deh." 
    "Mila menatap Diego dengan sinis."
    r "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"
    m "Siapa namanya?"
    r "Aku gatau sih belum kenalan…"
    d "Masa gatau sih... Nama dia Nara, perwakilan dari OSIS."
    m "Kok kamu tau sih?! Raka aja gatau, kok kamu bisa tahu?!"
    d "Kan tadi dia ngasih tau di depan. Gimana sih?"
    m "Oh iya, kan kamu merhatiin dia banget. Si paling perhatian." 
    r "Ah sudahlah..."
    jump scene_2c

label scene_2b_rahasia:
    r "Rahasia!."
    d "Yah kenapa? Kasih tau dong!"
    m "Diego apaansi. Itukan privasi dia, biarin aja. Lagi pula, kenapa sih pengen tau banget?"
    d "Aku penasaran siapa ceweknya."
    m "Giliran cewek aja cepet."
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

    show raka normal
    r "ini gurunya mana sih kok gaada? Telat kali ya…"
    l "(Luna berbincang dengan temannya dan ada sound effect suara percakapan)"
    r "Eh- itu luna bukan ya?"

    menu:
        "panggil luna":
            jump scene_3a
        "ga panggil luna":
            jump scene_3b

label scene_3a:
    show raka normal at left
    r "Luna..."
    show luna normal at right
    l "Eh- iya kenapa raka?"
    r "Gapapa sih, manggil aja."
    l "Eh? Gitu doang...? Hehe, kirain kenapa."
    l "Raka kenapa ya? Tiba-tiba manggil…"
    show ben normal at center
    show tiffany normal at right
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide raka normal 
    hide luna normal 
    hide ben normal
    jump scene_4

label scene_3b:
    show raka normal at left
    r "Kenapa ga aku panggil aja ya tadi? Siapa tau dia notice aku."
    r "Mungkin belum saatnya. Semoga nanti masih ada kesempatan ngobrol."
    show tiffany normal at right
    t "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide raka normal 
    hide tiffany normal

    jump scene_4

label scene_4:
    "Jam istirahat telah tiba, Raka berjalan menuju kantin dan melalui ruang perpustakaan."
    show raka normal at left
    r "hm… udah istirahat nih, pengen ke kantin sih.. Tapi belum ada teman, aku sama Diego dan Mila aja deh.."
    r "Eh- itu bukannya kakak kelas yang tadi ya?.. Siapa namanya.. Oh iya Nara! Aku sapa ga ya?"

    menu:
        "sapa nara":
            jump scene_4a_sapa
        "ga sapa":
            jump scene_4a_gasapa

label scene_4a_sapa:
    r "Halo… kak Nara ya? Yang tadi di auditorium."
    show nara normal at right
    n "Iya. Kenapa ya?"
    r "Kenalin kak, Aku Raka dari kelas 10 MIPA 5. Kalau kakak kelas apa?"
    n "Oh, aku 11 MIPA 5."
    r "Wah! sama dong, kakak lagi apa disini?"
    n "Oh, aku cuman mau baca novel sih."

    menu:
        "Wah! kaka suka baca novel juga?":
            jump scene_4a_sapa_v1
        "Aku fikir kaka mau rapat":
            jump scene_4a_sapa_v2
        "Sama siapa?":
            jump scene_4a_sapa_v3

label scene_4a_sapa_v1:
    n "iya, kamu baca novel?"
    r "Baru-baru ini sih kak, Ada rekomendasi ga ka?"
    n "Kamu sukanya genre apa?"
    r "Biasanya baca nya romance sih kak."
    n "Oh aku tahu yang bagus nih, love in bekasi"
    r "Oh iya, aku juga pernah denger juga"
    n "Nah itu, seru! Cobain deh.."
    r "Kalau kakak sukanya genre apa?"
    n "Aku sukanya fantasy."
    n "Tapi kadang juga baca self development sih."
    r "Wah! fantasy pasti kakaknya baca series Pluto dari Tiro Lio"
    n "Iya! Kamu bener."
    n "Aku koleksi semua seriesnya!"
    r "Aku masih penasaran banget soalnya."
    n "boleh tapi aku ga bawa bukunya, gimana kalau nanti kamu ke kelas aku aja sepulang sekolah?"
    r "boleh banget tuh kak!"
    r "Oke kak, aku duluan ya.. Udah ditunggu temen soalnya"
    n "Aku tunggu ya..."

    hide nara normal
    hide raka normal

    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."
    show raka normal at left
    show diego normal at right
    d "kok lama banget sih keluarnya?"

    menu:
        "cerita ketemu nara":
            jump scene_4a_sapa_v1_cerita
        "ga cerita":
            jump scene_4a_sapa_v1_gacerita

label scene_4a_sapa_v1_cerita:
    r "Tadi aku ketemu seseorang."
    d "Siapa lagi.. Tuh?"
    show mila normal at center
    m "Coba cerita"
    r "Jadi aku ketemu Nara yang anggota OSIS itu loh.."
    z "Oh.. Kak Nara.."
    m "kak Nara Kenapa ?"
    r "kayaknya aku tertarik deh, sama kak nara"
    z "hah!.. Serius?!.."
    r "Iya serius!... Ternyata kak nara orangnya suka baca novel, bantuin aku dong.."
    d "Bantuin gimana tuh?"
    m "“Bantuin deketin lah, gimana sih kamu!"
    d "Hehehe."
    r "Nanti aku mau ke kelas Kak Nara untuk pinjam bukunya. Kira-kira aku harus apa lagi ya?"
    d "Menurutku ya, setelah kamu baca bukunya, coba deh kamu ceritakan secara berkala ke Kak Nara. supaya, Kak Nara tahu kalau kamu benar-benar baca buku dia."
    m "Aku setuju sama Diego, tapi, jangan terlalu gegabah. Ga semua cewek suka langsung di deketin secara berkala."
    d "Hm.. bener juga."
    m "Emang buku apa yang dibaca sama kak Nara?"
    r "Nah! Bukunya itu yang sama persis kayak yang kamu baca Mil…"
    m "Hah? Yang mana? Banyak loh buku yang ku baca.."
    r "Yang kayak nama planet itu loh Mil…"
    d "Pluto ga sih Mil? Yang kamu pajang itu."
    m "Oh astaga! Yang itu."
    r "Nah! Pokoknya itu lah. Ceritain dong Mil itu kayak gimana…"
    m "Jadi-"
    d "Ih, waktu itu aku tanya ceritanya malah disuruh baca sendiri. Curang!"
    m "Diem dulu deh kamu Diego! Ini lagi serius!"
    m "Jadi, ceritanya tentang seorang character yang punya kekuatan super, tepatnya kekuatan menghilang. Tapi, dia sembunyikan kekuatan itu dari semua orang termasuk orang tuanya sendiri."
    m "Lalu, di suatu hari, ada temen sekelasnya yang bisa dibilang paling pintar diantara yang lain. Dia mulai curiga dengan si karakter utama ini, kalau Karakter ini punya kekuatan."
    m "Nah! dibuku edisi pertama ini, akan menceritakan hal tadi dan ternyata di dunia mereka, ga hanya pemeran utamanya yang punya kekuatan super."
    r "Menarik ya… pantesan aja Kak Nara suka."
    r "Siapa nama karakter utamanya Mil?"
    m "Nam-"
    d "Namanya Raya."
    m "Dan nama karakter pintar tadi adalah Alri"
    r "Terus, selanjutnya aku harus apa?"
    m "Nanti kamu ke-kelas dia sepulang sekolah kan?"
    r "Iya…"
    m "Nanti ajak pulang bareng aja.."
    d "setuju!"

    hide raka normal
    hide diego normal
    hide mila normal

    jump scene_5

label scene_4a_sapa_v1_gacerita:
    show mila normal at center
    r "aku tadi ke toilet dulu"
    m "Yaudah kalian mau pesen apa?"
    d "Aku ayam geprek"
    r "aku samain aja deh"
    m "Kebiasaan."
    
    hide raka normal
    hide diego normal
    hide mila normal

    jump scene_5
    
label scene_4a_sapa_v2:
    n "Engga sih."
    n "Aku duluan ya."
    r "Oke kak."

    hide raka normal
    hide nara normal

    jump scene_4b  

label scene_4a_sapa_v3:
    n "Sama siapapun itu, bukan urusan kamu!"
    r "Oh iya kak maaf."
    hide nara normal
    n "(pergi tanpa kata kata)"
    $ nara_hearts+=-1
    
    hide raka normal

    jump scene_4b

label scene_4b:
    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."
    show diego normal at left
    d "kok lama banget sih keluarnya?"
    show raka normal at right
    r "aku tadi ke toilet dulu"
    show mila normal at center
    m "Yaudah kalian mau pesen apa?"
    d "Aku ayam geprek"
    r "aku samain aja deh"
    m "Kebiasaan."

    hide diego normal
    hide raka normal
    hide mila normal

label scene_5:
    "Bell sekolah telah berbunyi, menandakan sudah tiba saatnya pulang sekolah. Sebelum bergegas pulang ke rumah, Raka menyempatkan diri mengunjungi kelas Nara untuk meminjam buku novelnya yang sudah dijanjikan."
    show raka normal at left
    r "(Hatiku berdegup kencang, aku pun melihat jendela kelas kak Nara namun, disana aku melihat dia sedang berbicara akrab dengan satu cowo.)"
    r "itu siapanya kak nara ya?” (Khawatir)"
    show nara normal at right
    r "Halo. Kak Nara"
    n "Eh- halo."
    r "Aku mau ambil buku yang tadi kakak pinjamkan…"
    n "Oh iya, Ini bukunya.. Jangan lupa dibaca ya…"
    r "Pasti dong kak!"
    show arga normal at center
    a "Siapa dia Ra?"
    n "Oh ini temen baruku. adik kelas kita, tadi ketemu di perpustakaan."
    a "Oh temen doang."
    r "(Hah? Mereka pacaran?!)"
    n "Oh iya, Raka. Kenalin ini temen aku, dia namanya Arga…"
    a "Iya kenalin aku Arga. Ketua OSIS di sekolah ini."
    r "(Ternyata hanya teman. Tapi kok deket banget ya? Apa jangan-jangan si Arga ini juga suka sama Kak Nara?)"
    r "Halo kak, aku Raka dari 10 MIPA 5. Salam kenal ya!"
    r "Oh iya kak mau ke toko buk—"
    hide raka normal
    hide arga normal
    show arga normal at left
    a "Ra, jadi kan kita makan bareng?"
    n "Jadi dong.. Kan udah janji"
    n "Tadi kenapa Raka?"
    hide arga normal
    show arga normal at center
    show raka normal at left
    r "Oh gapapa kak, gajadi"
    a "Yuk berangkat sekarang, nanti takuntya penuh"
    n "Yuk! Duluan ya raka"
    r "iya kak. hati hati ya.. Oh iya, makasih juga bukunya."
    n "Oh, tenang aja!"
    r "(Yah, padahal tadi seru kalau pergi bareng sambil ngobrolin novel plutonya Mila.)"

return
