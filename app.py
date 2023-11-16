import pickle
import streamlit as st
import io

# Function to fetch data from a local file
def fetch_data_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        st.error(f"Failed to load data from file: {file_path}\nError: {e}")
        return None

# Specify the file paths for movie data and similarity data
movie_data_path = 'movie_list.pkl'
similarity_data_path = 'similarity.pkl'

# Load movie data
movie_data = fetch_data_from_file(movie_data_path)
if movie_data:
    try:
        movies = pickle.loads(movie_data)
    except Exception as e:
        st.error(f"Failed to load movie data from file: {movie_data_path}\nError: {e}")
        movies = None

# Load similarity data
similarity_data = fetch_data_from_file(similarity_data_path)
if similarity_data:
    try:
        similarity = pickle.loads(similarity_data)
    except Exception as e:
        st.error(f"Failed to load similarity data from file: {similarity_data_path}\nError: {e}")
        similarity = None


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
