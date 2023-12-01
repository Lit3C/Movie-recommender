from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import os

def search(request):
    return render(request, 'app/search.html')

def lst(request):
    return render(request, 'app/list.html')

def booking(request):
    return render(request, 'app/booking.html')

def settings(request):
    return render(request, 'app/settings.html')

def stats(request):
    return render(request, 'app/stats.html')

# --------------------------------------------------------------------------------------------Read Pickle
table_finale_dummies_3 = pd.read_pickle('user_app/data/data_raw.pickle')
seen_movies = []
fav_movies = []

# --------------------------------------------------------------------------------------------Fonction ML
from sklearn.preprocessing import StandardScaler
def reco_sys(request):
    print(request)
    if request.method == 'POST':
        film_name = request.POST['film-search']
        print("HellooooWorld")
        print(film_name)
        
        film_name_contains_original = table_finale_dummies_3['originalTitle'].str.contains(film_name, case=False)
        film_name_contains_dir = table_finale_dummies_3['Director'].str.contains(film_name, case=False)
        film_name_contains_actor_1 = table_finale_dummies_3['actor_1'].str.contains(film_name, case=False)
        film_name_contains_actor_2 = table_finale_dummies_3['actor_2'].str.contains(film_name, case=False)
        film_name_contains_actor_3 = table_finale_dummies_3['actor_3'].str.contains(film_name, case=False)
        film_name_contains_actor_4 = table_finale_dummies_3['actor_4'].str.contains(film_name, case=False)
        film_name_contains_genres = table_finale_dummies_3['genres_x'].str.contains(film_name, case=False)
        film_name_contains_over = table_finale_dummies_3['overview'].str.contains(film_name, case=False)

        if film_name_contains_dir.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                    'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                    'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                    'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                    'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                    'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                    'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                    'language_fact', 'Director', 'cast', 'actor_1_fact', 'actor_2_fact',
                                                    'actor_3_fact', 'actor_4_fact', 'genres_fact', 'actor_1', 'actor_2',
                                                    'actor_3', 'actor_4'])
            film_features = table_finale_dummies_3.loc[film_name_contains_dir, X.columns]

        elif film_name_contains_original.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
                                                    'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'ratio_votes', 'averageRating', 'actor_1', 'actor_2',
                                                    'actor_3', 'actor_4'])
            film_features = table_finale_dummies_3.loc[film_name_contains_original, X.columns]

        elif film_name_contains_actor_1.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                    'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                    'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                    'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                    'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                    'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                    'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                    'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                    'actor_4', 'actor_2_fact', 'actor_3_fact',
                                                    'actor_4_fact', 'director_fact', 'genres_fact'])
            film_features = table_finale_dummies_3.loc[film_name_contains_actor_1, X.columns]

        elif film_name_contains_actor_2.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                    'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                    'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                    'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                    'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                    'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                    'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                    'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                    'actor_4', 'actor_1_fact', 'actor_3_fact',
                                                    'actor_4_fact', 'director_fact', 'genres_fact'])
            film_features = table_finale_dummies_3.loc[film_name_contains_actor_2, X.columns]

        elif film_name_contains_actor_3.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                    'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                    'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                    'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                    'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                    'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                    'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                    'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                    'actor_4', 'actor_1_fact', 'actor_2_fact',
                                                    'actor_4_fact', 'director_fact', 'genres_fact'])
            film_features = table_finale_dummies_3.loc[film_name_contains_actor_3, X.columns]

        elif film_name_contains_actor_4.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                    'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                    'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                    'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                    'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                    'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                    'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                    'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                    'actor_4', 'actor_1_fact', 'actor_2_fact', 'actor_3_fact',
                                                    'director_fact', 'genres_fact'])
            film_features = table_finale_dummies_3.loc[film_name_contains_actor_4, X.columns]

        elif film_name_contains_over.any():
            X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
                                                    'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'ratio_votes', 'averageRating', 'actor_1', 'actor_2',
                                                    'actor_3', 'actor_4'])
            film_features = table_finale_dummies_3.loc[film_name_contains_over, X.columns]

        else:
            print(f'Film, Director ou Comédien {film_name} non disponible.')
            return

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors=19)
        model_films.fit(X_scaled)

        neighbors = model_films.kneighbors(film_features_scaled)

        closest_films_index = neighbors[1][0]
        closest_films = table_finale_dummies_3[['originalTitle', 'primaryTitle', 'averageRating', 'vote_count', 'startYear', 'genres_x', 'runtime', 'overview', 'cast', 'Director', 'original_language', 'poster_path']].iloc[closest_films_index]
        distances = neighbors[0][0]

        context = {
            'title_search': film_name, 
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

def index(request):
    df_home_header = pd.read_pickle('user_app/data/header-movies.pickle')
    df_raw = pd.read_pickle('user_app/data/data_raw.pickle')
    # --------------------------------------------------------------------------------------------Fonction Rand Header
    df_home_header = df_home_header.dropna(subset=['overview'])
    
    df_home_header = df_home_header.sort_values(by='release_date', ascending=False).head(20)
    df_home_header = df_home_header.sample(n=1)
    df_home_header = df_home_header.replace('[\'', '').replace('\']', '')
    # --------------------------------------------------------------------------------------------Fonction Rand Seen Movies    
    df_rand_seen_movie = df_raw.dropna(subset=['poster_path'])
    df_rand_seen_movie = df_rand_seen_movie.sample(n=1)
    df_rand_seen_movie = df_rand_seen_movie.replace('[\'', '').replace('\']', '')
    # --------------------------------------------------------------------------------------------Fonction Reverse Choice
    df_reverse_choice= df_raw.sort_values(by= 'primaryTitle')
    already_seen = "Titanic"
    title_contains = (df_reverse_choice['originalTitle'].str.contains(already_seen, case= False))
    X = df_reverse_choice.drop(columns = ['tconst', 'primaryTitle', 'vote_count', 'vote_average',
       'revenue', 'budget', 'Action', 'Adventure', 'Animation',
       'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
       'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
       'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
       'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
       'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
       'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
       'actor_4', 'actor_1_fact', 'actor_2_fact', 'actor_3_fact',
       'actor_4_fact', 'director_fact', 'averageRating'])
    film_features = df_reverse_choice.loc[title_contains, X.columns]
    model_films = NearestNeighbors(n_neighbors= 18)
    model_films.fit(X)
    neighbors = model_films.kneighbors(film_features)
    farest_films_index = neighbors[1][0]
    farest_films = df_reverse_choice[['originalTitle', 'primaryTitle', 
                                       'averageRating', 'vote_count', 'startYear', 
                                       'genres_x', 'runtime', 'overview', 'cast', 
                                       'Director', 'original_language', 'poster_path'
                                       ]].iloc[farest_films_index]
    # --------------------------------------------------------------------------------------------Seen this, try this
    film_name = "bleach"
    
    film_name_contains_original = table_finale_dummies_3['originalTitle'].str.contains(film_name, case=False)
    film_name_contains_dir = table_finale_dummies_3['Director'].str.contains(film_name, case=False)
    film_name_contains_actor_1 = table_finale_dummies_3['actor_1'].str.contains(film_name, case=False)
    film_name_contains_actor_2 = table_finale_dummies_3['actor_2'].str.contains(film_name, case=False)
    film_name_contains_actor_3 = table_finale_dummies_3['actor_3'].str.contains(film_name, case=False)
    film_name_contains_actor_4 = table_finale_dummies_3['actor_4'].str.contains(film_name, case=False)
    film_name_contains_genres = table_finale_dummies_3['genres_x'].str.contains(film_name, case=False)
    film_name_contains_over = table_finale_dummies_3['overview'].str.contains(film_name, case=False)

    if film_name_contains_dir.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                'language_fact', 'Director', 'cast', 'actor_1_fact', 'actor_2_fact',
                                                'actor_3_fact', 'actor_4_fact', 'genres_fact', 'actor_1', 'actor_2',
                                                'actor_3', 'actor_4'])
        film_features = table_finale_dummies_3.loc[film_name_contains_dir, X.columns]

    elif film_name_contains_original.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
                                                'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'ratio_votes', 'averageRating', 'actor_1', 'actor_2',
                                                'actor_3', 'actor_4'])
        film_features = table_finale_dummies_3.loc[film_name_contains_original, X.columns]

    elif film_name_contains_actor_1.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                'actor_4', 'actor_2_fact', 'actor_3_fact',
                                                'actor_4_fact', 'director_fact', 'genres_fact'])
        film_features = table_finale_dummies_3.loc[film_name_contains_actor_1, X.columns]

    elif film_name_contains_actor_2.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                'actor_4', 'actor_1_fact', 'actor_3_fact',
                                                'actor_4_fact', 'director_fact', 'genres_fact'])
        film_features = table_finale_dummies_3.loc[film_name_contains_actor_2, X.columns]

    elif film_name_contains_actor_3.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                'actor_4', 'actor_1_fact', 'actor_2_fact',
                                                'actor_4_fact', 'director_fact', 'genres_fact'])
        film_features = table_finale_dummies_3.loc[film_name_contains_actor_3, X.columns]

    elif film_name_contains_actor_4.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'averageRating', 'vote_count', 'vote_average',
                                                'revenue', 'budget', 'num_genres', 'Action', 'Adventure', 'Animation',
                                                'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                                                'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                                                'Mystery', 'News', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War',
                                                'Western', 'inconnu', 'ratio_votes', 'originalTitle', 'startYear',
                                                'genres_x', 'runtime', 'overview', 'original_language', 'poster_path',
                                                'language_fact', 'Director', 'cast', 'actor_1', 'actor_2', 'actor_3',
                                                'actor_4', 'actor_1_fact', 'actor_2_fact', 'actor_3_fact',
                                                'director_fact', 'genres_fact'])
        film_features = table_finale_dummies_3.loc[film_name_contains_actor_4, X.columns]

    elif film_name_contains_over.any():
        X = table_finale_dummies_3.drop(columns=['tconst', 'primaryTitle', 'vote_count', 'vote_average', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
                                                'Director', 'original_language', 'poster_path', 'startYear', 'budget', 'num_genres', 'revenue', 'ratio_votes', 'averageRating', 'actor_1', 'actor_2',
                                                'actor_3', 'actor_4'])
        film_features = table_finale_dummies_3.loc[film_name_contains_over, X.columns]

    else:
        print(f'Film, Director ou Comédien {film_name} non disponible.')

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    film_features_scaled = scaler.transform(film_features)

    model_films = NearestNeighbors(n_neighbors=19)
    model_films.fit(X_scaled)

    neighbors = model_films.kneighbors(film_features_scaled)

    closest_films_index = neighbors[1][0]
    closest_films = table_finale_dummies_3[['originalTitle', 'primaryTitle', 'averageRating', 'vote_count', 'startYear', 'genres_x', 'runtime', 'overview', 'cast', 'Director', 'original_language', 'poster_path']].iloc[closest_films_index]
    # --------------------------------------------------------------------------------------------Top10 2023
    last_released = pd.read_pickle('user_app/data/last-released.pickle')
    # --------------------------------------------------------------------------------------------Top10 2023
    top_films = df_raw[df_raw['startYear'] == '2023'].nlargest(10, 'averageRating')
    top_films = df_raw[df_raw['startYear'] == '2023'].nlargest(10, 'vote_count')
    # --------------------------------------------------------------------------------------------Films Christmas
    films_christmas = df_raw[df_raw['poster_path'] != 'vide.png']
    films_christmas = films_christmas[df_raw['startYear'] > '1990']
    films_christmas = films_christmas[films_christmas['overview'].str.contains('christmas', case=False)]
    films_christmas = films_christmas[films_christmas['original_language'].str.contains('anglais', case=False)]
    films_christmas = films_christmas[films_christmas['genres_x'].str.contains('family', case=False)]
    films_christmas = films_christmas.nlargest(15, 'averageRating')
    # --------------------------------------------------------------------------------------------Langue serbe
    films_serbe = df_raw[df_raw['original_language'] == 'serbe']
    films_serbe = films_serbe.nlargest(3, ['averageRating', 'vote_count'])
    # --------------------------------------------------------------------------------------------context
    context = {
        'backdrop_path': df_home_header['backdrop_path'].values[0],
        'genres': df_home_header['genres'].values[0],
        'original_language': df_home_header['original_language'].values[0],
        'original_title': df_home_header['original_title'].values[0],
        'title': df_home_header['title'].values[0],
        'overview': df_home_header['overview'].values[0],
        'popularity': df_home_header['popularity'].values[0],
        'poster_path': df_home_header['poster_path'].values[0],
        'release_date': df_home_header['release_date'].values[0],
        'tagline': df_home_header['tagline'].values[0],
        'vote_average': df_home_header['vote_average'].values[0],
        'vote_count': df_home_header['vote_count'].values[0],
        'seen_rand_genres': df_rand_seen_movie['genres_x'].values[0],
        'seen_rand_original_language': df_rand_seen_movie['original_language'].values[0],
        'seen_original_title': df_rand_seen_movie['originalTitle'].values[0],
        'seen_title': df_rand_seen_movie['primaryTitle'].values[0],
        'seen_poster_path': df_rand_seen_movie['poster_path'].values[0],
        'already_seen': already_seen,
        'reverse_poster_path': farest_films['poster_path'].values.tolist(),
        'seentry_poster_path': closest_films['poster_path'].values.tolist(),
        'lastreleased_poster_path': last_released['poster_path'].values.tolist(),
        'top_poster_path': top_films['poster_path'].values.tolist(),
        'christmas_poster_path': films_christmas['poster_path'].values.tolist(),
        'serbe_poster_path': films_serbe['poster_path'].values.tolist(),
    }
    print(context['seentry_poster_path'])
    return render(request, 'app/app.html', context)

# --------------------------------------------------------------------------------------------Fonction FILTRE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def filtrer_table(request):
    table_totale_brute = pd.DataFrame(table_finale_dummies_3)

    # Récupérer les values items du filtre
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
    
    # Pagination
    # data_list = table_totale_brute.to_dict() # test pour pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(table_totale_brute, 50)  # nb éléments par page

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
        
    # Passez les données filtrées au modèle
    table_totale_brute = table_totale_brute.head(50)
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

# --------------------------------------------------------------------------------------------Fonction STORE IMAGE
def store_image_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        seen_movies.append(url)

        data = {'message': 'L\'URL a été stockée avec succès.'}
        return JsonResponse(data)
    else:
        # Retournez une erreur si la méthode n'est pas POST
        data = {'message': 'La méthode non autorisée a été utilisée.'}
        return JsonResponse(data, status=405)
