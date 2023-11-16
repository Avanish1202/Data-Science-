import pickle
import streamlit as st
import requests
import io

# Function to fetch data from a URL
def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Failed to load data from URL: {url}")
        return None

# Specify the URLs for movie data and similarity data
movie_data_url = 'movie_list.pkl'
similarity_data_url = 'similarity.pkl'

# Load movie data
movie_data = fetch_data_from_url(movie_data_url)
if movie_data:
    movies = pickle.load(io.BytesIO(movie_data))

# Load similarity data
similarity_data = fetch_data_from_url(similarity_data_url)
if similarity_data:
    similarity = pickle.load(io.BytesIO(similarity_data))

# Define the Streamlit app
def main():
    st.header('Movie Recommender System')
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

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

# Run the Streamlit app
if __name__ == '__main__':
    main()
