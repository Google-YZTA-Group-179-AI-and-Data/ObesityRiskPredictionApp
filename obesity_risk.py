# -*- coding: utf-8 -*-
# Spyder IDE
"""
YZTA - BOOTCAMP 2025

Multi-Class Prediction of Obesity Risk




VERİ SETİ HAKKINDA BİLGİ
________________________

Anket soruları ve insanların temel fiziksel özelliklerden yararlanılarak,
kişilerin kilo durumuna yönelik sağlık sınıflandırması yapılmaya çalışılmış.


Çoğu kategorik olmak üzere 16 adet özellik değişkeni, ve 1 adet hedef değişken bulunuyor.


Tüm sütunların anlamları şu şekilde:
    
FAF:                              haftada yapılan fiziksel aktivite süresi (saat)    
CALC:                             Alkol tüketimi sıklığı (`Never`: Hiç, `Sometimes`: Bazen, `Frequently`: Sık sık, `Always`: Her zaman) 
Age:                              Yaş
CAEC:                             Ana öğünler dışında yemek yeme sıklığı (`No`: Hayır, `Sometimes`: Bazen, `Frequently`: Sık sık, `Always`: Her zaman) 
Gender:                           Cinsiyet                                                 
FCVC:                             Sebze tüketim sıklığı (0-3 arası, genellikle 1: az, 2: orta, 3: çok)
Weight:                           Kilo (kg)                                                                       
SMOKE:                            Sigara kullanımı (`yes`: Evet, `no`: Hayır)                                               
TUE:                              Günlük teknoloji kullanımı süresi (saat)          
CH2O:                             Günlük su tüketimi (litre)                                                      
family_history_with_overweight :  Ailede obezite öyküsü (`yes`: Evet, `no`: Hayır)                               
MTRANS:                           Günlük ulaşım şekli (`Public_Transportation`: Toplu taşıma, `Walking`: Yürüyüş, `Automobile`: Araba, `Motorcycle`: Motosiklet, `Bike`: Bisiklet)
*NObeyesdad :                     Hedef değişken. Kilo ve obezite durumunu sınıflandıran 7 farklı düzey
Height:                           Boy (metre)                                                                     
SCC:                              Günlük kalorili içecek tüketimi (`yes`: Evet, `no`: Hayır)                                
NCP:                              Günlük ana öğün sayısı (ör: 1, 2, 3, 4)                                                   
FAVC:                             Yüksek kalorili yiyecek tüketimi (`yes`: Evet, `no`: Hayır)                               



Kategorik halde bırakılmış olan 9 adet sütun;
CALC, CAEC, Gender, SMOKE, family_history_with_overweight, MTRANS, 
NObeyesdad, SCC, ve FAVC değişkenleri "label encoding" ile dönüştürülerek veri seti hazırlanmış.

FCVC ve NCP de düşünüldüğünde, aslında tüm sütunların 11 tanesinin kategorik, 
6 tanesinin nümerik olduğunu görmek mümkün. 

Değerlerin çoğunlukla float yerine integer olduğunu görüyoruz.



Hedef değişkeni ve sınıfların anlamları:
    
    0 = Insufficient_Weight
    1 = Normal_Weight
    2 = Obesity_Type_I
    3 = Obesity_Type_II
    4 = Obesity_Type_III
    5 = Overweight_Level_I
    6 = Overweight_Level_II


"""




#%% 1) Import


import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt



myframe = pd.read_csv("merged_obesity_data.csv")



myframe.head()

myframe.info()  

myframe.describe() 

stats = myframe.describe()  # istatistikler stats değişkeni içerisinde

myframe.nunique()



"""
Veri setindeki değerlerin bazı temel özelliklerini kısaca inceledik.


** 6. sütun olan FCVC değişkeninde, tanımıyla alakasız ve çok absürt yüksek değerler var.
   Bunun sebebi araştırılmalı.


** hedef değişkenimiz "NObeyesdad" 13. sütun (12)
"""



#%% 2) Train-test setlerini hazırlama

import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


myarray = myframe.to_numpy()  # pandas formatından numpy formatına çevirdik


x = myarray                  # Özellik (feature) sütunları
x = np.delete(x, 12, axis=1) # hedef sütunu silindi
x = np.delete(x, 5, axis=1) # FCVC sütunu silindi


y = myarray[:,12]            # hedef değişkeni


# Eğitim ve test verilerinin hazırlanması
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)




#%% 3) Spesifik model eğitimleri 1: KNN


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix, precision_score
from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve
from sklearn.model_selection import GridSearchCV



mymodel = KNeighborsClassifier() # Sınıflandırma modeli



'''
Modelin muhtemel en iyi parametre kombinasyonunu bulmak için, yani optimizasyonu için Grid Search kullanabiliriz.
Seçilen modelin parametreleri için gerekli listeler hazırlanır, sonra Grid Search fonksiyonu ayarlanır.
İlk başta basit ve genel sayı aralığı verilip, daha sonra ilerledkçe parametre değerleri değiştirilir.
GridSearchCV fonksiyonu kendi içinde Çapraz-Doğrulama da yapar.
'''



# parameter grid
param_grid = {
    'n_neighbors': [3, 5, 6, 7, 8, 9, 10, 15 ],  # Number of neighbors to use
    'weights': ['uniform', 'distance'],  # Weight function used in prediction
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],  # Algorithm used to compute the nearest neighbors
    'leaf_size': [10, 15, 20, 25, 30, 35, 40, 50],  # Leaf size passed to BallTree or KDTree
    'metric': ['euclidean', 'manhattan', 'minkowski'],  # Distance metric to use
}



grid_search = GridSearchCV(mymodel, param_grid, cv=5, n_jobs=-1, verbose=0, scoring='accuracy')


grid_search.fit(x_train, y_train)



# En iyi model alınır
best_model = grid_search.best_estimator_



# Test verisinin sonuçları için metrikler hesaplanır---------------------------------------
print("\nTest Data Metrics")
test_predictions = best_model.predict(x_test)

s1 = accuracy_score(y_test, test_predictions)  
s2 = f1_score(y_test, test_predictions, average='weighted')
s3 = recall_score(y_test, test_predictions, average='weighted')
s4 = precision_score(y_test, test_predictions, average='weighted')  

print(f"Test Accuracy: {s1 * 100:.2f}%")  
print(f"Test F1 Score: {s2 * 100:.2f}%")
print(f"Test Recall: {s3 * 100:.2f}%")
print(f"Test Precision: {s4 * 100:.2f}%")


# Karışıklık Matrisi hangi sınıfların nasıl tahmin edildiğini gösterir
cm_test = confusion_matrix(y_test, test_predictions)  
print("\nConfusion Matrix (Unseen Data):")
print(cm_test)

plt.figure(figsize=(8, 6))
sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix - Test Data')
plt.show()




print(f"Mean CV Score: {grid_search.cv_results_['mean_test_score'][grid_search.best_index_] * 100:.2f}%")
print(f"Standard Deviation: {grid_search.cv_results_['std_test_score'][grid_search.best_index_] * 100:.2f}%")


# En iyi model parametrelerini yazdır
print("\nBest parameters:")
for param, value in grid_search.best_params_.items():
    print(f"{param}: {value}")


#%% 4) Random Forest 


from sklearn.ensemble import RandomForestClassifier


mymodel = RandomForestClassifier() 


param_grid = {
    'n_estimators': [50, 100, 200, 300, 350],  # Number of trees in the forest
    'max_features': ['auto', 'sqrt', 'log2'],  # Number of features to consider at every split
    'max_depth': [None, 20, 30, 40, 50],  # Maximum depth of the tree
    'min_samples_split': [3, 5, 10, 15],  # Minimum number of samples required to split an internal node
    'min_samples_leaf': [1, 2, 3],  # Minimum number of samples required to be at a leaf node
    'bootstrap': [True, False]  # Whether bootstrap samples are used when building trees
}



grid_search = GridSearchCV(mymodel, param_grid, cv=5, n_jobs=-1, verbose=0, scoring='accuracy')


grid_search.fit(x_train, y_train)



# En iyi model alınır
best_model = grid_search.best_estimator_



# Test verisinin sonuçları için metrikler hesaplanır---------------------------------------
print("\nTest Data Metrics")
test_predictions = best_model.predict(x_test)

s1 = accuracy_score(y_test, test_predictions)  
s2 = f1_score(y_test, test_predictions, average='weighted')
s3 = recall_score(y_test, test_predictions, average='weighted')
s4 = precision_score(y_test, test_predictions, average='weighted')  

print(f"Test Accuracy: {s1 * 100:.2f}%")  
print(f"Test F1 Score: {s2 * 100:.2f}%")
print(f"Test Recall: {s3 * 100:.2f}%")
print(f"Test Precision: {s4 * 100:.2f}%")


# Karışıklık Matrisi hangi sınıfların nasıl tahmin edildiğini gösterir
cm_test = confusion_matrix(y_test, test_predictions)  
print("\nConfusion Matrix (Unseen Data):")
print(cm_test)

plt.figure(figsize=(8, 6))
sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix - Test Data')
plt.show()




print(f"Mean CV Score: {grid_search.cv_results_['mean_test_score'][grid_search.best_index_] * 100:.2f}%")
print(f"Standard Deviation: {grid_search.cv_results_['std_test_score'][grid_search.best_index_] * 100:.2f}%")


# En iyi model parametrelerini yazdır
print("\nBest parameters:")
for param, value in grid_search.best_params_.items():
    print(f"{param}: {value}")


#%% 5) SVM 


from sklearn import svm


mymodel = svm.SVC(probability=True)


param_grid = {
    'C': [ 1, 5, 7, 9, 10, 11, 12, 15, 20],
    'kernel': ['linear', 'rbf' , 'sigmoid' ],
    'gamma': ['scale', 'auto', 0.1, 2, 5, 10]
    
    }




grid_search = GridSearchCV(mymodel, param_grid, cv=5, n_jobs=-1, verbose=0, scoring='accuracy')


grid_search.fit(x_train, y_train)



# En iyi model alınır
best_model = grid_search.best_estimator_



# Test verisinin sonuçları için metrikler hesaplanır---------------------------------------
print("\nTest Data Metrics")
test_predictions = best_model.predict(x_test)

s1 = accuracy_score(y_test, test_predictions)  
s2 = f1_score(y_test, test_predictions, average='weighted')
s3 = recall_score(y_test, test_predictions, average='weighted')
s4 = precision_score(y_test, test_predictions, average='weighted')  

print(f"Test Accuracy: {s1 * 100:.2f}%")  
print(f"Test F1 Score: {s2 * 100:.2f}%")
print(f"Test Recall: {s3 * 100:.2f}%")
print(f"Test Precision: {s4 * 100:.2f}%")


# Karışıklık Matrisi hangi sınıfların nasıl tahmin edildiğini gösterir
cm_test = confusion_matrix(y_test, test_predictions)  
print("\nConfusion Matrix (Unseen Data):")
print(cm_test)

plt.figure(figsize=(8, 6))
sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix - Test Data')
plt.show()




print(f"Mean CV Score: {grid_search.cv_results_['mean_test_score'][grid_search.best_index_] * 100:.2f}%")
print(f"Standard Deviation: {grid_search.cv_results_['std_test_score'][grid_search.best_index_] * 100:.2f}%")


# En iyi model parametrelerini yazdır
print("\nBest parameters:")
for param, value in grid_search.best_params_.items():
    print(f"{param}: {value}")




#%% 6) Gradient Boost


from sklearn.ensemble import GradientBoostingClassifier


mymodel = GradientBoostingClassifier()


param_grid = {
    'n_estimators': [180, 200, 250, 300 ],
    'learning_rate': [0.01, 0.02, 0.05],
    'max_depth': [4, 5, 6],
    'min_samples_split': [2, 3],
    'min_samples_leaf': [2, 5, 8],
    'subsample': [1.0],
    'max_features': ['sqrt']
}




grid_search = GridSearchCV(mymodel, param_grid, cv=5, n_jobs=-1, verbose=0, scoring='accuracy')


grid_search.fit(x_train, y_train)



# En iyi model alınır
best_model = grid_search.best_estimator_



# Test verisinin sonuçları için metrikler hesaplanır---------------------------------------
print("\nTest Data Metrics")
test_predictions = best_model.predict(x_test)

s1 = accuracy_score(y_test, test_predictions)  
s2 = f1_score(y_test, test_predictions, average='weighted')
s3 = recall_score(y_test, test_predictions, average='weighted')
s4 = precision_score(y_test, test_predictions, average='weighted')  

print(f"Test Accuracy: {s1 * 100:.2f}%")  
print(f"Test F1 Score: {s2 * 100:.2f}%")
print(f"Test Recall: {s3 * 100:.2f}%")
print(f"Test Precision: {s4 * 100:.2f}%")


# Karışıklık Matrisi hangi sınıfların nasıl tahmin edildiğini gösterir
cm_test = confusion_matrix(y_test, test_predictions)  
print("\nConfusion Matrix (Unseen Data):")
print(cm_test)

plt.figure(figsize=(8, 6))
sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix - Test Data')
plt.show()




print(f"Mean CV Score: {grid_search.cv_results_['mean_test_score'][grid_search.best_index_] * 100:.2f}%")
print(f"Standard Deviation: {grid_search.cv_results_['std_test_score'][grid_search.best_index_] * 100:.2f}%")


# En iyi model parametrelerini yazdır
print("\nBest parameters:")
for param, value in grid_search.best_params_.items():
    print(f"{param}: {value}")




#%% 7) Diğer modeller


from sklearn.utils import all_estimators

# sınıflandırıcı olan tüm modelleri seçiyoruz
estimators = all_estimators(type_filter="classifier")
allclass = []
for name, ClassifierClass in estimators:
    print(f"Initializing {name}")
    try:
        clfs = ClassifierClass()
        allclass.append(clfs)
    except Exception as e:
        print(f"Error initializing {name}: {str(e)}")



# sorun çıkaran bazı modeller manuel olarak silinebilir
allclass.pop(11)



metrics = []
for model in allclass:
    model_name = model.__class__.__name__
    print(f"Training and evaluating {model_name}")
    try:
        model.fit(x_train, y_train)
        y_prediction = model.predict(x_test)
        metrics.append((
            model_name,
            accuracy_score(y_test, y_prediction),
            recall_score(y_test, y_prediction, average='weighted'),
            precision_score(y_test, y_prediction, average='weighted'),
            f1_score(y_test, y_prediction, average='weighted')
        ))
    except Exception as e:
        print(f"Error with {model_name}: {str(e)}")
        metrics.append((model_name, -1, -1, -1, -1))

resultdf = pd.DataFrame(metrics, columns=["Classifier model", "Accuracy", "Recall", "Precision", "F1_score"])
resultdf = resultdf.sort_values("Accuracy", ascending=False)
print(resultdf)




#%% 8) Model kaydetme ve import



from joblib import dump, load


# modeli daha sonra kullanmak için kaydedelim
model_file_path = "boost_obesity.joblib"
dump(best_model, model_file_path)
print(f"Model şuraya kaydedildi: {model_file_path}")



#%% 9) Model kullanımı

modell = load(model_file_path)


# Örnek bir kullanım göstermek için hazırlanan veri setinden bir satırı seçip test edelim

select = int(input("Verisetinden seçmek istediğiniz satır numarasını girin : "))

prediction2 = modell.predict(x[select,:].reshape(1,-1))  






# Sonucu yazdırma
print(prediction2)

if prediction2 == 0 :
    print("Insufficient_Weight")
elif prediction2 == 1 :
    print("Normal_Weight")
elif prediction2 == 2 :
    print("Obesity_Type_I")
elif prediction2 == 3 :
    print("Obesity_Type_II")
elif prediction2 == 4 :
    print("Obesity_Type_III")
elif prediction2 == 5 :
    print("Overweight_Level_I")
elif prediction2 == 6 :
    print("Overweight_Level_II")



# Doğruluğu karşılaştıralım, tabi bu sadece elimizdeki veri seti için yapabileceğimiz bir örnek olacak
if prediction2 == y[select] :
    print("Tahmin doğru")
else :
    print("Tahmin yanlış")  
    
    
    
    
#%% 10) Notlar


"""
En iyi model parametreleri (daha da fazla denenebilir):
    
    Gradient Boost
    
    learning_rate: 0.05
    max_depth: 5
    max_features: sqrt
    min_samples_leaf: 5
    min_samples_split: 2
    n_estimators: 200
    subsample: 1.0
    
"""

"""
En iyi sonuç:
    
    Test metrikleri:
    
    Test Accuracy: 90.52%
    Test F1 Score: 90.51%
    Test Recall: 90.52%
    Test Precision: 90.52%
    
    
    5'li çapraz doğrulama doğruluğu (accuracy):
        
    Mean CV Score: 91.14%
    Standard Deviation: 0.39%
    
"""


"""
BAZI ÖNEMLİ KONULAR
___________________________________



41, 238, 32, 974 gibi alakasız ve yüksek değerlere sahip olan FCVC sütununu kaldırdım.
Açıklamasında "Sebze tüketim sıklığı (0-3 arası, genellikle 1: az, 2: orta, 3: çok)" olarak geçmesine rağmen neden böyle bir şey olduğu sorgulanmalı.



Kategorik verileri sayısallaştırırken, bazılarında Label Encoding yerine diğer encoding yöntemlerini de deneyebiliriz.
Onun dışında, klasik ML modellerinin yanı sıra Yapay Sinir Ağı (MLP) modeli de denenebilir.




Bu aşamadan sonraki süreçte artık modeli deploy etmek, modelimizi uygulama içinde kullanmak kalıyor.

Modeli 3 şekilde kullanabiliriz:
    
    
    Heroku, MongoDB, Digital Ocean gibi bir bulut sunucu hizmeti üzerinden modeli deploy edebiliriz. 
    Modelin ve gerekli asgari kodların çalışacağı bir ortam gerekiyor.
    
    
    Modeli ve model kodlarını doğrudan mobil uygulamada çalışacak şekle getirebiliriz. Firebase gibi bazı sistemler bunu sağlayabiliyor. Ancak bu konuda bazı kısıtlar mevcut.
    
    
    Ya da, model kodlarını lokal bilgisayar üzerinden çalıştırıp web site / mobil uygulamaya sonuçları gönderebiliriz. 



"""


