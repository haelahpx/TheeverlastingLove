
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




label start:
    scene auditorium
    with fade

    play music "bgm_school_day.mp3"

    $ profile_raka = store.character_profiles["Raka"]
    $ profile_luna = store.character_profiles["Luna"]
    $ profile_nara = store.character_profiles["Nara"]

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

    jump kantin_gerbang 

label kantin_gerbang:
    
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

    jump kantin_duduk


label kantin_duduk:
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
            jump versi_luna
        "Ceritain Nara":
            jump versi_nara
        "Gak cerita":
            jump versi_rahasia


label versi_luna:
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
    jump raka_pergi


label versi_nara:
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
    jump raka_pergi


label versi_rahasia:
    R "Rahasia!."
    D "Yah kenapa? Kasih tau dong!"
    M "Diego apaansi. Itukan privasi dia, biarin aja. Lagi pula, kenapa sih pengen tau banget?"
    D "Aku penasaran siapa ceweknya."
    M "Giliran cewek aja cepet."
    R "Ah sudahlah..."
    jump raka_pergi


label raka_pergi:
    hide raka
    hide diego
    hide mila

    "Raka meninggalkan Diego dan Mila di kantin."

    return
