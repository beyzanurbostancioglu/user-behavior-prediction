
import pandas as pd
import ast

# 1. Veri setlerini yükleme
products_df = pd.read_csv('products.csv')
users_df = pd.read_csv('users.csv')
sessions_df = pd.read_csv('sessions.csv')

print("Veri setleri başarıyla yüklendi.")

# 2. Pozitif ve Negatif Örnekleri Oluşturma
# Bu kısım, her oturumdaki her gösterilen ürün için bir satır oluşturur.
# Bu satırlar, tıklanıp tıklanmadığına ve satın alınıp alınmadığına dair etiketler (0 veya 1) içerir.

# 'displayed_products' gibi liste içeren sütunları string'den listeye dönüştürme
sessions_df['displayed_products'] = sessions_df['displayed_products'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
sessions_df['clicked_products'] = sessions_df['clicked_products'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
sessions_df['purchased_products'] = sessions_df['purchased_products'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Boş listeleri doğru bir şekilde işleme
sessions_df['clicked_products'] = sessions_df['clicked_products'].apply(lambda x: x if isinstance(x, list) else [])
sessions_df['purchased_products'] = sessions_df['purchased_products'].apply(lambda x: x if isinstance(x, list) else [])

# Yeni, işlenmiş veri setini oluşturmak için boş bir liste
processed_data = []

for index, row in sessions_df.iterrows():
    session_id = row['session_id']
    user_id = row['user_id']
    search_term = row['search_term']
    displayed_products = row['displayed_products']
    clicked_products = row['clicked_products']
    purchased_products = row['purchased_products']

    for product_id in displayed_products:
        # Tıklama ve Satın Alma için etiketleri oluşturma
        is_clicked = 1 if product_id in clicked_products else 0
        is_purchased = 1 if product_id in purchased_products else 0

        processed_data.append({
            'session_id': session_id,
            'user_id': user_id,
            'product_id': product_id,
            'search_term': search_term,
            'is_clicked': is_clicked,
            'is_purchased': is_purchased
        })

features_df = pd.DataFrame(processed_data)
print("\nÖrnekler başarıyla oluşturuldu. İlk 5 satır:")
print(features_df.head())


# 3. Diğer Özellikleri Birleştirme
# Ürün ve kullanıcı bilgilerini, her bir etkileşim satırına ekleyelim.
features_df = pd.merge(features_df, products_df, on='product_id', how='left')
features_df = pd.merge(features_df, users_df, on='user_id', how='left')

print("\nTüm özellikler birleştirildi. İlk 5 satır:")
print(features_df.head())

# 4. Kategorik Verileri Sayısal Hale Getirme (One-Hot Encoding)
# Makine öğrenmesi modelleri 'TrendyolMilla', 'Siyah', 'Kadın' gibi metinleri anlayamaz.
# Bu yüzden onları sayısal değerlere dönüştürüyoruz.

# features_df.py dosyasında bu satırı bulun
features_df = pd.get_dummies(features_df, columns=['brand', 'color', 'gender', 'city', 'subcategory'], drop_first=True)

print("\nKategorik özellikler dönüştürüldü. Son DataFrame'in ilk 5 satırı:")
print(features_df.head())

# 5. İhtiyacımız Olmayan Sütunları Kaldırma
# 'search_term' şimdilik kalsın, daha sonra metin analizi için kullanabiliriz.
features_df = features_df.drop(columns=['product_name', 'search_term', 'category'])

# 6. Son DataFrame'i Kaydetme
# Bu, modelimizin doğrudan kullanacağı son veri seti olacak.
features_df.to_csv('processed_features.csv', index=False)

print("\nÖn işlemden geçmiş veri başarıyla 'processed_features.csv' dosyasına kaydedildi.")