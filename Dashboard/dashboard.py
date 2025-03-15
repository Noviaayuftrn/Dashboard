import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
main_data = pd.read_csv("Dashboard/main_data.csv")

# Mapping data cuaca
weather_mapping = {
    1: 'Cerah / Berawan Tipis',
    2: 'Berkabut / Berawan',
    3: 'Salju Ringan / Hujan Ringan',
    4: 'Hujan Lebat / Kabut Salju'
}
main_data['weather_desc'] = main_data['weathersit'].map(weather_mapping)

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

    season_filter = st.multiselect("Pilih Musim:", options=main_data['season'].unique(), default=main_data['season'].unique())
    weather_filter = st.multiselect("Pilih Kondisi Cuaca:", options=main_data['weather_desc'].unique(), default=main_data['weather_desc'].unique())

    filtered_data = main_data[(main_data['season'].isin(season_filter)) & (main_data['weather_desc'].isin(weather_filter))]

    # Plot Jumlah Penyewa vs Suhu
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x='temp', y='cnt', data=filtered_data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title("Jumlah Penyewa vs Suhu")
    ax.set_xlabel("Suhu (temp)")
    ax.set_ylabel("Jumlah Penyewa (cnt)")
    plt.grid(True)
    st.pyplot(fig)

    # Plot Jumlah Penyewa vs Kelembapan
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x='hum', y='cnt', data=filtered_data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title("Jumlah Penyewa vs Kelembapan")
    ax.set_xlabel("Kelembapan (hum)")
    ax.set_ylabel("Jumlah Penyewa (cnt)")
    plt.grid(True)
    st.pyplot(fig)

    # Plot Jumlah Penyewa vs Kondisi Cuaca
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weather_desc', y='cnt', data=filtered_data, estimator=sum, palette='viridis', ax=ax)
    ax.set_title('Jumlah Penyewa Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Total Jumlah Penyewa (cnt)')
    plt.xticks(rotation=45) 
    st.pyplot(fig)

elif option == "Data Berdasarkan Kondisi Waktu":
    st.subheader("Penyewaan Sepeda Berdasarkan Jam")
    
    selected_hours = st.slider("Pilih Rentang Jam:", min_value=0, max_value=23, value=(0, 23))

    time_filtered_data = main_data[(main_data['hr'] >= selected_hours[0]) & (main_data['hr'] <= selected_hours[1])]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", data=time_filtered_data, marker="o", color="red", ax=ax)

    ax.set_title('Penyewaan Sepeda Berdasarkan Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Penyewa (cnt)')
    plt.grid(True)
    st.pyplot(fig)
