

# 🏥 Obezite Risk Tahmin Uygulaması

Makine öğrenmesi kullanarak bireylerin obezite riskini tahmin eden, React ve Python Flask tabanlı tam yığın bir web uygulamasıdır. Uygulama Vercel üzerinden dağıtılmıştır.

## 🚀 Özellikler

- **Yapay Zekâ Destekli Tahminleme**: Obezite veri seti üzerinde eğitilmiş Random Forest sınıflandırıcısı
- **Duyarlı Tasarım (Responsive Design)**: Masaüstü, tablet ve mobil cihazlarda sorunsuz çalışır
- **Gerçek Zamanlı Analiz**: Anında sağlık riski değerlendirmesi
- **Detaylı Açıklamalar**: Tahminlerin arkasındaki mantık açıkça belirtilir
- **Kişiselleştirilmiş Öneriler**: Kullanıcıya özel sağlık tavsiyeleri
- **Profesyonel Arayüz**: Modern, sağlık odaklı kullanıcı deneyimi

## 🛠️ Teknoloji Yığını

### Ön Yüz (Frontend)
- **React 18** _–_ Arayüz kütüphanesi
- **Vite** – Derleme aracı
- **Tailwind CSS** – Stil oluşturma
- **Axios** – API çağrıları
- **Prettier** – Kod biçimlendirme

### Arka Yüz (Backend)
- **Python 3.9+** – Çalışma zamanı
- **Flask** – Web çatısı
- **scikit-learn** – Makine öğrenmesi
- **pandas** – Veri işleme
- **numpy** – Sayısal hesaplama

### Dağıtım
- **Vercel** – Barındırma platformu
- **Sunucusuz Fonksiyonlar** – Arka uç dağıtımı

## 📦 Kurulum ve Yapılandırma

### Gereksinimler
- Node.js 18+ ve npm
- Python 3.9+
- Git

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/yourusername/obesity-prediction-app.git
cd obesity-prediction-app
```

### 2. Backend Kurulumu
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

# Ana dizine train.csv dosyanızı ekleyin. Şu sütunları içermelidir:
# ID, Age, Gender, Height, Weight, CALC, FAVC, FCVC, NCP, SCC, SMOKE, CH2O,
# family_history_with_overweight, FAF, TUE, CAEC, MTRANS, NObeyesdad

python app.py
```

### 3. Frontend Kurulumu
```bash
npm install
npm run dev
```

### 4. Uygulamaya Erişim
- Ön Yüz: http://localhost:5173
- Arka Yüz API: http://localhost:5000

## 🚀 Dağıtım (Deployment)

### Backend’i Vercel’e Dağıtmak

1. **Backend’i Hazırlayın**
```bash
mkdir obesity-backend
cd obesity-backend
cp ../app.py .
cp ../requirements.txt .
cp ../vercel.json .
cp ../train.csv .
```

2. **Vercel ile Dağıtım**
```bash
npm install -g vercel
vercel --prod
```

3. **Backend URL’nizi not alın** (örn. `https://your-backend-123.vercel.app`)

### Frontend’i Vercel’e Dağıtmak

1. **React Uygulamasında API URL’sini Güncelleyin**
```javascript
const API_URL = 'https://your-backend-123.vercel.app/api'
```

2. **Dağıtım**
```bash
npm run build
vercel --prod
```

## 📊 Veri Seti Gereksinimleri

`train.csv` şu sütunları içermelidir:
- `ID` – Benzersiz kimlik
- `Age` – Yaş (yıl)
- `Gender` – Erkek/Kadın
- `Height` – Boy (cm)
- `Weight` – Kilo (kg)
- `CALC` – Kalori tüketim takibi (yes/no)
- `FAVC` – Yüksek kalorili besin tüketimi (yes/no)
- `FCVC` – Sebze tüketim sıklığı (1-3)
- `NCP` – Ana öğün sayısı (1-4)
- `SCC` – Ara öğün tüketimi (no/Sometimes/Frequently/Always)
- `SMOKE` – Sigara kullanımı (yes/no)
- `CH2O` – Günlük su tüketimi (1-3)
- `family_history_with_overweight` – Ailede fazla kilo geçmişi (yes/no)
- `FAF` – Fiziksel aktivite sıklığı (0-3)
- `TUE` – Teknoloji kullanımı süresi (0-2)
- `CAEC` – Alkol tüketimi (no/Sometimes/Frequently/Always)
- `MTRANS` – Ulaşım türü (Walking/Public_Transportation/Automobile/Bike)
- `NObeyesdad` – Hedef değişken (obezite seviyesi)

## 🔧 Yapılandırma

### Ortam Değişkenleri

**Backend (.env)**
```
FLASK_ENV=production
MODEL_PATH=obesity_model.pkl
```

**Frontend (.env)**
```
VITE_API_URL=https://your-backend-url.vercel.app/api
```

## 🧪 Test Süreci

### Backend Testleri
```bash
curl http://localhost:5000/api/health

curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 25, "gender": "Male", "height": 175, "weight": 70, ...}'
```

### Frontend Testleri
```bash
npm run dev
npm run build
npm run preview
```

## 📱 API Uç Noktaları

### GET /api/health
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### POST /api/predict
```json
{
  "prediction": "Normal_Weight",
  "confidence": 85.3,
  "explanation": ["Vücut kitle indeksiniz normal aralıkta", "..."],
  "bmi": 22.9,
  "risk_level": "Low",
  "recommendations": ["Sağlıklı alışkanlıklara devam edin", "..."]
}
```

## 🤝 Katkıda Bulunmak

1. Repoyu çatallayın (fork)
2. Yeni bir dal (branch) oluşturun
3. Gerekli değişiklikleri yapın
4. Testlerinizi ekleyin
5. Pull Request gönderin

## 📄 Lisans

Bu proje MIT Lisansı kapsamında lisanslanmıştır – Detaylar için `LICENSE` dosyasına bakınız.

## 🙏 Teşekkürler

- Veri sağlayıcılarına
- scikit-learn geliştirici topluluğuna
- React ve Flask topluluklarına
- Vercel platformuna

---

**⚠️ Tıbbi Uyarı**: Bu uygulama yalnızca eğitim ve araştırma amaçlıdır. Tıbbi teşhis veya tedavi için sağlık uzmanlarına başvurulmalıdır.


# 🏥 Obesity Risk Prediction App - Sprint 1 Detaylı Rapor ve Belgelendirme

> Google Yapay Zekâ ve Teknoloji Akademisi | Grup 179 | Sprint 1 Dönemi: 24 Haziran - 6 Temmuz 2025  
> Proje Sahipleri: **Atalay Aygül**, **Özkan Bırak**  
> Scrum Master: **Özkan Bırak**  
> Takım Üyeleri: Gökhan Mutlu, Oğuzhan Memiş, Fatmanur Şahin  

---

## 📌 Her Sprint Sonunda Beklenen Öğeler

Sprint sürecimiz, Google YZTA tarafından belirtilen şu yapılandırmalar etrafında şekillendirilmiştir:

- 📝 **Sprint Notları**  
- 📊 **Tahmin Edilen ve Tamamlanan Puanlar**  
- 🧠 **Tahmin Mantığı**  
- 🗓️ **Daily Scrum Günlükleri**  
- 🗂️ **Sprint Board Güncellemeleri**  
- 🖼️ **Screenshot'lar**  
- 🧪 **Sprint Review**  
- 🎯 **Sprint Retrospective**

---

## 📘 Ürün Tanımı

**Obesity Risk Prediction App**, bireylerin sağlık verilerine dayanarak obezite riskini makine öğrenmesi modelleriyle tahmin etmeyi amaçlayan, yapay zekâ destekli bir tam yığın (full-stack) web uygulamasıdır.

---

## 🔍 Ürün Özellikleri

- **🔬 Yapay Zekâ ile Tahminleme:** Random Forest modelini temel alır.
- **⚡ Gerçek Zamanlı Sonuçlar:** Kullanıcının form girdileriyle anlık sonuç verir.
- **💬 Tahmin Açıklamaları:** SHAP/LIME gibi araçlarla karar şeffaflığı.
- **🧠 Sağlık Tabanlı Tavsiyeler:** Kişiselleştirilmiş sağlık önerileri.
- **📱 Mobil Uyumlu:** Responsive tasarım, modern kullanıcı arayüzü.

---

## 🎯 Sprint 1 – Planlama ve Süreç

### 🗓️ Sprint Süresi:
- **Başlangıç:** 24 Haziran 2025
- **Bitiş:** 6 Temmuz 2025
- **Süre:** 2 Hafta

### ✅ Sprint Hedefleri:
- Veri seti analizi ve temizliği
- Proje klasör mimarisi kurulumu
- React ve Flask bazlı temel sistem kurulumu
- Versiyon kontrol entegrasyonu (GitHub)
- İlk API yapılandırmaları ve arayüz prototipi

---

## 📈 Sprint Tahmin Puanları

| User Story | Açıklama | Puan |
|------------|----------|------|
| Veri Temini | Kaggle üzerinden veri indirme | 3 |
| Ön İşleme | Encoding, null temizleme | 5 |
| Model Entegrasyonu | RandomForest modelinin eğitilmesi | 8 |
| Frontend Prototip | React bileşenlerinin ilk kurulumu | 5 |
| Backend Setup | Flask ile API başlatılması | 5 |
| Docker & Vercel Yapılandırması | Temel CI/CD entegrasyonu | 5 |
| GitHub Yapılandırması | README, .gitignore, yapı kurulumu | 4 |
| Notion + Scrum Günlükleri | Daily Scrum kayıtları | 2 |
| Toplam |  | **37 SP** |

### 🎯 Gerçekleşen: 35 SP tamamlandı  
> Docker deployment kısmı eksik kaldı ve Sprint 2’ye devredildi.

---

## 🧠 Tahmin Mantığı

Tahmin puanlaması, Scrum Poker ile aşağıdaki kriterlere göre yapılmıştır:

- Görevin teknik karmaşıklığı
- Zaman tahmini
- Ekip deneyimi
- Dış bağımlılıklar (örneğin Vercel kurulumu vs.)

---

## 🗓️ Daily Scrum Günlükleri

- Her gün saat **21:00**'de Google Meet üzerinden toplantı gerçekleştirildi.
- Notlar **Notion** üzerinden tutuldu.
- Günlük toplantılarda 3 temel soru yanıtlandı:
  1. Dün ne yaptım?
  2. Bugün ne yapacağım?
  3. Karşılaştığım engeller nelerdir?

---

## 📌 Sprint Board ve Güncellemeler

- Airtable üzerinden **Kanban board** kullanıldı.
- Her görev; "Kategorize Edilmemiş", "Yapılacak", "Devam Ediyor", "Bitti" sütunlarıyla izlenmiştir.

🔗 [Airtable Kanban Tablomuz](https://airtable.com/invite/l?inviteId=invGHsXUc6IiFsVk0)

---

## 📸 Screenshotlar

### 📍 Sprint Board
![Kanban Board](https://drive.google.com/uc?export=view&id=18CWY_AznkcXN7mXoZUiWjtSCVUtd-ILN)

![Sprint Beklentileri Görseli](https://drive.google.com/uc?export=view&id=1LwzKu1Ux81Qd6dbsQ5s1lCN_sUlVcyhX)

---

## ✅ Sprint Review

### Tamamlananlar:

- Kaggle veri seti indirildi ve analiz edildi.
- Flask backend ile tahmin API'si yazıldı.
- React arayüzü oluşturuldu, form tasarımı başlatıldı.
- Kategorik veriler encode edildi.
- GitHub kurulumu tamamlandı ve versiyon kontrol başladı.

---

## 🔍 Sprint Retrospective

| Zorluk | Açıklama |
|--------|----------|
| Özellik Anlamı | CAEC, SCC gibi değişkenler domain bilgisi gerektiriyor. |
| Şeffaflık | Model yorumlanabilirliğini artırmak için SHAP/LIME entegrasyonu Sprint 2'ye bırakıldı. |
| Ortam Sorunu | Python paket sürümleri arasında uyumsuzluk yaşandı. Çözüldü. |

### ✨ Öğrenilenler

- Feature engineering süreci çok kritik.
- Basit arayüz bile kullanıcı deneyiminde fark yaratıyor.
- GitHub üzerinden yapılan atomik commit'ler ileride ciddi fayda sağlıyor.

---

## 🧭 Bir Sonraki Sprint Planı (Sprint 2)

| Hedef | Detay |
|-------|-------|
| XGBoost ve LightGBM entegrasyonu | Model başarımını artırmak için |
| SHAP ve LIME | Tahmin açıklamalarının görselleştirilmesi |
| Test Otomasyonu | GitHub Actions ile pipeline kurulumu |
| Kullanıcı Geri Bildirimi | Prototip testlerine başlamak |

---

## 📂 Klasör Yapısı

```
OBESITYRISKPREDICTIONAPP/
|
├── ap.py
├── index.html
├── nginx.conf
├── package.json
├── requirements.txt
├── vite.config.json
├── vercel.json
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── .gitignore
|
├── data/
│   ├── train.csv
│   └── train (1).csv
│
├── src/
│   ├── App.css
│   └── App.jsx
│
└── README.md
```

---

## 🛡️ Etik ve Güvenlik Notu

- Tahminler yalnızca **eğitim ve araştırma** amaçlıdır.
- **Tıbbi tavsiye yerine geçmez**.
- Veri gizliliği ve kullanıcı güvenliği en önemli önceliklerden biridir.

---

## 🧠 Katılımcı Durumu

| Takım Üyesi | Katılım |
|-------------|---------|
| Atalay Aygül | ✅ Aktif |
| Özkan Bırak | ✅ Aktif |
| Gökhan Mutlu | ⛔ Katkı Sağlamadı |
| Oğuzhan Memiş | ⚠️ Sınırlı |
| Fatmanur Şahin | ⛔ Katkı Sağlamadı |

---

## 📜 Lisans

MIT License - Ayrıntılar için `LICENSE` dosyasına bakınız.

---

