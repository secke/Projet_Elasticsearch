from crypt import methods
from flask import Flask, render_template, redirect,request, url_for,session,flash

import sys

sys.path.append('.')
sys.path.append('..')

import model.data as donnes
from model.data import es

app=Flask(__name__)

app.config['SECRET_KEY']='elastic'


@app.route('/', methods=('GET','POST'))
def accueil():
    # if request.method=='POST':
    mot=request.form.get('mot_chercher')
    session['mot']=mot
    if mot:
        return redirect(url_for('resultats'))
    return render_template('accueil.html')

@app.route('/resultats')
def resultats():
    mot=session['mot']
    if not mot:
        flash("")
    recup001=es.search(index='indice_boursier', query={"match_phrase_prefix":{"nom":mot}})
    recup=recup001['hits']['hits'][0]['_source']
    # session.pop('mot', None)
    return render_template('resultats.html', recup=recup)