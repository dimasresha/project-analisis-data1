import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
from streamlit_option_menu import option_menu

#Navigasi Sidebar
with st.sidebar :
    selected = option_menu ('DATA PEMINJAMAN SEPEDA WASHINGTON DC 2011', 
    ['Hubungan Antara Cuaca dan Peminjaman Sepeda di Washington DC',
    'Perubahan Peminjaman Sepeda Sepanjang Minggu (Week Day) di Washington D.C. pada Tahun 2011'],
    default_index=0)

#HALAMAN 1
if (selected== 'Hubungan Antara Cuaca dan Peminjaman Sepeda di Washington DC') :
    st.title('Hubungan Antara Cuaca dan Peminjaman Sepeda di Washington DC.')
    # Membaca dataset
    hour_day_df = pd.read_csv('dataset_gabungan.csv')

    # Menampilkan data
    st.subheader("TABEL DATASET:")
    st.write(hour_day_df.head())


    # Menghitung korelasi antara variabel cuaca dan jumlah peminjaman sepeda
    correlation = hour_day_df[['temp_y', 'hum_y', 'windspeed_y', 'cnt_y']].corr()

    #VISUALISASI
    st.subheader("VISUALISASI DATA:")

    # Menampilkan heatmap korelasi
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Heatmap Korelasi Antara Cuaca dan Jumlah Peminjaman Sepeda')
    heatmap_fig = plt.gcf()  # Mengambil objek gambar saat ini
    st.pyplot(heatmap_fig)

    # Menampilkan pairplot korelasi
    pairplot = sns.pairplot(hour_day_df, vars=['temp_y', 'hum_y', 'windspeed_y', 'cnt_y'])
    pairplot.fig.suptitle('Pairplot Korelasi Antara Cuaca dan Jumlah Peminjaman Sepeda')
    pairplot_fig = pairplot.fig  # Mengambil objek gambar pairplot
    st.pyplot(pairplot_fig)

    #Kesimpulan
    st.subheader("CONCLUSION:")
    st.write("Dari dataset, hasil, dan visualisasi yang telah dijalankan, diketahui bahwa suhu memiliki korelasi positif dan cukup signifikan tehadap jumlah peminjaman sepeda, kemudian kelembaban menunjukkan korelasi yang terbilang negatif cukup kuat. Sementara itu, kecepatan angin tidak memiliki korelasi yang signifikan dengan jumlah peminjaman sepeda. Visualisasi yang dilakukan menggunakan heatmap memberikan gambaran jelas tentang hubungan atau korelasi tersebut. Dari pembahasan tersebut, disimpulkan bahwa cuaca yang lebih hangan cenderung meningkatkan minat orang untuk menggunakan sepeda, sementara cuaca yang lembab mengurangi minta tsb. Analisis ini dapat membantu penyedia jasa peminjaman sepeda untuk merencanakan straegi operasional mengacu pada prakiraan cuaca.")

if (selected== 'Perubahan Peminjaman Sepeda Sepanjang Minggu (Week Day) di Washington D.C. pada Tahun 2011') :
    st.title('Perubahan Peminjaman Sepeda Sepanjang Minggu (Week Day) di Washington D.C. pada Tahun 2011')

    # Membaca dataset
    hour_day_df = pd.read_csv('dataset_gabungan.csv')

    # Mengonversi kolom 'dteday_x' menjadi tipe data datetime
    hour_day_df['dteday_x'] = pd.to_datetime(hour_day_df['dteday_x'])

    # Menambahkan kolom 'week' untuk mengekstrak jam dari tanggal
    hour_day_df['week'] = hour_day_df['dteday_x'].dt.weekday

    # Menghitung total peminjaman sepeda per hari (weekday)
    peminjaman_per_hari = hour_day_df.groupby('weekday_x')['cnt_y'].sum()

    # Menampilkan total peminjaman sepeda per hari dalam bentuk tabel
    st.write("## Total Peminjaman Sepeda per Hari (Weekday)")
    st.write(peminjaman_per_hari)

    # Membuat plot bar untuk total peminjaman sepeda per hari (weekday)
    st.write("## Grafik Total Peminjaman Sepeda per Hari (Weekday)")
    fig, ax = plt.subplots(figsize=(7, 4))
    peminjaman_per_hari.plot(kind='bar', color='lightgreen', ax=ax)
    ax.set_title('Total Peminjaman Sepeda per Hari (Weekday)')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Total Peminjaman Sepeda')
    ax.set_xticklabels(peminjaman_per_hari.index, rotation=0)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)

    #Kesimpulan
    st.subheader("CONCLUSION:")
    st.write("Tidak terjadi perbedaan yang signifikan antara hari ke hari dalam peminjaman sepeda. Hal tersebut dapat terjadi karena faktor rutinitas. Konsistensi dalam pola penggunaan ini bisa disebabkan oleh jadwal yang teratur dan kebiasaan pengguna sepeda.Walaupun polanya cenderung stabil pada hari kerja, nalisis yang lebih lanjut tetap diperlukan untuk memahami tren, pola harian, dan factor lain yang mungkin perpengaruh.")