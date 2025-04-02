import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('cleaned_movies.csv')
    return df

# Function to extract genres
def get_unique_genres(df):
    genres = df['genres'].str.split('|').explode().str.strip().unique()
    return sorted(genres)


def main():
    st.title("Movie Explorer by Genre")

    df = load_data()
    
    genres = get_unique_genres(df)

    selected_genre = st.selectbox("Select Genre", genres)
    
    filtered_movies = df[df['genres'].str.contains(selected_genre, case=False, na=False)]

    if not filtered_movies.empty:
        st.subheader(f"Movies in {selected_genre} Genre")
        st.dataframe(filtered_movies[['title', 'year']])
    else:
        st.write(f"No movies found for the genre: {selected_genre}")

if __name__ == "__main__":
    main()
