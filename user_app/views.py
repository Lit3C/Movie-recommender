from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import os


def index(request):
    return render(request, 'app/app.html')

def search(request):
    return render(request, 'app/search.html')

df_raw = pd.read_pickle('user_app/data/data_raw.pickle')
from sklearn.preprocessing import StandardScaler
def reco_sys(request):
    print(request)
    if request.method == 'POST':
        title_search = request.POST['film-search']
        print("HellooooWorld")
        print(title_search)
        film_name_contains = df_raw['originalTitle'].str.contains(title_search, case= False)

        X = df_raw.drop(columns = ['tconst', 'primaryTitle', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
        'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'ratio_votes'])

        film_features = df_raw.loc[film_name_contains, X.columns]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors= 19)
        model_films.fit(X_scaled)

        neighbors = model_films.kneighbors(film_features_scaled)

        closest_films_index = neighbors[1][0]
        closest_films = df_raw[['originalTitle', 'primaryTitle', 'averageRating', 'vote_count', 'startYear', 'genres_x', 'runtime', 'overview', 'cast', 'Director', 'original_language', 'poster_path']].iloc[closest_films_index]
        distances = neighbors[0][0]

        context = {
            'title_search': title_search, 
            'originalTitle': closest_films['originalTitle'].values.tolist(),
            'primaryTitle': closest_films['primaryTitle'].values.tolist(),
            'averageRating': closest_films['averageRating'].values.tolist(),
            'vote_count': closest_films['vote_count'].values.tolist(),
            'startYear': closest_films['startYear'].values.tolist(),
            'genres_x': closest_films['genres_x'].values.tolist(),
            'runtime': closest_films['runtime'].values.tolist(),
            'overview': closest_films['overview'].values.tolist(),
            'cast': closest_films['cast'].values.tolist(),
            'director': closest_films['Director'].values.tolist(),
            'original_language': closest_films['original_language'].values.tolist(),
            'poster_path': closest_films['poster_path'].values.tolist(),
            'distances': distances
        }
    return render(request, 'app/result.html', context)

def reco_sys_click(request):
    print(request)
    if request.method == 'POST':
        title_search = request.POST['film-search']
        print("HellooooWorld")
        print(title_search)
        title_search_contains = df_raw['originalTitle'].str.contains(title_search, case= False)

        X = df_raw.drop(columns = ['tconst', 'primaryTitle', 'director_x', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
        'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'actor_1', 'actor_2', 'actor_3', 'actor_4', 'actor_3_fact', 'actor_4_fact', 'director_fact'])

        film_features = df_raw.loc[title_search_contains, X.columns]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors= 19)
        model_films.fit(X_scaled)

        neighbors = model_films.kneighbors(film_features_scaled)

        closest_films_index = neighbors[1][0]
        closest_films = df_raw[[
            'originalTitle',
            'primaryTitle',
            'averageRating',
            'vote_count',
            'startYear',
            'genres_x',
            'runtime',
            'overview',
            'cast',
            'Director',
            'original_language',
            'poster_path'
            ]].iloc[closest_films_index]
        distances = neighbors[0][0]

        context = {
            'title_search': title_search, 
            'originalTitle': closest_films['originalTitle'].values.tolist(),
            'primaryTitle': closest_films['primaryTitle'].values.tolist(),
            'averageRating': closest_films['averageRating'].values.tolist(),
            'vote_count': closest_films['vote_count'].values.tolist(),
            'startYear': closest_films['startYear'].values.tolist(),
            'genres_x': closest_films['genres_x'].values.tolist(),
            'runtime': closest_films['runtime'].values.tolist(),
            'overview': closest_films['overview'].values.tolist(),
            'cast': closest_films['cast'].values.tolist(),
            'director': closest_films['Director'].values.tolist(),
            'original_language': closest_films['original_language'].values.tolist(),
            'poster_path': closest_films['poster_path'].values.tolist(),
            'distances': distances
        }
        data = {'message': 'La fonction Python a été exécutée avec succès.'}
    return render(request, 'app/result.html', context), JsonResponse(data)
    
    

def lst(request):
    return render(request, 'app/list.html')

def booking(request):
    return render(request, 'app/booking.html')

def settings(request):
    return render(request, 'app/settings.html')

def stats(request):
    return render(request, 'app/stats.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def filtrer_table(request):
    table_totale_brute = pd.DataFrame(df_raw)

    # Récupérer les paramètres de filtre depuis la requête GET
    genre_choisi = request.GET.get('genre', '')
    annee_choisie = request.GET.get('annee', '')
    duree_classe = request.GET.get('duree_classe', '')
    nom_acteur_choisi = request.GET.get('nom_acteur', '').lower()
    realisateur_choisi = request.GET.get('realisateur', '').lower()
    note_choisie = request.GET.get('note', '')
    langue_choisie = request.GET.get('langue', '')

    # Filtrer le DataFrame en fonction des paramètres de la requête
    if genre_choisi:
        table_totale_brute = table_totale_brute[table_totale_brute['genres_x'].str.contains(genre_choisi, case=False)]

    if annee_choisie:
        table_totale_brute = table_totale_brute[table_totale_brute['startYear'] == str(annee_choisie)]
    # Filtrer le DataFrame en fonction de la classe de durée saisie
    if duree_classe:
        if duree_classe == '0-60 min':
            table_totale_brute = table_totale_brute[table_totale_brute['runtime'] <= 60]
        elif duree_classe == '60-120 min':
            table_totale_brute = table_totale_brute[(table_totale_brute['runtime'] > 60) & (table_totale_brute['runtime'] <= 120)]
        elif duree_classe == 'au-delà de 120 min':
            table_totale_brute = table_totale_brute[table_totale_brute['runtime'] > 120]
    # Filtrer les données pour l'acteur choisi dans la colonne 'cast'
    if nom_acteur_choisi:
        table_totale_brute = table_totale_brute[table_totale_brute['cast'].str.lower().str.contains(nom_acteur_choisi, na=False)]
    # Filtrer les données pour le réalisateur choisi dans la colonne 'directors'
    if realisateur_choisi:
        table_totale_brute = table_totale_brute[table_totale_brute['Director'].str.lower().str.contains(realisateur_choisi, na=False)]
    # Filtrer les données pour la note choisie
    if note_choisie:
        table_totale_brute['vote_average'] = table_totale_brute['vote_average'].astype(float)
        table_totale_brute = table_totale_brute[table_totale_brute['vote_average'] == float(note_choisie)]    
    if langue_choisie:
        table_totale_brute = table_totale_brute.loc[table_totale_brute['original_language'] == langue_choisie]
    
    # data_list = table_totale_brute.to_dict()
    # Paginer les résultats
    page = request.GET.get('page', 1)
    paginator = Paginator(table_totale_brute, 25)  # nb éléments par page

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
        
    # Passez les données filtrées au modèle
    table_totale_brute = table_totale_brute.head(100)
    context = {
        'movies': movies,
        'filtered_movies' : table_totale_brute,
        'originalTitle' : table_totale_brute["originalTitle"].values.tolist(),
        'primaryTitle': table_totale_brute['primaryTitle'].values.tolist(),
        'averageRating': table_totale_brute['averageRating'].values.tolist(),
        'vote_count': table_totale_brute['vote_count'].values.tolist(),
        'startYear': table_totale_brute['startYear'].values.tolist(),
        'genres_x': table_totale_brute['genres_x'].values.tolist(),
        'runtime': table_totale_brute['runtime'].values.tolist(),
        'overview': table_totale_brute['overview'].values.tolist(),
        'cast': table_totale_brute['cast'].values.tolist(),
        'director': table_totale_brute['Director'].values.tolist(),
        'original_language': table_totale_brute['original_language'].values.tolist(),
        'poster_path': table_totale_brute['poster_path'].values.tolist(),
            }    
    print(f"Genre choisi : {genre_choisi}")
    print(f"Année choisi : {annee_choisie}")
    print(f"Durée choisi : {duree_classe}")
    print(f"Nom Acteur choisi : {nom_acteur_choisi}")
    print(f"Réalisateur choisi : {realisateur_choisi}")
    print(f"Note choisi : {note_choisie}")
    print(f"Langue choisi : {langue_choisie}")
    print("STOP")
    print(f"Type de 'movies' : {type(context['movies'])}")
    print("FIN")
    return render(request, 'app/search.html', context)