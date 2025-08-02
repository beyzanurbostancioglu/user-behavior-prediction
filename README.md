# # 🚀 E-ticaret Kullanıcı Davranışı Tahmin Projesi 🛍️

Bu proje, e-ticaret platformlarındaki kullanıcı davranışlarını analiz etmek ve tahmin etmek için uçtan uca bir makine öğrenmesi çözümünü simüle eder. Bir kullanıcının arama oturumunda gösterilen ürünler arasından hangi ürünlere **tıklayacağını** ve hangi ürünleri **satın alacağını** tahmin eden modeller geliştirmeyi amaçlamaktadır.

## 🌟 Proje Amacı

Temel amacımız, veri odaklı yaklaşımlar kullanarak kullanıcı deneyimini iyileştiren bir sistemin nasıl oluşturulacağını göstermektir. Bu proje, gerçek dünya verilerinin karmaşıklığını basitleştirerek, bir makine öğrenmesi projesinin temel adımlarını anlaşılır bir şekilde sunar.

## 📂 Proje Yapısı

Proje, her biri belirli bir görevi yerine getiren dört ana Python dosyasından oluşur.

```bash
 datathon/
├── veri_olustur.py         # 💾 Örnek verileri (ürün, kullanıcı, oturum) oluşturur.
├── ozellik_muhendisligi.py   # ⚙️ Ham veriyi makine öğrenmesi için hazırlar ve işler.
├── model_egitimi.py        # 🧠 Tıklama ve satın alma için iki ayrı modeli eğitir.
├── tahmin.py               # 🔮 Eğitilmiş modellerle yeni bir oturum için tahminler yapar ve sonuçları görselleştirir.
├── products.csv            # Ürün bilgileri.
├── users.csv               # Kullanıcı bilgileri.
├── sessions.csv            # Kullanıcı oturum verileri.
├── processed_features.csv  # İşlenmiş ve modele hazır veri.
├── click_model.pkl         # Kaydedilmiş tıklama tahmini modeli.
├── purchase_model.pkl      # Kaydedilmiş satın alma tahmini modeli.
└── README.md
 ```


## 🛠️ Kullanılan Teknolojiler

Bu proje, aşağıdaki popüler Python kütüphanelerini kullanmaktadır:

* `pandas`: Veri işleme ve analizi için vazgeçilmez bir araç.
* `numpy`: Sayısal işlemler ve veri manipülasyonu için kullanılır.
* `scikit-learn`: Makine öğrenmesi modellerini oluşturmak ve değerlendirmek için ana kütüphanemiz.
* `joblib`: Eğitilmiş modelleri kolayca kaydetmek ve yüklemek için kullanılır.
* `matplotlib`: Tahmin sonuçlarını görselleştirmek için kullanılır.

## 🚀 Hızlı Başlangıç

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla izleyin:

1.  **Depoyu klonlayın ve klasöre gidin:**
    ```bash
    git clone [https://github.com/beyzanurbostancioglu/user-behavior-prediction.git](https://github.com/beyzanurbostancioglu/user-behavior-prediction.git)
    cd datathon
    ```
2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install pandas numpy scikit-learn joblib matplotlib
    ```
3.  **Projenin akışını adım adım çalıştırın:**
    ```bash
    # Örnek veri setlerini oluşturun
    python veri_olustur.py

    # Özellik mühendisliği yaparak veriyi hazırlayın
    python ozellik_muhendisligi.py

    # Tıklama ve satın alma modellerini eğitin
    python model_egitimi.py

    # Yeni bir oturum için tahminler yapın. Bu komut, ayrıca sonuçları görselleştiren bir grafik penceresi açacaktır.
    python tahmin.py
    ```

## 📊 Proje Çıktıları ve Analiz

Bu proje, küçük ve sentetik bir veri seti üzerinde çalışıldığı için model performansları başlangıç seviyesinde kalmaktadır. Ancak, bu durum gerçek dünya projelerinde veri kalitesinin ve niceliğinin model başarısı üzerindeki kritik etkisini göstermektedir.

Son adımda, eğitilen modellerin yeni bir senaryo için nasıl tahminler ürettiğini göreceksiniz. `tahmin.py` komutu çalıştırıldığında, tahmin olasılıklarını gösteren **etkileyici bir çubuk grafik** ekranda belirecektir. Bu grafik, projenin en önemli çıktılarından biridir ve bir makine öğrenmesi sisteminin tahminlerini nasıl yorumlayacağımıza dair somut bir örnek teşkil eder. Bu proje, daha karmaşık ve büyük ölçekli projelere geçiş için sağlam bir temel oluşturmaktadır.

---
