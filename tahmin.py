# tahmin.py dosyasına bu kodu yapıştırın
import pandas as pd
import joblib

# 1. Kaydedilmiş modelleri yükleme
try:
    click_model = joblib.load('click_model.pkl')
    purchase_model = joblib.load('purchase_model.pkl')
    print("Modeller başarıyla yüklendi.")
except FileNotFoundError:
    print("Modeller bulunamadı. Lütfen 'model_egitimi.py' dosyasını çalıştırmayı unutmayın.")
    exit()

# 2. Tahmin yapılacak yeni bir test oturumu oluşturma


new_session_data = {
    'session_id': 11,
    'user_id': 1,
    'search_term': 'siyah jean',
    'displayed_products': [1, 6, 11] # Siyah Jean Pantolon, Siyah Havuç Pantolon, Siyah Kot Ceket
}


products_df = pd.read_csv('products.csv')
users_df = pd.read_csv('users.csv')

# 3. Özellik Mühendisliği (Test verisi için)

processed_test_data = []

user_id = new_session_data['user_id']
displayed_products = new_session_data['displayed_products']
for product_id in displayed_products:
    processed_test_data.append({
        'session_id': new_session_data['session_id'],
        'user_id': user_id,
        'product_id': product_id,
        'search_term': new_session_data['search_term']
    })

test_features_df = pd.DataFrame(processed_test_data)

# Özellikleri birleştirme
test_features_df = pd.merge(test_features_df, products_df, on='product_id', how='left')
test_features_df = pd.merge(test_features_df, users_df, on='user_id', how='left')

# Kategorik verileri dönüştürme (modelin beklediği formatta olmalı)
test_features_df = pd.get_dummies(test_features_df, columns=['brand', 'color', 'gender', 'city', 'subcategory', 'category'], drop_first=True)

# Eğitim verisiyle aynı sütunlara sahip olmasını sağlama (Eksik sütunları 0 ile doldurma)
train_columns = pd.read_csv('processed_features.csv').drop(columns=['is_clicked', 'is_purchased']).columns

# Eksik sütunları 0 ile doldurma ve sıralamayı eşitleme
missing_cols = set(train_columns) - set(test_features_df.columns)
for c in missing_cols:
    test_features_df[c] = 0
test_features_df = test_features_df[train_columns]

# İhtiyacımız olmayan sütunları kaldırma
columns_to_drop = ['product_name', 'search_term']
existing_columns = [col for col in columns_to_drop if col in test_features_df.columns]
test_features_df = test_features_df.drop(columns=existing_columns)

# 4. Tahminleri Yapma
click_predictions_proba = click_model.predict_proba(test_features_df)[:, 1] # Olasılık skorlarını al
purchase_predictions_proba = purchase_model.predict_proba(test_features_df)[:, 1]

# 5. Sonuçları Görüntüleme
results = test_features_df[['product_id']].copy()
results['click_proba'] = click_predictions_proba
results['purchase_proba'] = purchase_predictions_proba

print("\n--- Yeni Oturum İçin Tahmin Sonuçları ---")
print("Oturum ID:", new_session_data['session_id'])
print("Kullanıcı ID:", new_session_data['user_id'])
print("Arama Terimi:", new_session_data['search_term'])
print("\nTahminler (Olasılık Skorları):")
print(results)

# En yüksek olasılığa sahip ürünleri tahmin olarak seçme (Örnek: Top-1)
top_click_product = results.sort_values(by='click_proba', ascending=False).iloc[0]
top_purchase_product = results.sort_values(by='purchase_proba', ascending=False).iloc[0]

print("\n--- Tahmini Sonuçlar (En Yüksek Olasılığa Göre) ---")
print(f"Tahmini Tıklanan Ürün ID: {int(top_click_product['product_id'])} (Olasılık: {top_click_product['click_proba']:.2f})")
print(f"Tahmini Satın Alınan Ürün ID: {int(top_purchase_product['product_id'])} (Olasılık: {top_purchase_product['purchase_proba']:.2f})")

import matplotlib.pyplot as plt

# 6. Tahmin Sonuçlarını Görselleştirme
print("\n--- Tahmin Sonuçları Görselleştiriliyor ---")

# Ürün ID'lerini etiket olarak kullanalım
product_labels = [f"Ürün {pid}" for pid in results['product_id']]
x = range(len(product_labels))

# Grafiğin boyutunu ve başlığını ayarlayalım
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35  # Çubukların genişliği

# Tıklama olasılıklarını çubuk grafik olarak çizme
rects1 = ax.bar(x, results['click_proba'], width, label='Tıklama Olasılığı', color='skyblue')

# Satın alma olasılıklarını çubuk grafik olarak çizme (biraz kaydırarak)
rects2 = ax.bar([p + width for p in x], results['purchase_proba'], width, label='Satın Alma Olasılığı', color='lightcoral')

# Etiketler, başlık ve diğer detayları ayarlama
ax.set_ylabel('Olasılık Skoru')
ax.set_title('Gösterilen Ürünlerin Tıklanma ve Satın Alma Olasılıkları')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(product_labels)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Her çubuğun üzerine olasılık değerini yazma
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Dikey kaydırma
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()