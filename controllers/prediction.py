from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import pickle 

#les columns du tableau
def columns():
    return ["id","Fname","Lname",'Sex','Age', 'ALB', 'ALP', 'ALT', 'AST',
       'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT',"Resp"]

#le chargement du model
loaded_model = pickle.load(open("final_model.sav", 'rb'))

#lecture du dataframe
df=pd.read_csv("hepathie_c.csv")

#donner utils du formulaire
def form_util_values(form):
    age=form.get('age')
    sex=form.get('sex')
    alb=form.get('alb')
    alp=form.get('alp')
    alt=form.get('alt')
    ast=form.get('ast')
    bil=form.get('bil')
    che=form.get('che')
    chol=form.get('chol')
    crea=form.get('crea')
    ggt=form.get('ggt')
    prot=form.get('prot')
    return age,sex,alb,alp,alt,ast,bil,che,chol,crea,ggt,prot

#donner pour la prediction
def form2data(form):
    
    return np.array([form_util_values(form)],dtype=np.float).reshape(1,-1)


def predict(data):
    np.array(data)
    data=StandardScaler().fit_transform(data)
    return loaded_model.predict(data)
