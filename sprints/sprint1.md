# Sprint 1 Raporu – Obezite Risk Tahmin Uygulaması

**Proje Adı:** Obesity Risk Prediction App  
**Sprint Numarası:** 1  
**Sprint Süresi:** 24 Haziran 2025 – 6 Temmuz 2025  
**Sprint Süresi:** 2 hafta  
**Sprint Takımı:** Google YZTA Group 179  
**Sprint Sahibi:** Atalay Aygül ve Özkan Bırak  
**Scrum Master:** Özkan Bırak  
**Sprint Hedefi:** Veri setinin toplanması, ön işlenmesi ve proje yapısının temellerinin oluşturulması.

---

## 🎯 Sprint 1 Hedefleri

Bu sprintte aşağıdaki hedeflerin gerçekleştirilmesi planlanmıştır:

- 📥 Obezite ile ilişkili yaşam tarzı ve fiziksel özellikleri içeren veri setinin toplanması ve incelenmesi  
- 🧹 Verinin temizlenmesi, eksik değerlerin işlenmesi ve uygun şekilde dönüştürülmesi  
- 📁 Proje klasör yapısının oluşturulması ve GitHub üzerinden versiyon kontrolünün başlatılması  
- 📄 İlk bulguların ve kararların belgelenmesi

---

## ✅ Tamamlanan İşler

| Görev | Açıklama | Durum |
| --- | --- | --- |
| Veri Seti Toplama | Kaggle üzerinden obezite veri seti indirildi ve `data/` klasörüne yerleştirildi. | ✅ Tamamlandı |
| Veri Setlerinin Birleştirilip Kategorik Sütunların Encode Edilmesi | Veri setleri birleştirilerek daha geniş ve çeşitli bir örneklem elde edildi. Ardından, makine öğrenmesi modellerinin çalışabilmesi için kategorik sütunlar sayısal değerlere dönüştürüldü (encoding). | ✅ Tamamlandı |
| GitHub Yapılandırması | `README.md`, `requirements.txt` ve src klasörleri oluşturuldu. Versiyon kontrolü başlatıldı. | ✅ Tamamlandı |

Kanban Tablosu: [Google Drive](https://drive.google.com/file/d/18CWY_AznkcXN7mXoZUiWjtSCVUtd-ILN/view?usp=sharing)

---

## 📈 Teknik Bulgular ve Gözlemler

- Veri seti 17 özellik ve 1 hedef değişkenden oluşmaktadır. Hedef değişken 7 sınıflı kategorik bir değişkendir (Underweight, Normal Weight, Obesity Type I, vb.).
- Fiziksel aktivite, fast food tüketimi ve su içme alışkanlıkları gibi değişkenler hedef değişkenle yüksek korelasyon göstermektedir.

---

## ✨ Sprint Retrospective

## 🧩 Karşılaşılan Zorluklar

| Zorluk | Açıklama |
| --- | --- |
| 🧪 Özellik Mühendisliği | Bazı değişkenlerin (ör. `CAEC`, `SCC`) anlamları açık değildir ve domain bilgisi gerektirmektedir. Bu değişkenlerin etkili kullanımı için daha fazla analiz yapılması gerekmektedir. |
| 🛠️ Model Yorumlanabilirliği | Sağlık alanında kullanılacak bir modelin kararlarının açıklanabilir olması önemlidir. Bu nedenle SHAP ve LIME gibi araçların entegrasyonu sonraki sprintte planlanmaktadır. |
| 📦 Ortam Uyumsuzlukları | Bazı kütüphane sürümleri arasında uyumsuzluk yaşanmıştır. `requirements.txt` dosyası güncellenerek bu sorun giderilmiştir. |

---

## 📚 Öğrenilen Dersler

- Basit modeller bile doğru ön işleme ile yüksek performans gösterebilir. Ancak yorumlanabilirlik ve genelleme yeteneği için daha gelişmiş modeller gereklidir.
- GitHub üzerinden düzenli commit ve açıklayıcı mesajlar, takım içi iş birliğini kolaylaştırmaktadır.
- EDA süreci, modelleme öncesi veri hakkında sezgisel bilgi edinmek için vazgeçilmezdir.

---

## 📌 Sonraki Sprint için Önerilen Adımlar

| Görev | Açıklama |
| --- | --- |
| 🧠 Yeni Modeller | XGBoost, LightGBM ve SVM gibi daha gelişmiş modeller test edilecek. |
| 🧰 Açıklanabilirlik | SHAP ve LIME gibi araçlarla model kararları görselleştirilecek. Özellikle sağlık alanında bu adım kritik öneme sahiptir. |
| 🧪 Test Otomasyonu | Notebook'ların test edilebilir hale getirilmesi ve CI/CD entegrasyonu için GitHub Actions yapılandırılacak. |
| 📄 Belgeler | `README.md` dosyası genişletilecek, kullanım kılavuzu ve model açıklamaları eklenecek. |

---

## 📂 Mevcut Depo Yapısı

```
OBESITYRISKPREDICTIONAPP/
│
├── docs/
│   ├── sprint-1/
│   │   ├── Sprint_1_Review.md
│   │   ├── Sprint_1_Retrospective.md
│   │   └── Sprint_1_Report.md
│   └── README_Docs.md
│
├── data/
│   ├── train.csv
│   └── train (1).csv
│
├── src/
│   ├── App.css
│   ├── App.jsx
│   ├── ap.py
│   ├── index.html
│   ├── nginx.conf
│   ├── package.json
│   ├── requirements.txt
│   ├── vite.config.json
│   ├── vercel.json
│   ├── docker-compose.yml
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── .gitignore
│
├── README.md
```

---

## 📌 Ek Notlar

- Proje, sağlık alanında kullanılacağı için etik sorumluluklar göz önünde bulundurulmalıdır. Modelin yanlış tahminleri ciddi sonuçlar doğurabilir.
- Kullanıcı arayüzü geliştirilirken kullanıcı gizliliği ve veri güvenliği ön planda tutulmalıdır.
- Modelin farklı yaş grupları ve cinsiyetler üzerindeki performansı ayrı ayrı değerlendirilecektir.

## Kanban Tablomuz

Kanban tablomuza [[bu](https://airtable.com/invite/l?inviteId=invGHsXUc6IiFsVk0&inviteToken=c14ed47856b30a163c7e14f6fad6487a7b1323b5bb430540083641b6b84a9e7a&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts)] linkten ulaşabilirsiniz.