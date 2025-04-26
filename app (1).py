import streamlit as st
import pandas as pd
import base64
import numpy as np

# --- Fungsi untuk mengatur latar belakang ---
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Fungsi untuk menghitung BMR dan kebutuhan kalori ---
def hitung_bmr(jenis_kelamin, berat_kg, tinggi_cm, usia_tahun, tingkat_aktivitas):
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_kg) + (4.799 * tinggi_cm) - (5.677 * usia_tahun)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_kg) + (3.098 * tinggi_cm) - (4.330 * usia_tahun)
    else:
        return None, None

    if tingkat_aktivitas.lower() == 'ringan':
        kebutuhan_kalori = bmr * 1.2
    elif tingkat_aktivitas.lower() == 'sedang':
        kebutuhan_kalori = bmr * 1.375
    elif tingkat_aktivitas.lower() == 'berat':
        kebutuhan_kalori = bmr * 1.55
    elif tingkat_aktivitas.lower() == 'sangat berat':
        kebutuhan_kalori = bmr * 1.725
    else:
        kebutuhan_kalori = bmr * 1.2  # Default jika tidak valid

    return bmr, kebutuhan_kalori

# --- Data Menu Makanan 4 Sehat 5 Sempurna (Contoh Sebagian) ---
data_menu = {
    "Pagi": [
        {"nama": "Nasi Goreng Ayam", "kkal_per_gram": 1.5, "deskripsi": "Nasi dengan ayam, telur, dan sayuran."},
        {"nama": "Bubur Ayam", "kkal_per_gram": 0.8, "deskripsi": "Bubur nasi dengan suwiran ayam dan pelengkap."},
        {"nama": "Roti Gandum Selai Kacang", "kkal_per_gram": 2.8, "deskripsi": "Roti gandum dengan selai kacang."},
        # ... tambahkan menu pagi lainnya hingga total 100
    ],
    "Siang": [
        {"nama": "Nasi Ayam Bakar", "kkal_per_gram": 1.8, "deskripsi": "Nasi dengan ayam bakar dan lalapan."},
        {"nama": "Nasi Ikan Goreng", "kkal_per_gram": 2.0, "deskripsi": "Nasi dengan ikan goreng dan sayur."},
        {"nama": "Gado-gado", "kkal_per_gram": 1.2, "deskripsi": "Sayuran rebus dengan bumbu kacang."},
        # ... tambahkan menu siang lainnya hingga total 100
    ],
    "Malam": [
        {"nama": "Nasi Tahu Tempe", "kkal_per_gram": 1.1, "deskripsi": "Nasi dengan tahu dan tempe bacem/goreng."},
        {"nama": "Nasi Tim Ayam", "kkal_per_gram": 1.3, "deskripsi": "Nasi lembek dengan cincangan ayam dan sayuran."},
        {"nama": "Ikan Pesmol Nasi", "kkal_per_gram": 1.6, "deskripsi": "Ikan dengan bumbu pesmol dan nasi."},
        # ... tambahkan menu malam lainnya hingga total 100
    ],
    "Selingan": [
        {"nama": "Buah Apel", "kkal_per_gram": 0.5, "deskripsi": "Buah apel segar."},
        {"nama": "Yogurt Plain", "kkal_per_gram": 0.6, "deskripsi": "Yogurt tanpa tambahan gula."},
        {"nama": "Kacang Almond", "kkal_per_gram": 5.8, "deskripsi": "Segenggam kacang almond."},
        # ... tambahkan menu selingan lainnya hingga total 100
    ],
    "Pelengkap": [
        {"nama": "Susu Rendah Lemak", "kkal_per_gram": 0.7, "deskripsi": "Segelas susu rendah lemak."},
        # ... tambahkan pelengkap lainnya hingga total 100
    ]
}

# --- Pengaturan Latar Belakang ---
background_image_url = "https://images.unsplash.com/photo-1540189490227-7159967d9c7c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Zm9vZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60" # Ganti dengan URL gambar Anda
set_background(background_image_url)

# --- Judul dan Deskripsi Web ---
st.title("Aplikasi Penghitung Kalori & Saran Menu 4 Sehat 5 Sempurna")
st.markdown("Selamat datang di aplikasi sederhana untuk menghitung kebutuhan kalori harian Anda dan mendapatkan saran menu makanan sehat berdasarkan prinsip 4 Sehat 5 Sempurna.")
st.markdown("---")

# --- Input Data Pengguna ---
st.subheader("Masukkan Data Diri Anda")
nama = st.text_input("Nama Lengkap:")
tinggi = st.number_input("Tinggi Badan (cm):", min_value=1.0, max_value=300.0, value=170.0)
berat = st.number_input("Berat Badan (kg):", min_value=1.0, max_value=500.0, value=70.0)
usia = st.number_input("Usia (Tahun):", min_value=1, max_value=150, value=30, step=1)
jenis_kelamin = st.radio("Jenis Kelamin", ("Laki-laki", "Perempuan"))
tingkat_aktivitas = st.selectbox(
    "Tingkat Aktivitas",
    ("Ringan", "Sedang", "Berat", "Sangat Berat")
)
st.markdown("---")

# --- Perhitungan Kebutuhan Kalori dan Saran Menu ---
if st.button("Hitung Kebutuhan Kalori & Berikan Saran Menu"):
    bmr, kebutuhan_kalori = hitung_bmr(jenis_kelamin, berat, tinggi, usia, tingkat_aktivitas)
    if bmr is not None:
        st.subheader("Hasil Perhitungan Kebutuhan Kalori")
        st.write(f"Basal Metabolic Rate (BMR) Anda adalah: **{bmr:.2f}** kalori.")
        st.write(f"Perkiraan Kebutuhan Kalori Harian Anda adalah: **{kebutuhan_kalori:.2f}** kalori.")
        st.markdown("---")

        st.subheader("Saran Menu Makanan 4 Sehat 5 Sempurna")
        st.info(f"Berikut adalah contoh saran menu makanan dengan perkiraan kebutuhan kalori harian Anda sekitar **{kebutuhan_kalori:.0f}** kalori. Sesuaikan porsi sesuai kebutuhan Anda.")

        def display_menu(meal_type):
            st.subheader(meal_type)
            for i, menu in enumerate(data_menu[meal_type][:3]): # Menampilkan 3 contoh per waktu makan
                st.write(f"{i+1}. **{menu['nama']}** ({menu['kkal_per_gram']:.2f} kkal/gram): {menu['deskripsi']}")
            st.markdown("...") # Tanda bahwa ada lebih banyak menu

        display_menu("Pagi")
        display_menu("Siang")
        display_menu("Malam")
        display_menu("Selingan")
        display_menu("Pelengkap")

        st.markdown("---")
        st.balloons() # Animasi balon setelah perhitungan dan saran ditampilkan

    else:
        st.error("Jenis kelamin tidak valid.")

# --- Penutup Aplikasi ---
st.markdown("## Terima kasih telah menggunakan aplikasi ini!")
st.markdown("Semoga membantu Anda dalam perjalanan menuju hidup sehat.")
