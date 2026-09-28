import streamlit as st
import pandas as pd
from datetime import datetime
import io
import requests

# URL Google Web App resmi Pak Rudy yang sudah terhubung ke Google Sheets
URL_GOOGLE_SHEETS = "https://google.com"

# Konfigurasi Tampilan Tab Web Browser
st.set_page_config(page_title="Portal Pengajian Pancasila Pangkalan Bun", page_icon="🕌", layout="centered")

# ==========================================
# HEADER UTAMA WEBSITE DENGAN KOLOM SEJAJAR (FIXED COLUMNS)
# ==========================================
# FIX UTAMA: Memberikan parameter (2) secara tegas agar terhindar dari TypeError pembagian layar
col_judul, col_garuda = st.columns(2)

with col_judul:
    st.markdown('<h2 style="font-family: Georgia, serif; font-size: 24px; font-weight: 800; color: #1E4D2B; margin-top: 10px; letter-spacing: 1px;">🕌 PORTAL INFORMASI AL-FATH BUNDARAN PANCASILA</h2>', unsafe_allowed_html=True)
    st.markdown('<h5 style="font-family: Arial, sans-serif; font-size: 13px; color: #D4AF37; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;">Kelompok Al-Fath Bundaran Pancasila - Pangkalan Bun</h5>', unsafe_allowed_html=True)

with col_garuda:
    # Memasang Lambang Garuda Pancasila Lingkaran Emas Resmi secara stabil
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 5px;">
            <div style="width: 80px; height: 80px; background: white; border-radius: 50%; padding: 5px; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3); border: 2.5px solid #D4AF37; display: flex; align-items: center; justify-content: center;">
                <img src="https://wikimedia.org" style="width: 100%; height: auto; object-fit: contain;">
            </div>
        </div>
    """, unsafe_allowed_html=True)

# --- MENU NAVIGASI BANNER UTAMA ---
pilihan_menu = st.sidebar.radio("Navigasi Portal Publik:", [
    "🏠 Beranda & Agenda", 
    "📖 Buku Digital Program Kegiatan",
    "🚰 Shodaqoh", 
    "📞 Hubungi Humas"
])

# ==========================================
# MENU 1: BERANDA & AGENDA KEGIATAN
# ==========================================
if pilihan_menu == "🏠 Beranda & Agenda":
    st.image("https://unsplash.com", caption="Dokumentasi Kegiatan Silaturahmi Jamaah Bundaran Pancasila", use_container_width=True)
    st.header("📢 Pengumuman & Jadwal Kegiatan Terdekat")
    
    st.info("🗓️ **Pengajian Rutin**\n\nHari / Waktu: Setiap Hari Senin Malam Senin (Ba'da Maghrib - Selesai)\n\nTempat: Masjid Al-Fath Kelompok Bundaran Pancasila, Pangkalan Bun\n\nMateri Pengajian: Al-Qur'an & Al-Hadith\n\n*Terbuka untuk seluruh jamaah dan simpatisan Pangkalan Bun.")
    st.success("🍉 **Gerakan Shodaqoh**\n\nMari salurkan infaq dan shodaqoh terbaik Anda untuk didistribusikan berupa paket makanan dan yang lain kepada para pekerja jalanan, dhuafa, dan musafir di sekitar kawasan Bundaran Pancasila Arut Selatan.")

# ==========================================
# MENU 2: BUKU DIGITAL PROGRAM KEGIATAN
# ==========================================
elif pilihan_menu == "📖 Buku Digital Program Kegiatan":
    st.header("📖 Buku Digital Panduan Program Kegiatan Pengajian")
    st.write("Berikut adalah kurikulum terpadu pembinaan generasi penerus dan jamaah Kelompok Bundaran Pancasila - Pangkalan Bun berdasarkan tingkatan umur:")

    with st.expander("👶 1. Kelompok PAUD / Anak Usia Dini (Usia 3 - 5 Tahun)"):
        st.subheader("🎯 Fokus: Pembentukan Karakter & Cinta Masjid")
        st.write("- **Materi Utama:** Pengenalan Huruf Hijaiyah metode Tilawaty Visual, Adab harian (Adab makan, tidur, dan orang tua), serta hafalan doa-doa pendek harian.")
        st.write("- **Metode Pembelajaran:** Belajar sambil bermain, mewarnai kaligrafi, dan kisah-kisah nabi interaktif menggunakan media proyektor digital.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Sabtu sore pukul 15.30 - 17.00 WIB di Aula PAUD Sekretariat Pancasila.")

    with st.expander("🧒 2. Kelompok Cabe Rawit / Sekolah Dasar (Usia 6 - 12 Tahun)"):
        st.subheader("🎯 Fokus: Kelancaran Membaca Al-Quran & Praktek Ibadah")
        st.write("- **Materi Utama:** Target khatam Tilawaty menuju Al-Quran tajwid praktis, hafalan Juz Amma (Juz 30), tata cara berwudhu, dan gerakan shalat fardhu secara mandiri.")
        st.write("- **Program Unggulan:** Pesantren Kilat Liburan Sekolah dan Simulasi Manasik Haji Anak di area luar lapangan Bundaran Pancasila.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Senin s/d Kamis pukul 16.00 - 17.15 WIB (TPA Sore).")

    with st.expander("🧑 3. Kelompok Remaja / SMP & SMA (Usia 13 - 19 Tahun)"):
        st.subheader("🎯 Fokus: Pemantapan Akidah, Kepemimpinan & Benteng Pergaulan")
        st.write("- **Materi Utama:** Pengajian Al-Qur'an & Al-Hadith, Fiqih Remaja (Pubertas & Thaharah), pengenalan IT/Coding dasar Islami, serta diskusi interaktif problematika remaja masa kini.")
        st.write("- **Program Unggulan:** Cinta Alam Indonesia (Camping Religi - CAI), Olahraga Silat ASAD / Futsal, serta pelatihan kepengurusan Remaja.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Sabtu Malam Minggu (Ba'da Isya) - Selesai di Masjid Al-Fath.")

    with st.expander("🧕 4. Kelompok Usia Mandiri / Mahasiswa, Pekerja & Usia Pra-Nikah"):
        st.subheader("🎯 Fokus: Kemandirian Ekonomi Syariah & Pembinaan Keluarga Sakinah")
        st.write("- **Materi Utama:** Pendalaman Kitab Hadits Shahih Bukhari-Muslim, Fiqih Muamalah (Bebas Riba & Perdagangan Syariah), serta Manajemen Rumah Tangga Islami (Parenting Jamaah).")
        st.write("- **Program Unggulan:** Workshop Kewirausahaan Umat, Baitul Maal Kelompok (Dana Usaha Mandiri), dan Konseling Keluarga Islami.")
        st.write("- **Jadwal Kegiatan:** Setiap Hari Ahad Pagi (Pukul 08.00 - 10.00 WIB) & Ahad Malam Senin.")

    st.write("---")
    st.subheader("📥 Unduh Dokumen Kurikulum Resmi")
    st.write("Anda dapat mengunduh ringkasan buku saku digital berformat teks PDF ini untuk disimpan di perangkat smartphone Anda:")
    
    st.link_button(
        label="📥 Download Buku Panduan Kurikulum Pancasila (PDF)",
        url="https://google.com"
    )

# ==========================================
# MENU 3: SEKTOR KHIDMAT SOSIAL & SHODAQOH AIR MINUM
# ==========================================
elif pilihan_menu == "🚰 Shodaqoh":
    st.header("🚰 Fasilitas Penyediaan Air Minum Gratis & Shodaqoh Umat")
    st.write("Rasulullah SAW bersabda: *'Sedekah apa yang paling utama?' Beliau menjawab: 'Air minum.'* (HR. Abu Daud)")
    st.info("Sebagai wujud nyata pengabdian kepada masyarakat Pangkalan Bun, Kelompok Bundaran Pancasila menyediakan posko depot air minum higienis gratis di area luar sekretariat. Fasilitas ini ditujukan bebas bagi para musafir, pengemudi ojek online, pedagang kaki lima, petugas kebersihan, maupun warga sekitar yang melintas.")
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.subheader("📍 Lokasi Posko Depot")
        st.write("Area Komplek Masjid Al-Fath Bundaran Pancasila, Kelurahan Madurejo, Kecamatan Arut Selatan, Pangkalan Bun, Kotawaringin Barat.")
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
    st.header("📞 Pusat Kontak Layanan")
    st.write("**📍 Alamat Sekretariat:**")
    st.write("Komplek Masjid Al-Fath Bundaran Pancasila, Kelurahan Madurejo, Kecamatan Arut Selatan, Pangkalan Bun, Kabupaten Kotawaringin Barat, Kalimantan Tengah.")
    st.write("**📱 WhatsApp Humas Resmi:**")
    st.write("+62 822-5552-2986 (Humas Kelompok Al-Fath)")
    st.write("**✉️ Email Resmi:**")
    st.write("info@pengajian-alfath-bundaran-pancasila.org")

# --- FOOTER HAK CIPTA ---
st.write("---")
st.caption("© 2026 Kelompok Al-Fath Bundaran Pancasila - Pangkalan Bun. All Rights Reserved.")
