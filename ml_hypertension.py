import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve, classification_report
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Veri setini yükle
df = pd.read_csv('Hypertension-risk-model-main.csv')

# Eksik değerleri temizle
df = df.dropna()

# Kategorik değişkenleri sayısal değerlere dönüştür
label_encoder = LabelEncoder()
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Özellikler ve hedef değişkeni ayır
X = df.drop(['Risk'], axis=1)
y = df['Risk']

# Eğitim ve test seti olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Başarım metrikleri
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
cm = confusion_matrix(y_test, y_pred)

# Sonuçları yazdır
print(f"Doğruluk (Accuracy): {accuracy:.2f}")
print(f"Kesinlik (Precision): {precision:.2f}")
print(f"Duyarlılık (Recall): {recall:.2f}")
print(f"F1 Skoru: {f1:.2f}")
print(f"ROC-AUC: {roc_auc:.2f}")
print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred))
print("\nKarmaşıklık Matrisi:\n", cm)

# Karmaşıklık matrisi görselleştir
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Karmaşıklık Matrisi')
plt.xlabel('Tahmin Edilen')
plt.ylabel('Gerçek')
plt.savefig('ml_confusion_matrix.png')
plt.close()

# ROC Eğrisi
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f'ROC AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Eğrisi')
plt.legend(loc='lower right')
plt.savefig('ml_roc_curve.png')
plt.close()

# Sonuçları txt olarak kaydet
with open('ml_results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Doğruluk (Accuracy): {accuracy:.2f}\n")
    f.write(f"Kesinlik (Precision): {precision:.2f}\n")
    f.write(f"Duyarlılık (Recall): {recall:.2f}\n")
    f.write(f"F1 Skoru: {f1:.2f}\n")
    f.write(f"ROC-AUC: {roc_auc:.2f}\n\n")
    f.write("Sınıflandırma Raporu:\n" + classification_report(y_test, y_pred) + "\n")
    f.write("Karmaşıklık Matrisi:\n" + np.array2string(cm) + "\n")

print("Makine öğrenmesi modeli başarıyla eğitildi ve sonuçlar kaydedildi.") 