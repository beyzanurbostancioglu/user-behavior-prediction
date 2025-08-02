
import pandas as pd
import numpy as np

# 20 ürün için örnek veriler
products_data = {
    'product_id': range(1, 21),
    'product_name': ['Siyah Jean Pantolon', 'Mavi Skinny Jean', 'Beyaz Mom Jean', 'Bej Keten Pantolon', 'Kargo Pantolon',
                     'Siyah Havuç Pantolon', 'Gri Eşofman Altı', 'Düz Kesim Jean', 'Yüksek Bel Pantolon', 'Bol Paça Pantolon',
                     'Siyah Kot Ceket', 'Basic T-shirt', 'Oversize Hoodie', 'Desenli Elbise', 'Çizgili Gömlek',
                     'Triko Kazak', 'Spor Şort', 'Siyah Deri Ceket', 'Palazzo Pantolon', 'Krem Rengi Jean'],
    'category': ['Giyim'] * 20,
    'subcategory': ['Pantolon', 'Pantolon', 'Pantolon', 'Pantolon', 'Pantolon',
                    'Pantolon', 'Pantolon', 'Pantolon', 'Pantolon', 'Pantolon',
                    'Ceket', 'T-shirt', 'Hoodie', 'Elbise', 'Gömlek',
                    'Kazak', 'Şort', 'Ceket', 'Pantolon', 'Pantolon'],
    'brand': ['TrendyolMilla', 'Mavi', 'TrendyolMilla', 'Koton', 'TrendyolMilla',
              'TrendyolMilla', 'Nike', 'TrendyolMilla', 'Zara', 'Mavi',
              'Pull&Bear', 'H&M', 'TrendyolMan', 'Vakko', 'Adidas',
              'TrendyolMilla', 'Puma', 'Zara', 'Mango', 'TrendyolMilla'],
    'price': np.random.randint(100, 500, size=20),
    'color': ['Siyah', 'Mavi', 'Beyaz', 'Bej', 'Haki',
              'Siyah', 'Gri', 'Mavi', 'Siyah', 'Siyah',
              'Siyah', 'Beyaz', 'Gri', 'Siyah', 'Lacivert',
              'Ekru', 'Siyah', 'Siyah', 'Beyaz', 'Krem']
}
products_df = pd.DataFrame(products_data)
products_df.to_csv('products.csv', index=False)
print("Ürünler verisi başarıyla oluşturuldu:")
print(products_df.head())


# 5 kullanıcı için örnek veriler
users_data = {
    'user_id': range(1, 6),
    'age': np.random.randint(18, 50, size=5),
    'gender': ['Kadın', 'Erkek', 'Kadın', 'Erkek', 'Kadın'],
    'city': ['İstanbul', 'Ankara', 'İzmir', 'İstanbul', 'Bursa']
}
users_df = pd.DataFrame(users_data)
users_df.to_csv('users.csv', index=False)
print("\nKullanıcılar verisi başarıyla oluşturuldu:")
print(users_df.head())


# 10 oturum için örnek veriler
sessions_data = []

# Oturum 1: Kullanıcı 1, "pantolon" arıyor
sessions_data.append({
    'session_id': 1,
    'user_id': 1,
    'search_term': 'pantolon',
    'displayed_products': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20],  # Pantolon alt kategorisindeki ürünler
    'clicked_products': [1, 5, 9, 19],
    'purchased_products': [1],
    'timestamp': '2025-07-29 12:05:00'
})

# Oturum 2: Kullanıcı 2, "kot ceket" arıyor
sessions_data.append({
    'session_id': 2,
    'user_id': 2,
    'search_term': 'kot ceket',
    'displayed_products': [11, 18],  # Ceket alt kategorisindeki ürünler
    'clicked_products': [11],
    'purchased_products': [],
    'timestamp': '2025-07-29 12:10:00'
})

# Oturum 3: Kullanıcı 3, "bol paça pantolon" arıyor
sessions_data.append({
    'session_id': 3,
    'user_id': 3,
    'search_term': 'bol paça pantolon',
    'displayed_products': [10, 19], # Bol paça pantolonlara en yakın ürünler
    'clicked_products': [10],
    'purchased_products': [10],
    'timestamp': '2025-07-29 12:15:00'
})

# Oturum 4: Kullanıcı 1, "siyah pantolon" arıyor
sessions_data.append({
    'session_id': 4,
    'user_id': 1,
    'search_term': 'siyah pantolon',
    'displayed_products': [1, 6, 9, 10], # Renk ve alt kategoriye göre filtrelenmiş
    'clicked_products': [6],
    'purchased_products': [],
    'timestamp': '2025-07-29 12:20:00'
})

# Oturum 5: Kullanıcı 4, "elbise" arıyor
sessions_data.append({
    'session_id': 5,
    'user_id': 4,
    'search_term': 'elbise',
    'displayed_products': [14],
    'clicked_products': [14],
    'purchased_products': [14],
    'timestamp': '2025-07-29 12:25:00'
})

# Oturum 6: Kullanıcı 5, "basic t-shirt" arıyor
sessions_data.append({
    'session_id': 6,
    'user_id': 5,
    'search_term': 'basic t-shirt',
    'displayed_products': [12],
    'clicked_products': [],
    'purchased_products': [],
    'timestamp': '2025-07-29 12:30:00'
})

# Oturum 7: Kullanıcı 3, "skinny jean" arıyor
sessions_data.append({
    'session_id': 7,
    'user_id': 3,
    'search_term': 'skinny jean',
    'displayed_products': [2, 8],
    'clicked_products': [2, 8],
    'purchased_products': [2],
    'timestamp': '2025-07-29 12:35:00'
})

# Oturum 8: Kullanıcı 2, "hoodie" arıyor
sessions_data.append({
    'session_id': 8,
    'user_id': 2,
    'search_term': 'hoodie',
    'displayed_products': [13],
    'clicked_products': [],
    'purchased_products': [],
    'timestamp': '2025-07-29 12:40:00'
})

# Oturum 9: Kullanıcı 5, "gömlek" arıyor
sessions_data.append({
    'session_id': 9,
    'user_id': 5,
    'search_term': 'gömlek',
    'displayed_products': [15],
    'clicked_products': [15],
    'purchased_products': [15],
    'timestamp': '2025-07-29 12:45:00'
})

# Oturum 10: Kullanıcı 4, "jean" arıyor
sessions_data.append({
    'session_id': 10,
    'user_id': 4,
    'search_term': 'jean',
    'displayed_products': [1, 2, 3, 8, 20],
    'clicked_products': [3, 20],
    'purchased_products': [20],
    'timestamp': '2025-07-29 12:50:00'
})

sessions_df = pd.DataFrame(sessions_data)
sessions_df.to_csv('sessions.csv', index=False)
print("\nOturumlar verisi başarıyla oluşturuldu:")
print(sessions_df.head())