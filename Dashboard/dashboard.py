import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
main_data = pd.read_csv("Dashboard/main_data.csv")

# # Pisahkan menjadi dua DataFrame: df_day dan df_hour
# df_day = main_data[main_data['dteday'].notna()]
# df_hour = main_data[main_data['hr'].notna()]

# Sidebar
st.sidebar.title("Dashboard Penyewaan Sepeda")
st.sidebar.markdown("**• Nama: Novia Ayu Fitriana**")
st.sidebar.markdown("**• Email: a524xam376@devacademy.id**")
st.sidebar.markdown("**• Cohort ID: A524XAM376**")
option = st.sidebar.radio("Pilih Analisis:", ["Data Berdasarkan Kondisi Alam", "Data Berdasarkan Kondisi Waktu"])

# Visualisasi
st.title("Analisis Penyewaan Sepeda")

# Deskripsi
st.markdown("""
Selamat datang di Dashboard! 
Dashboard ini dibuat untuk menyajikan hasil analisis data secara interaktif. Silakan pilih opsi di sidebar untuk melihat bagaimana kondisi alam dan waktu aktivitas memengaruhi penyewaan sepeda.
""")

if option == "Data Berdasarkan Kondisi Alam":
    st.subheader("Penyewaan Sepeda Berdasarkan Suhu, Kelembapan, dan Cuaca")

    # Menambahkan selectbox
    analysis_option = st.selectbox("Pilih Grafik yang Ingin Ditampilkan:", ["Jumlah Penyewa vs Suhu", "Jumlah Penyewa vs Kelembapan", "Jumlah Penyewa vs Kondisi Cuaca"])

    if analysis_option == "Jumlah Penyewa vs Suhu":
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.set(style='whitegrid')
        sns.regplot(x='temp', y='cnt', data=main_data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
        ax.set_title("Jumlah Penyewa vs Suhu")
        ax.set_xlabel("Suhu (temp)")
        ax.set_ylabel("Jumlah Penyewa (cnt)")
        plt.grid(True)
        st.pyplot(fig)

        st.write("Grafik ini menunjukkan hubungan antara suhu udara dan jumlah penyewa sepeda. "
                 "korelasi antara penyewa dan kondisi suhu adalah jika kondisi suhu tinggi (> 0.5) maka jumlah penyewa meningkat.")

    elif analysis_option == "Jumlah Penyewa vs Kelembapan":
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.set(style='whitegrid')
        sns.regplot(x='hum', y='cnt', data=main_data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
        ax.set_title("Jumlah Penyewa vs Kelembapan")
        ax.set_xlabel("Kelembapan (hum)")
        ax.set_ylabel("Jumlah Penyewa (cnt)")
        plt.grid(True)
        st.pyplot(fig)

        st.write("Grafik ini menggambarkan dampak kelembapan terhadap jumlah penyewa sepeda. "
                 "Korelasi antara penyewa dan kondisi kelembapan adalah jika kelembapan tinggi maka jumlah penyewa cenderung menurun.")

    elif analysis_option == "Jumlah Penyewa vs Kondisi Cuaca":
        weather_mapping = {
            1: 'Cerah / Berawan Tipis',
            2: 'Berkabut / Berawan',
            3: 'Salju Ringan / Hujan Ringan',
            4: 'Hujan Lebat / Kabut Salju'
        }
        main_data['weather_desc'] = main_data['weathersit'].map(weather_mapping)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='weather_desc', y='cnt', data=main_data, estimator=sum, hue='season', palette='viridis', ax=ax)
        ax.set_title('Jumlah Penyewa Berdasarkan Kondisi Cuaca')
        ax.set_xlabel('Kondisi Cuaca')
        ax.set_ylabel('Total Jumlah Penyewa (cnt)')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.write("Grafik tersebut menunjukkan hubungan antara jumlah penyewa sepeda dengan kondisi cuaca berdasarkan musim. Terlihat bahwa kondisi cuaca 'Cerah / Berawan Tipis' memiliki jumlah penyewa tertinggi di semua musim, menunjukkan bahwa pengguna cenderung menyewa sepeda ketika cuaca mendukung. Kondisi 'Berkabut / Berawan' juga menunjukkan jumlah penyewa yang cukup tinggi, meskipun tidak setinggi cuaca cerah, menandakan bahwa sedikit awan tidak menghalangi aktivitas penyewaan. Sebaliknya, kondisi 'Salju Ringan / Hujan Ringan' memiliki jumlah penyewa yang sangat rendah di semua musim, yang mungkin disebabkan oleh ketidaknyamanan bersepeda dalam cuaca buruk. Perbandingan antar musim menunjukkan bahwa musim tertentu (terutama musim 2 dan 3) memiliki jumlah penyewa yang lebih tinggi, mengindikasikan bahwa suhu yang lebih hangat atau cuaca yang lebih baik lebih menarik bagi pengguna. Secara keseluruhan, grafik ini memperlihatkan bahwa cuaca cerah sangat memengaruhi peningkatan aktivitas penyewaan sepeda, sementara cuaca buruk mengurangi jumlah penyewa secara signifikan.")

elif option == "Data Berdasarkan Kondisi Waktu":
    st.subheader("Penyewaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", data=main_data, marker="o", color="red", ax=ax)

    ax.set_title('Penyewaan Sepeda Berdasarkan Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Penyewa (cnt)')
    plt.grid(True, linestyle="--", alpha=0.6)

    st.pyplot(fig)

    st.write("Grafik ini menampilkan pola penyewaan sepeda berdasarkan jam dalam sehari. \n"
             "Dapat diamati bahwa ada jam-jam tertentu dengan jumlah penyewa yang lebih tinggi, "
             "khususnya di pagi hari (sekitar jam 7-9) dan sore hari (sekitar jam 16-19) yaitu di mana banyak orang berpergian untuk kuliah/kerja. Namun jumlah penyewaan cenderung rendah pada saat malam hari hingga dini hari menandakan minimnya aktivitas di luar ruangan dikarenakan waktu istirahat setelah beraktivitas.")
