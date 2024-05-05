# 📁 Dosya Yükleme ve İndirme Projesi

Bu Django projesi, dosya yükleme, listeleme, silme ve yeniden adlandırma işlemlerini gerçekleştirmek için tasarlanmıştır. Kullanıcılar bu web uygulaması aracılığıyla dosyalarını kolayca yönetebilirler.

https://github.com/Renanuya/django-file-project/assets/69991160/873793ed-3d17-4ec1-ba9c-070e084a3ad0

## 📋 İçindekiler
- [🚀 Kurulum](#-kurulum)
- [📄 Kullanım](#-kullanım)
- [⭐ Özellikler](#-özellikler)
- [🛠️ Teknolojiler](#️-teknolojiler)
- [🤝 Katılım](#-katılım)

## 🚀 Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/yourusername/fileUploadAndDownloadProject.git
   cd fileUploadAndDownloadProject
   ```

2. Sanal bir ortam oluşturun ve etkinleştirin:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # Linux/macOS
   myenv\Scripts\activate      # Windows
   ```

3. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Veritabanını oluşturun ve migrasyonları uygulayın:
   ```bash
   python manage.py migrate
   ```

5. Projeyi başlatın:
   ```bash
   python manage.py runserver
   ```

6. Tarayıcınızda `http://127.0.0.1:8000/` adresine giderek projeyi görüntüleyin.

## 📄 Kullanım

- **Dosya Yükleme**: Ana sayfada "Upload A New File" düğmesine tıklayarak yeni bir dosya yükleyin.
- **Dosya Silme**: Her dosya kartının altında bulunan "Delete" düğmesine tıklayarak bir dosyayı silebilirsiniz. Silme işlemi geri alınamaz.
- **Dosya Yeniden Adlandırma**: Her dosya kartının altında bulunan "Rename" düğmesine tıklayarak bir dosyanın adını değiştirebilirsiniz.

## ⭐ Özellikler

- Dosya yükleme ve saklama
- Dosya listeleme, silme ve yeniden adlandırma
- Kullanıcı dostu arayüz

## 🛠️ Teknolojiler

Bu projede aşağıdaki teknolojiler kullanılmıştır:

- **Django**: Web uygulama çatısı.
- **Bootstrap**: Arayüz tasarımı için CSS ve JS kütüphanesi.
- **SQLite**: Hafif veritabanı kullanılarak dosya kayıtları saklanır.
- **JavaScript**: Müşteri tarafı doğrulama ve etkinlikler için kullanılmıştır.

## 🤝 Katılım

- Bu depoyu çatallayın (fork) ve geliştirmelerinizi yapın.
- Yeni özellikler eklemek veya hataları düzeltmek için Pull Talepler (Pull Requests) gönderin.
- Hataları bildirmek veya önerilerde bulunmak için konu (issue) açın.
