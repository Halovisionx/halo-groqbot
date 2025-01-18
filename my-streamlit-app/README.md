# My Streamlit App

Bu proje, kullanıcıların etkileşimli veri görselleştirmeleri oluşturmasına olanak tanıyan bir Streamlit uygulamasıdır.

## Kurulum

Projenin çalışabilmesi için gerekli bağımlılıkları yüklemek için aşağıdaki adımları izleyin:

1. Bu depoyu klonlayın:
   ```
   git clone <repo-url>
   cd my-streamlit-app
   ```

2. Gerekli Python paketlerini yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Kullanım

Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

```
streamlit run src/app.py
```

Tarayıcınızda otomatik olarak açılacak olan uygulama arayüzü üzerinden etkileşimde bulunabilirsiniz.

## Proje Yapısı

- `src/app.py`: Uygulamanın giriş noktasıdır.
- `src/components/__init__.py`: Uygulamanın bileşenlerini içeren paket.
- `requirements.txt`: Proje için gerekli Python paketlerini listeler.