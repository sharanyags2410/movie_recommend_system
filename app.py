import streamlit as st
import pickle
import requests

with open("movie_list.pkl", 'rb') as file:
    movies = pickle.load(file)
    movies_list=movies["title"].values
with open("similarity.pkl", 'rb') as file1:
    similarity = pickle.load(file1)    


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500"+poster_path
    return full_path



st.header("Movie Recommender System")
select_value=st.selectbox("Select movie from dropdows",movies_list)


def recommand(movie):
  index=movies[movies["title"]==movie].index[0]
  distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
  recommand_movie=[]
  recommand_poster=[]
  for i in distance[0:5]:
    movies_id=movies.iloc[i[0]].id
    recommand_movie.append(movies.iloc[i[0]].title)
    recommand_poster.append(fetch_poster(movies_id))
  return recommand_movie,recommand_poster   



if st.button("Show Recommand"):
    movie_name ,movie_poster = recommand(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
        
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
        
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
        
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
        
    with col5:
        st.text(movie_name[4])  
        st.image(movie_poster[4])              
