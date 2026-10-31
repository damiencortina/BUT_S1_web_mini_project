from flask import Flask, flash, render_template, redirect, request

app = Flask(__name__)
app.secret_key = '0teEr9wWrpqUm@eV'

typeSki = [{'id': 1, 'libelleType': 'Mini-ski'}, {'id': 2, 'libelleType': 'Ski de fond'},
           {'id': 3, 'libelleType': 'Ski de piste'}, {'id': 4, 'libelleType': 'Ski de randonnée'},
           {'id': 5, 'libelleType': 'Freestyle'}, {'id': 6, 'libelleType': 'Freeride'}, ]
skis = [{'id': 1, 'modeleSki': 'Wedze 500', 'dateAchat': '2019-05-20', 'etat': 'Très Bon', 'prixAchat': '240',
         'prixLocation': '50', 'taille': '172', 'typeSki_id': 5, 'imageSki': 'wedze_500.jpg'},
        {'id': 2, 'modeleSki': 'Wedze 500 Slash 100', 'dateAchat': '2020-09-13', 'etat': 'Neuf', 'prixAchat': '360',
         'prixLocation': '75', 'taille': '184', 'typeSki_id': 6, 'imageSki': 'wedze_500_slash_100.jpg'},
        {'id': 3, 'modeleSki': 'Inovix XC S 500', 'dateAchat': '2019-11-19', 'etat': 'Assez Bon', 'prixAchat': '155',
         'prixLocation': '30', 'taille': '205', 'typeSki_id': 2, 'imageSki': 'inovix_xc_s_500.jpg'},
        {'id': 4, 'modeleSki': 'Rossignol Experience 80', 'dateAchat': '2018-09-12', 'etat': 'Très Bon',
         'prixAchat': '380', 'prixLocation': '38', 'taille': '174', 'typeSki_id': 3,
         'imageSki': 'rossignol_experience_80.jpg'},
        {'id': 5, 'modeleSki': 'Wedze Mountain touring MT85', 'dateAchat': '2018-07-11', 'etat': 'Très Bon',
         'prixAchat': '575', 'prixLocation': '56', 'taille': '176', 'typeSki_id': 4,
         'imageSki': 'wedze_mountain_touring_mt85.jpg'},
        {'id': 6, 'modeleSki': 'Atomic Redster X5', 'dateAchat': '2019-05-20', 'etat': 'Assez Bon', 'prixAchat': '370',
         'prixLocation': '32', 'taille': '177', 'typeSki_id': 3, 'imageSki': 'atomic_redster_x5.png'},
        {'id': 7, 'modeleSki': 'Rossignol Experience 84', 'dateAchat': '2019-11-01', 'etat': 'Bon', 'prixAchat': '540',
         'prixLocation': '35', 'taille': '184', 'typeSki_id': 3, 'imageSki': 'rossignol_experience_84.png'},
        {'id': 8, 'modeleSki': 'Salomon Max 8S', 'dateAchat': '2017-02-11', 'etat': 'Très Bon', 'prixAchat': '500',
         'prixLocation': '50', 'taille': '165', 'typeSki_id': 3, 'imageSki': 'salomon_max_8s.png'},
        {'id': 9, 'modeleSki': 'Atomic Vantage 77 TI', 'dateAchat': '2019-05-20', 'etat': 'Bon', 'prixAchat': '420',
         'prixLocation': '41', 'taille': '156', 'typeSki_id': 3, 'imageSki': 'atomic_vantage_77_ti.jpg'},
        {'id': 10, 'modeleSki': 'Dynastar Vertical Deer', 'dateAchat': '2017-11-25', 'etat': 'Mauvais',
         'prixAchat': '697', 'prixLocation': '22', 'taille': '180', 'typeSki_id': 4,
         'imageSki': 'dynastar_vertical_deer.jpg'},
        {'id': 11, 'modeleSki': 'Elan Ripstick 96', 'dateAchat': '2020-04-16', 'etat': 'Très Bon', 'prixAchat': '490',
         'prixLocation': '42', 'taille': '181', 'typeSki_id': 6, 'imageSki': 'elan_ripstick_96.jpg'},
        {'id': 12, 'modeleSki': 'Salomon Distance M10 GW L90', 'dateAchat': '2019-08-30', 'etat': 'Neuf',
         'prixAchat': '299', 'prixLocation': '34', 'taille': '125', 'typeSki_id': 1,
         'imageSki': 'salomon_distance_m10_gw_l90.jpg'},
        {'id': 13, 'modeleSki': 'Rossignol Freeze Xpress GW', 'dateAchat': '2020-01-04', 'etat': 'Très Bon',
         'prixAchat': '269', 'prixLocation': '21', 'taille': '118', 'typeSki_id': 1,
         'imageSki': 'rossignol_freeze_xpress_gw.jpg'}, ]


@app.route("/", methods=["GET"])
def show_layout():
    return render_template('layout.html')


@app.route("/type-ski/show", methods=["GET"])
def show_type_ski():
    return render_template('type_ski/show_type_ski.html', typeSki=typeSki)


@app.route("/type-ski/add", methods=["GET"])
def add_type_ski():
    return render_template('type_ski/add_type_ski.html')


@app.route("/type-ski/add", methods=["POST"])
def valid_add_type_ski():
    message = 'Type de ski ajouté - libellé : ' + str(request.form.get('libelleType'))
    flash(message, 'success')
    return redirect('/type-ski/show')


@app.route("/type-ski/delete", methods=["GET"])
def delete_type_ski():
    id_type_ski = request.args.get('id', type=int)
    message = 'Suppression d\'un type de ski (id : ' + str(id_type_ski) + ')'
    flash(message, 'danger')
    return redirect('/type-ski/show')


@app.route("/type-ski/edit", methods=["GET"])
def edit_type_ski():
    id_type_ski = request.args.get('id', type=int)
    type_ski = typeSki[id_type_ski - 1]
    return render_template('type_ski/edit_type_ski.html', typeSki=type_ski)


@app.route("/type-ski/edit", methods=["POST"])
def valid_edit_type_ski():
    message = 'Type de ski modifié - libellé : ' + str(request.form.get('libelleType')) + ' (id : ' + str(
        request.form.get('id')) + ')'
    flash(message, 'success')
    return redirect('/type-ski/show')


@app.route("/ski/show", methods=["GET"])
def show_ski():
    return render_template('ski/show_ski.html', skis=skis)


@app.route("/ski/add", methods=["GET"])
def add_ski():
    return render_template('ski/add_ski.html', typesSki=typeSki)


@app.route("/ski/add", methods=["POST"])
def valid_add_ski():
    message = 'Modèle de ski ajouté - modèle : ' + str(request.form.get('modeleSki')) + ' , type de ski : ' + str(
        request.form.get('typeSki_id')) + ' , date d\'achat : ' + str(
        request.form.get('dateAchat')) + ' , état : ' + str(request.form.get('etat')) + ' , prix d\'achat : ' + str(
        request.form.get('prixAchat')) + ' , prix de location : ' + str(
        request.form.get('prixLocation')) + ' , taille : ' + str(request.form.get('taille')) + ' , image : ' + str(
        request.form.get('imageSki'))
    flash(message, 'success')
    return redirect('/ski/show')


@app.route("/ski/delete", methods=["GET"])
def delete_ski():
    id_ski = request.args.get('id', type=int)
    message = 'Suppression d\'un modèle de ski (id : ' + str(id_ski) + ')'
    flash(message, 'danger')
    return redirect('/ski/show')


@app.route("/ski/edit", methods=["GET"])
def edit_ski():
    id_ski = request.args.get('id', type=int)
    ski = skis[id_ski - 1]
    return render_template('ski/edit_ski.html', ski=ski, typesSki=typeSki)


@app.route("/ski/edit", methods=["POST"])
def valid_edit_ski():
    message = 'Modèle de ski modifié - modèle : ' + str(request.form.get('modeleSki')) + ' , type de ski : ' + str(
        request.form.get('typeSki_id')) + ' , date d\'achat : ' + str(
        request.form.get('dateAchat')) + ' , état : ' + str(request.form.get('etat')) + ' , prix d\'achat : ' + str(
        request.form.get('prixAchat')) + ' , prix de location : ' + str(
        request.form.get('prixLocation')) + ' , taille : ' + str(request.form.get('taille')) + ' , image : ' + str(
        request.form.get('imageSki')) + ' (id : ' + str(request.form.get('id')) + ')'
    flash(message, 'success')
    return redirect('/ski/show')


@app.route("/ski/filtre", methods=["GET"])
def filtre_ski():
    return render_template('ski/front_ski_filtre_show.html', skis=skis, typesSki=typeSki)

@app.route('/ski/filtre', methods=['POST'])
def filtre_article_valid():
    filter_word = request.form.get('filter_word', None)
    min_price = request.form.get('min_price', None)
    max_price = request.form.get('max_price', None)
    filter_items = request.form.getlist('filter_items')
    if filter_word and filter_word != "":
        message = u'Modèles contenant : ' + filter_word
        flash(message, 'success')
    if min_price or max_price:
        val_min=str(min_price).replace(' ', '').replace(',', '.')
        val_max=str(max_price).replace(' ', '').replace(',', '.')
        if val_min.replace('.', '', 1).isdigit() and val_max.replace('.', '', 1).isdigit():
            if float(val_min) < float(val_max):
                message = u'Prix compris entre : ' +  val_min + "€ et "+ val_max + "€"
                flash(message, 'success')
            else:
                message=u'min < max'
                flash(message, 'warning')
        else:
            message=u'Prix min ('+val_min+') et prix max ('+val_max+') doivent être tous les deux des numériques positifs'
            flash(message, 'warning')
    if filter_items and filter_items != []:
        message=u'Modèles sélectionnés :  '
        for case in filter_items:
            message+=' id : '+case+ '  '
        flash(message, 'success')
    return redirect('/ski/filtre')