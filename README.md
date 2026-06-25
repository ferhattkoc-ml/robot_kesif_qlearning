<div align="center">

# 🤖 Autonomous Robot Navigation with Q-Learning

**GridWorld'de Pekiştirmeli Öğrenme ile Otonom Rota Bulma**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)
[![Reinforcement Learning](https://img.shields.io/badge/RL-Q%20Learning-FF6F00?style=for-the-badge&logo=python&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**5×5 GridWorld · 4 Aksiyon · 2 Engel · Bellman Güncellemesi ile Optimum Politika**

</div>

---

## 📌 Proje Hakkında

Bu proje, bir **Q-Learning** ajanının 5×5 GridWorld ortamında engellerden kaçınarak hedef duruma ulaşmayı öğrenmesini simüle eder. Ajan tam keşifle başlar ve **Bellman Denklemi** tabanlı Q-tablosu güncellemeleriyle kademeli olarak optimum rotayı keşfeder.

---

## 🗺️ Ortam Tasarımı

| Parametre | Değer |
|-----------|-------|
| **Grid Boyutu** | 5×5 (25 durum) |
| **Aksiyon Uzayı** | 4 (Yukarı, Aşağı, Sol, Sağ) |
| **Başlangıç** | (0, 0) |
| **Hedef** | (4, 4) |
| **Engeller** | (0,1), (1,3), (3,1), (3,3), (4,1) |

### GridWorld Görseli

![Grid Environment](images_grid.png)

---

## 🏆 Ödül Mekanizması

Küçük adım cezaları, ajanı mümkün olan en kısa yolu bulmaya iter.

| Olay | Ödül |
|------|------|
| 🎯 **Hedefe Ulaşma** | **+10** |
| 🧱 **Engele Çarpma** | −3 |
| 👣 **Standart Hareket** | −0.1 |

---

## 🧠 Q-Learning Konfigürasyonu

Keşif (exploration) ve sömürü (exploitation) dengesi **ε-greedy** stratejisi ile yönetilir.

| Hiperparametre | Değer | Açıklama |
|----------------|-------|----------|
| **α (Learning Rate)** | 0.1 | Yeni bilginin eski bilginin yerini alma oranı |
| **γ (Discount Factor)** | 0.99 | Gelecek ödüllerin bugünkü değere indirgenme katsayısı |
| **ε (Initial Epsilon)** | 1.0 | Başlangıçta tam keşif |
| **ε Decay** | 0.995 | Her episodda epsilon azalma çarpanı |
| **ε (Minimum)** | 0.1 | Minimum keşif oranı |

---

## 🧮 Q-Update Rule (Bellman Denklemi)

```
Q(s, a) ← Q(s, a) + α [ r + γ · maxₐ' Q(s', a') − Q(s, a) ]
```

| Değişken | Anlamı |
|----------|--------|
| `s` | Mevcut durum |
| `a` | Seçilen aksiyon |
| `r` | Alınan ödül |
| `s'` | Bir sonraki durum |
| `α` | Öğrenme oranı |
| `γ` | İndirim faktörü |

---

## 📈 Öğrenme Performansı

Eğitim ilerledikçe ajan rastgele keşiften optimize yol seçimine geçer.

![Learning Curve](learning_curve.png)

---

## ⚙️ Kullanım

```bash
# 1. Depoyu klonla
git clone https://github.com/ferhattkoc-ml/robot_kesif_qlearning.git
cd robot_kesif_qlearning

# 2. Sanal ortam oluştur (opsiyonel)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Çalıştır
python robot_kesif.py
```

---

## 🛠️ Tech Stack

| Kategori | Teknolojiler |
|----------|-------------|
| **Dil** | Python 3.8+ |
| **Hesaplama** | NumPy |
| **Görselleştirme** | Matplotlib |
| **RL Algoritması** | Q-Learning (tabular, ε-greedy) |

---

## 📂 Proje Yapısı

```
robot_kesif_qlearning/
├── robot_kesif.py                  # Ana Q-Learning uygulaması
├── images_grid.png                 # GridWorld ortam görseli
├── learning_curve.png              # Öğrenme eğrisi grafiği
├── requirements.txt                # Bağımlılıklar
└── README.md                       # Bu dosya
```

---

## 🧠 Öğrenilen Kavramlar

- ✅ **Q-Learning** — Model-free off-policy RL algoritması
- ✅ **Bellman Denklemi** — Optimal Q-değeri güncelleme
- ✅ **ε-greedy** — Keşif/sömürü dengesi stratejisi
- ✅ **GridWorld** — Tabular RL için temel benchmark ortamı
- ✅ **Policy Learning** — Durumdan aksiyona optimum haritalama

---

## 👤 Yazar

**Ferhat Koç** · [GitHub](https://github.com/ferhattkoc-ml) · [LinkedIn](https://linkedin.com/in/ferhattkocc/)

> ⭐ Bu projeyi beğendiyseniz bir yıldız bırakmayı unutmayın!

---

<div align="center">
  <sub>Built with ❤️ by Ferhat Koç</sub>
</div>
