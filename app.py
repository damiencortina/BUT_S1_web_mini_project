from flask import Flask,render_template, redirect

app = Flask(__name__)

typeSki = [
    {'id' : 1 ,'libelleType':'Mini-ski'},
    {'id' : 2 ,'libelleType':'Ski de fond'},
    {'id' : 3 ,'libelleType':'Ski de piste'},
    {'id' : 4 ,'libelleType':'Ski de randonnée'},
    {'id' : 5 ,'libelleType':'Freestyle'},
    {'id' : 6 ,'libelleType':'Freeride'},
]
skis = [
   {'id' : 1 ,'modeleSki':'Wedze 500', 'dateAchat':'2019-05-20', 'etat':'Très Bon', 'prixAchat':'240', 'prixLocation':'50', 'taille':'172', 'typeSki_id':5, 'imageSki': 'wedze_500.jpg'},
   {'id' : 2 ,'modeleSki':'Wedze 500 Slash 100', 'dateAchat':'2020-09-13', 'etat':'Neuf', 'prixAchat':'360', 'prixLocation':'75', 'taille':'184', 'typeSki_id':6, 'imageSki': 'wedze_500_slash_100.jpg'},
   {'id' : 3 ,'modeleSki':'Inovix XC S 500', 'dateAchat':'2019-11-19', 'etat':'Assez Bon', 'prixAchat':'155', 'prixLocation':'30', 'taille':'205', 'typeSki_id':2, 'imageSki': 'inovix_xc_s_500.jpg'},
   {'id' : 4 ,'modeleSki':'Rossignol Experience 80', 'dateAchat':'2018-09-12', 'etat':'Très Bon', 'prixAchat':'380', 'prixLocation':'38', 'taille':'174', 'typeSki_id':3, 'imageSki': 'rossignol_experience_80.jpg'},
   {'id' : 5 ,'modeleSki':'Wedze Mountain touring MT85', 'dateAchat':'2018-07-11', 'etat':'Très Bon', 'prixAchat':'575', 'prixLocation':'56', 'taille':'176', 'typeSki_id':4, 'imageSki': 'wedze_mountain_touring_mt85.jpg'},
   {'id' : 6 ,'modeleSki':'Atomic Redster X5', 'dateAchat':'2019-05-20', 'etat':'Assez Bon', 'prixAchat':'370', 'prixLocation':'32', 'taille':'177', 'typeSki_id':3, 'imageSki': 'atomic_redster_x5.png'},
   {'id' : 7 ,'modeleSki':'Rossignol Experience 84', 'dateAchat':'2019-11-01', 'etat':'Bon', 'prixAchat':'540', 'prixLocation':'35', 'taille':'184', 'typeSki_id':3, 'imageSki': 'rossignol_experience_84.png'},
   {'id' : 8 ,'modeleSki':'Salomon Max 8S', 'dateAchat':'2017-02-11', 'etat':'Très Bon', 'prixAchat':'500', 'prixLocation':'50', 'taille':'165', 'typeSki_id':3, 'imageSki': 'salomon_max_8s.png'},
   {'id' : 9 ,'modeleSki':'Atomic Vantage 77 TI', 'dateAchat':'2019-05-20', 'etat':'Bon', 'prixAchat':'420', 'prixLocation':'41', 'taille':'156', 'typeSki_id':3, 'imageSki': 'atomic_vantage_77_ti.jpg'},
   {'id' : 10 ,'modeleSki':'Dynastar Vertical Deer', 'dateAchat':'2017-11-25', 'etat':'Mauvais', 'prixAchat':'697', 'prixLocation':'22', 'taille':'180', 'typeSki_id':4, 'imageSki': 'dynastar_vertical_deer.jpg'},
   {'id' : 11 ,'modeleSki':'Elan Ripstick 96', 'dateAchat':'2020-04-16', 'etat':'Très Bon', 'prixAchat':'490', 'prixLocation':'42', 'taille':'181', 'typeSki_id':6, 'imageSki': 'elan_ripstick_96.jpg'},
   {'id' : 12 ,'modeleSki':'Salomon Distance M10 GW L90', 'dateAchat':'2019-08-30', 'etat':'Neuf', 'prixAchat':'299', 'prixLocation':'34', 'taille':'125', 'typeSki_id':1, 'imageSki': 'salomon_distance_m10_gw_l90.jpg'},
   {'id' : 13 ,'modeleSki':'Rossignol Freeze Xpress GW', 'dateAchat':'2020-01-04', 'etat':'Très Bon', 'prixAchat':'269', 'prixLocation':'21', 'taille':'118', 'typeSki_id':1, 'imageSki': 'rossignol_freeze_xpress_gw.jpg'},
]

@app.route("/", methods=["GET"])
def show_layout():
    return render_template('layout.html')

@app.route("/type-ski/show", methods=["GET"])
def show_type_ski():
    return render_template('show_type_ski.html', typeSki=typeSki)

@app.route("/type-ski/add", methods=["GET"])
def add_type_ski():
    return render_template('add_type_ski.html')

@app.route("/type-ski/add", methods=["POST"])
def valid_add_type_ski():
    return redirect('/type-ski/show')

@app.route("/type-ski/delete", methods=["GET"])
def delete_type_ski():
    return redirect('/type-ski/show')

@app.route("/type-ski/edit", methods=["GET"])
def edit_type_ski():
    idSki = request.args.get('id')-1
    return render_template('edit_type_ski.html')

@app.route("/type-ski/edit", methods=["POST"])
def valid_edit_type_ski():
    return redirect('/type-ski/show')

@app.route("/ski/show", methods=["GET"])
def show_ski():
    return render_template('show_ski.html', skis=skis)

@app.route("/ski/add", methods=["GET"])
def add_ski():
    return render_template('add_ski.html')

@app.route("/ski/add", methods=["POST"])
def valid_add_ski():
    return redirect('/ski/show')

@app.route("/ski/delete", methods=["GET"])
def delete_ski():
    id = request.args.get('id')
    ski = skis[id-1]
    typeSki = typeSki[ski.typeSki_id]
    message = 'Suppression d\une référence de ski :' + ski.modeleSki + ' (de type '+ typeSki ')'
    flash(message, 'is-danger')
    return redirect('/ski/show')

@app.route("/ski/edit", methods=["GET"])
def edit_ski():
    return render_template('edit_ski.html', ski=idSki, typeSki=typeSki)

@app.route("/ski/edit", methods=["POST"])
def valid_edit_ski():
    return redirect('/ski/show')

@app.route("/ski/filtre", methods=["GET"])
def filtre_ski():
    return render_template('front_ski_filtre_show.html')
