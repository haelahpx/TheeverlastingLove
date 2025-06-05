
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

label start:
    scene auditorium
    with fade

    play music "bgm/videoplayback.m4a"

    show raka normal at left_terang
    with dissolve
    R "Hari ini adalah hari pertamaku masuk SMA."
    R "Aku kepikiran deh, aku bisa ga ya cepat beradaptasi dan dapat teman baru? Hm…"

    play sound "footstep.ogg"

    show luna normal at left
    L "Hai!"

    show raka kaget at center
    R "(kaget)"
    R "(dalam hati) Wah! Dia siapa? Cantik banget… Ceria, penuh semangat dan ramah banget…"
    show raka normal at center
    R "Oh! Hai?"

    L "Boleh kenalan ga? Nama kamu siapa?"
    R "Eh- boleh… aku Raka."
    R "Kalau nama kamu?"
    L "Luna! Namaku Luna…"

    play sound "mic_test.ogg"

    show nara normal at right
    N "Test, test, test…"
    N "Halo semuanya, nama saya Nara sebagai perwakilan dari OSIS. Ada pemberitahuan, bagi peserta didik baru SMA Harapan Bangsa, di mohon untuk mencatat informasi yang tertera di mading sekolah sebagai arahan mengenai kegiatan MPLS sekolah kami."

    R "(dalam hati) Wah, kakak itu... bisa banget bawa diri. Udah keren, kalem, cantik pula. Komplit banget sih."

    jump scene_2

label scene_2:
    scene bg_kantin_gate with fade

    "Raka berjalan menuju arah kantin sekolahnya dan mencari kedua sahabatnya yang selalu bersama sejak SMP hingga saat ini."
    "Kedua sahabatnya ini sudah menjalin hubungan asmara bersama sejak SMP hingga saat ini."
    show raka normal at left
    play sound "shout.ogg"
    D "Rakaaa!"
    M "Siniiii!"
    R "Eh- itu mereka."

    show raka normal at left
    show diego normal at center
    show mila normal at right

    R "Diegoo! Milaa!"

    jump scene_2a

label scene_2a:
    scene bg_kantin_table with fade

    "Raka, Diego dan Mila berjalan menuju meja makan kantin untuk melanjutkan percakapan mereka."
    show mila normal at left
    M "Gimana hari pertama kamu Raka?"
    hide mila normal
    show raka normal at left
    R "Biasa aja sih, gaada yang seru."
    hide raka normal
    show mila normal at left
    M "Ah iya? Kok gitu sih…"
    hide mila normal
    show diego normal at left
    D "Masa sih? Ga ada ketemu cewek gitu?"
    hide diego normal
    show mila normal at left
    M "Diego! Apaansih."
    hide mila normal
    show raka normal at left
    R "Eh- hehehe… Ada sih…"
    hide raka normal
    show diego normal at left
    D "Hah? Serius? Siapa?!"

    menu:
        "Ceritain Luna":
            jump scene_2b_luna
        "Ceritain Nara":
            jump scene_2b_nara
        "Gak cerita":
            jump scene_2b_rahasia

label scene_2b_luna:
    show diego normal at left 
    R "Tadi ada cewe rambutnya pirang, cantik banget… ramah dan ceria gitu orangnya, seolah-olah punya banyak energi seharian."
    show mila normal at left
    M "Oh iya? Kayaknya tadi aku lihat deh, emang cantik banget tuh.."
    D "Eh- emang ada? Kok aku ga liat sih..." 
    "Diego tampak agak sedikit kecewa."
    M "Kenapa kecewa gitu mukanya?! Dih cantik dikit langsung gitu." 
    R "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"
    D "Siapa namanya?"
    M "Kenapa harus ditanya?" 
    "Mila menatap Diego dengan sinis."
    R "Namanya Luna."
    D "Namanya cantik deh…"
    M "Ribut yuk?"
    R "Ah sudahlah..."
    jump scene_2c

label scene_2b_nara:
    R "Kalian lihat ga sih cewe yang kasih pengumuman di auditorium tadi?"
    D "Oh... itu! aku merhatiin dia tadi, yang tinggi dan cantik itu kan?"
    M "Merhatiin banget nih, kayakya sampai detail begitu."
    D "Oh ya.. jelas! dia cantik banget sih emang…"
    M "Terserah deh." 
    "Mila menatap Diego dengan sinis."
    R "Udah-udah jangan berantem, mau aku lanjutin ga nih ceritanya?"
    M "Siapa namanya?"
    R "Aku gatau sih belum kenalan…"
    D "Masa gatau sih... Nama dia Nara, perwakilan dari OSIS."
    M "Kok kamu tau sih?! Raka aja gatau, kok kamu bisa tahu?!"
    D "Kan tadi dia ngasih tau di depan. Gimana sih?"
    M "Oh iya, kan kamu merhatiin dia banget. Si paling perhatian." 
    R "Ah sudahlah..."
    jump scene_2c

label scene_2b_rahasia:
    R "Rahasia!."
    D "Yah kenapa? Kasih tau dong!"
    M "Diego apaansi. Itukan privasi dia, biarin aja. Lagi pula, kenapa sih pengen tau banget?"
    D "Aku penasaran siapa ceweknya."
    M "Giliran cewek aja cepet."
    R "Ah sudahlah..."
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
    R "ini gurunya mana sih kok gaada? Telat kali ya…"
    L "(Luna berbincang dengan temannya dan ada sound effect suara percakapan)"
    R "Eh- itu luna bukan ya?"

    menu:
        "panggil luna":
            jump scene_3a
        "ga panggil luna":
            jump scene_3b

label scene_3a:
    show raka normal at left
    R "Luna..."
    show luna normal at right
    L "Eh- iya kenapa raka?"
    R "Gapapa sih, manggil aja."
    L "Eh? Gitu doang...? Hehe, kirain kenapa."
    L "Raka kenapa ya? Tiba-tiba manggil…"
    show ben normal at center
    T "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide raka normal 
    hide luna normal 
    hide ben normal
    jump scene_4

label scene_3b:
    show raka normal at left
    R "Kenapa ga aku panggil aja ya tadi? Siapa tau dia notice aku."
    R "Mungkin belum saatnya. Semoga nanti masih ada kesempatan ngobrol."
    show ben normal at right
    T "Halo anak-anak maaf ibu baru datang, selamat ya..bagi kalian yang keterima di SMA harapan bangsa, di kelas ini ibu sebagai wali kelas kalian. Kenalin nama ibu, Ibu Tiffany."

    hide raka normal 
    hide ben normal

    jump scene_4

label scene_4:
    "Jam istirahat telah tiba, Raka berjalan menuju kantin dan melalui ruang perpustakaan."
    show raka normal at left
    R "hm… udah istirahat nih, pengen ke kantin sih.. Tapi belum ada teman, aku sama Diego dan Mila aja deh.."
    R "Eh- itu bukannya kakak kelas yang tadi ya?.. Siapa namanya.. Oh iya Nara! Aku sapa ga ya?"

    menu:
        "sapa nara":
            jump scene_4a_sapa
        "ga sapa":
            jump scene_4a_gasapa

label scene_4a_sapa:
    R "Halo… kak Nara ya? Yang tadi di auditorium."
    show nara normal at right
    N "Iya. Kenapa ya?"
    R "Kenalin kak, Aku Raka dari kelas 10 MIPA 5. Kalau kakak kelas apa?"
    N "Oh, aku 11 MIPA 5."
    R "Wah! sama dong, kakak lagi apa disini?"
    N "Oh, aku cuman mau baca novel sih."

    menu:
        "Wah! kaka suka baca novel juga?":
            jump scene_4a_sapa_v1
        "Aku fikir kaka mau rapat":
            jump scene_4a_sapa_v2
        "Sama siapa?":
            jump scene_4a_sapa_v3

label scene_4a_sapa_v1:
    N "iya, kamu baca novel?"
    R "Baru-baru ini sih kak, Ada rekomendasi ga ka?"
    N "Kamu sukanya genre apa?"
    R "Biasanya baca nya romance sih kak."
    N "Oh aku tahu yang bagus nih, love in bekasi"
    R "Oh iya, aku juga pernah denger juga"
    N "Nah itu, seru! Cobain deh.."
    R "Kalau kakak sukanya genre apa?"
    N "Aku sukanya fantasy."
    N "Tapi kadang juga baca self development sih."
    R "Wah! fantasy pasti kakaknya baca series Pluto dari Tiro Lio"
    N "Iya! Kamu bener."
    N "Aku koleksi semua seriesnya!"
    R "Aku masih penasaran banget soalnya."
    N "boleh tapi aku ga bawa bukunya, gimana kalau nanti kamu ke kelas aku aja sepulang sekolah?"
    R "boleh banget tuh kak!"
    R "Oke kak, aku duluan ya.. Udah ditunggu temen soalnya"
    N "Aku tunggu ya..."

    hide nara normal
    hide raka normal

    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."
    show raka normal at left
    show diego normal at right
    D "kok lama banget sih keluarnya?"

    menu:
        "cerita ketemu nara":
            jump scene_4a_sapa_v1_cerita
        "ga cerita":
            jump scene_4a_sapa_v1_gacerita

label scene_4a_sapa_v1_cerita:
    R "Tadi aku ketemu seseorang."
    D "Siapa lagi.. Tuh?"
    show mila normal at center
    M "Coba cerita"
    R "Jadi aku ketemu Nara yang anggota OSIS itu loh.."
    Z "Oh.. Kak Nara.."
    M "kak Nara Kenapa ?"
    R "kayaknya aku tertarik deh, sama kak nara"
    Z "hah!.. Serius?!.."
    R "Iya serius!... Ternyata kak nara orangnya suka baca novel, bantuin aku dong.."
    D "Bantuin gimana tuh?"
    M "“Bantuin deketin lah, gimana sih kamu!"
    D "Hehehe."
    R "Nanti aku mau ke kelas Kak Nara untuk pinjam bukunya. Kira-kira aku harus apa lagi ya?"
    D "Menurutku ya, setelah kamu baca bukunya, coba deh kamu ceritakan secara berkala ke Kak Nara. supaya, Kak Nara tahu kalau kamu benar-benar baca buku dia."
    M "Aku setuju sama Diego, tapi, jangan terlalu gegabah. Ga semua cewek suka langsung di deketin secara berkala."
    D "Hm.. bener juga."
    R "jadi aku harus gimana?"
    M "Nanti kamu ke-kelas dia sepulang sekolah kan?"
    R "Iya…"
    M "Nanti ajak pulang bareng aja.."
    D "setuju!"

    hide raka normal
    hide diego normal
    hide mila normal

    jump scene_5

label scene_4a_sapa_v1_gacerita:
    show mila normal at center
    R "aku tadi ke toilet dulu"
    M "Yaudah kalian mau pesen apa?"
    D "Aku ayam geprek"
    R "aku samain aja deh"
    M "Kebiasaan."
    
    hide raka normal
    hide diego normal
    hide mila normal

    jump scene_5
    
label scene_4a_sapa_v2:
    N "Engga sih."
    N "Aku duluan ya."
    R "Oke kak."

    hide raka normal
    hide nara normal

    jump scene_4b  

label scene_4a_sapa_v3:
    N "Sama siapapun itu, bukan urusan kamu!"
    R "Oh iya kak maaf."
    hide nara normal
    N "(pergi tanpa kata kata)"
    
    hide raka normal

    jump scene_4b

label scene_4b:
    "Raka menuju kantin dimana Diego dan Mila sedang istirahat bersama."
    show diego normal at left
    D "kok lama banget sih keluarnya?"
    show raka normal at right
    R "aku tadi ke toilet dulu"
    show mila normal at center
    M "Yaudah kalian mau pesen apa?"
    D "Aku ayam geprek"
    R "aku samain aja deh"
    M "Kebiasaan."

    hide diego normal
    hide raka normal
    hide mila normal

label scene_5:
    "Bell sekolah telah berbunyi, menandakan sudah tiba saatnya pulang sekolah. Sebelum bergegas pulang ke rumah, Raka menyempatkan diri mengunjungi kelas Nara untuk meminjam buku novelnya yang sudah dijanjikan."
    show raka normal at left
    R "(Hatiku berdegup kencang, aku pun melihat jendela kelas kak Nara namun, disana aku melihat dia sedang berbicara akrab dengan satu cowo.)"
    R "itu siapanya kak nara ya?” (Khawatir)"
    show nara normal at right
    R "Halo. Kak Nara"
    N "Eh- halo."
    R "Aku mau ambil buku yang tadi kakak pinjamkan…"
    N "Oh iya, Ini bukunya.. Jangan lupa dibaca ya…"
    R "Pasti dong kak!"
    show arga normal at center
    A "Siapa dia Ra?"
    N "Oh ini temen baruku. adik kelas kita, tadi ketemu di perpustakaan."
    A "Oh temen doang."
    R "(Hah? Mereka pacaran?!)"
    N "Oh iya, Raka. Kenalin ini temen aku, dia namanya Arga…"
    A "Iya kenalin aku Arga. Ketua OSIS di sekolah ini."
    R "(Ternyata hanya teman. Tapi kok deket banget ya? Apa jangan-jangan si Arga ini juga suka sama Kak Nara?)"
    R "Halo kak, aku Raka dari 10 MIPA 5. Salam kenal ya!"
    R "Oh iya kak mau ke toko buk—"
    hide raka normal
    hide arga normal
    show arga normal at left
    A "Ra, jadi kan kita makan bareng?"
    N "Jadi dong.. Kan udah janji"
    N "Tadi kenapa Raka?"
    hide arga normal
    show arga normal at center
    show raka normal at left
    R "Oh gapapa kak, gajadi"
    A "Yuk berangkat sekarang, nanti takuntya penuh"
    N "Yuk! Duluan ya raka"
    R "iya kak. hati hati ya.. Oh iya, makasih juga bukunya."
    N "Oh, tenang aja!"



return
