# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 17:03:56 2022

@author: marta
"""

reset -f

from google.colab import drive # For linking colab to Google Drive
import pandas as pd # For dataframe handling
import numpy as np # For matrix and list computations
import matplotlib.pyplot as plt # For advanced graphs
import scipy.stats as stats
from pandas.api.types import CategoricalDtype
import seaborn as sns
import matplotlib.pyplot as plt 


os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()


wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape


#VARIABLE TARGET: KILÓMETROS

print(db.kms.describe) #QC

print(db.groupby('kms').size())

#Cálculo numérico de la variable target: media, desviación típica, cuartiles y mediana.
db.kilometros.describe() 

#Creamos variable nominal a partir de la variable target cuantitativa

db.loc[(db['kms'] < 20),"kms_cat"]= "Very Low" 
db.loc[(db['kms']>=20) & (db['kms']<40) ,"kms_cat"]= "Low"
db.loc[(db['kms']>=40) & (db['kms']<60),"kms_cat"]= "Normal"
db.loc[(db['kms']>=60) & (db['kms']<80),"kms_cat"]= "Hight"
db.loc[(db['kms'] >=80),"kms_cat"]= "Very Hight"

x=db['kms']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title('Figura 1.Registro numérico kilometros diarios en usuarios')
plt.ylabel('frecuencia')
plt.xlabel('días de actividad aeróbica al año')
props = dict(boxstyle='round', facecolor='white', lw=0.5)       
textstr = '$\mathrm{n}=%.0f$'%(n)                              
plt.text (75,60, textstr , bbox=props) 
plt.show()


#tabla de porcentajes
mytable = db.groupby(['kms_cat']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
mytable3 = round(mytable2,1)
mytable3


bar_list = ['Very Low','Low','Normal','Hight','Very Hight']
plt.bar(bar_list, sorted(mytable3,reverse=True), edgecolor='black')
plt.ylabel('porcentaje')
plt.title('Figura 2. Porcentaje actividad diario en los usuarios')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text (3.5,60, textstr , bbox=props) 
plt.show()

#VARIABLE PREDICTIVA EDAD

print(db.groupby('age').size())

x=db['age']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(15,23,step=1))
plt.title("figura 11. Registro numérico de la Edad")
plt.ylabel('frecuencia')
plt.xlabel('Edad alumnos')
plt.show()


##Estudio Nominal
mytable = db.groupby(['age']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(mytable2.index,mytable2,edgecolor='black')
plt.ylabel('porcentaje (%)')
plt.title('Figura 12. Porcentaje de los usuasrios según edad')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(21.5, 25, textstr, bbox=props)
plt.show()

##Nominal vs Cualitativo
print(db.groupby('age').size())

age1= db.loc[db.age==15,"kms"]
age2= db.loc[db.age==16,"kms"]
age3= db.loc[db.age==17,"kms"]
age4= db.loc[db.age==18,"kms"]
age5= db.loc[db.age==19,"kms"]
age6= db.loc[db.age==20,"kms"]
age7= db.loc[db.age==21,"kms"]
age8= db.loc[db.age==22,"kms"]


res=stats.f_oneway(age1,age2,age3,age4,age5,age6,age7,age8)
print(res) # El pvalue es 0.0043 por lo que es significativo el consumo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="age", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 90, step=5))
plt.ylim(0,90) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.95,65,'Mean:19.39''\n''n:395' '\n' 't:3.004' '\n' 'Pval.:0.004', bbox=props)
plt.xlabel('Edad')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 13. Actividad aeróbica según la Edad.''\n')


pd.crosstab(db.kms_cat, db.age, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.age, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.age, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)


my_ct2=my_ct.transpose() 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') 
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(2.5, 110, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.004', bbox=props)
plt.xlabel('Edad')
plt.title('Figura 14. Porcentaje de aeróbica según la Edad.''\n')
plt.legend(['Very Hight','Hight','Normal','Low','Very Low'])
plt.ylim(0,140)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')


#variable predictiva: GÉNERO

mytable = db.groupby(['gender']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

bar_list = ['F','M']
plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('Figura 6 . Porcentaje por género')
plt.text(1,50 ,'n: 395')
plt.show()

#ESTUDIO VARIABLE NOMINAL SEXO SOBRE TARGET
sex_femin= db.loc[db.sex=="F","kms"]
sex_masc= db.loc[db.sex=="M","kms"]
res=stats.ttest_ind(sex_femin, sex_masc,equal_var=False)
print(res)#El pvalue es 0.000 por lo que es significativo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="gender", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 45, step=5))

plt.ylim(0,45) 
plt.axhline(y=db.consumoDia.mean(),linewidth=1, linestyle= 'dashed', color="green")

props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.10,35,'Mean:19.39''\n''n:395' '\n' 't:-5.420' '\n' 'Pval.:0.000', bbox=props)

plt.xlabel('gender')
plt.ylabel('kms')
plt.title('Figure 7. Actividad aeróbica según el Género.''\n')

#Crostabulation
pd.crosstab(db.kms_cat, db.gender, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.gender, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.gender, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)

#Stadistical test
ct = pd.crosstab(db.kms_cat, db.gender)
ct
stats.chi2_contingency(ct)

my_ct2=my_ct.transpose() #Primero hay que treansponer la tabla para poder representarla graficamente
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') #Mapas de colores https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(0.5, 70, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Género')
plt.title('Figura 8. Porcentaje de actividad diaria por Sexo.''\n')
plt.legend(['Very Hight','Hight','Normal','Low','Very Low'])
plt.ylim(0,120)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')



#vARIABLE PREDICTORA: GÉNERO

##Estudio Nominal
mytable = db.groupby(['gender']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))


bar_list = ['man','womon']
plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('porcentaje')
plt.title('Figura 3. Porcentaje género')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(2, 60, textstr, bbox=props)
plt.show()

print(db.groupby('gender').consumoDia.mean())

#Nominal-Cuantitativo

m= db.loc[db.guardian=='man',"kms"]
w= db.loc[db.guardian=='woman',"kms"]


res=stats.f_oneway(f,m)

print(res) #El pvalue es 0.486 por lo que no es significativo 


plt.figure(figsize=(7,5))
ax = sns.pointplot(x="gender", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 45, step=5))
plt.ylim(0,45) 
plt.axhline(y=db.consumoDia.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.70,35,'Mean:19.39''\n''n:395' '\n' 't:0.722' '\n' 'Pval.:0.486', bbox=props)
plt.xlabel('Género')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 4. Actividad aeróbica según el género.''\n')
plt.show()



#ESTUDIO VARIABLE NOMINAL SMOKER SOBRE TARGET

db.loc[(db['smoker']==0),"smoker_str"]= "NO" 
db.loc[(db['smoker']==1), "smoker_str"]= "YES"

print(db.groupby('smoker_str').size())

bar_list = ['NO', 'YES']
mytable = db.groupby(['smoker_str']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('Figura 9. porcentaje de fumadores')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(1, 30, textstr, bbox=props)
plt.show()

smoker_no= db.loc[db.smoker==0,"kms"]
smoker_yes= db.loc[db.smoker==1,"kms"]

res=stats.f_oneway(smoker_no, smoker_yes)
print(res) #El pvalue es 0.208 por lo que no es significativo


plt.figure(figsize=(7,5))
ax = sns.pointplot( x="smoker", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 45, step=5))
plt.ylim(0,45) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(3,35,'Mean:19.39''\n''n:395' '\n' 't:1.477' '\n' 'Pval.:0.208', bbox=props)
plt.xlabel('Estado de salud')
plt.ylabel('Consumo Alcohol')
plt.title('Figure 10. Consumo Alcohol según el estado de salud.''\n')


#ESTUDIO VARIABLE NOMINAL DRINKING SOBRE TARGET

db.loc[(db['drinking']==0),"drinking_str"]= "NO" 
db.loc[(db['drinking']==1), "drinking_str"]= "YES"

print(db.groupby('drinking_str').size())

bar_list = ['NO', 'YES']
mytable = db.groupby(['drinking_str']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('Figura 9. porcentaje de bebedores')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(1, 30, textstr, bbox=props)
plt.show()

drinking_no= db.loc[db.drinking==0,"kms"]
drinking_yes= db.loc[db.drinking==1,"kms"]

res=stats.f_oneway(drinking_no, drinking_yes)
print(res) #El pvalue es 0.208 por lo que no es significativo


plt.figure(figsize=(7,5))
ax = sns.pointplot( x="drinking", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 45, step=5))
plt.ylim(0,45) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(3,35,'Mean:19.39''\n''n:395' '\n' 't:1.477' '\n' 'Pval.:0.208', bbox=props)
plt.xlabel('Estado de salud')
plt.ylabel('Consumo Alcohol')
plt.title('Figure 10. Actividad aeróbica según el consumo de alcohol.''\n')

#ESTUDIO VARIABLE NOMINAL previouspatology SOBRE TARGET

db.loc[(db['previouspatology']==0),"previouspatology_str"]= "NO" 
db.loc[(db['previouspatology']==1), "previouspatology_str"]= "YES"

print(db.groupby('previouspatology_str').size())

bar_list = ['NO', 'YES']
mytable = db.groupby(['previouspatology_str']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('Figura 9. porcentaje de clientes con patologías previas')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(1, 30, textstr, bbox=props)
plt.show()

previouspatology_no= db.loc[db.previouspatology==0,"kms"]
previouspatology_yes= db.loc[db.previouspatology==1,"kms"]

res=stats.f_oneway(previouspatology_no, previouspatology_yes)
print(res) #El pvalue es 0.208 por lo que no es significativo


plt.figure(figsize=(7,5))
ax = sns.pointplot( x="previouspatology", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 45, step=5))
plt.ylim(0,45) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(3,35,'Mean:19.39''\n''n:395' '\n' 't:1.477' '\n' 'Pval.:0.208', bbox=props)
plt.xlabel('Patologías previas')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 10. Actividad aeróbica segñun patologias previas.''\n')


#VARIABLE PREDICTIVA cholesterol


#Creamos variable nominal a partir de la variable target cuantitativa

db.loc[(db['cholesterol'] < 170, "cholesterol_cat"]= "Good" 
db.loc[(db['cholesterol'] >=170, "cholesterol_cat"]= "Bad"


x=db['cholesterol']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title('Figura 1.Registro numérico colesterol en usuarios')
plt.ylabel('frecuencia')
plt.xlabel('días de actividad aeróbica al año')
props = dict(boxstyle='round', facecolor='white', lw=0.5)       
textstr = '$\mathrm{n}=%.0f$'%(n)                              
plt.text (75,60, textstr , bbox=props) 
plt.show()


#tabla de porcentajes
mytable = db.groupby(['cholesterol_cat']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
mytable3 = round(mytable2,1)
mytable3


bar_list = ['Good', 'Bad']
plt.bar(bar_list, sorted(mytable3,reverse=True), edgecolor='black')
plt.ylabel('porcentaje')
plt.title('Figura 2. Porcentaje colesterol usuarios')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text (3.5,60, textstr , bbox=props) 
plt.show()


print(db.groupby('cholesterol').size())

cholesterol1= db.loc[db.age<170,"kms"]
cholesterol2= db.loc[db.age>=170,"kms"]

res=stats.f_oneway(cholesterol1,cholesterol2)
print(res) # El pvalue es 0.0043 por lo que es significativo el consumo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="cholesterol", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 90, step=5))
plt.ylim(0,90) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.95,65,'Mean:19.39''\n''n:395' '\n' 't:3.004' '\n' 'Pval.:0.004', bbox=props)
plt.xlabel('cholesterol')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 13. cholesterol1 según activida aeróbica.''\n')


pd.crosstab(db.kms_cat, db.cholesterol1, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.cholesterol1, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.cholesterol1, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)


my_ct2=my_ct.transpose() 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') 
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(2.5, 110, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.004', bbox=props)
plt.xlabel('Edad')
plt.title('Figura 14. Porcentaje de aeróbica según la Edad.''\n')
plt.legend(['Good',Bad'])
plt.ylim(0,140)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')




#VARIABLE PREDICTIVA bloodpressure_sist


#Creamos variable nominal a partir de la variable target cuantitativa

db.loc[(db['bloodpressure_sist'] <120, "bloodpressure_sist_cat"]= "Good" 
db.loc[(db['bloodpressure_sist'] >=120, "bloodpressure_sist_cat"]= "Bad"


x=db['cholesterol']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title('Figura 1.Registro numérico tensión en usuarios')
plt.ylabel('frecuencia')
plt.xlabel('días de actividad aeróbica al año')
props = dict(boxstyle='round', facecolor='white', lw=0.5)       
textstr = '$\mathrm{n}=%.0f$'%(n)                              
plt.text (75,60, textstr , bbox=props) 
plt.show()


#tabla de porcentajes
mytable = db.groupby(['bloodpressure_sistcat']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
mytable3 = round(mytable2,1)
mytable3


bar_list = ['Good', 'Bad']
plt.bar(bar_list, sorted(mytable3,reverse=True), edgecolor='black')
plt.ylabel('porcentaje')
plt.title('Figura 2. Porcentaje bloodpressure_sist usuarios')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text (3.5,60, textstr , bbox=props) 
plt.show()


print(db.groupby('bloodpressure_sist').size())

bloodpressure_sistl1= db.loc[db.bloodpressure_sist<170,"kms"]
bloodpressure_sist2= db.loc[db.bloodpressure_sist>=170,"kms"]

res=stats.f_oneway(bloodpressure_sist1,bloodpressure_sist2)
print(res) # El pvalue es 0.0043 por lo que es significativo el consumo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="cholesterol", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 90, step=5))
plt.ylim(0,90) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.95,65,'Mean:19.39''\n''n:395' '\n' 't:3.004' '\n' 'Pval.:0.004', bbox=props)
plt.xlabel('cholesterol')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 13. bloodpressure_sist según activida aeróbica.''\n')


pd.crosstab(db.kms_cat, db.bloodpressure_sist, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.bloodpressure_sist, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.bloodpressure_sist, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)


my_ct2=my_ct.transpose() 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') 
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(2.5, 110, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.004', bbox=props)
plt.xlabel('Edad')
plt.title('Figura 14. Porcentaje de aeróbica según la Edad.''\n')
plt.legend(['Good',Bad'])
plt.ylim(0,140)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')



#VARIABLE PREDICTIVA bloodpressure_diast


#Creamos variable nominal a partir de la variable target cuantitativa

db.loc[(db['bloodpressure_diast'] <120, "bloodpressure_diast_cat"]= "Good" 
db.loc[(db['bloodpressure_diast'] >=120, "bloodpressure_diast_cat"]= "Bad"


x=db['bloodpressure_diast']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,105,step=5))
plt.title('Figura 1.Registro numérico tensión en usuarios')
plt.ylabel('frecuencia')
plt.xlabel('días de actividad aeróbica al año')
props = dict(boxstyle='round', facecolor='white', lw=0.5)       
textstr = '$\mathrm{n}=%.0f$'%(n)                              
plt.text (75,60, textstr , bbox=props) 
plt.show()


#tabla de porcentajes
mytable = db.groupby(['bloodpressure_diast']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
mytable3 = round(mytable2,1)
mytable3


bar_list = ['Good', 'Bad']
plt.bar(bar_list, sorted(mytable3,reverse=True), edgecolor='black')
plt.ylabel('porcentaje')
plt.title('Figura 2. Porcentaje bloodpressure_diast usuarios')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text (3.5,60, textstr , bbox=props) 
plt.show()


print(db.groupby('bloodpressure_diast').size())

bloodpressure_diast1= db.loc[db.bloodpressure_diast<170,"kms"]
bloodpressure_diast2= db.loc[db.bloodpressure_diast>=170,"kms"]

res=stats.f_oneway(bloodpressure_diast1,bloodpressure_diast2)
print(res) # El pvalue es 0.0043 por lo que es significativo el consumo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="bloodpressure_diast", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 90, step=5))
plt.ylim(0,90) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.95,65,'Mean:19.39''\n''n:395' '\n' 't:3.004' '\n' 'Pval.:0.004', bbox=props)
plt.xlabel('cholesterol')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 13. bloodpressure_sist según activida aeróbica.''\n')


pd.crosstab(db.kms_cat, db.bloodpressure_diast, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.bloodpressure_diast, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.bloodpressure_diast, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)


my_ct2=my_ct.transpose() 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') 
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(2.5, 110, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.004', bbox=props)
plt.xlabel('Edad')
plt.title('Figura 14. Porcentaje de aeróbica según la bloodpressure_diast.''\n')
plt.legend(['Good',Bad'])
plt.ylim(0,140)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')



# VARIABLE PREDICTIVA bodyfat



print(db.groupby('bodyfat').size())

x=db['bodyfat']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(15,23,step=1))
plt.title("figura 11. Registro numérico de la bodyfat")
plt.ylabel('frecuencia')
plt.xlabel('Edad alumnos')
plt.show()


##Estudio Nominal
mytable = db.groupby(['bodyfat']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(mytable2.index,mytable2,edgecolor='black')
plt.ylabel('porcentaje (%)')
plt.title('Figura 12. Porcentaje de los usuasrios según edad')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(21.5, 25, textstr, bbox=props)
plt.show()

##Nominal vs Cualitativo
print(db.groupby('age').size())

age1= db.loc[db.age==15,"kms"]
age2= db.loc[db.age==16,"kms"]
age3= db.loc[db.age==17,"kms"]
age4= db.loc[db.age==18,"kms"]
age5= db.loc[db.age==19,"kms"]
age6= db.loc[db.age==20,"kms"]
age7= db.loc[db.age==21,"kms"]
age8= db.loc[db.age==22,"kms"]


res=stats.f_oneway(age1,age2,age3,age4,age5,age6,age7,age8)
print(res) # El pvalue es 0.0043 por lo que es significativo el consumo

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="age", y="kms", data=db,ci=95, join=0)
plt.yticks(np.arange(0, 90, step=5))
plt.ylim(0,90) 
plt.axhline(y=db.kms.mean(),linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.95,65,'Mean:19.39''\n''n:395' '\n' 't:3.004' '\n' 'Pval.:0.004', bbox=props)
plt.xlabel('Edad')
plt.ylabel('Actividad aeróbica')
plt.title('Figure 13. Actividad aeróbica según la Edad.''\n')


pd.crosstab(db.kms_cat, db.age, margins=True) #1º la VD  target, 2º La predicción
pd.crosstab(db.kms_cat, db.age, normalize='columns', margins=True)*100    #Para que nos de en porcentajes
my_ct = pd.crosstab(db.kms_cat, db.age, normalize='columns', margins=True)*100  
my_ct=round(my_ct,1)
print(my_ct)


my_ct2=my_ct.transpose() 
my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues') 
props = dict(boxstyle='round', facecolor='white', lw=0.50)
plt.text(2.5, 110, 'Chi2: 30.306''\n''n: 731' '\n' 'Pval.: 0.004', bbox=props)
plt.xlabel('Edad')
plt.title('Figura 14. Porcentaje de aeróbica según la Edad.''\n')
plt.legend(['Very Hight','Hight','Normal','Low','Very Low'])
plt.ylim(0,140)
plt.xticks(rotation='horizontal')
plt.savefig('cross_tab_plot.svg')



#VARIABLE PREDICTIVA 

print(db.groupby('G3').size())

x=db['G3']

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,21,step=1))
plt.title("figura 15. Registro numérico de la Nota Final")
plt.ylabel('frecuencia')
plt.xlabel('Edad alumnos')
plt.show()



mytable = db.groupby(['G3']).size()
n= (mytable.sum())
mytable2= (mytable/n)*100
print(round(mytable2,1))

plt.bar(mytable2.index,mytable2,edgecolor='black')
plt.ylabel('porcentaje (%)')
plt.title('Figura 16. Porcentaje de los alumnos según la nota final')
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(20, 21, textstr, bbox=props)
plt.show()

#SCATTERPLOR : CONSUMO DIAS -NOTAS FINALES


x=db.G3
y=db.consumoDia
plt.title='Figura 17 . Consumo de alcohol según notas finales.''\n'
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
plt.ylabel('consumo alcohol')
plt.xlabel('Notas finales')
plt.show()

#MODELO DE REGRESIÓN LINEAL

#importamos la libreria
from statsmodels.formula.api import ols


#MODELO : KILOMETROS + EDAD

model1= ols('kms ~ age  ', data=db).fit()
print(model1.summary2())



#MODELO : KILOMETROS + EDAD + GENERO

model1= ols('kms ~ age + gender ', data=db).fit()
print(model1.summary2())

#MODELO: KMS, EDAD Y COMSUMO ALCOHOL
model2= ols('kms ~ age + gender + drinking ', data=db).fit()
print(model2.summary2())



#MODELO: KMS, EDAD, COMSUMO ALCOHOL Y FUMADOR
model3= ols('kms ~ age + drinking + smoker ', data=db).fit()
print(model3.summary2())

#MODELO: KMS, EDAD, COMSUMO ALCOHOL, FUMADOR y patologias previas

model4= ols('kms ~ age + drinking + smoker + previouspatology ', data=db).fit()
print(model4.summary2())


#MODELO: KMS, EDAD, COMSUMO ALCOHOL, FUMADOR, BEBEDOR, NIVEL DE COLESTEROL


db.cholesterol.hist()

dummies = pd.get_dummies(db.cholesterol)                                               #Hace la tabla de dummies
colnames = {1:'Good', 2:'Bad'}      #asignar nombres de variables a los numeros
dummies.rename(columns=colnames, inplace = True)                                #asignar nombres de variables a los numeros
db = pd.concat([db,dummies], axis=1)

model5= ols('kms ~ + age + drinking + smoker + previouspatology + Bad', data=db).fit()
print(model5.summary2())



#MODELO: KMS, EDAD, bebedor, FUMADO, bloodpressure_sist


db.bloodpressure_sist.hist()

dummies = pd.get_dummies(db.bloodpressure_sist)                                               #Hace la tabla de dummies
colnames = {1:'Good', 2:'Bad'}      #asignar nombres de variables a los numeros
dummies.rename(columns=colnames, inplace = True)                                #asignar nombres de variables a los numeros
db = pd.concat([db,dummies], axis=1)

model6= ols('kms ~ + age + drinking + smoker + previouspatology + Bad', data=db).fit()
print(model6.summary2())


#MODELO: KMS, EDAD, FUMADOR, BEBEDOR, bloodpressure_diast


db.bloodpressure_diast.hist()

dummies = pd.get_dummies(db.bloodpressure_diast)                                               #Hace la tabla de dummies
colnames = {1:'Good', 2:'Bad'}      #asignar nombres de variables a los numeros
dummies.rename(columns=colnames, inplace = True)                                #asignar nombres de variables a los numeros
db = pd.concat([db,dummies], axis=1)

model6= ols('kms ~ + age + drinking + smoker + previouspatology + Bad', data=db).fit()
print(model6.summary2())







#COMPARACIÓN MODELOS DE REGRESIÓN

from stargazer.stargazer import Stargazer 

stargazer = Stargazer([model1, model2, model3, model4, model5, model6, model7])                 #Genera una tabla en html
stargazer.render_html()
