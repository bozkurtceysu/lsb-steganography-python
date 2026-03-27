# -*- coding: utf-8 -*-

LSB Steganografi Uygulaması Geliştirici: [Ceysu/bozkurtceysu]

import cv2
import numpy as np

# 1. Metni 1 ve 0'lar haline getiren yardımcı fonksiyon
def metni_binary_yap(metin):
    return ''.join([format(ord(i), "08b") for i in metin])

# 2. Veri Gömme Fonksiyonu
def manuel_lsb_gomme(resim_yolu, gizli_mesaj, cikti_yolu):
    resim = cv2.imread(resim_yolu)

    # GÜVENLİK KONTROLÜ
    if resim is None:
        print(f"HATA: '{resim_yolu}' dosyası bulunamadı! ")
        return

    gizli_mesaj += "#####" # Bitiş ayırıcısı
    binary_mesaj = metni_binary_yap(gizli_mesaj)

    duz_resim = resim.flatten()

    # Her bir mesaj bitini, pikselin son bitine (LSB) yaz
    for i in range(len(binary_mesaj)):
        duz_resim[i] = (duz_resim[i] & 254) | int(binary_mesaj[i])

    stego_resim = duz_resim.reshape(resim.shape)
    cv2.imwrite(cikti_yolu, stego_resim)
    print("Başarılı: Mesaj resmin içine gömüldü ve kaydedildi!")

# 3. Veri Çıkarma Fonksiyonu
def manuel_lsb_cikarma(stego_resim_yolu):
    resim = cv2.imread(stego_resim_yolu)

    if resim is None:
        print(f"HATA: '{stego_resim_yolu}' dosyası bulunamadı!")
        return ""

    duz_resim = resim.flatten()

    # Piksellerin sadece son bitlerini (LSB) al
    lsb_bitleri = duz_resim & 1
    binary_veri = "".join([str(bit) for bit in lsb_bitleri])

    cozulen_mesaj = ""
    for i in range(0, len(binary_veri), 8):
        byte = binary_veri[i:i+8]
        cozulen_mesaj += chr(int(byte, 2))
        if cozulen_mesaj[-5:] == "#####": # Ayırıcıyı bulduğunda dur
            break

    return cozulen_mesaj[:-5]

    # 4. Matematiksel Kalite Ölçüm (PSNR/MSE) Fonksiyonu
def mse_psnr_hesapla(orijinal_yol, stego_yol):
    orijinal = cv2.imread(orijinal_yol)
    stego = cv2.imread(stego_yol)

    if orijinal is None or stego is None:
        print("HATA: Kalite ölçümü için resimler okunamadı!")
        return

    # Saf NumPy tabanlı MSE ve PSNR hesabı
    mse = np.mean((orijinal.astype(np.float64) - stego.astype(np.float64)) ** 2)

    if mse == 0:
        psnr = float('inf')
    else:
        psnr = 10 * np.log10((255 ** 2) / mse)

    print(f"MSE Değeri : {mse:.6f}")
    print(f"PSNR Değeri : {psnr:.2f} dB")

# TEST KISMI

print("--- Steganografi Testi Başlıyor ---")

# Veriyi Gömelim
manuel_lsb_gomme("IMG_8045.JPG", "LSB Steganografi Testi!", "stego_test.png")

# Veriyi Geri Çıkaralım
bulunan_mesaj = manuel_lsb_cikarma("stego_test.png")
print(f"Resimden Çıkarılan Gizli Mesaj: {bulunan_mesaj}")

# Kaliteyi Ölçelim
print("\n--- Matematiksel Kalite Ölçümü ---")
mse_psnr_hesapla("IMG_8045.JPG", "stego_test.png")
