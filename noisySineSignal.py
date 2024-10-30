import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data

#wavelet filtresi ile filtrelenmiş sinyal

num_points = 1000
x = np.linspace(0, 10, num_points)
signal = np.sin(x)
noise = np.random.normal(0, 0.5, num_points)
noisy_signal = signal + noise

#gürültü gidermek için
dalgacık = 'db6'
coeffs = pywt.wavedec(noisy_signal,dalgacık,level=7)


seviye = np.median(np.abs(coeffs[-1])) / 0.66 # gürültüyü tahmin eder
esik_deger = seviye * np.sqrt(2*np.log(len(noisy_signal))) # eşik değeri bulur

#  Yüksek frekanslı dalgacık katsayılarını eşikleme işlemiden sonra oluşan yeni katsayıların listler.
denoised_coeffs = list(map(lambda x: pywt.threshold(x, esik_deger, mode='hard'), coeffs))

# gürültü filtrelenmiş sinyali elde eder
filtered_signal = pywt.waverec(denoised_coeffs, dalgacık)


plt.figure(figsize=(10, 6))
plt.plot(x, signal, label="Orijinal Sinyal")
plt.plot(x, noisy_signal, label="Gürültülü Sinyal", color = 'orange', alpha=0.6)
plt.plot(x,filtered_signal, label = "filtrelenmiş sinyal", color = 'blue', alpha = 0.6)
plt.legend()
plt.xlabel("Zaman")
plt.ylabel("Genlik")
plt.title("Orijinal, Gürültülü ve Filtrelenmiş Sinyal")
plt.show()
