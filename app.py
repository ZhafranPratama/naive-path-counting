import streamlit as st
import time

st.set_page_config(
    page_title="Naive Path Counting Analysis",
    layout="centered"
)

st.title("📊 Analisis Kompleksitas Algoritma")
st.subheader(
    "Perbandingan Algoritma Iteratif dan Rekursif "
    "pada Masalah Naive Path Counting"
)

st.write("""
Masalah *Naive Path Counting* menghitung jumlah jalur dari titik (0,0) ke (n,n)
pada grid dua dimensi dengan pergerakan *kanan* dan *bawah*.
""")

def path_count_rekursif(i, j):
    if i == 0 or j == 0:
        return 1
    return path_count_rekursif(i - 1, j) + path_count_rekursif(i, j - 1)

def path_count_iteratif(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n][n]

n = st.number_input(
    "Masukkan ukuran grid (n x n)",
    min_value=1,
    max_value=15,
    value=5,
    step=1,
    help="Nilai besar akan membuat algoritma rekursif sangat lambat"
)

if st.button("🔍 Jalankan Analisis"):
    t0 = time.perf_counter()
    hasil_iteratif = path_count_iteratif(n)
    t1 = time.perf_counter()
    waktu_iteratif = t1 - t0

    t2 = time.perf_counter()
    hasil_rekursif = path_count_rekursif(n, n)
    t3 = time.perf_counter()
    waktu_rekursif = t3 - t2

    st.write("## 📌 Hasil Perhitungan")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Algoritma Iteratif (DP)")
        st.write(f"Jumlah Jalur: *{hasil_iteratif}*")
        st.write(f"Waktu Eksekusi: *{waktu_iteratif:.6f} detik*")
        st.write("Kompleksitas Waktu: *O(n²)*")

    with col2:
        st.info("Algoritma Rekursif Naive")
        st.write(f"Jumlah Jalur: *{hasil_rekursif}*")
        st.write(f"Waktu Eksekusi: *{waktu_rekursif:.6f} detik*")
        st.write("Kompleksitas Waktu: *O(2ⁿ)*")

    st.write("## 🧠 Analisis Kompleksitas")
    st.markdown("""
    *Observasi:*
    - Kedua algoritma menghasilkan jumlah jalur yang *sama*
    - Waktu eksekusi algoritma rekursif meningkat *secara eksponensial*
    - Algoritma iteratif memiliki performa *jauh lebih stabil*

    *Kesimpulan:*
    - Algoritma rekursif naive tidak efisien untuk grid besar
    - Algoritma iteratif (Dynamic Programming) lebih optimal
    - Perbedaan kompleksitas *sangat signifikan* seiring pertumbuhan n
    """)