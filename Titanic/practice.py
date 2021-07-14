# @Author : AaronJny
import  numpy  as  np
import  pandas  as  pd
from  sklearn . feature_extraction  import  DictVectorizer
from  sklearn . svm  import  SVC
from  sklearn . model_selection  import  cross_val_score
from  sklearn . tree  import  DecisionTreeClassifier
from  sklearn . ensemble  import  RandomForestClassifier
from  sklearn . linear_model  import  LogisticRegression
from  sklearn . naive_bayes  import  MultinomialNB
from  sklearn . neighbors  import  KNeighborsClassifier
from  sklearn . ensemble  import  AdaBoostClassifier

# 讀取數據集
train_data  =  pd . read_csv ( 'dataset/train.csv' )
test_data  =  pd . read_csv ( 'dataset/test.csv' )

# 選擇用於訓練的特徵
features  = [ 'Pclass' , 'Sex' , 'Age' , 'SibSp' , 'Parch' , 'Fare' , 'Embarked' ]
x_train  =  train_data [ features ]
x_test  =  test_data [ features ]

y_train  =  train_data [ 'Survived' ]

# 檢查缺失值
print  '訓練數據信息：'
x_train . info ()
print  '-' * 30
print  '測試數據信息：'
x_test . info ()

# 使用登錄最多的港口來填充登錄港口的nan值
print  ' \n \n \n登錄港口信息：'
print  x_train [ 'Embarked' ]. value_counts ()
x_train [ 'Embarked' ]. fillna ( 'S' , inplace = True )
x_test [ 'Embarked' ]. fillna ( 'S' , inplace = True )

# 使用平均年齡來填充年齡中的nan值
x_train [ 'Age' ]. fillna ( x_train [ 'Age' ]. mean (), inplace = True )
x_test [ 'Age' ]. fillna ( x_test [ 'Age' ]. mean (), inplace = True )

# 使用票價的均值填充票價中的nan值
x_test [ 'Fare' ]. fillna ( x_test [ 'Fare' ]. mean (), inplace = True )

# 將特徵值轉換成特徵向量
dvec  =  DictVectorizer ( sparse = False )

x_train  =  dvec . fit_transform ( x_train . to_dict ( orient = 'record' ))
x_test  =  dvec . transform ( x_test . to_dict ( orient = 'record' ))

# 打印特徵向量格式
print  ' \n \n \n特徵向量格式'
print  dvec . feature_names_

# 支持向量機
svc  =  SVC ()
# 決策樹
dtc  =  DecisionTreeClassifier ()
# 隨機森林
rfc  =  RandomForestClassifier ()
# 邏輯回歸
lr  =  LogisticRegression ()
# 貝葉斯
nb  =  MultinomialNB ()
# K鄰近
knn  =  KNeighborsClassifier ()
# AdaBoost
boost  =  AdaBoostClassifier ()


print  ' \n \n \n模型驗證:'
print  'SVM acc is' , np . mean ( cross_val_score ( svc , x_train , y_train , cv = 10 ))
print  'DecisionTree acc is' , np . mean ( cross_val_score ( dtc , x_train , y_train , cv = 10 ))
print  'RandomForest acc is' , np . mean ( cross_val_score ( rfc , x_train , y_train , cv = 10 ))
print  'LogisticRegression acc is' , np . mean ( cross_val_score ( lr , x_train , y_train , cv = 10 ))
print  'NaiveBayes acc is' , np . mean ( cross_val_score ( nb , x_train , y_train , cv = 10 ))
print  'KNN acc is' , np . mean ( cross_val_score ( knn , x_train , y_train , cv = 10 ))
print  'AdaBoost acc is' , np . mean ( cross_val_score ( boost , x_train , y_train , cv = 10 ))

# 訓練
boost . fit ( x_train , y_train )
# 預測
y_predict  =  boost . predict ( x_test )
# 保存結果
result  = { 'PassengerId' : test_data [ 'PassengerId' ],
          'Survived' : y_predict }
result  =  pd . DataFrame ( result )
result . to_csv ( 'submission.csv' , index = False )
