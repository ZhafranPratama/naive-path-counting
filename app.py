import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Naive Path Counting Analysis",
    layout="centered"
)

st.title("Analisis Kompleksitas Algoritma")
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
    max_value=10000,
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

    st.write("## Hasil Perhitungan")

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

    st.write("## Grafik Perbandingan Waktu Eksekusi")
    
    benchmark_range = list(range(1, n + 1))
    waktu_iteratif_list = []
    waktu_rekursif_list = []

    with st.spinner("🔄 Sedang membuat grafik perbandingan..."):
        for val in benchmark_range:
            t0 = time.perf_counter()
            path_count_iteratif(val)
            t1 = time.perf_counter()
            waktu_iteratif_list.append(t1 - t0)

            if val <= 20:
                t2 = time.perf_counter()
                path_count_rekursif(val, val)
                t3 = time.perf_counter()
                waktu_rekursif_list.append(t3 - t2)
            else:
                waktu_rekursif_list.append(None)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(benchmark_range, waktu_iteratif_list, marker='o', 
            linewidth=2.5, markersize=8, label='Algoritma Iteratif (DP)', 
            color='#2ecc71', alpha=0.8)

    waktu_rekursif_dengan_range = [(benchmark_range[i], waktu_rekursif_list[i]) 
                                    for i in range(len(benchmark_range)) 
                                    if waktu_rekursif_list[i] is not None]
    if waktu_rekursif_dengan_range:
        range_rekursif, waktu_rekursif_filtered = zip(*waktu_rekursif_dengan_range)
        ax.plot(range_rekursif, waktu_rekursif_filtered, marker='s', 
                linewidth=2.5, markersize=8, label='Algoritma Rekursif Naive', 
                color='#e74c3c', alpha=0.8)

    ax.set_xlabel('Ukuran Grid (n x n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Waktu Eksekusi (detik)', fontsize=12, fontweight='bold')
    ax.set_title('Perbandingan Waktu Eksekusi: Iteratif vs Rekursif', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=11, loc='upper left')
    ax.set_yscale('log') 

    plt.tight_layout()
    st.pyplot(fig)

    st.write("## Analisis Kompleksitas")
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