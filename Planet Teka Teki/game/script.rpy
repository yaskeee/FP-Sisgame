# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Soal Teka-Teki")
define u = Character("???")
define c = Character("Operator")
define m = Character("Mesin Penjawab Otomatis")
define z = Character("Zapie")



# The game starts here.

label start:

    play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    scene background
    with fade

    show star32

    "\"Selamat datang di Planet Teka-Teki\""

    "\"Apakah kalian siap menghadapi petualangan yang menakjubkan ini dengan jalan yang berliku, aksi mendebarkan, dan teka-teki yang harus dipecahkan?\""
    "\"Jika siap, game ini memang untuk kalian!\""

    "\"Tugas kalian adalah memecahkan setiap teka-teki dan memilih jawaban yang tepat.\""
    "\"Semua teka-teki dalam petualangan ini berkaitan dengan pengolahan data..\""
    "\"Untuk memecahkannya, kalian harus menggunakan pengetahuan kalian tentang tabel, bagan, grafik, rata-rata, dan teori kemungkinan.\""

    "\"Saat mengikuti petualangan ini, kalian akan mengumpulkan DATA-DATA yang diperlukan untuk menyelamatkan Pangkalan Alpha.\""
    "\"Kalian akan memasukkan DATA ke DATA PAD, sebuah alat elektronik pengolah data yang kalian bawa.\""
    "\"Cobalah untuk menyimpan DATA apa yang telah dikumpulkan ketika mengikuti petualangan ini.\""
    "\"Kalian akan membutuhkan semua data tersebut untuk menyelesaikan petualangan dengan sukses.\""

    "\"Baiklah.. mari kita mulai petualangannya..\""
    "\"...\""

    # scene bg room
    # with fade

    label startpage:

        show star4

        b "Bersiap untuk mendarat. Pesawat antariksa kalian siap untuk mendarat di Pangkalan Alpha di Planet Teka-teki."
        b "Kalian dikirim untuk memasok barang-barang kebutuhan dan memperbarui sistem komputer di pangkalan tersebut."
        b "Akan tetapi, ada yang tidak beres."
        b "Lampu-lampu disana berkedip-kedip."
        b "Pintu ruang pengunci udara terbuka lebar."
        b "Komputer-komputer mati."
        b "Dan, semua awak pangkalan menghilang."
        b "Kalian harus menyelamatkan para awak."
        b "Kalian juga harus menyalakan kembali listrik, menutup pengunci udara, dan menyalakan ulang komputer."
        b "Barulah setelah itu kalian bisa mengumpulkan data yang dibutuhkan untuk menyelidiki apa yang terjadi."

        b "Apakah kalian siap menghadapi tantangan ini?"

        menu:
            "Siap menghadapi tantangan":
                jump moon11
            "Belum siap menghadapi tantangan":
                jump planet20
    #START END-------------------------------------

    label roket4:

        b "Kalian melangkah masuk ke Kubah Laboratorium. Semua berantakan. Lampu peringatan berkedip dan semua peralatan sudah hancur."
        b "Labu kimia mendidih dan tabung percobaan pecah."
        b "Pintu menuju reaktor nuklir terbuka dan berayun tak beraturan. Monitor komputer dipenuhi dengan simbol dan tanda-tanda aneh."

        show roket4
        with fade
        b "Kemudian kalian menemukan sebuah pesan di papan tulis..."

        jump roket20
    #roket4 END------------------------------------

    label planet4:

        show planet4
        with fade

        b "Kalian mengikuti arah yang ditunjukkan DATA PAD. Jalur itu membawa kalian melewati ruang mekanik."
        b "Kalian berhenti sebentar untuk mengambil sebuah gulungan besar kabel listrik."
        b "Kalian telah mengikuti petunjuk arah yang benar. Dalam beberapa menit, kalian sampai di ruang panel surya."

        jump star32
    #planet4 END-----------------------------------

    label star5:

        b "Kalian menulis perintah untuk memutar piringan satelit yang masih utuh agar mengarah ke planet Z."
        b "Kemudian, kalian mencoba mengirim sinyal. Namun, tidak ada yang terjadi."
        b "Sebuah tampilan video memperlihatkan adanya gangguan. Robot alien telah menghilang dari kawah!"
        b "Robot itu telah mengambil satu potongan besar dari piringan satelit kedua."
        b "Kalian harus segera menghentikannya sebelum ia memakan piringan satelit lebih banyak lagi."
        b "Rhombus segera datang untuk mengatasi masalah! Dia bergegas menuju ke ruang pengunci udara, menyalakan roket di punggungnya, dan langsung meluncur ke piringan satelit."
        b "Di sana, dia menghadapi robot alien. Robot itu terlihat kuat dan berbahaya di hadapan Rhombus."
        b " Akan tetapi, cukup dengan sebuah sengatan listrik dari kantung sumber tenaga Rhombus semua selesai---si robot alien terdiam mematung"
        b "Sekarang, Rhombus harus memperbaiki bagian yang rusak. Dia mengirim sinyal meminta bantuan. Bagaimana cara memutar bagian itu agar terpasang kembali di tempat semula dengan pas?"

        menu:
            "Memutarnya sebesar 90 derajat searah jarum jam!":
                jump star12
            "Memutarnya sebesar 90 derajat berlawanan dengan arah jarum jam!":
                jump scope37
    #star5 END-------------------------------------

    label ion5:

        b "Itu benar, Tanaman itu tumbuh dalam beberapa menit---padahal seharusnya butuh beberapa minggu!"
        b "Buah-buahan itu matang dalam beberapa detik---padahal seharusnya butuh beberapa hari! Sesuatu yang aneh terjadi di Biodome!"

        jump star31
    #ion5 END--------------------------------------

    label roket6:

        b "Ternyata salah. Hanya alien yang telah memakan besi dan baja yang akan tertarik oleh magnet. Magnet tidak dapat menarik alien yang telah memakan alumunium dan tembaga"
        b "Alumunium dan tembaga memang termasuk di dalam himpunan logam pada diagram venn, tapi keduanya tidak berada dalam himpunan bahan magnetis. Alumunium dan tembaga adalah logam nonmagnetis."

        jump star17
    #label END-------------------------------------

    label planet6:

        b "Panel kontrol memperlihatkan nilai suhu. Kalian dapat mengubah temperatur dengan menekan tombol panah atas dan panah bawah."
        b "Kalian memutuskan untuk menurunkan temperatur hingga minus 5 derajat celcius."
        b "Ini seharusnya akan menghentikan cacing-cacing itu."

        menu:
            "Tekan panah biru 4 kali":
                jump scope7
            "Tekan panah biru 5 kali":
                jump roket32
    #label END-------------------------------------

    label star6:

        #CHECKPOINT

        b "Itu jumlah yang benar"
        b "Kalian nanti akan membutuhkan angka ini untuk memastikan bahwa semua rbot mikro itu telah dinonaktifkan."
        b "Sekarang, kalian harus menyelidiki bagian lain dari Pangkalan Alpha."
        b "Mungkin ada masalah lain yang harus diselesaikan, sebelum kalian menemukan kembali para awak."

        #DATA ITEM 1 masukkan DATA PAD

        jump roket14
    #label END-------------------------------------

    label ion7:

        b "Kalian mencentang kotak BESAR. DATA PAD kalain mulai terasa panas. Asap muncul  dari balik tombol-tombolnya! Sebuah pesan muncul di layar!"
        show ion7
        with fade
        "\"GAGAL MENGOLAH DATA! GAGAL MENGOLAH DATA!\""
        b "Demgan cepat kalian menghapus tanda centang di kotak itu dan mengulannginya lagi."
        b "BESAR bukan karakteristik yang benar."
        b "Lihat kembail tabel. Beberapa benda besar, seperti jendela, belum rusak, bukan?"

        jump roket28
    #label END-------------------------------------

    label moon7:

        b "Kalian mendekati pintu masuk ke Biodome"
        b "Biodome adalah sebuah rumah kaca raksasa di mana para awak Pangkalan Alpha menanam tanaman pangan untuk kebutuhan mereka."
        b "Selain sebagai sumber makanan, tanaman pangan itu membantu mendaur ulang udara dan air."
        b "Sebuah termometer di pintu ruangan pengunci udara memperlihatkan temperatur di dalam Biodome."
        b "Berapakah angka yang ditunjukkan oleh termometer tersebut?"

        menu:
            "Temperatur 4,5 derajat Celcius":
                jump planet34
            "Temperatur 45 derajat Celcius":
                jump ion17
    #label END-------------------------------------

    label scope7:

        b "Temperatur turunn hingga 5 derajat Celcius."
        b "Suhu itu masih belum cukup dingin! Cacing-cacing itu masih menggeliat! Pesawat antariksa masih terus membesar!"
        b "Menekan tombol -10 derajat Celcius sebanyak 4 kali akan menurunkan temperatur sebesar 40 derajat Celcius (45 - 40 = 5)."
        b "Berapa derajat lagi kalian harus menurunkan temperatur agar menjadi minus 5 derajat Celcius?"

        jump planet6
    #label END-------------------------------------

    label roket8:

        b "Benar sekali! Modus adalah nilai yang paling sering muncul dalam sebuah himpunan data."
        b "Delapan planet---sama seperti jumlah planet dalam sistem tata surya Bumi! Kemudian."
        b "kalian ingat---penjelajah ruang angkasa pertama menemukan bahwa planet-planet yang tidak dihuni memiliki ukuran dan jangkauan temperatur yang mirip dengan Bumi!"

        jump roket12
    #label END-------------------------------------

    label planet8:

        b "Kalian melangkah melewati pengunci udara, menuju ke Kubah Habitat dan melihat kerusakan yang terjadi."
        b "Tampaknya, sesuatu telah memakan meja dan kursi."
        show planet8
        with fade
        b "Kalian menggunakan pensil khusus untuk membuat turus di DATA PAD kalian."
        b "Kalian memasukkan seluruh jumlahnya di kolom total."
        b "Ada berapa total Sendok Logam yang rusak?"

        menu:
            "14 Sendok Logam rusak":
                jump star23
            "12 Sendok Logam rusak":
                jump planet38
    #label END-------------------------------------

    label star8:

        show star8
        with fade

        b "Benar! Pintu brankas terbuka lebar. Kalian menemukan stik data di dalamnya."
        b "Kalian mencolokannya ke DATA PAD untuk memindahkan data di dalamnya."
        b "Cara umum untuk menuliskan tanggal dalam bentuk digit adalah hari/bulan/tahun."
        b "Jadi, 28 Juli 2254 ditulis sebagai 28/07/2254."
        b "Sekarang, kalian bisa menghadapi petualangan berikutnya."

        jump ion11
    #label END-------------------------------------

    label ion9:

        b "Di luar Kubah Habitat, kalian menemukan sebuah kawah yang belum pernah kalian lihat."
        b "Di dalamnya, terlihat seperti ada sebuah pesawat antarkisa mainan."
        b "Kalian menggunakan kamera DATA PAD untuk memeriksanya."
        b "Ternyata itu bukan mainan! Itu pesawat yang digunakan para alien untuk menuju pangkalan ini."
        b "Ada barisan robot alien kecil keluar dari pesawat antariksa itu, Mengarah ke Kubah Habitat! Kemudian, kalian memperhatikan simbol-simbol alien yang berbentuk aneh di pesawat."
        b "Kalian memprogram DATA PAD untuk menerjemahkan simbol-simbol itu."
        b "Tabel terjemahan yang dihasilkan adalah sebagai berikut..."

        show ion9
        with fade

        b "DATA PAD menerjemahkan kata pertama..."
        "\"P A S U K A N\""
        b "Dan, dua kata berikutnya..."
        "\"P E N D A U R   U L A N G\""
        b "Kalian menggunakan tabel tadi untuk menerjemahkan kata keempat..."
        b "Apakah hasil terjemahan dari kata keempat?"

        menu:
            "L O G A M":
                jump moon13
            "M E T A L":
                jump star36
    #label END-------------------------------------

    label roket10:

        b "Rhombus menutupi wajah dengan tangan, lalu menggelengkan kepala!"
        b "Periksa kembali tabel itu. Planet X hampir tidak memiliki oksigen sama sekali di atmosfernya."
        b "Berapa banyak oksigen di atmosfer planer Z?"

        jump roket16
    #label END-------------------------------------

    label planet10:

        b "Kalian memprogram DATA PAD unntuk menganalisis tanah Biodome."
        b "Kalian terkesima ketika layar menampilkan diagram batang yang membandingkan tanah Biodome dengan tanah normal."
        b "Bagaimana perbandingan jumlah cacing pada tanah Biodome dengan tanah biasa?"

        menu:
            "Tanah Biodome memiliki lebih banyak cacing":
                jump ion43
            "Tanah Biodome memiliki lebih sedikit cacing":
                jump planet40
    #label END-------------------------------------

    label star10:

        b "Benar sekali! Para alien yang memakan baja akan tertarik oleh magnet, sedangkan alien yang memakan alumunium dan tembaga tidak."
        b "Alumunium dan tembaga  adalah jenis logam yang tidak bersifat magnetis."

        jump roket40
    #label END-------------------------------------

    label ion11:

        b "Kalian kembali ke pesawat antariksa untuk mengisi ulang tabung oksigen dan mengambil makanan berenergi tinggi."
        b "Kalian memutuskan untuk melihat pesawat alien lebih dekat."
        b "Akan lebih baik jika kalian memiliki lebih banyak data tentang alien yang mengancam itu."

        jump star21
    #label END-------------------------------------

    label moon11:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0

        b "Pesawat antariksa kalian berhasil mendarat di area landasan. Denah di layar komputer memperlihatkan tampilan pangkalan."
        show bulan11
        with fade
        b "Lampu darurat berwarna merah berkedip-kedip di sebelah Kubah Habitat, Kubah Laboratorium, dan Kubah Komunkasi."
        b "Lampu peringatan kuning menyala, menunjukkan bahwa temperatur suhu di Biodome sedang meninggi! Kalian bergegas memakai pakaian luar angkasa."

        jump roket14
    #label END-------------------------------------

    label scope11:

        b "Kalian baru saja memasukkan kode yang salah!"
        b "Lampu peringatan mulai berkedip."
        b "Kalian memiliki satu lagi kesempatan sebelum brankas itu terkunci selamanya."
        b "Agustus adalah bulan kedelapan. Bulan keberapakah Juli?"

        jump planet22
    #label END-------------------------------------

    label roket12:

        b "Kalian meminta komputer untuk mencari planet yang ukurannya kira-kira sama besar dengan Bumi di antara empat sistem tata surya berplanet delapan"
        b "Ternyata ada satu di setiap sistem tata surya tersebut!"
        b "Untuk membantu menentukan planet mana yang tidak dihuni, kalian meminta agar suhu maksimum dan minimum setiap planet ditampilkan."
        b "Planet manakah yang memiliki jangkauan temperatur yang sama dengan Bumi?"

        menu:
            "Planet W dan Y":
                jump roket22
            "Planet X dan Z":
                jump roket16
    #label END-------------------------------------

    label planet12:

        b "Kalian mencoba terhubung dengan komputer Kubah Laboratorium melalui DATA PAD"
        b "Sebuah peringatan muncul..."
        "\"Serangan Virus! Semua data komputer diacak-acak! Sistem pengamanan laboratorium tidak bisa berjalan! Kebocoran radiasi!\""
        b "Untuk bisa masuk ke dalam dan menghentikan serangan itu, kalian harus memasukkan kata kunci yang tepat pada layar sentuhnya."

        jump ion37
    #label END-------------------------------------

    label star12:

        b "Itu instruksi yang benar! Rhombus memutar potongan itu."
        b "Ternyata memang pas dan bisa masuk dengan sempurna."
        b "Piringan itu mulai mengirimkan pesan kalian."

        jump ion19
    #label END-------------------------------------

    label ion13:

        b "Kalian mendekati ruang pengunci udara di Kubah Komunikasi."
        b " Kalian berencana untuk menghubungi alien yang bertanggung jawab atas kerusakan di Pangkalan Alpha."
        b "Sebelum berupaya masuk, kalian membuat daftar beberapa informasi yang akan kalian butuhkan."
        b "Kalian mencentang kotak di samping setiap data yang telah kalian kumpulkan."

        menu:
            "DATA telah terkumpul":
                jump roket38
            "DATA belum terkumpul":
                jump roket14
    #label END-------------------------------------

    label moon13:

        show bulan13
        with fade

        b "PASUKAN PENDAUR ULANG LOGAM"
        b "Kedengarannya seperti pesawat tempur alien! Akan tetapi, pasukan itu segera bergerak tanpa kendali."
        b "Alien pengunyah logam akan segera menghancurkan seluruh Kubah Habitat jika hubungan listrik yang kalian buat gagal."
        b "Kalian mengambil sebuah wadah plastik dari pesawat antariksa kalian. Dengan hati-hati, kalian memungut robot-robot alien kecil itu dari kawah. Kalian mengurungnya di dalam wadah plastik."
        b "Cara ini seharusnya bisa menghentikan lebih banyak serangan robot alien di pangkalan."
        b "Kalian memeriksa permukaan benda logam dengan mikroskop. Semua robot alien telah berhenti bekerja . Mereka berjatuhan ke lantai bagaikan lalat mati. Rencana kalian berhasil dengan baik."

        jump planet22
    #label END-------------------------------------

    label scope13:

        b "Benar! Ketika alien-alien itu  telah menyerap semua materi makhluk hidup di Biodome, mereka akan berhenti tumbuh."

        jump star43
    #label END-------------------------------------

    label roket14:

        show roket14
        with fade

        b "Pangkalan Alpha mana yang akan kamu selidiki?"

        menu:
            "Kubah Habitat":
                jump star29
            "Kubah Laboratorium":
                jump star27
            "Biodome":
                jump moon7
            "Kubah Komunikasi":
                jump ion13
    #label END-------------------------------------

    label planet14:

        b "Setelah memiliki data air dan tanah, kalian mulai memikirkan teori yang bisa menjelaskan apa yang terjadi."
        b "Kalian menyusun hipotesis kalian dalam bentuk diagram alur di DATA PAD..."
        b "bagaimana hasil hipotesis kalian tentang alien pendaur ulang?"

        menu:
            "Alien pendaur ulang akan terus tumbuh selamanya":
                jump scope15
            "Alien pendaur ulang akhirnya akan berhenti tumbuh":
                jump scope13
    #label END-------------------------------------

    label star14:

        b "Kalian memilih kombinasi yang lebih masuk akal. Tiga dari empat kombinasi memiliki setidaknya satu lampu hijau."
        b "Hanya satu kombinasi yang memiliki dua merah."
        b "Pintu di dalam ruang pengunci udara bergeser. Kalian pun memasuki Kubah Laboratorium."

        jump roket4
    #label END-------------------------------------

    label ion15:

        scene background

        b "Benar sekali! Tinggi batang memperlihatkan bahwa jumlah pisau yang rusak adalah 24, dan jumlah sendok yang rusak adalah 14."
        b "Selisih antara 24 dan 14 adalah 10."

        jump roket28
    #label END-------------------------------------

    label scope15:

        b "Tidak, pasukan alien pendaur ulang tidak bisa terus tumbuh selamanya."
        b "Pada akhirnya, semua materi dari makhluk hidup di Biodome akan terserap oleh mereka."
        b "Lihat perkiraan di kotak terakhir pada diagram alur."

        jump planet14
    #label END-------------------------------------

    label moon15:

        b "Sebuah jam penghitung mundur tampil di monitor komputer."
        b "Dalam 60 detik, reaktor akan meledak!"
        "\"60, 59, 58, .....\""
        b "Kalian harus bertindak cepat! kelain menggunakan program perkiraan risiko  di DATA PAD untuk membantu memutuskan apa yang harus dilakukan."
        b " Berikut hasil data yang diperoleh."
        b "Waktu yang ada hanya cukup untuk satu tindakan. Kalian harus membuat keputusan tepat saat ini juga!"

        menu:
            "Potong pasokan listrik reaktor":
                jump star38
            "Menyalakan ulang komputer reaktor":
                jump planet42
    #label END-------------------------------------

    label roket16:

        b "Benar! Planet X dan Z sepertinya paling mirip dengan Bumi. Mungkinkah salah satu di antaranya adalah planet Zorgon?"
        b "Semua makhluk hidup cerdas yang pernah ditemukan bernapas dengan oksigen."
        b "Kalian meminta komputer untuk membandingkan kandungan gas di atmosfer kedua planet itu dengan kandungan gas di atmosfer Bumi."

        menu:
            "Planet X memiliki atmosfer yang mirip dengan Bumi":
                jump roket10
            "Planet Z memiliki atmosfer yang mirip dengan Bumi":
                jump planet28
    #label END-------------------------------------

    label planet16:
        scene background
        with fade

        b "Benar! Semua barang yang rusak terbuat dari logam. Sesuatu di pangkalan sepertinya \"memakan\" logam-logam itu."
        b "Semua pisau terbuat dari logam, dan semua dimakan."
        b "Akan tetapi, ada sebagian sendok yang terbuat dari plastik dan semua masih utuh."
        b "Kalian harus bertindak cepat sebelum semua benda logam di Pangkalan Alpha dihancurkan!."

        jump roket26
    #label END-------------------------------------

    label star17:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0
        b "Kalian mencoba memikirkan cara untuk menghentikan robot-robot alien."
        b "Tidak ada udara yang tersisa di Kubah Habitat, jadi kalian tidak bisa menggunakan mesin penyedot debu untuk menyedot mereka."
        b "Namun, kemudian kalian menndapatkan ide bagus---para alien itu terbuat dari logam."
        b "Beberapa jenis logam dapat tertarik oleh magnet! Kalian mencari di DATA PAD lebih banyak informasi tentang magnet dan logam."
        b "Kalian menemukan data yang disajikan dalam bentuk diagram VENN."

        show star17
        with fade

        b "Kalian memutuskan untuk melakukan sebuah percobaan."
        b "Baju antariksa kalian dilengkapi dengan sepatu bot magnet yang membantu kalian menempel di sebuah permukaan benda di luar angkasa."
        b "Kalian mengambil salah satu magnet dari bagian bawah sepatu bot."
        b "Kalian menggesekkan magnet ke berbagai permukaan berbeda."
        b "Kemudian, kalian mengamati magnet dan permukaan-permukaan tersebut secara lebih seksama dengan mikroskop DATA PAD."
        b "Bagaimana hasil dari percobaan yang telah kalian lakukan?"

        menu:
            "Alien akan bersifat magnetis":
                jump roket6
            "Hanya sebagian Alien yang akan bersifat magnetis":
                jump star10
    #label END-------------------------------------

    label ion17:

        #show gambar

        b "Kalian berpikir temperatur di dalam Biodome mencapai 45 derejat celcius."
        b "Ini lebih panas dari suhu yang seharusnya."
        b "Kalian menyalakan sistem pendingin di baju antariksa kalian dan melewati pintu ruang pengunci udara."
        b "Kalian benar. Situasi di dalam terasa seperti di hutan hujan."
        b "Wortel-wortel terlihat setinggi pepohonan. Bunga matahari terlihat sebesar roda gerobak. Tomat terlihat sebesar bola sepak."

        jump ion39
    #label END-------------------------------------

    label roket18:

        show roket18
        with fade

        b "Kalian mengikuti arah yang ditunjukkan DATAPAD."
        b "Sepertinya, rute yangdiberikan membawa kalian ke bagian belakang Pangkalan Alpha. Dan, tampaknya itu tidak benar."
        b "Kemudian, diantara lubang-lubang di lantai, kalianmelihat sesuatu yang bergerak-gerak."
        b "teryata itu adalah salah satu robot alien."
        b "Namun, itu tidak seperti robot kecil yang ada di Kubah Habitat."
        b "Alien itu hampir saja memakan semua piringan satelit!"
        b "Ukurannya besar! Kepala mekanis robot alien itu berputar."
        b "Mata elektroniknya melihat kalian."
        b "Kaki mekanisnya mulai melangkah mendekati kalian."
        b "Di ujung kedua tangan robot itu terdapat capit raksasa."
        b "Keduanya dapat memotong logam semudah memotong kertas."
        "."
        ".."
        "..."
        b "Tiba-tiba, ada kilatan dari belakang kalian."
        b "Tenyata, itu sebuah sinar laser yang sangat kuat."
        b "Sebuah lubang dengan letupan asap tiba-tiba terbentuk di depan robot alien."
        b "Alien itu terjungkal dan masuk ke dalamnya. Dia terjebak di sana!"
        b "Siapa atau apakah yang telah menolong kalian?"
        b "Angka-angka pada kotak itu adalah sebuah koordinat."
        b "Posisi awal kalian adalah di kotak 9, 7."
        b "Jika kalian melihat angka-angka di bagian bawah, kalian menemukan bahwa 9 adalah jumlah kolom."
        b "Dan, jika kalian melihat ke samping, terlihat bahwa 7 adalah jumlah baris."
        b "Ketiak menuliskan koordinat, kalian harus menuliskan jumlah kolom (angka di bagian bawah) terlebih dulu, baru kemudian jumlah baris (angka di bagian samping)."

        jump ion35
    #label END-------------------------------------

    label planet18:

        b "Benar! Seseorang baru saja menambahkan 25 persen pupuk alien ke dalam air tersebut!"

        jump planet10
    #label END-------------------------------------

    label star19:

        b "Kemudian, kalian melihat sesuatu yang aneh di tengah-tengah Biodome."
        b "Ternyata, itu sebuah pesawat antariksa."
        b "Akan tetapi, benda itu juga memiliki akar dan daun!"
        b "Dia tumbuh membesar! ada sesuatu tertulis di badan pesawat itu."
        b "DATA PAD kalian menerjemahkan tulisan alien tersebut..."

        "\"PASUKAN PENDAUR ULANG DENGAN KEMAMPUAN MENGEMBANGKAN DIRI\""

        jump planet14
    #label END-------------------------------------

    label ion19:

        b "Sinyal kalian dijawab."
        b "Sebuah suara menjawab dengan bahasa yang terdengar seperti suara kicauan burung!"
        b "Akan tetapi, komputer dengan otomatis menerjemahkannya."

        u "Terima kasih telah menghubungi Sistem Komunikasi Telepon Antarplanet Zorgon. Ada yang bisa saya bantu?"

        b "Ternyata itu tersambung dengan Operator dari Sistem Komunikasi Telepon Antarplanet Zorgon."

        "\"---Saya perlu berbicara dengan seseorang dari Perusahaan Pendaur Ulang Galaksi\""
        c "Apakah anda mempunyai nomornya"

        b "Kalian menyebutkan angka dari alien pengumpul data."

        "\"Tolong hubungkan dengan Zorgon 1123452001.\""

        c "Sedang disambungkan."

        b "Jawab si operator."



        jump ion31
    #label END-------------------------------------

    label roket19:

        m "Saluran telepon anda masih dalam antrean..."

        b "Kata mesin penjawab otomastis."

        m "Telepon anda akan segera kami jawab . Kami sangat menghargai waktu anda."

        b "Akhirnya, saluran teleon kalian tersambung."
        b "Ternyata itu sambungan video! Sesosok alien dengan wajah aneh, namun ramah, muncul di layar."

        u "Selamat sore. Anda sedang berbicara dengan Zapie."
        z "Bisa anda sebutkan nomor akun anda?"

        b "Kalian menjelaskan bahwa kalian tidak memiliki nomor akun."
        b "Kalian tidak pernah mendengar planet Zorgon atau Pendaur Ulang Galaksi hingga kapal antariksa mereka menghancurkan Pangkalan Alpha."
        b "Zapie terlihat ketakutan. Dia terus menerus meminta maaf."
        b "Sekelompok pasukan pendaur ulang secara tidak sengaja telah terbang ke planet yang jauh secara acak."
        b "Seharusnya, mereka mendarat di planet yang sudah kosong untuk mencari bahan dan data yang tidak lagi dibutuhkan!"
        b "Keluhan kalian adalah keluhan yang ke-27 pada hari ini!"

        jump planet23
    #label END-------------------------------------

    label roket20:

        b "Kalian menuliskan \"Virus Alien\" pada program pencari di DATA PAD."
        b "Setelah beberapa saat, inilah yang ditampilkan di layar."

        #show gambra virus

        b "Kalian melihat layar komputer."
        b "Kalian mengamati pola-pola virus dalam tulisan alien."
        b "Semua pola itu adalah bayangan cermin dari salah satu pola yang ada di DATA PAD kalian."
        b "Apa bentuk pola yang kalian dapatkan dari hasil pencarian DATA PAD?"

        menu:
            "Virus Skaro":
                jump roket36
            "Virus Kronos":
                jump moon37
    #label END-------------------------------------

    label planet20:

        show planet20
        with fade

        b "Tidak Perlu takut. Ini adalah petuaangan yang menasyikkan dan bantuan akan selalu ada untuk kalian."
        b "Jika kalian terjebak atau berada dalam bahaya, penolong misterius akan menuntun dan menjaga kalian agar tetap aman."
        b "Ikuti saja petunjuknya, satu demi satu, dan lihat seberapa jauh perjalanan yang bisa kalian tempuh."
        b "Kalian mungkin akan terkejut saat mengetahui seberapa luas pengetahuan kalian."
        b "Semoga berhasil."

        jump moon11
    #label END-------------------------------------

    label star21:

        b "Sementara pesawat alien masih di dalam wadah plastik, kalian mencoba melakukan koneksi nirkabel antara DATA PAD kalian dengan kapal itu."
        b "Data terunduh ke dalam layar DATA PAD..."
        "."
        ".."
        "..."
        b "Data itu terlihat seperti bahasa yang tidak karuan dan tidak bermakna."
        b "Kemudian, kalian menjalankan program penerjemah."

        show star21
        with fade

        b "Ternyata itu sebuah panduan pengguna!"
        b "Rupanya, secara tidak sengaja pasukan pendaur ulang telah mendarat di Pangkalan Alpha."
        b "Kalian menyalin nomor serinya."
        b "Kalian melihat bahwa panduan tersebut menggunakan simbol berupa gambar untuk memberi angka pada robot-robot mikro itu."
        b "Kalian memutuskan untuk menghitung seluruh angka berdasarkan jumlah robot dan memasukkannya ke dalam DATA PAD."
        b "Berapakah jumlah robot yang akan kalian masukkan ke dalam DATA PAD?"

        menu:
            "1.100":
                jump ion33
            "11.000":
                jump star6
    #label END-------------------------------------

    label roket22:

        b "Kalian menunjuk ke gambar-gambar planet W dan Z yang ada di layar komputer."
        b "Mata Rhombus mulai memancarkan percikan cahaya"
        b "Asap muncul dari penunjuk baterainya. Itu adalah planet yang salah!"
        b "Jangkauan adalah jarak antara nilai terendah dan nilai tertinggi. Suhu maksimum bumi adalah 60 derejat Celcius dan suhu minimumnya adalah minus 90 derejata Celcius."
        b "Berarti jangkaunnya adalah 150 derajat."
        b "Dua planet mana yang memiliki jangkauan suhu yang sama?"

        b"Cepat periksa lagi sebelum Rhombus terbakar!"

        jump roket12
    #label END-------------------------------------

    label planet22:

        b "Kalian telah menghentikan robot-robot alien di Kubah Habitat."
        b "Sekarang, kalian harus menjelajahi bagian lain Pangkalan Alpha untuk menyelamatkan para awak."
        b "Kemudian, kalian ingat pesan Amy."
        b "Kalian harus menemukan stik data."
        b "Tanpa itu, kalian tidak akan bisa memasuki bagian yang aman di pangkalan itu."
        b "Amy berkata bahwa para awak telah menyimpannya di sebuah tempat yang terlindungi."
        b "Tentu saja---brankas rahasia di Kubah Habitat!"
        b "Kalian menemukan brankas rahasia itu di dinding,"
        b "Brankas itu terbuat dari lapisan berlian super kuat dan tahan benturan."
        b "Brankas itu tidak terbuat dari logam, jadi para alien tidak bisa merusaknya."
        b "Kalian membaca keterangan tambahan dari Amy di DATA PAD..."

        show planet22
        with fade

        b "Keypad di brankas hanya terdiri atas angka-angka dan garis miring."
        b "Kalian harus memasukkan tanggal lahir Amy dalam format angka."
        b "Bagaimana format dari tanggal lahir Amy yang benar?"

        menu:
            "28/07/2254":
                jump star8
            "28/08/2254":
                jump scope11
    #label END-------------------------------------

    label star23:

        show star23
        with fade

        b "Betul sekali. Ada 14 buah sendok logam yang rusak."
        b "Turus adalah sebuah cara cepat untuk menghitung jumlah dari benda-benda atau kejadian-kejadian."
        b "Tabel angkanya adalah tabel frekuensi."
        b "Dalam tabel frekuensi inim setiap turus bernilai satu."

        jump roket30
    #label END-------------------------------------

    label ion23:

        b "DATA PAD kalian segera membuat panggilan."
        b "DATA PAD Vineeta menjawab."
        b "Awalnya, kalian melihat ruang Kubah Laboratorium di layar DATA PAD, tapi kemudian sebuah pola alien aneh muncul di layar dan pola itu mulai berputar."
        show ion23
        with fade
        b "Kalian merasa pusing. Kalian juga juga tidak bisa berhenti melihatnya."
        b "Kalian mulai mengantuk."
        b "Tiba-tiba, kalian mendengar suara gerakan benda logam."
        b "Benda logam itu menghantam lengan kalian."
        b "DATA PAD kalian jatuh ke lantai dan mata kalian langsung terbuka kembali."
        b "Hampir saja. Apa itu yang baru saja menyelamatkan kalian?"
        b "Vineeta adalah kepala ilmuwan, bukan komandan stasiun."
        b "periksa kembali tabel tadi"

        jump star29
    #label END-------------------------------------

    label moon23:

        b "Kalian mempelajari semua data yang telah kalian kumpulkan."
        b "Namun, kalian tetap saja tidak bisa menemukan cara untuk memperbaiki kerusakan yang disebabkan oleh pesawat antariksa alien itu!"
        b "Hanya ada satu hal yang bisa dilakukan."
        b "Kalian harus pergi ke Kubah Komunikasi dan menghubungi alien pembuat pesawat pendaur ulang itu!"

        jump roket14
    #label END-------------------------------------

    label planet23:

        b "Zapie menjelaskan apa yang akan dilakukannya."
        b "Jika kalian memberi tahu dia berapa banyak pasukan yang dilepas, juga nomor seri cacing-cacing, dia akan mengirim kode untuk membalik program pendaur ulang mereka."
        b "Untungnya, kalian sudah mengumpulkan semua data di DATA PAD."
        b "Kalian mengunggah informasi dan mengamati apa yang terjadi di pangkalan melalui monitor video."

        jump ion24
    #label END-------------------------------------

    label roket26:

        b "DATA PAD kalian memilki kamera yang juga dapat digunakan sebagai mikroskop canggih."
        b "Kalian mendekatkan lensa ke salah satu sendok yang rusak."
        b "Inilah yang kalian lihat..."

        show roket26
        with fade

        b "Terlihat sendok itu seperti dimakan oleh kerumunan \"serangga\" kecil."
        b "Kalian memfokuskan lensa ke salah satu \"serangga\" dan memperbesar tampilannya."
        b "Ternyata, itu sama sekali bukan serangga."
        b "Itu adalah robot alien---seperti mainan."
        b "Robot-robot itu memotong-motong logam dan menempelkannya ke tubuh mereka."
        b "Kalian harus memperhatikan secara seksama, robot-robot itu tampak membesar di hadapan mata kalian."

        #show robot membesar

        b "Kalian memprogram DATA PAD untuk membuat diagram garis yang akan menganalisis tingkat pertumbuhan robot alien itu."
        b "DATA PAD meminta kalian untuk memasukkan ukuran alien itu setelah 12 jam."
        b "Berapa ukuran yang kalian masukkan pada DATA PAD?"

        menu:
            "masukkan 3,5 cm":
                jump moon41
            "masukkan 3.5 m":
                jump star41
    #label END-------------------------------------

    label planet27:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0

        b "Tidak---itu tidak benar!"
        b "Salah satu lebah raksasa meninggalkan bunga tomat."
        b "Dia mengarah ke kalian!"
        b "Dengungannya memekakkan telinga."
        b "Sengatnya sebesar pisau belati!"

        b "Kemudian, terdengar suara berdengung keras, semacam peringatan."
        b "Awan asap mengepul dari atas bahu kalian dan mengenai lebah itu,"
        b "Lebah itu pun pergi, Hampir saja!"

        b "Tomat berubah kuning dalam 6,5 detik dan matang sempurna setelah 12,0 detik."
        b "Jadi jumlah yang dibutuhkan untuk berubah dari kuning ke merah adalah 12,0 dikurangi 6,5 detik."

        jump ion39
    #label END-------------------------------------

    label ion27:

        b "Kalian memang beruntung!"
        b "Tepat ketika kalian memasukkan angka 36, panah-panah sedang menunjuk pada 3 dan 6."
        b "Sangat bijaksana memilih hasil dengan kemungkinan (probabilitas) muncul paling besar,"

        jump roket42
    #label END-------------------------------------

    label star27:

        b "Kalian melewati landasan luncur dan masuk ke Kubah Laboratorium,"
        b "Ruang pengunci udaranya masih tertutup. Pasti masih ada udara di dalamnya."
        b "Kemudian, kalian melihat pesawat alien kecil."
        b "Sepertinya, pesawat itu jatuh di sebelah pintu masuk Kubah Laboratorium!"
        b "DATA PAD kalian menerjemahkan simbol alien di badan pesawat..."
        "\"PASUKAN PENGUMPUL DATA\"."
        b "Kabel hitam keluar dari pesawat itu."
        b "Kabel-kabel itu tumbuh ke segala arah, seperti tanaman rambat."
        b "Satu kabel sudah mencapai Kubah Laboratorium."
        b "Kabel itu menancap secara otomatis ke colokan data di pintu pengunci udara!"

        jump planet12
    #label END-------------------------------------

    label roket28:

        b "Pisau yang rusak lebih banyak dibandingkan sendok logam yang rusak."
        b "Namun, beberapa benda tidak tidak rusak sama sekali,"
        b "Sungguh membingungkan. Kalian menyusun data dalam bentuk diagram Carroll."
        b "Kalian menyortir data tersebut berdasarkan warna, ukuran, dan bahan."
        b "Sekarang kalian memiliki dua buah tabel hasil penyortiran di DATA PAD."

        show roket28
        with fade

        b "Kini, kalian merasa tahu kaitan antara semua benda yang rusak."
        b "DATA PAD meminta kalian untuk mencentang karakterisktik umum yang dimiliki oleh semua benda yang rusak."
        b "Karakteristik mana yang kalian centang?"

        menu:
            "Besar":
                jump ion7
            "Logam":
                jump planet16
    #label END-------------------------------------

    label planet28:

        b "Ya, atmosfer planet Z lebih mirip dengan Bumi."
        b "Mungkinkah itu planet Zorgon? Kalian harus mengirim sinyal dan menunggu jawaban!"

        jump star5
    #label END-------------------------------------

    label star29:

        b "Kalian melangkah turun dari pesawat antariksa."
        b "Pintu ruang pengunci udara dalam keadaan terbuka lebar."
        b "Di ruangan inilah tempat para awak makan, tidur, dan bersantai."
        b "Sekarang tempat itu kosong, dingin, dan hampa udara."
        b "Kalian melihat layar DATA PAD yang kalian bawa."

        show star29
        with fade

        b "Disitu ditampilkan tabel awak Pangkalan Alpha."
        b "Kalian dapat menghubungi DATA PAD mereka dengan cara mengetuk tanda di sebelah kiri nama mereka."
        b "Kalian mencoba untuk menghubungi komandan stasiun."

        #show daftar tabel awak

        b "Kontak awak mana yang akan kalian panggil?"

        menu:
            "panggil Vineeta":
                jump ion23
            "panggil Amy":
                jump planet32
    #label END-------------------------------------

    label ion29:

        b "Itu kode yang salah."
        b "Ketika kalian menekan 6, panah pertama sedang menunjuk ke angka 3."
        b "Panah berputar lebih cepat."
        b "Salah satu kabel dari pesawat alien mulai merayap ke arah kalian."
        b "Kabel itu ingin menempel di pakaian antariksa kalian!"
        b "Kemudian, dengan disertai suara dengkingan keras, sebuah tangan mekanik yang dilengkapi denga pemotong kabel muncul dari belakang kalian."
        b "Pemotongnya langsung mendekati kabel itu dan memutuskannya."
        b "Hampir saja!"
        b "Ada tiga angka 3 di putaran pertama, tapi hanya ada dua angka 6 dan satu angka 4."
        b "Ini berarti bahwa angka 3 memiliki kemungkinan paling besar untuk muncul dan menjadi digit pertama."
        b "Angka mana yang memiliki kemungkinan besar untuk menjadi digit kedua?"

        jump ion37
    #label END-------------------------------------

    label roket30:

        b "DATA PAD kalian memperlihatkan data frekuensi dalam bentuk diagram batang."

        show roket30
        with fade

        b "Kenapa sebagian benda rusak, sementara ada benda-benda lain yang masih utuh?"
        b "Kalian mencoba memahami data yang ada."
        b "Kalian membandingnkan semua bilangan."
        b "Pisau yang rusak lebih banyak dibandingnkan sendok logam yang rusak."
        b"Berapakah perbedaan satu selisih antara jumlah pisau yang rusak dengan sendok logam yang rusak?"

        menu:
            "10":
                jump ion15
            "8":
                jump roket34
    #label END-------------------------------------

    label planet30:

        b "Kalian baru saja memilih kombinasi yang salah!"
        b "Ruang pengunci udara mulai dipenuhi gas berwarna ungu."
        b "Gas itu mulai meluruhkan baju antariksa kalian! Kemudian, semburan air yang kuat mengenai pakaian antariksa kalian---dari mana datangnya itu?"
        b "Gas itu menguap dan akhirnya menghilang."
        b "Ada empat kombinasi warna untuk lampu itu."
        b "Tiga dari empat kombinasi seharusnya memiliki satu lampu hijau."
        b "Kemungkinan muncul paling tidak satu lampu hijau adalah 3/4 atau 75 persen."
        b "Kemungkinan munculnya dua lampu merah hanya 1/4 atau 25 persen."
        b "Cepat, masukkan kembali pilihan kalian."

        jump roket42
    #label END-------------------------------------

    label star31:

        b "Kalian memutuskan untuk menganalisis tanah dan air di Biodome."
        b "Kalian harus mencari tahu apa yang sebenarnya terjadi."
        b "Pertama-tama, kalian mengambil sampel air dari semprotan air."
        b "Tentu kalian sudah tahu bahwa ada pupuk yang ditambahkan kedalam air tersebut, tapi kalian tetap saja terkesima ketika melihat diagram pai di DATA PAD!"
        b "Bagaimana hasil dari diagram pai yang ditampilkan DATA PAD?"

        menu:
            "air terkontaminasi mengandung 10 persen pupuk alien":
                jump moon39
            "air terkontaminasi mengandung 25 persen pupuk alien":
                jump planet18
    #label END-------------------------------------

    label ion31:

        b "Oh tidak, itu adalah alat penjawab telepon!"
        c "Terima kasih telah menghubungi Perusahaan Pendaur Ulang Galaksi."
        c "Untuk masalah terkait penjualan, silahkan tekan 1."
        c "Untuk melacak pesanan anda, silahkan tekan 2."
        c "Untuk suku cadang dan pelayanan, silahkan tekan 3."
        c "Untuk keperluan lain, silahkan tunggu."

        b "Kalian pun menunggu."

        jump roket19
    #label END-------------------------------------

    label roket32:

        #CHECKPOINT

        b "Temperatur turun hingga minus 5 derajat celcius."
        b "Cacing-cacing itu berhenti bergerak."
        b "Kalian baru saja menghentikan proses daur ulang."
        b "Akan tetapi, bisakah proses ini dibalik?"
        b "Jika tidak bisa, itu artinya makanan dan oksigen di pangkalan baru saja terbuang percuma!"
        b "Kalian memeriksa salah satu cacing pendaur ulang dengan mikroskop."

        b "DATA PAD menerjemahkan tulisan alien di kepala cacing..."

        "\"NOMOR SERI: X/002.\""

        b "Kalian menyimpan nomor itu di DATA PAD."

        jump moon23
    #label END-------------------------------------

    label planet32:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0

        scene background

        b "DATA PAD kalian membuat sambungan komunikasi."
        b "DATA PAD Amy mengirimkan sebuah rekaman pesan"
        "\"Perhatian! Perhatian!\""
        b "Rekaman suara Amy terdengar."

        "\"Sesuatu yang aneh terjadi disini. Kami terpaksa meninggalkan Kubah Habitat.\""
        "\"Namun, kami telah menyimpan stik data di tempat yang aman. Kau akan membutuhkannya untuk menyelamatkan stasiun.\""
        "\"Ulang tahunku adalah kuncinya.\""
        "\"Namun, pertama-tama kau harus mencari tahu penyebab kerusakannya.\""
        "\"Berhati-hatilah, para alien itu terlihat seperti mainan, tapi mereka akan terus membesar!\""
        "\"Tidak ada waktu lagi...\""

        b "Kalian tidak bisa memahami semua isi pesan itu."
        b "Akan tetapi, kalian tetap memutuskan untuk menyelidiki lebih jauh---dan bersikap waspada pada alien yang terlihat seperti mainan."

        jump planet8
    #label END-------------------------------------

    label star32:

        show star32
        with fade

        b "Kalian menyambungkan kabel ke panel surya."
        b "Kemudian, sambil mengulur kabel, kalian kembali lagi ke Kubah Habitat."
        b "Kalian menyambungkan ujung kabel yang lain ke jeruji logam."
        b "Ketika kedua matahari planet ni terbit, listrik akan menghentikan para alien di tempat."

        jump ion9
    #label END-------------------------------------

    label ion33:

        b "Ketika kalian memasukkan angka 1.100, sebuah peringatan muncul..."
        "\"PERHATIAN : DATA AKAN RUSAK BERAT\""
        b "Nyaris saja! Jika angka yang kalian masukkan salah, beberapa robot mikro mungkin akan tetap aktif."
        b "Kunci menunjukkan bahwa seharusnya kalian menghitung dalam ribuan ketika akan menjumlahkan semua simbol gambar,"
        b "Jangan lupa menambahkan dua buah simbol berbentuk setengah gambar, masing-masing bernilai 500."

        jump star21
    #label END-------------------------------------

    label moon33:

        b "Kalian menjelaskan penemuan kalian pada para awak."
        b "Tak seorang pun pernah mendengar planet Zorgon."
        b "Bersama-sama, kalian memutuskan menggunakan teleskop pangkalan untuk mencari planet yang diduga paling kuat sebagai planet Zorgon di sistem tata surya."
        b "Komputer menganalisis sepuluh sistem tata surya terdekat dari data teleskop."

        #show analisis komputer

        b "Kalian mulai membicarakan data planet itu."
        b "Ketika kalian menyebutkan angka yang merupakan modus dari jumlah planet, Rhombus berbunyi nyaring!"
        b "Menurut kalian berapakah modus dari data tersebut?"

        menu:
            "11":
                jump planet36
            "8":
                jump roket8
    #label END-------------------------------------

    label roket34:
        scene background

        b "Tidak, selisih itu tidak benar."
        b "Tinggi batang menunjukkan bahwa jumlah pisau yang rusak adalah 24, dan jumlah sendok logam yang rusak adalah 14."
        b "Berapakah selisih antara 24 dan 14?"

        jump roket30
    #label END-------------------------------------

    label planet34:

        b "Kalian pikir suhunya hanya 4,5 derajat Celcius."
        b "Kalian lalu menyalakan pemanas di dalam pakaian antariksa kalian."
        b "Kalian membuka pintu ruang pengunci udara dan masuk ke dalam Biodome."
        b "Rasanya seperti di dalam sauna!"
        b "Bahkan, ada uap di dalam helm kalian."
        b "Kalian mulai pusing karena suhu di dalam ruangan itu terlalu panas."
        b "Kemudian terdengar suara keras."
        b "Tangan mekanis memegang dan menarik kalian kembali ke dalam ruangan pengunci udara."
        b "Tubuh kalian kembali mendingin,"
        b "Skala termometer dimulai dari 0 derajat Celcius hingga 100 derajat Celcius."
        b "Masing-masing bagian mewakili 10 derajat."

        jump moon7
    #label END-------------------------------------

    label star34:

        #CHECKPOINT

        b "Pesan lain dari alien muncul di monitor Kubah Laboratorium."
        b "Kalian menggunakan program penerjemah di DATA PAD..."

        "\"PROSES PENGUMPULAN DATA TERHENTI\""
        "\"UNTUK BANTUAN TEKNIS, HUBUNGI PLANET ZORGON 112 345 2011\""
        "\"TARIF STANDAR PAGGILAN ANTARPLANET AKAN DIBERLAKUKAN.\""
        "\"SILAHKAN HUBUNGI PELAYANAN KOMUNIKASI DI DAERAH ANDA UNTUK MENGETAHUI TARIFNYA\""

        b "Kalian belum pernah mendengar tentang planet Zorgon, tapi kalian menduga bahwa dari sanalah pesawat alien pengumpul data ini berasal!"
        b "Kalian mencatat nomor tadi."
        b "Kalian memutuskan untuk mencoba menghubungi planet misterius ini."
        b "Pesawat antariksa kecil mereka harus dihentikan!"

        jump roket14
    #label END-------------------------------------

    label ion35:

        show ion35
        with fade

        b "Listrik di Kubah Habitat mati"
        b "Pakaian antariksa kalian tidak memiliki cukup tenaga untuk memberi sengatan listrik ke semua alien."
        b "Kalian harus mencari sumber listrik yang lebih besar."
        b "Kemudian, kalian teringat pada sel tenaga matahari di denah pangkalan,"
        b "Jika kalian bisa menghubungkannya dengan Kubah Habitat, rencana kalian pasti berhasil."
        b "Kalian kembali menampilkan denah pangkalan di DATA PAD."
        b "Kali ini, kalian membuat kisi-kisi untuk membantu menentukan rute perjalanan yang akan kalian tempuh."

        b "Saat ini, kalian berada di kisi persegi 9, 7."
        b "Kalian harus memprogram DATA PAD untuk memandu kalian ke tempat panel surya berada."

        b "Kemana koordinat yang akan kalian tuju?"

        menu:
            "4, 6":
                jump planet4
            "6, 4":
                jump roket18
    #label END-------------------------------------

    label roket36:

        b "Kalian mengunggah virus Skaro ke komputer Kubah Laboratorium."
        b "Ternyata salah! Sekarang ada dua Virus di dalam sistem."
        b "Kekacauan di Kubah Laboratorium makin menjadi-jadi."
        b "Reaktor mulai bergetar dan mengeluarkan asap!"
        b "Sekali lagi, lihat polanya."
        b "Dengan cepat kalian membuat duplikasi virus Skaro di DATA PAD."
        b "Kalian membalikkannya secara vertikal dan horizontal untuk membuat bayangan cermin."
        b "Kemudian, kalian mengunggah bayangan cermin itu ke komputer Kubah Laboratorium."
        b "Ternyata berhasil. Pola virus langsung berhenti! Reaktor pun berhenti bergetar."

        jump roket20
    #label END-------------------------------------

    label star36:

        show star36
        with fade

        b "Kalian menuliskan kata \"METAL\" di DATA PAD."
        b "DATA PAD mulai bergetar. Sinar laser menyorot ke berbagai arah dari layarnya."
        b "Awas meledak!"
        b "Terjemahan kalian salah!, periksa lagi simbol-simbol di tabel."
        b "Cepat---coba terjemahkan kembali!"

        jump ion9
    #label END-------------------------------------

    label planet36:

        b "Rhombus terlihat gelisah."
        b "Kepalanya berputar dan dai melompat-lompat! Itu angka yang salah!"
        b "Modus adalah nilai yang paling sering muncul (umum) dalam sebuah himpunan data."
        b "Cepat, pilih angka lain sebelum Rhombus meledak!"

        jump moon33
    #label END-------------------------------------

    label ion37:

        b "Kalian meminta perbendaharaan kode dari DATA PAD."
        b "Kode itu seharusnya berupa dua digit angka, misalnya 66."
        b "Akan tetapi, bukannya dua digit angka yang keluar di layar, melainkan dua buah pemintal."
        b "Panah pemintal berputar dengan liar ketika virus mengubah-ubah angka secara acak."

        b "Angka mana saja yang harus kalian masukkan?"
        b "Kalian memutuskan memilih angka yang memiliki kemungkinan paling besar untuk muncul di setiap pemintal."
        b "Berapakah angka yang akan kalian pilih?"

        menu:
            "masukkan 63":
                jump ion29
            "masukkan 36":
                jump ion27
    #label END-------------------------------------

    label scope37:

        b "Itu putaran yang salah!"
        b "Rhombus mencoba memasang potongan itu di tempatnya, tetapi tidak berhasil!"
        b "Alien mulai terbangun setelah sebelumnya terkena sengatamn listrik."
        b "Tangan mekanisnya mulai bergerak perlahan mendekati benda-benda logam."
        b "Kalian harus cepat! Beri Rhombus perintah yang tepat."
        b "Lihatlah bentuk itu kembali."
        b "Kalian harus memutarnya ke kanan agar bisa masuk ke tempat semula dengan pas."

        jump star5
    #label END-------------------------------------

    label moon37:

        b "Kalian mengunggah virus Kronos ke komputer Kubah Laboratorium."
        b "Kalian telah memilih virus yang tepat."
        b "Pola virus Kronos menghentikan pola cermin mereka."
        b "Melalui jendela kubah, kalian bisa melihat kabel data dari pesawat alien mulai mengeluarkan asap."
        b "Kemudian, kabel itu terlepas dari colokan yang ada di pintu ruangan pengunci udara, lalu kembali merayap ke pesawatnya."
        b "Kabel itu tidak menyukai efek dari \"antivirus\" yang kalian berikan!"
        b "Komputer menyala kembali."
        b "Semua mulai bekerja lagi secara normal."
        b "Akan tetapi, tidak dengan reaktornya."
        b "Reaktor mulai berkilau dan mengeluarkan radiasi biru."
        b "Reaktor mulai tidak terkendali."

        jump moon15
    #label END-------------------------------------

    label planet38:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0

        scene background

        b "Itu jumlah yang salah!"
        b "Tepat ketika kalian menulis 12, sebuah pesan muncul di layar DATA PAD..."
        "\"SISTEM RUSAK, MEMATIKAN DIRI\""
        b "Oh, tidak! Tanpa DATA PAD kalian tidak bisa apa-apa!"
        b "Turus adalah sebuah cara cepat untuk menghitung jumlah dari benda-benda atau kejadian-kejadian."
        b "Tabel angkanya adalah tabel frekuensi."
        b "Dalam tabel frekuensi inim setiap turus bernilai satu."
        b "Cepat, periksa kembali jumlah turus untuk sendok logam!"

        jump planet8
    #label END-------------------------------------

    label star38:

        b "Kalian memutuskan pembangkit listrik reaktor."
        b "Namun, ternyata itu tidak berpengaruh apapun."
        b "Kilauan radiasi makin membesar!"
        b "Kemungkinan bernilai 1 artinya sesuatu itu pasti terjadi."
        b "Kemungkinan 0.5 artinya terjadi atau tidak terjadinya sesuati memiliki kesempatan yang sama---misalnya ketika melempar koin."
        b "Kemungkinan untuk mendapatkan gambar sama besar dengan kemungkinan  untuk mendapatkan angka."
        b "Jadi, tetap saja ada kemungkinan bahwa reaktor akan meledak!"
        b "Seharusnya kalian memilih tindakan yang memiliki kemungkinan terjadinya ledakan paling kecil."
        b "Masih ada sedikit waktu untuk memilih tindakan lain."

        jump moon15
    #label END-------------------------------------

    label roket38:

        b "Kalian menekan tombol masuk di ruangan pengunci udara."
        b "Sebuah pesan muncul di layar."
        "\"Area aman. Masukkan kode keamanan pangkalan.\""
        b "Kalian memasukkan kode yang diperoleh dari stik data."
        b "Ruang pengunci udara bekerja."
        b "Ketika kalian memasuki ruang pengunci udara, kalian menyadari bahwa ada sesuatu yang ikut masuk bersama kalian!"
        b "Ternyata Rhombus, robot penjaga Pangkalan Alpha."
        b "Dialah yang selama ini membantu kalian!"

        jump ion41
    #label END-------------------------------------

    label ion39:

        b "Kalian sedang memperhatikan sekeliling ketika sebuah tomat raksasa dari sebuah tanaman jatuh ke tanah."
        b "Hanya dalam beberapa detik, tomat itu membusuk dan hancur di atas tanah."
        b "Biji-bijinya mulai bertunas."
        b "Pohon tomat baru segera tumbuh tepat di depan mata kalian."
        b "Tomat-tomat itu mengeluarkan bunga."
        b "Lebah raksasa medekatinya sambil berdengung."
        b "Bunga-bunga itu berubah menjadi buah tomat baru dan segera matang."

        b " Kalian menggunakan perekam video DATA PAD untuk merekam pertumbuhan sebuah tomat."
        b "Kalian memutarnya kembali dan inilah hasilnya..."

        # show tomat

        b " Berapa detik yang dibutuhkan tomat untuk matang dari kuning ke merah?"

        menu:
            "12 Detik":
                jump planet27
            "5,5 Detik":
                jump ion5
    #label END-------------------------------------

    label moon39:

        b "Tidak, ada lebih banyak pupuk alien dalam air itu!"
        b "Tiba-tiba kekuatan semprotan air meningkat."
        b "Semprotan itu begitu kuat hingga bisa mnejatuhkan kalian."
        b "Kemudian, sebuah kaki mekanis menginjak selang tersebut dan menghentikan aliran airnya."
        b "\"irisan\" dalam sebuah diagram pai menunjukkan pecahan dari seluruh bagian yang membentuk pai  utuh."
        b "Besar irisan \"pupuk alien\" dalam air Biodome sebanyak seperempat bagian dari keseluruhan pai."
        b "Berapakah seperempat jika ditulis dalam persentase?"

        jump star31
    #label END-------------------------------------

    label roket40:

        show roket40
        with fade

        b "Ketika kalian mengamati para alien di kabel tembaga, mereka semua bergerak cepat satu arah"
        b "Mereka mendorong kabel itu kearah kalian, mereka bermaksud menusuk baju antariksa kalian."
        b "Tiba-tiba, sebuah lengan mekanik menggapai dari belakang kalian."
        b "Terdengar suara keras diikuti dengan kilauan biru."
        b "Sentakan listrik mengalir di kawat."
        b "Para alien membeku ketika aliran listrik mengenai tubuh mereka."
        b "Itu dia! Listrik! Semua logam menghantarkan listrik!"
        b "Entah bagaimana caranya, yang jelas kalian harus mengalirkan listrik ke semua benda logam di Kubah Habitat."
        b "Itu akan menghentikan para alien."

        jump ion35
    #label END-------------------------------------

    label planet40:

        b "Kalian memutuskan untuk memeriksa tananh dan mencari tahu penyebab kenapa tanah itu memiliki lebih sedikit cacing."
        b "Kalian membungkuk dan mengambil segenggam tanah."
        b "Kalian salah. Ternyata tanah itu penuh dengan cacing yang menggeliat-geliat!"
        b "Tapi, itu bukan cacing biasa!"
        b "Tubuhnya hangat dan berlendir, tapi kepalanya mekanis, dengan gigi tajam yang mampu mengunyah apapun."
        b "Mereka mulai menggigiti sarung tangan kalian."
        b "kalian mengguncangkan tangan, tapi mereka tetap menempel!"
        b "Lihat kembali ukuran pecahan \"cacing\" pada tanah Biodome---jauh lebih besar daripada ukuran pecahan \"cacing\" pada tanah normal."
        b "Tepat ketika cacing-cacing itu akan mengunyah sarung tangan kalian, sebuah lengan mekanis datang dari belakang kalian."
        b "Lengan tersebut menyemprot cacing-cacing itu dengan cairan dingin yang membekukan."
        b "Mereka langsung berhenti menggeliat dan jatuh ke tanah."
        b "Hampir saja. Ada seseorang yang menjaga kalian!"

        jump planet10
    #label END-------------------------------------

    label star41:

        b "Benar sekali! Hanya dalam 12 jam, robot alien akan setinggi 3,5 m."
        b "Itu sama tingginya dengan lampu jalan."
        b "Coba bayangkan, berapa besar kerusakan yang akan dibuatnya!"
        b "Dan, masih ada ribuan lagi robot alien di Kubah Habitat."
        b "Kalian harus bertindak cepat!"

        jump star17
    #label END-------------------------------------

    label moon41:

        show bulan41
        with fade

        b "Ketika kalian memasukkan 3,5 cm, para alien berbalik dan melihat ke lensa kamera."
        b "mereka berkumpul di sendok dan mulai berbaris. Mereka mendekati kalian!"
        b "Jika mereka berhasil mencapai kalian, mereka akan memakan semua logam di pakaian antariksa kalian!"
        b "Kemudian, di belakang kalian terdengar suara keras."
        b "Sebuah gelas pelastik jatuh dan menimpa sendok itu---menjebak para alien di dalamnya."
        b "Hampir saja! Siapakah atau apakah yang melakukan itu?"
        b "Grafik menunjukkan bahwa dalam 12 jam, alien akan setinggi 350 cm!"
        b "Berapa meterkah itu?"

        jump roket26
    #label END-------------------------------------

    label ion41:

        b "Pintu bagian dalam ruang pengunci udara terbuka."
        b "Kalian dan Rhombus masuk ke dalam Kubah Komunikasi."
        b "Kalian langsung disambut oleh sorak-sorai!"
        b "Di sinilah para awak berlindung. Mereka semua ada di sini."

        b "Komandan stasiun, Amy menjelaskan bagaimana mereka sebelumnya mengamati sebuah bintang jatuh."
        b "Kemudian mereka kehilangan kendali terhadap sistem pangkalan."
        b "Semua awak berkumpul di satu-satunya area paling aman di Pangkalan Alpha---yaitu Kubah Komunikasi."
        b "Mereka berhasil mengirim pesan darurat, tapi tidak lama kemudian komputer di Kubah Komunikasi rusak."
        b "Semua komputer terinfeksi virus yang sama dengan virus yang ada di komputer Kubah Laboratorium."
        b "Kalian Tahu cara memperbaikinya! Kalian harus mengunggah virus Kronos ke komputer,"
        b "Dengan segera, komputer itu menyala kembali."
        b "Sekarang, kalian bisa mencoba menghubungi para alien!"

        jump moon33
    #label END-------------------------------------

    label roket42:

        b "Pintu ruang pengunci udara membuka, kalian segera masuk ke dalam"
        b "Pintu luar pun menutup."
        b "Di dalam, kalian menekan tombol \"OPERASIKAN\", Namun tidak ada yang terjadi."
        b "Ruang pengunci udara seharusnya dipenuhi udara sehingga kalian bisa melepas helm."
        b "Kemudian, pintu bagian dalam terbuka."
        b "Kalian terjebak disini!"
        b "Kalian melihat dua lampu berkedip secara acak merah dan hijau."
        b "Sebuah virus telah merusak sistem pengaturannya."
        b "Kalian melihat empat kombinasi..."
        b "DATA PAD kalian memperlihatkan sebuah pesan..."

        "\"Pilih kombinasi yang paling mungkin terjadi agar pintu terbuka.\""
        "\"Hati-hati, pilihan yang salah bisa mengakibatkan kerusakan yang lebih besar.\""

        b "Bagaimana kombinasi lampu yang benar?"

        menu:
            "Paling tidak satu lampu hijau":
                jump star14
            "Dua lampu merah":
                jump planet30
    #label END-------------------------------------

    label planet42:

        b "Kalian memilih tindakan yang tepat"
        b "Menyalakan ulang komputer reaktor adalah langkah terbaik yang bisa dilakukan."
        b "Kemungkinan terjadinya ledakan paling kecil."

        b "Jika sebuah kemungkinan bernilai 1, artinya sesuatu itu pasti akan terjadi."
        b "Jika bernilai 0 maka tidak mungkin terjadi."
        b "Kemungkinan 0,1 artinya ada satu dari sepuluh kemungkinan (10 persen) bahwa sesuatu hal akan terjadi."
        b "Sebanyak sembilan dari sepuluh kemungkinan, reaktor tidak akan meledak."

        b "Begitu komputer selesai menyala ulang, komputer bisa kembali mengontrol reaktor. Reaktor mendingin dan kilauan radiasi menghilang."
        b "Hitung mundur berhenti di 0,3 detik---tepat pada waktunya!"

        jump star34
    #label END-------------------------------------

    label ion43:

        b "Dengan hati-hati kalian mengambil sedikit sampel tanah"
        b "Kalian menggunakan sebuah sendok panjang."
        b "Kalian benar. Tanah ini dipenuhi oleh cacing!"
        b "Akan tetapi, itu bukan cacing biasa!"
        b "Tubuh mereka berlendir, tapi kepala mereka mekanis, dengan gigi tajam yang mampu mengunyah!"
        b "Kalian menggoyang mereka hingga jatuh dari sendok, jauh dari tempat kalian berdiri."

        jump star19
    #label END-------------------------------------

    label star43:
        play music "sounds/space chill.mp3" fadeout 1.0 fadein 1.0

        b "Namun, apa yang selanjutnya terjadi setelah pertumbuhan alien-alien itu berhenti!"
        b "Hei, itu adalah sebuah pesawat antariksa."
        b "Benda itu pasti akan terbang, dan membawa materi yang didaur ulang ke planet asalnya."
        b "Itu akan segera terjadi!"
        b "ketika pesawat alien makin besar, pertumbuhan tanaman-tanaman melambat."
        b "Tanaman baru makin kecil. Semua diserap oleh pesawat alien."
        b "Tak lama lagi, tak akan ada tanaman yang tersisa untuk menghasilkan makanan dan oksigen di Pangkalan Alpha."
        b "Kalian harus menghentikan pesawat itu sebelum lepas landas!"
        b "Kemudian, kalian ingat sesuatu---suhu! Ketika cacing itu kedinginan, mereka berhenti bekerja."
        b "Kalian langsung berlari ke mesin pengontrol lingkungan Biodome."

        jump planet6
    #label END-------------------------------------

    label ion24:

        #"END GAME"

        b "Di dalam Kubah Habitat, para robot mikro mulai memperbaiki kerusakan yang sebelumnya mereka buat."
        b "Di Biodome, tanaman antariksa mulai mengecil."
        b "Cacing-cacing melepaskan nutrisi kembali ke dalam tanah."
        b "Tanaman normal mulai tumbuh kembali."
        b "Di dalam Kubah Laboratorium, alarm berhenti dan komputer kembali bekerja normal."
        b "Bahkan, robot alien raksasa membangun kembali piringan satelit yang tadi mereka hancurkan."
        b "Para robot mikro, cacing-cacing, dan kabel pengumpul data kembali ke dalam pesawat kecil, tempat asal mereka."
        b "Mereka akan segera kembali ke planet Zorgon untuk diperbaiki."
        b "Zapie meminta maaf dan dia telah menyiapkan kejutan."
        z "Untuk membayar kerusakan yang kami sebabkan, kami mengundang kalian untuk berlibur gratis ke planet Bajak Laut, taman hiburan terbesar  di seluruh penjuru semesta."
        b "Kalian tidak sabar menunggu."
        b "Kalian juga memastikan agar tersedia tempat bagi Rhombus untuk perjalanan itu."
        b "Dia layak mendapatkanya."
    #label END-------------------------------------



    # This ends the game.

    return

#
#     label roket6:
#
#         b "-----soal-----"
#
#         jump star17
#     #label END-------------------------------------
#
#
#
#
#
#
#
#
# label planet6:
#
#         b "-----soal-----"
#
#         menu:
#             "pilih A":
#                 jump scope7
#             "pilih B":
#                 jump roket32
#     #label END-------------------------------------
