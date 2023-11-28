from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import os

df_knn = pd.read_pickle('user_app/data/table_totale_dum.pickle')

from sklearn.preprocessing import StandardScaler
def reco_sys(film_name):

    X = df_knn.drop(columns = ['tconst', 'primaryTitle', 'director', 'vote_count', 'vote_average', 'averageRating'])

    if film_name not in df_knn['primaryTitle'].values:
        print(f"The film '{film_name}' is not found.")
        return

    film_features = df_knn.loc[df_knn['primaryTitle'] == film_name, X.columns]
    if film_features.empty:
        print(f"The features for the film '{film_name}' are not available.")
        return

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    film_features_scaled = scaler.transform(film_features)

    model_films = NearestNeighbors(n_neighbors= 6)
    model_films.fit(X_scaled)

    neighbors = model_films.kneighbors(film_features_scaled)

    closest_films_index = neighbors[1][0][1:]
    closest_films = df_knn['primaryTitle'].iloc[closest_films_index]
    distances = neighbors[0][0][1:]

    print(f'les films les plus proches de {film_name} sont : \n{closest_films}')
    print("Respectives distances : ", distances)
    return HttpResponse("Training done")