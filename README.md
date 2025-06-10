# Hipertansiyon Risk Analizi Projesi

Bu proje, hipertansiyon riski tahmini için makine öğrenmesi teknikleri kullanarak kapsamlı bir veri analizi çalışmasıdır. Kaggle'dan alınan hipertansiyon tahmin veri seti üzerinde keşifsel veri analizi (EDA) ve makine öğrenmesi modelleri uygulanmıştır.

## 📋 Proje Özeti

Bu çalışma, çeşitli sağlık göstergeleri ve risk faktörlerini kullanarak hipertansiyon riskini tahmin etmeyi amaçlamaktadır. Proje, biyoinformatik dersi final ödevi olarak hazırlanmıştır.

### 🎯 Hedefler
- Hipertansiyon risk faktörlerini analiz etmek
- Veri setindeki ilişkileri keşfetmek
- Makine öğrenmesi modeli ile risk tahmini yapmak
- Kapsamlı görselleştirmeler oluşturmak

## 📊 Veri Seti

- **Kaynak**: Kaggle Hipertansiyon Tahmin Veri Seti
- **Örnek Sayısı**: 4,240
- **Özellik Sayısı**: 13 (Risk hariç)
- **Hedef Değişken**: Risk (Hipertansiyon Riski - 0: Düşük, 1: Yüksek)

### Özellikler
- `age`: Yaş
- `BMI`: Vücut Kitle İndeksi
- `sysBP`: Sistolik Kan Basıncı
- `diaBP`: Diyastolik Kan Basıncı
- `heartRate`: Kalp Atış Hızı
- `glucose`: Kan Şekeri
- `cigsPerDay`: Günde Sigara Sayısı
- `BPMeds`: Kan Basıncı İlaçları
- `prevalentStroke`: Önceki İnme
- `prevalentHyp`: Önceki Hipertansiyon
- `diabetes`: Diyabet
- `totChol`: Toplam Kolesterol
- `education`: Eğitim Seviyesi

## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+
- pip

### Adımlar

1. **Repository'yi klonlayın:**
```bash
git clone https://github.com/firatdemir47/hypertension-risk-analysis.git
cd hypertension-risk-analysis
```

2. **Virtual environment oluşturun:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

## 📁 Proje Dosyaları

### Ana Scriptler
- `hypertension_eda.py` - Keşifsel veri analizi ve görselleştirme
- `ml_hypertension.py` - Makine öğrenmesi modeli
- `create_word_report.py` - Word raporu oluşturma

### Veri ve Raporlar
- `Hypertension-risk-model-main.csv` - Ana veri seti
- `eda_raporu.md` - EDA analiz raporu
- `ml_results.txt` - Makine öğrenmesi sonuçları
- `requirements.txt` - Python bağımlılıkları

### Görselleştirmeler (Çalıştırıldıktan sonra oluşur)
- `hipertansiyon_dagilimi.png` - Risk dağılımı
- `korelasyon_matrisi.png` - Özellikler arası korelasyon
- `yas_dagilimi.png` - Yaş dağılımı
- `bmi_dagilimi.png` - BMI dağılımı
- `kan_basinci_dagilimlari.png` - Kan basıncı dağılımları
- `sayisal_ozellikler_kutu_grafik.png` - Kutu grafikleri
- `ozellik_cift_grafik.png` - Özellik çift grafikleri
- `ml_confusion_matrix.png` - Karmaşıklık matrisi
- `ml_roc_curve.png` - ROC eğrisi

## 🚀 Kullanım

### 1. Keşifsel Veri Analizi
```bash
python hypertension_eda.py
```
Bu script:
- Veri setini yükler ve temizler
- Kapsamlı görselleştirmeler oluşturur
- EDA raporu oluşturur

### 2. Makine Öğrenmesi Modeli
```bash
python ml_hypertension.py
```
Bu script:
- Lojistik regresyon modeli eğitir
- Model performansını değerlendirir
- Sonuçları kaydeder

### 3. Word Raporu Oluşturma
```bash
python create_word_report.py
```
Bu script:
- Tüm analizleri içeren Word raporu oluşturur
- Görselleştirmeleri rapora ekler

## 📈 Sonuçlar

### Makine Öğrenmesi Modeli
- **Algoritma**: Lojistik Regresyon
- **Veri Bölünmesi**: %80 eğitim, %20 test
- **Performans Metrikleri**: Doğruluk, Kesinlik, Duyarlılık, F1-Skoru, ROC-AUC

### Ana Bulgular
- Yaş ve kan basıncı değerleri hipertansiyon riski ile güçlü korelasyon gösterir
- BMI ve kan şekeri değerleri önemli risk faktörleridir
- Model, hipertansiyon riskini tahmin etmede yüksek performans gösterir

## 📊 Görselleştirmeler

Proje, aşağıdaki görselleştirmeleri içerir:

### Veri Dağılımları
- Hipertansiyon risk dağılımı
- Yaş ve BMI dağılımları
- Kan basıncı ölçümlerinin analizi

### İlişki Analizleri
- Özellikler arası korelasyon matrisi
- Özellik çift grafikleri
- Kutu grafikleri

### Model Performansı
- Karmaşıklık matrisi
- ROC eğrisi

## 📷 Görselleştirme Örnekleri

Aşağıda, analiz ve modelleme sırasında otomatik olarak üretilen bazı görsellerin örnekleri yer almaktadır:

### Hipertansiyon Risk Dağılımı
![hipertansiyon_dagilimi](https://github.com/user-attachments/assets/1ef17894-28b6-488d-8822-52590b5b1b3e)

Veri setindeki düşük ve yüksek riskli bireylerin dağılımı.

### Yaş Dağılımı
![yas_dagilimi](https://github.com/user-attachments/assets/746829a5-8d94-464b-afd8-df46f0c643e4)

Katılımcıların yaş dağılımı.

### BMI Dağılımı
![bmi_dagilimi](https://github.com/user-attachments/assets/b59d73ac-e8b1-468d-a313-d305d333a720)

Vücut kitle indeksi (BMI) dağılımı.

### Kan Basıncı Dağılımları
![kan_basinci_dagilimlari](https://github.com/user-attachments/assets/656d9f3d-a40e-4b1f-810e-26fc6e509145)

Sistolik ve diyastolik kan basıncı değerlerinin dağılımı.

### Özellikler Arası Korelasyon Matrisi
![korelasyon_matrisi](https://github.com/user-attachments/assets/ce1a79b7-6299-4c3a-9ef9-818452cfc861)

Tüm değişkenler arasındaki korelasyonları gösterir.

### Sayısal Özellikler Kutu Grafik
![sayisal_ozellikler_kutu_grafik](https://github.com/user-attachments/assets/3c5edfce-c37e-4800-b28a-6528b18c2b4d)

Temel sayısal değişkenlerin kutu grafikleri.

### Özellik Çift Grafik
![ozellik_cift_grafik](https://github.com/user-attachments/assets/1ecc7df7-0db4-40ca-8e3d-8515f3e67a09)

Seçili değişkenler arasındaki ilişkiler.

### Karmaşıklık Matrisi
![ml_confusion_matrix](https://github.com/user-attachments/assets/ea6790ff-51ec-46cd-9301-dde5e508ec84)

Makine öğrenmesi modelinin tahmin performansını gösterir.

### ROC Eğrisi
![ml_roc_curve](https://github.com/user-attachments/assets/5d8512fc-f1c5-4267-abcc-aa17ba891b2e)

Modelin ROC eğrisi ve AUC değeri.

## 🔧 Teknik Detaylar

### Kullanılan Kütüphaneler
- **pandas**: Veri manipülasyonu
- **numpy**: Sayısal işlemler
- **matplotlib & seaborn**: Görselleştirme
- **scikit-learn**: Makine öğrenmesi
- **python-docx**: Word raporu oluşturma

### Model Parametreleri
- **Algoritma**: LogisticRegression
- **max_iter**: 1000
- **random_state**: 42
- **test_size**: 0.2

## 📝 Raporlar

### EDA Raporu (`eda_raporu.md`)
- Veri seti genel bakış
- Temel istatistikler
- Görselleştirme açıklamaları
- Bulgular ve yorumlar

### ML Sonuçları (`ml_results.txt`)
- Model performans metrikleri
- Sınıflandırma raporu
- Karmaşıklık matrisi

### Word Raporu
- Kapsamlı analiz raporu
- Görselleştirmeler
- Sonuçlar ve öneriler

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

**Firat Demir**
- GitHub: [@firatdemir47](https://github.com/firatdemir47)

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilir veya doğrudan iletişime geçebilirsiniz.

---

**Not**: Bu proje eğitim amaçlı hazırlanmıştır. Tıbbi kararlar için profesyonel sağlık hizmetlerine başvurunuz. 
