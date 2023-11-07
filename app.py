import pickle
import streamlit as st
import requests
import io

# Function to fetch the movie poster
def fetch_poster(movie_id):
    # Your fetch_poster function code here

# Function to recommend movies
def recommend(movie):
    # Your recommend function code here

# Streamlit app
st.header('Movie Recommender System')

# Download the pickle file from GitHub
pickle_url = 'https://github.com/Avanish1202/Data-Science-/raw/main/movie_list.pkl'
response = requests.get(pickle_url)
if response.status_code == 200:
    # Load the data using the io module
    movies = pickle.load(io.BytesIO(response.content))
else:
    st.error("Failed to load movie data. Please check the URL.")

# Download the similarity pickle file from GitHub
similarity_url = 'https://github.com/Avanish1202/Data-Science-/raw/main/similarity.pkl'
response = requests.get(similarity_url)
if response.status_code == 200:
    # Load the data using the io module
    similarity = pickle.load(io.BytesIO(response.content))
else:
    st.error("Failed to load similarity data. Please check the URL.")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
