
# import libraries

import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open("movies_dict.pkl" ,"rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl" ,"rb"))

def recommender(movie):
    
    # First fetch the movie title index from which we have to recommend next 5 movies
    movies_index = movies[movies["title"]== movie].index[0]
    
    # calcualte the similarity score of that movie with another movies
    distances = similarity[movies_index]
    
    # sort the list without disturbing its index pos using enumerate and list also fetch top 5 movie in a reverse order
    movies_list = sorted(list(enumerate(distances)) ,reverse= True , key = lambda x : x[1])[1:6]
    

    recommended_movies  = []
    for i in movies_list:
        
        # print high similarity score movies with title with index pos as a input
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies




st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    " Select Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommender(selected_movie_name)
    for i in recommendations:
        st.write(i)