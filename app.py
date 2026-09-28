import streamlit as st
import pandas as pd
from datetime import datetime
import io
import requests

# Menggunakan jembatan Web App URL Google Sheets Pak Rudy yang sudah aktif
URL_GOOGLE_SHEETS = "https://google.com"

# Konfigurasi Tampilan Tab Web Browser
st.set_page_config(page_title="Portal Pengajian Pancasila Pangkalan Bun", page_icon="🕌", layout="centered")

# --- GAYA DESAIN KUSTOM (ISLAMIC GREEN THEME) ---
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; text-align: center; color: #1E4D2B; margin-bottom: 5px; }
    .sub-title { font-size:16px !important; text-align: center; color: #444444; margin-bottom: 25px; font-style: italic; }
    .section-header { font-size:20px !important; font-weight: bold; color: #1E4D2B; border-bottom: 2px solid #1E4D2B; padding-bottom: 5px; margin-top: 25px; margin-bottom: 15px; }
    .info-card { background-color: #F0F7F4; padding: 20px; border-radius: 10px; border-left: 6px solid #1E4D2B; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .tier-title { font-size:18px !important; font-weight: bold; color: #2E6B3E; margin-bottom: 5px; }
    .footer-text { text-align: center; font-size: 12px; color: #888888; margin-top: 20px; border-top: 1px solid #eeeeee; padding-top: 15px; }
    </style>
""", unsafe_allowed_html=True)

# --- HEADER UTAMA WEBSITE ---
st.markdown('<div class="main-title">🕌 PORTAL INFORMASI & LAYANAN UMAT</div>', unsafe_allowed_html=True)
st.markdown('<div class="sub-title">Kelompok Bundaran Pancasila - Pangkalan Bun, Kotawaringin Barat</div>', unsafe_allowed_html=True)

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
    st.markdown('<div class="section-header">📢 Maklumat & Jadwal Kegiatan Terdekat</div>', unsafe_allowed_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h4>🗓️ Pengajian Rutin Majelis Taklim</h4>
        <p><b>Hari / Waktu:</b> Setiap Hari Ahad Malam Senin (Ba'da Maghrib - Selesai)<br>
        <b>Tempat:</b> Sekretariat Utama Kelompok Bundaran Pancasila, Pangkalan Bun<br>
        <b>Materi Kajian:</b> Pendalaman Kitab Hadits Riyadhus Shalihin & Fiqih Praktis<br>
        <i>*Terbuka untuk seluruh jamaah umum masyarakat Pangkalan Bun.</i></p>
    </div>
    <div class="info-card">
        <h4>🍉 Gerakan Sedekah Jumat Berkah</h4>
        <p>Mari salurkan infaq pangan terbaik Anda untuk didistribusikan berupa paket makanan berkah pasca Shalat Jumat kepada para pekerja jalanan, dhuafa, dan musafir di sekitar kawasan Arut Selatan.</p>
    </div>
    """, unsafe_allowed_html=True)

# ==========================================
# MENU 2: BUKU DIGITAL PROGRAM KEGIATAN
# ==========================================
elif pilihan_menu == "📖 Buku Digital Program Kegiatan":
    st.markdown('<div class="section-header">📖 Buku Digital Panduan Program Kegiatan Pengajian</div>', unsafe_allowed_html=True)
    st.write("Berikut adalah kurikulum terpadu pembinaan generasi penerus dan jamaah Kelompok Bundaran Pancasila - Pangkalan Bun berdasarkan tingkatan umur:")

    with st.expander("👶 1. Kelompok PAUD / Anak Usia Dini (Usia 3 - 5 Tahun)"):
        st.markdown('<div class="tier-title">🎯 Fokus: Pembentukan Karakter & Cinta Masjid</div>', unsafe_allowed_html=True)
        st.write("""
        *   **Materi Utama:** Pengenalan Huruf Hijaiyah metode Iqra Visual, Adab harian (Adab makan, tidur, dan orang tua), serta hafalan doa-doa pendek harian.
        *   **Metode Pembelajaran:** Belajar sambil bermain, mewarnai kaligrafi, dan kisah-hikayat nabi interaktif menggunakan media proyektor digital.
        *   **Jadwal Kegiatan:** Setiap Hari Sabtu sore pukul 15.30 - 17.00 WIB di Aula PAUD Sekretariat Pancasila.
        """)

    with st.expander("🧒 2. Kelompok Cabe Rawit / Sekolah Dasar (Usia 6 - 12 Tahun)"):
        st.markdown('<div class="tier-title">🎯 Fokus: Kelancaran Membaca Al-Quran & Praktek Ibadah</div>', unsafe_allowed_html=True)
        st.write("""
        *   **Materi Utama:** Target khatam Iqra menuju Al-Quran tajwid praktis, hafalan Juz Amma (Juz 30), tata cara berwudhu, dan gerakan shalat fardhu secara mandiri.
        *   **Program Unggulan:** Pesantren Kilat Liburan Sekolah dan Simulasi Manasik Haji Anak di area luar lapangan Bundaran Pancasila.
        *   **Jadwal Kegiatan:** Setiap Hari Senin s/d Kamis pukul 16.00 - 17.15 WIB (TPA Sore).
        """)

    with st.expander("🧑 3. Kelompok Remaja / SMP & SMA (Usia 13 - 19 Tahun)"):
        st.markdown('<div class="tier-title">🎯 Fokus: Pemantapan Akidah, Kepemimpinan & Benteng Pergaulan</div>', unsafe_allowed_html=True)
        st.write("""
        *   **Materi Utama:** Kajian Akidah Islamiyah anti-radikalisme, Fiqih Remaja (Pubertas & Thaharah), pengenalan IT/Coding dasar Islami, serta diskusi interaktif problematika remaja masa kini.
        *   **Program Unggulan:** Kegiatan Pencinta Alam (Camping Religi), Olahraga Memanah/Futsal Berjamaah, serta pelatihan kepengurusan Majelis Taklim Remaja.
        *   **Jadwal Kegiatan:** Setiap Hari Sabtu Malam Minggu (Ba'da Isya) - Selesai di Posko Utama.
        """)

    with st.expander("🧕 4. Kelompok Usia Mandiri / Mahasiswa, Pekerja & Orang Tua"):
        st.markdown('<div class="tier-title">🎯 Fokus: Kemandirian Ekonomi Syariah & Pembinaan Keluarga Sakinah</div>', unsafe_allowed_html=True)
        st.write("""
        *   **Materi Utama:** Pendalaman Kitab Hadits Shahih Bukhari-Muslim, Fiqih Muamalah (Bebas Riba & Perdagangan Syariah), serta Manajemen Rumah Tangga Islami (Parenting Jamaah).
        *   **Program Unggulan:** Workshop Kewirausahaan Umat, Baitul Maal Kelompok (Dana Usaha Mandiri), dan Konseling Keluarga Islami.
        *   **Jadwal Kegiatan:** Setiap Hari Ahad Pagi (Pukul 08.00 - 10.00 WIB) & Ahad Malam Senin.
        """)

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
    st.markdown('<div class="section-header">🚰 Fasilitas Penyediaan Air Minum Gratis</div>', unsafe_allowed_html=True)
    st.write("Rasulullah SAW bersabda: *'Sedekah apa yang paling utama?' Beliau menjawab: 'Air minum.'* (HR. Abu Daud)")
    st.info("Sebagai wujud nyata pengabdian kepada masyarakat Pangkalan Bun, Kelompok Bundaran Pancasila menyediakan posko depot air minum higienis gratis di area luar sekretariat. Fasilitas ini ditujukan bebas bagi para musafir, pengemudi ojek online, pedagang kaki lima, petugas kebersihan, maupun warga sekitar yang melintas.")
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.subheader("📍 Lokasi Posko Depot")
        st.write("Area Bundaran Pancasila, Kelurahan Madurejo, Kecamatan Arut Selatan, Pangkalan Bun, Kotawaringin Barat (Kalimantan Tengah).")
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
    st.markdown('<div class="section-header">📞 Pusat Kontak Layanan & Informasi Umat</div>', unsafe_allowed_html=True)
    st.markdown("""
    <div class="info-card">
        <p><b>📍 Alamat Sekretariat Fisik:</b><br>
