import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
from sklearn.manifold import TSNE

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def recommend_tracks(song_vectors, n_songs=10):
    data = pd.read_csv(r"Bot/data.csv")
    number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
    metadata_cols = ['name', 'year', 'artists']
    
    song_matrix = np.array(list(song_vectors))
    song_center = np.mean(song_matrix, axis=0)
    
    song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=20, verbose=False))], verbose=False)

    X = data.select_dtypes(np.number)
    number_cols = list(X.columns)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data['cluster_label'] = song_cluster_labels
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs + 1][0])
    rec_songs = data.iloc[index]
    
    return rec_songs[metadata_cols][1:]