# Turkish-live-sign-language-detection-and-subtitle-application.
türkçe : 
Bu kod, canlı olarak görüntüdeki işaretleri algılayıp bunları altyazıya döken bir programı gerçekleştirmektedir. İşaret dili harflerini tanımak için "turk-isaret-dili-alfabesi-1.gif" adlı görseli kullanabilirsiniz. Program, 0.5 ve üzeri doğruluk değerine sahip olan harfleri algılar ve bu harfleri alt yazı bölümüne ekler. Eğer aynı harf birden fazla kez tespit edilirse, sadece bir kez alınır ve diğerleri yok sayılır.

Kod dosyası ve ağırlık dosyası bulunmaktadır. YOLOv5 ağırlık dosyası, Kaggle'daki "TR Sign Language" veri seti kullanılarak eğitilmiştir. Kod, kamera üzerinde çalışacak şekilde tasarlanmıştır. Kodu düzgün bir şekilde çalıştırmak için ağırlık dosyasının ve kodun aynı klasörde olduğundan emin olunmalıdır.

Kod çalıştırıldıktan sonra, ek olarak klasöre koyduğunuz bir resimden istediğiniz harfi deneyerek tespit yapabilirsiniz. Kodun daha iyi çalışması için siyah bir arka plan kullanmanız önerilir. Metni daha akıcı bir şekilde göstermek için bazı düzenlemeler yapılabilir.

Not: Kodun doğru bir şekilde çalışabilmesi için numpy, cv2 ve torch kütüphanelerinin yüklü olması gerekmektedir. Gerekli kütüphaneleri yüklediğinizden emin olun.

Torch versiyonu: 2.0.0+cpu
NumPy versiyonu: 1.24.3
OpenCV versiyonu: 4.7.0

english :

Here , a program has been developed that will detect the signs in the live video and translate them into subtitles . You can view the image named turk-isaret-dili-alphabesi-1.gif to see the used sign language letters. The program takes the letter it sees with an accuracy of over 0.5 and adds it to the subtitle section. 
If a letter is detected more than once, take it only once and the rest is ignored. There is a code file and a weight file. The yolov5 weight file was created by training the yolov5 dataset on kaggle https://www.kaggle.com/datasets/berkaykocaoglu/tr-sign-language. 

The code file is running on the camera . The code page must be run, keeping in mind that the weight file and the code must be in the same folder to run the code properly.

After the code is run, you can determine the letter you want from the picture that is added to the folder by trying it. Try using black background for code to work better.

Torch version: 2.0.0+cpu
NumPy version: 1.24.3
OpenCV version: 4.7.0



# program output :


https://github.com/ilyasdemir-demirilyas/Turkish-live-sign-language-detection-and-subtitle-application./assets/80126067/2044ec76-81fc-4530-add3-ec342ed33a22

