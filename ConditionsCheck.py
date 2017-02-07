import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import chi2, SelectKBest
import pickle
import numpy as np


df = pd.read_csv('DriverCauses.csv',index_col=False)

df_final_x = df[['Time','Surface','Age','Sex','Vehicle']]
df_final_y = df['Severity']

df_final_x.ix[((df_final_x.Time >= 2200) & (df_final_x.Time < 2400)) |
              ((df_final_x.Time >= 0) & (df_final_x.Time < 600)), 'Time'] = 0
df_final_x.ix[((df_final_x.Time >= 600) & (df_final_x.Time < 1400)), 'Time'] = 1
df_final_x.ix[((df_final_x.Time >= 1400) & (df_final_x.Time < 2200)), 'Time'] = 2
df_final_x.to_csv('trainedOn.csv')

#df_best_feature = SelectKBest(chi2, k=5).fit_transform(df_final_x, df_final_y)
    
#print df_best_feature.head()
df_final_train_x,  df_test_x, df_final_train_y, df_test_y = train_test_split(df_final_x,\
                                                                            df_final_y, test_size=0.25,\
                                                                            random_state=10)
    
#param_grid =  {'n_estimators':[20,25,26,27], 'min_samples_leaf':[2,3,4], \
#                'min_samples_split':[2,3,4,5], 'random_state':[56]}

param_grid_2 = { 'hidden_layer_sizes': [(20, 10, 5), (100, ), (60, )], 'activation':['relu', 'logistic',],\
                'max_iter':[200,300,400], 'random_state':[56]}

clf2 = MLPClassifier()
#clf1 = RandomForestClassifier()

#clf = GridSearchCV(clf1, param_grid)
clf_2 = GridSearchCV(clf2, param_grid_2)

#clf.fit(df_final_train_x, df_final_train_y)
clf_2.fit(df_final_train_x, df_final_train_y)
#print clf.best_params_
#score = accuracy_score(df_test_y, clf.predict(df_test_x))
#print 'rf', score

#print df_final_train_x

print clf_2.best_params_
score1 = accuracy_score(df_test_y, clf_2.predict(df_test_x))
print score1
with open('NeuralNetModel.pickle', 'wb') as handle:
    pickle.dump(clf_2, handle, protocol=pickle.HIGHEST_PROTOCOL)
print clf_2.predict_proba([[0,2,59,1,1]])