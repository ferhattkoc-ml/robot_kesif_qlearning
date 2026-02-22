# 🤖 Q-Learning ile Robot Keşfi (Gridworld Navigation)

Bu proje, 5x5 boyutunda bir ızgara (grid) ortamında bulunan bir robotun, engellere çarpmadan başlangıç noktasından hedefe ulaşmayı kendi kendine öğrendiği bir Pekiştirmeli Öğrenme (Reinforcement Learning) uygulamasıdır. Ajan, ortamı keşfetmek ve en ideal yolu bulmak için **Q-Learning** algoritmasını kullanmaktadır.

## 📌 Proje Detayları ve Ortam (Environment)

* **Durum Uzayı (State Space):** 5x5 Grid (Toplam 25 durum)
* **Eylem Uzayı (Action Space):** 4 (Yukarı, Aşağı, Sağa, Sola)
* **Başlangıç Noktası:** `(0, 0)`
* **Hedef Noktası:** `(4, 4)`
* **Engeller:** `(0,1), (1,3), (3,1), (3,3), (4,1)`

### 🏆 Ödül Mekanizması (Reward System)
Ajanın öğrenme sürecini yönlendiren ödül sistemi şu şekildedir:
* **Hedefe Ulaşma:** `+10` puan
* **Engele Çarpma:** `-3` puan
* **Standart Adım:** `-0.1` puan

## 🧠 Kullanılan Algoritma ve Parametreler

Ajan, deneyimlerinden öğrenmek için model-free bir algoritma olan Q-Learning'i kullanır. Keşfetme ve sömürme (exploration vs. exploitation) dengesi, azalan epsilon (epsilon-decay) stratejisi ile sağlanmıştır.

* **Öğrenme Oranı (Alpha - $\alpha$):** 0.1
* **İndirim Faktörü (Gamma - $\gamma$):** 0.99
* **Başlangıç Epsilon Değeri:** 1.0
* **Epsilon Azalma Oranı (Decay):** 0.995

### 🧮 Q-Tablosu Güncelleme Kuralı
Ajan, her adımda Q-değerlerini aşağıdaki Bellman Denklemi temelli matematiksel formüle göre günceller:

$$Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

* $s$: Mevcut durum
* $a$: Seçilen eylem
* $r$: Alınan ödül
* $s'$: Sonraki durum
* $\alpha$: Öğrenme oranı
* $\gamma$: İndirim faktörü

## 📈 Sonuçlar ve Öğrenme Eğrisi (Learning Curve)

Ajan ilk bölümlerde (episodes) ortamı tamamen rastgele keşfederken (exploration) ve sık sık engellere çarparken, bölümler ilerledikçe Q-tablosunu güncelleyerek hedefe giden optimal yolu öğrenmiştir (exploitation). 

Aşağıdaki grafik, ajanın eğitim süresi boyunca her bölümde topladığı toplam ödül miktarını göstermektedir:

![Öğrenme Eğrisi](learning_curve.png) 

*(Not: Bu grafiği elde etmek için `matplotlib` kütüphanesi kullanılmıştır.)*

## 🚀 Kurulum ve Kullanım

Projeyi kendi bilgisayarında çalıştırmak için aşağıdaki adımları izleyebilirsin:

1. Repoyu klonlayın:
   ```bash
   git clone [https://github.com/ferhattkoc-ml/robot-kesif-qlearning.git](https://github.com/ferhattkoc-ml/robot-kesif-qlearning.git)
