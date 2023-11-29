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
        title_search_contains = df_raw['originalTitle'].str.contains(title_search, case= False)

        X = df_raw.drop(columns = ['tconst', 'primaryTitle', 'director_x', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
        'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'actor_1', 'actor_2', 'actor_3', 'actor_4', 'actor_3_fact', 'actor_4_fact', 'director_fact'])

        film_features = df_raw.loc[title_search_contains, X.columns]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors= 16)
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
    return render(request, 'app/result.html', context)

def reco_sys_click(request):
    print(request)
    if request.method == 'POST':
        title_search = movie_title
        print("HellooooWorld")
        print(title_search)
        title_search_contains = df_raw['originalTitle'].str.contains(title_search, case= False)

        X = df_raw.drop(columns = ['tconst', 'primaryTitle', 'director_x', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
        'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'actor_1', 'actor_2', 'actor_3', 'actor_4', 'actor_3_fact', 'actor_4_fact', 'director_fact'])

        film_features = df_raw.loc[title_search_contains, X.columns]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors= 16)
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

table_totale_brute = pd.read_pickle('user_app/data/data_raw.pickle')
def filtrer_table(request):
    if request.method == 'POST':
        # ------------------------------------------------------------------------------------------------ GENRE
        # Convertir et formater la colonne 'genres_x'
        table_totale_brute['genres_x'] = table_totale_brute['genres_x'].astype(str).str.lower()
        # Créer une copie du DataFrame pour éviter de modifier l'original
        genre = table_totale_brute.copy()
        # Diviser la colonne 'genres_x' en listes
        genre['genres_x'] = genre['genres_x'].apply(lambda x: x.split(','))
        # Explosion du DataFrame pour traiter les listes de genres
        genre_1 = genre.explode('genres_x')
        # Remplacer les valeurs NaN dans la colonne 'genres_x' par 'inconnu'
        genre_1['genres_x'].replace('nan', 'inconnu', inplace= True)
        # Obtenir la liste unique des genres
        list_genres = genre_1['genres_x'].unique()
        # Saisie manuelle du genre par l'utilisateur
        genre_choisi = request.POST['genre']
        # Filtrer le DataFrame en fonction du genre choisi
        if genre_choisi:
            table_totale_brute = genre_1[genre_1['genres_x'] == genre_choisi]
        # ------------------------------------------------------------------------------------------------ ANNÉE
        # Saisie manuelle de l'année par l'utilisateur
        annee_choisie = request.POST['annee']
        if annee_choisie:
            # Convertir la colonne 'release_date' en datetime
            table_totale_brute['release_date'] = pd.to_datetime(table_totale_brute['release_date'], format='%Y-%m-%d')
            # Filtrer le DataFrame en fonction de l'année choisie
            table_totale_brute = table_totale_brute[table_totale_brute['release_date'].dt.year == int(annee_choisie)]
        # ------------------------------------------------------------------------------------------------ DURÉE
        # Trier le DataFrame par la colonne 'runtime'
        table_totale_brute = table_totale_brute.sort_values(by='runtime')
        # Afficher les classes de durée disponibles
        classes_de_duree = ['0-60 min', '60-120 min', 'au-delà de 120 min']
        print("Classes de durée disponibles :", classes_de_duree)
        # Saisie manuelle de la classe de durée par l'utilisateur
        duree_classe = request.POST['duration']
        if duree_classe:
            # Filtrer le DataFrame en fonction de la classe de durée saisie
            if duree_classe == '0-60 min':
                table_totale_brute = table_totale_brute[table_totale_brute['runtime'] <= 60]
            elif duree_classe == '60-120 min':
                table_totale_brute = table_totale_brute[(table_totale_brute['runtime'] > 60) & (table_totale_brute['runtime'] <= 120)]
            elif duree_classe == 'au-delà de 120 min':
                table_totale_brute = table_totale_brute[table_totale_brute['runtime'] > 120]
        # ------------------------------------------------------------------------------------------------ ACTEUR/RÉALISATEUR
        # Choix de l'acteur
        nom_acteur_choisi = request.POST['cast']
        nom_acteur_choisi = nom_acteur_choisi.lower()
        if nom_acteur_choisi:
            # Filtrer les données pour l'acteur choisi dans la colonne 'cast'
            table_totale_brute = table_totale_brute[table_totale_brute['cast'].str.lower().str.contains(nom_acteur_choisi, na=False)]
        # Choix du réalisateur
        realisateur_choisi = request.POST['director']
        realisateur_choisi = realisateur_choisi.lower()
        if realisateur_choisi:
            # Filtrer les données pour le réalisateur choisi dans la colonne 'directors'
            table_totale_brute = table_totale_brute[table_totale_brute['director'].str.lower().str.contains(realisateur_choisi, na=False)]
        #  ------------------------------------------------------------------------------------------------ NOTE
        note_choisie = request.POST['note']  # faire des classes de valeurs
        if note_choisie:
            # la colonne 'vote_average' a le même type que la valeur entrée
            table_totale_brute['vote_average'] = table_totale_brute['vote_average'].astype(float)
            # Filtrer les données pour la note choisie
            table_totale_brute = table_totale_brute[table_totale_brute['vote_average'] == float(note_choisie)]
        # ------------------------------------------------------------------------------------------------ LANGUE
        # Saisie manuelle de la langue par l'utilisateur
        langue_choisie = request.POST['langue']
        if langue_choisie:
            table_totale_brute = table_totale_brute.loc[table_totale_brute['original_language'] == langue_choisie]
        # return table_totale_brute
        context = {
            'originalTitle': table_totale_brute['originalTitle'].values.tolist(),
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
        print(genre_choisi)
        print(realisateur_choisi)
        print(f"type de genre_choisi : {type(context['genres_x'])}")
        return render(request, 'app/search.html', context)
