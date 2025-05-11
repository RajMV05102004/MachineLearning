import streamlit as st
import pickle

# Load data
movies = pickle.load(open(r'D:\ML Projects\MovieRecommendationSystem\movies.pkl', 'rb'))
movies_list = movies['title']
similarity = pickle.load(open(r'D:\ML Projects\MovieRecommendationSystem\similarity.pkl', 'rb'))

# Recommend function (only names)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_list = []
    for i in distances[1:6]:
        recommended_list.append(movies.iloc[i[0]].title)
    return recommended_list

# Streamlit UI
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select the Movie you watched to get recommended ',
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie_name)

    st.subheader("Top 5 Recommended Movies:")
    for idx, name in enumerate(recommended_movie_names, start=1):
        st.write(f"{idx}. {name}")
