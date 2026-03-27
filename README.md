# lsb-steganography-python
Image steganography using LSB (Least Significant Bit) technique implemented in Python

# English
 # Description
This project implements image steganography using the Least Significant Bit (LSB) technique in Python.
It allows hiding secret text messages inside images and extracting them back without noticeable visual distortion. Additionally, the project evaluates image quality using MSE (Mean Squared Error) and PSNR (Peak Signal-to-Noise Ratio) metrics.

 # How It Works
 The input message is converted into binary format
 Each bit of the message is embedded into the least significant bits of image pixels
 A delimiter (#####) is used to mark the end of the hidden message
 During extraction, LSB bits are read and converted back into characters


# Features
 Hide secret messages inside images
 Extract hidden messages from images
 Automatic message termination using delimiter
 Image quality analysis using MSE and PSNR
 Simple and efficient NumPy-based implementation

# Technologies Used
Python
OpenCV (cv2)
NumPy


 # Quality Metrics
 MSE (Mean Squared Error): Measures the difference between original and stego image
 PSNR (Peak Signal-to-Noise Ratio): Measures image quality (higher is better)


# Türkçe
# Açıklama
Bu proje, Python kullanarak En Önemsiz Bit (LSB - Least Significant Bit) tekniği ile görüntüler içerisine gizli veri saklama ve bu veriyi geri çıkarma işlemlerini gerçekleştirmektedir.
Ayrıca proje, orijinal ve stego görüntü arasındaki farkı ölçmek için MSE (Ortalama Kare Hata) ve PSNR (Tepe Sinyal-Gürültü Oranı) hesaplamalarını da içermektedir.


  # Nasıl Çalışır?
 Gizli mesaj binary (ikili) formata dönüştürülür
 Mesajın her biti, piksel değerlerinin en önemsiz bitine (LSB) yazılır
 Mesaj sonuna ##### ayırıcı eklenir
 Çözme işleminde bu ayırıcıya kadar veri okunur

 
# Özellikler
 Görüntü içine gizli mesaj gömme
 Gizli mesajı görüntüden çıkarma
 Otomatik mesaj sonlandırma (delimiter)
 MSE ve PSNR ile kalite analizi
 NumPy tabanlı verimli implementasyon

# Kullanılan Teknolojiler
 Python
 OpenCV (cv2)
 NumPy

 # Kalite Ölçümleri
 MSE: Orijinal ve stego görüntü arasındaki farkı ölçer
 PSNR: Görüntü kalitesini ölçer (yüksek olması daha iyidir



