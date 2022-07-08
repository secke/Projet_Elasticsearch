import os
import sys
sys.path.append('.')
sys.path.append('..')

from base.config import es
### RECUPÉRATION DES DONNÉES ################

#### BEAUTIFULSOUP ####################
import requests
from bs4 import BeautifulSoup
import html5lib

############### recupération du lien des data ###########
url="https://finance.yahoo.com/world-indices"
resultat=requests.get(url)
html=resultat.text

############# instance de bs4 #################
soup=BeautifulSoup(html,"html.parser")

###########" RECUPÉRATION DES NOMS DES INDICES BOURSIERS #######"
papa=soup.find("table", attrs={'class':'W(100%)'})
noms=papa.find_all("td", attrs={"class":"Va(m) Ta(start) Px(10px) Fz(s)"})
noms_indices=[n.text for n in noms]

############### RECUPÉRATION DES COURS DES INDICES BOURSIERS ####
prix=papa.find_all("td", attrs={"class":"Va(m) Ta(end) Pstart(10px) Fw(600) Fz(s)"})
prix_=[p.text for p in prix]
prix_actions=[int(vir.replace(',','').split('.')[0]) for vir in prix_]

############ RECUPÉRATION DES CHARTS DES COURS DES INDICES #########
papa=soup.find("table", attrs={'class':'W(100%)'})
noeud_chart=papa.find_all("a", attrs={"target":"_blank"})
charts=["https://finance.yahoo.com"+ch.get_attribute_list('href')[0] for ch in noeud_chart]

############## CONVERTIR EN DICTIONNAIRE ############
dicto=[]
for i, j, k in zip(noms_indices,prix_actions,charts):
    dicto.append({"nom":i,"prix":j,"chart":k})

############ CRÉATION DE L'INDEX 'indice_boursiers' ##############
# es.indices.create(index='indice_boursier',ignore=400)

########### INSERTION DES DONNÉES DANS ÉLASTICSEARCH #############
# for ind in range(len(dicto)):
#     print(dicto[ind])
#     es.index(index='indice_boursier', document=dicto[ind], id=ind)

