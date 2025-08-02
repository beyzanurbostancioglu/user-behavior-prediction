
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, classification_report
import joblib

# 1. İşlenmiş veriyi yükleme
features_df = pd.read_csv('processed_features.csv')
print("İşlenmiş veri başarıyla yüklendi. Veri boyutu:", features_df.shape)

# 2. Veriyi Hazırlama
# 'is_clicked' ve 'is_purchased' hedeflerimiz olduğu için onları ayırıyoruz.
# Diğer tüm sütunlar ise özelliklerimiz (X) olacak.

# Tıklama Tahmini için
X_click = features_df.drop(columns=['is_clicked', 'is_purchased'])
y_click = features_df['is_clicked']

# Satın Alma Tahmini için
X_purchase = features_df.drop(columns=['is_clicked', 'is_purchased'])
y_purchase = features_df['is_purchased']


# 3. Eğitim ve Test Setlerini Ayırma
# Verimizin %80'ini eğitim için, %20'sini test için ayırıyoruz.
# random_state parametresi, her çalıştırmada aynı verinin ayrılmasını sağlar.

# Tıklama Modeli için
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_click, y_click, test_size=0.2, random_state=42)

# Satın Alma Modeli için
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_purchase, y_purchase, test_size=0.2, random_state=42)


# 4. Modeli Eğitme
click_model = LogisticRegression(solver='liblinear', random_state=42)
purchase_model = LogisticRegression(solver='liblinear', random_state=42)

# Tıklama modelini eğitme
print("\nTıklama tahmini modeli eğitiliyor...")
click_model.fit(X_train_c, y_train_c)

# Satın alma modelini eğitme
print("Satın alma tahmini modeli eğitiliyor...")
purchase_model.fit(X_train_p, y_train_p)


# 5. Tahmin Yapma ve Modeli Değerlendirme


# Tıklama Modeli
y_pred_c = click_model.predict(X_test_c)
print("\n--- Tıklama Tahmini Model Değerlendirmesi ---")
print("Doğruluk Oranı (Accuracy):", accuracy_score(y_test_c, y_pred_c))
print("Recall Skoru:", recall_score(y_test_c, y_pred_c, average='macro'))
print("\nSınıflandırma Raporu:\n", classification_report(y_test_c, y_pred_c))

# Satın Alma Modeli
y_pred_p = purchase_model.predict(X_test_p)
print("\n--- Satın Alma Tahmini Model Değerlendirmesi ---")
print("Doğruluk Oranı (Accuracy):", accuracy_score(y_test_p, y_pred_p))
# purchase_model için pozitif örnekler az olduğu için recall skorunu hesaplarken hata verebilir. Bu nedenle, 'zero_division=0' parametresini kullanıyoruz.
print("Recall Skoru:", recall_score(y_test_p, y_pred_p, average='macro', zero_division=0))
print("\nSınıflandırma Raporu:\n", classification_report(y_test_p, y_pred_p, zero_division=0))


# 6. Eğitilmiş Modelleri Kaydetme

joblib.dump(click_model, 'click_model.pkl')
joblib.dump(purchase_model, 'purchase_model.pkl')
print("\nModeller 'click_model.pkl' ve 'purchase_model.pkl' olarak kaydedildi.")