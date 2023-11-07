import pickle
import streamlit as st
import requests
import io

# Define the URLs for movie data and similarity data
pickle_url = 'https://github.com/Avanish1202/Data-Science-/raw/main/movie_list.pkl'
similarity_url = 'https://github.com/Avanish1202/Data-Science-/raw/main/similarity.pkl'

# Function to fetch the movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # Fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Streamlit app
st.header('Movie Recommender System')

# Attempt to load the movie data from the URL
response = requests.get(pickle_url)
if response.status_code == 200:
    # Load the data using the io module
    movies = pickle.load(io.BytesIO(response.content))
    # Attempt to load the similarity data from the URL
    response = requests.get(similarity_url)
    if response.status_code == 200:
        similarity = pickle.load(io.BytesIO(response.content))
    else:
        st.error("Failed to load similarity data. Please check the URL.")
else:
    st.error("Failed to load movie data. Please check the URL.")

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
