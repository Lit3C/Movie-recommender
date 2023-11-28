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
    context = {'a':'Hello World'}
    return render(request, 'app/search.html', context)

df_table_neighbor = pd.read_pickle('user_app/data/table_finale_dummies.pickle')
from sklearn.preprocessing import StandardScaler
def reco_sys(request):
    print(request)
    if request.method == 'POST':
        film_name = request.POST['film-search']
        print("HellooooWorld")
        print(film_name)
        film_name_contains = df_table_neighbor['originalTitle'].str.contains(film_name, case= False)

        X = df_table_neighbor.drop(columns = ['tconst', 'primaryTitle', 'director_x', 'vote_count', 'vote_average', 'averageRating', 'originalTitle', 'genres_x','runtime', 'overview', 'cast',
        'director_y', 'original_language', 'poster_path', 'startYear'])

        film_features = df_table_neighbor.loc[film_name_contains, X.columns]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        film_features_scaled = scaler.transform(film_features)

        model_films = NearestNeighbors(n_neighbors= 9)
        model_films.fit(X_scaled)

        neighbors = model_films.kneighbors(film_features_scaled)

        closest_films_index = neighbors[1][0]
        closest_films = df_table_neighbor[['originalTitle', 'averageRating', 'vote_count', 'startYear', 'genres_x', 'runtime', 'overview', 'cast', 'director_y', 'original_language', 'poster_path']].iloc[closest_films_index]
        distances = neighbors[0][0]

        context = {
            'film_name': film_name, 
            'closest_films': closest_films,
            'distances': distances
        }
    return render(request, 'app/search.html', context)
    
    

def list(request):
    return render(request, 'app/list.html')

def booking(request):
    return render(request, 'app/booking.html')

def settings(request):
    return render(request, 'app/settings.html')

def stats(request):
    return render(request, 'app/stats.html')
