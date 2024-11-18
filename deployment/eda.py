import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load 
@st.cache_data
def load_data():
    df = pd.read_csv('loan_approval_dataset.csv') 
    return df

def show_eda():
    # judul app
    st.title("Exploratory Data Analysis (EDA)")

    # Load data
    df = load_data()

    # display data mentah
    st.subheader("Raw Data")
    st.write("Berikut adalah data mentah yang digunakan untuk analisis. Data ini mencakup berbagai informasi penting terkait pinjaman.")
    st.write(df)

    # Display data statistics
    st.subheader("Data Summary")
    st.write("Ringkasan statistik dari data yang ada, termasuk nilai rata-rata, standar deviasi, serta nilai minimum dan maksimum dari setiap kolom numerik.")
    st.write(df.describe())

    # Visualizations
    st.subheader("Visualizations")
    
    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    st.write("Visualisasi ini menunjukkan hubungan antar variabel numerik dalam dataset. Semakin dekat nilai korelasinya ke 1 atau -1, semakin kuat hubungannya.")
    numerical_cols = df.select_dtypes(include=['float64', 'int64'])  # Memilih hanya kolom numerik
    correlation_matrix = numerical_cols.corr()  # Membuat matriks korelasi

    # Membuat heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    plt.title('Heatmap Korelasi antar kolom numerikal')
    st.pyplot(fig)  # Menampilkan heatmap 

    # Count Plot for categorical columns
    st.subheader("Count Plot")
    st.write("Pilih kolom kategorikal untuk melihat distribusi jumlah dari setiap kategori.")
    categorical_col = st.selectbox("Select a categorical column", df.select_dtypes(include=['object']).columns)
    fig, ax = plt.subplots()
    sns.countplot(x=categorical_col, data=df, ax=ax)
    st.pyplot(fig)
    
    
    # Histogram for numerical columns
    st.subheader("Histogram")
    st.write("Gunakan histogram untuk melihat distribusi frekuensi dari variabel numerik pilihan Anda.")
    numerical_col_hist = st.selectbox("Select a numerical column for Histogram", df.select_dtypes(include=['int64', 'float64']).columns)
    fig, ax = plt.subplots()
    sns.histplot(df[numerical_col_hist], bins=30, kde=True, ax=ax)
    st.pyplot(fig)