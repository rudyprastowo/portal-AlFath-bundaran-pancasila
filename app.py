import streamlit as st
import pandas as pd
from datetime import datetime
import io
import requests

# URL Google Web App yang sudah Pak Rudy buat
URL_GOOGLE_SHEETS = "https://google.com"

# Konfigurasi Tampilan Tab Web Browser
st.set_page_config(page_title="Portal Pengajian Pancasila Pangkalan Bun", page_icon="🕌", layout="centered")

# --- HEADER UTAMA WEBSITE ---
st.title("🕌 PORTAL INFORMASI & LAYANAN UMAT")
st.subheader("Kelompok Al-Fath Bundaran Pancasila - Pangkalan Bun")

# --- MENU NAVIGASI BANNER UTAMA ---
pilihan_menu = st.sidebar.radio("Navigasi Portal Publik:", [
    "🏠 Beranda & Agenda", 
    "📖 Buku Digital Program Kegiatan",
    "🚰 Sedekah Air Minum", 
    "📞 Hubungi Humas"
])

# ==========================================
# MENU 1: BERANDA & AGENDA KEGIATAN
# ==========================================
if pilihan_menu == "🏠 Beranda & Agenda":
    st.image("https://unsplash.com", caption="Dokumentasi Kegiatan Silaturahmi Jamaah Bundaran Pancasila", use_container_width=True)
    st.header("📢 Maklumat & Jadwal Kegiatan Terdekat")
    
    st.info("🗓️ **Pengajian Rutin Majelis Taklim**\n\nHari / Waktu: Setiap Hari Ahad Malam Senin (Ba'da Maghrib - Selesai)\n\nTempat: Sekretariat Utama Kelompok Bundaran Pancasila, Pangkalan Bun\n\nMateri Kajian: Pendalaman Kitab Hadits Riyadhus Shalihin & Fiqih Praktis\n\n*Terbuka untuk seluruh jamaah umum masyarakat Pangkalan Bun.")
    st.success("🍉 **Gerakan Sedekah Jumat Berkah**\n\nMari salurkan infaq pangan terbaik Anda untuk didistribusikan berupa paket makanan berkah pasca Shalat Jumat kepada para pekerja jalanan, dhuafa, dan musafir di sekitar kawasan Arut Selatan.")

# ==========================================
# MENU 2: BUKU DIGITAL PROGRAM KEGIATAN
# ==========================================
elif pilihan_menu == "📖 Buku Digital Program Kegiatan":
    st.header("📖 Buku Digital Panduan Program Kegiatan Pengajian")
    st.write("Berikut adalah kurikulum terpadu pembinaan generasi penerus dan jamaah Kelompok Bundaran Pancasila - Pangkalan Bun berdasarkan tingkatan umur:")

    with st.expander("👶 1. Kelompok PAUD / Anak Usia Dini (Usia 3 - 5 Tahun)"):
        st.subheader("🎯 Fokus: Pembentukan Karakter & Cinta Masjid")
        st.write("- **Materi Utama:** Pengenalan Huruf Hijaiyah metode Iqra Visual, Adab harian (Adab makan, tidur, dan orang tua), serta hafalan doa-doa pendek harian.")
        st.write("- **Metode Pembelajaran:** Belajar sambil bermain, mewarnai kaligrafi, dan kisah-kisah nabi interaktif menggunakan media proyektor digital.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Sabtu sore pukul 15.30 - 17.00 WIB di Aula PAUD Sekretariat Pancasila.")

    with st.expander("🧒 2. Kelompok Cabe Rawit / Sekolah Dasar (Usia 6 - 12 Tahun)"):
        st.subheader("🎯 Fokus: Kelancaran Membaca Al-Quran & Praktek Ibadah")
        st.write("- **Materi Utama:** Target khatam Iqra menuju Al-Quran tajwid praktis, hafalan Juz Amma (Juz 30), tata cara berwudhu, dan gerakan shalat fardhu secara mandiri.")
        st.write("- **Program Unggulan:** Pesantren Kilat Liburan Sekolah dan Simulasi Manasik Haji Anak di area luar lapangan Bundaran Pancasila.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Senin s/d Kamis pukul 16.00 - 17.15 WIB (TPA Sore).")

    with st.expander("🧑 3. Kelompok Remaja / SMP & SMA (Usia 13 - 19 Tahun)"):
        st.subheader("🎯 Fokus: Pemantapan Akidah, Kepemimpinan & Benteng Pergaulan")
        st.write("- **Materi Utama:** Kajian Akidah Islamiyah anti-radikalisme, Fiqih Remaja (Pubertas & Thaharah), pengenalan IT/Coding dasar Islami, serta diskusi interaktif problematika remaja masa kini.")
        st.write("- **Program Unggulan:** Kegiatan Pencinta Alam (Camping Religi), Olahraga Memanah/Futsal Berjamaah, serta pelatihan kepengurusan Majelis Taklim Remaja.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Sabtu Malam Minggu (Ba'da Isya) - Selesai di Posko Utama.")

    with st.expander("🧕 4. Kelompok Usia Mandiri / Mahasiswa, Pekerja & Orang Tua"):
        st.subheader("🎯 Fokus: Kemandirian Ekonomi Syariah & Pembinaan Keluarga Sakinah")
        st.write("- **Materi Utama:** Pendalaman Kitab Hadits Shahih Bukhari-Muslim, Fiqih Muamalah (Bebas Riba & Perdagangan Syariah), serta Manajemen Rumah Tangga Islami (Parenting Jamaah).")
        st.write("- **Program Unggulan:** Workshop Kewirausahaan Umat, Baitul Maal Kelompok (Dana Usaha Mandiri), dan Konseling Keluarga Islami.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Ahad Pagi (Pukul 08.00 - 10.00 WIB) & Ahad Malam Senin.")

    st.write("---")
    st.subheader("📥 Unduh Dokumen Kurikulum Resmi")
    st.write("Anda dapat mengunduh ringkasan buku saku digital berformat teks PDF ini untuk disimpan di perangkat smartphone Anda:")
    st.download_button(
        label="📄 Download Buku Panduan Kurikulum Pancasila.pdf",
        data="Dokumen contoh teks isi panduan kurikulum kurikulum pengajian Kelompok Bundaran Pancasila Pangkalan Bun tahun 2026.",
        file_name="Buku_Panduan_Program_Pengajian_Pancasila.pdf",
        mime="text/plain"
    )

# ==========================================
# MENU 3: SEKTOR KHIDMAT SOSIAL (AIR MINUM GRATIS)
# ==========================================
elif pilihan_menu == "🚰 Sedekah Air Minum":
    st.header("🚰 Fasilitas Penyediaan Air Minum Gratis")
    st.write("Rasulullah SAW bersabda: *'Sedekah apa yang paling utama?' Beliau menjawab: 'Air minum.'* (HR. Abu Daud)")
    st.info("Sebagai wujud nyata pengabdian kepada masyarakat Pangkalan Bun, Kelompok Bundaran Pancasila menyediakan posko depot air minum higienis gratis di area luar sekretariat. Fasilitas ini ditujukan bebas bagi para musafir, pengemudi ojek online, pedagang kaki lima, petugas kebersihan, maupun warga sekitar yang melintas.")
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.subheader("📍 Lokasi Posko Depot")
        st.write("Area Bundaran Pancasila, Kelurahan Sidorejo, Kecamatan Arut Selatan, Pangkalan Bun, Kotawaringin Barat (Kalimantan Tengah).")
    with col_info2:
        st.subheader("🕒 Waktu Pelayanan")
        st.write("Setiap hari Senin s/d Ahad, pukul 06.00 WIB hingga 21.00 WIB.")
        
    st.write("---")
    st.write("#### 📥 Pengajuan Permohonan Air Minum untuk Majelis / Acara Keagamaan")
    with st.form("form_air_minum", clear_on_submit=True):
        nama_pemohon = st.text_input("Nama Lengkap / Nama Lembaga")
        whatsapp = st.text_input("Nomor HP / WhatsApp Aktif")
        tujuan_acara = st.text_area("Keperluan Acara / Deskripsi Kegiatan")
        jumlah_butuh = st.number_input("Jumlah Kebutuhan (Dus / Galon)", min_value=1, step=1)
        
        if st.form_submit_button("Kirim Pengajuan"):
            if nama_pemohon and whatsapp:
                waktu_kirim = datetime.now().strftime("%Y-%m-%d %H:%M")
                payload = {"sheet": "Layanan_Air", "row": [waktu_kirim, nama_pemohon, whatsapp, tujuan_acara, jumlah_butuh]}
                try:
                    res = requests.post(URL_GOOGLE_SHEETS, json=payload)
                    if res.status_code == 200:
                        st.success("🗣️ Pengajuan Anda berhasil dikirim! Petugas Humas Kelompok Bundaran Pancasila akan segera memverifikasi lewat WhatsApp.")
                    else:
                        st.error("Gagal mengirim data ke server. Mohon coba sesaat lagi.")
                except:
                    st.error("Terjadi masalah jaringan internet.")
            else:
                st.warning("Mohon isi kolom Nama dan Nomor WhatsApp Anda terlebih dahulu.")

# ==========================================
# MENU 4: LAYANAN HUBUNGI HUMAS
# ==========================================
elif pilihan_menu == "📞 Hubungi Humas":
    st.header("📞 Pusat Kontak Layanan & Informasi Umat")
    st.write("**📍 Alamat Sekretariat Fisik:**")
    st.write("Kawasan Bundaran Pancasila, Kelurahan Madurejo, Kecamatan Arut Selatan, Pangkalan Bun, Kabupaten Kotawaringin Barat, Kalimantan Tengah.")
    st.write("**📱 WhatsApp Humas Resmi:**")
    st.write("+62 812-3456-7890 (Humas Kelompok Al-Fath)")
    st.write("**✉️ Email Resmi:**")
    st.write("info@pengajian-pancasila.org")

# --- FOOTER HAK CIPTA ---
st.write("---")
st.caption("© 2026 Kelompok Al-Fath Bundaran Pancasila - Pangkalan Bun. All Rights Reserved.")
