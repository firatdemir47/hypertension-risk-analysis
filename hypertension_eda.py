import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Görselleştirme ayarları
sns.set_palette("husl")

# Veri setini yükleme
df = pd.read_csv('Hypertension-risk-model-main.csv')

# Temel veri keşfi
print("Veri Seti Boyutu:", df.shape)
print("\nİlk 5 Satır:")
print(df.head())
print("\nTemel İstatistikler:")
print(df.describe())
print("\nEksik Değerler:")
print(df.isnull().sum())

# Veri temizleme
# Eksik değerleri temizleme
df = df.dropna()

# Kategorik değişkenleri sayısal değerlere dönüştürme
label_encoder = LabelEncoder()
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Görselleştirmeleri oluşturma
def create_visualizations():
    # 1. Hedef Değişken Dağılımı
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Risk', data=df)
    plt.title('Hipertansiyon Risk Dağılımı')
    plt.xlabel('Hipertansiyon Riski')
    plt.ylabel('Vaka Sayısı')
    plt.savefig('hipertansiyon_dagilimi.png')
    plt.close()

    # 2. Korelasyon Matrisi
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Özellikler Arası Korelasyon Matrisi')
    plt.tight_layout()
    plt.savefig('korelasyon_matrisi.png')
    plt.close()

    # 3. Yaş Dağılımı
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], kde=True)
    plt.title('Yaş Dağılımı')
    plt.xlabel('Yaş')
    plt.ylabel('Frekans')
    plt.savefig('yas_dagilimi.png')
    plt.close()

    # 4. BMI Dağılımı
    plt.figure(figsize=(10, 6))
    sns.histplot(df['BMI'], kde=True)
    plt.title('Vücut Kitle İndeksi (BMI) Dağılımı')
    plt.xlabel('BMI')
    plt.ylabel('Frekans')
    plt.savefig('bmi_dagilimi.png')
    plt.close()

    # 5. Kan Basıncı Dağılımları
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df['sysBP'], kde=True)
    plt.title('Sistolik Kan Basıncı')
    plt.xlabel('Sistolik Kan Basıncı (mmHg)')
    plt.ylabel('Frekans')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df['diaBP'], kde=True)
    plt.title('Diyastolik Kan Basıncı')
    plt.xlabel('Diyastolik Kan Basıncı (mmHg)')
    plt.ylabel('Frekans')
    plt.tight_layout()
    plt.savefig('kan_basinci_dagilimlari.png')
    plt.close()

    # 6. Sayısal özellikler için kutu grafikleri
    numerical_features = ['age', 'BMI', 'sysBP', 'diaBP', 'heartRate', 'glucose']
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(numerical_features, 1):
        plt.subplot(2, 3, i)
        sns.boxplot(y=df[feature])
        plt.title(f'{feature} Kutu Grafiği')
    plt.tight_layout()
    plt.savefig('sayisal_ozellikler_kutu_grafik.png')
    plt.close()

    # 7. Seçili özellikler için çift grafik
    selected_features = ['age', 'BMI', 'sysBP', 'diaBP', 'Risk']
    sns.pairplot(df[selected_features], hue='Risk')
    plt.savefig('ozellik_cift_grafik.png')
    plt.close()

# Rapor oluşturma
def generate_report():
    report = f"""
    # Hipertansiyon Tahmin Veri Seti - Keşifsel Veri Analizi Raporu

    ## Veri Seti Genel Bakış
    - Toplam örnek sayısı: {len(df)}
    - Özellik sayısı: {len(df.columns)}
    - Hedef değişken: Risk (Hipertansiyon Riski)

    ## Veri Özeti
    {df.describe().to_markdown()}

    ## Temel Bulgular
    1. Veri setindeki hipertansiyon risk dağılımı
    2. Farklı özellikler arasındaki korelasyonlar
    3. Yaş ve BMI dağılımları
    4. Kan basıncı ölçümlerinin analizi
    5. Özellikler arası ilişkilerin çift grafiklerle gösterimi

    ## Görselleştirmeler
    Tüm görselleştirmeler ayrı PNG dosyaları olarak kaydedildi:
    - hipertansiyon_dagilimi.png
    - korelasyon_matrisi.png
    - yas_dagilimi.png
    - bmi_dagilimi.png
    - kan_basinci_dagilimlari.png
    - sayisal_ozellikler_kutu_grafik.png
    - ozellik_cift_grafik.png

    ## Sonuç
    Bu keşifsel veri analizi, hipertansiyon tahmin veri setindeki çeşitli sağlık göstergeleri ile hipertansiyon riski arasındaki ilişkileri ortaya koymaktadır.
    Görselleştirmeler, farklı özelliklerin dağılımlarını ve aralarındaki korelasyonları anlamamıza yardımcı olmaktadır.
    """

    with open('eda_raporu.md', 'w', encoding='utf-8') as f:
        f.write(report)

# Analizi çalıştır
create_visualizations()
generate_report()

print("EDA başarıyla tamamlandı! Oluşturulan dosyaları kontrol edin:")
print("- eda_raporu.md (analiz raporunu içerir)")
print("- Çeşitli PNG dosyaları (görselleştirmeleri içerir)") 