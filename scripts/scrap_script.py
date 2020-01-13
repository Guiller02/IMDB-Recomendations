#!/usr/bin/env python
# coding: utf-8

# ## Imports

# In[1]:


from bs4 import BeautifulSoup as bs
import requests

import pandas as pd


# ## Creating a function with loop for insert on each array

# In[2]:


def scrap_data(option):
    if option == 1:
        
        for content in movie_contents:
            if content.find('span', attrs = {'class':'certificate'}) is not None:
            # The name of the movie
                movie_name = content.h3.a.text
                movies_names.append(movie_name)
            # The year of the movie
                movie_year = content.h3.find('span', class_ = 'lister-item-year').text
                if movie_year[1].isdigit() == False:
                    movie_year = movie_year.strip('(I) (')
                else:
                    movie_year = movie_year.strip('()')
                movies_years.append(movie_year)
            # The rating of the movie
                movie_imdb = float(content.strong.text)
                movies_imdb_ratings.append(movie_imdb)
            # The number of votes of the movie
                movie_vote = content.find('span', attrs = {'name':'nv'})['data-value']
                movies_votes.append(int(movie_vote))
            #the Age rating of the movie
                movie_age_rating = content.find('span', attrs = {'class':'certificate'}).text
                movies_ages.append(movie_age_rating)
            #The runtime of the movie
                movie_runtime = content.find('span', attrs = {'class':'runtime'}).text.strip(' min')
                movies_runtimes.append(movie_runtime)
            #The genres of the movie
                movie_genre = content.find('span', attrs = {'class':'genre'}).text.strip()
                movies_genres.append(movie_genre)
            #The director of the movie
                movie_director = content.find('p',class_='').find_all('a')[0].text
                movies_directors.append(movie_director)
            #The actors from the movie
                if len(content.find('p',class_='').find_all('a'))>=5:
                    movies_actors1 = content.find('p',class_='').find_all('a')[1].text
                    movies_actors2 = content.find('p',class_='').find_all('a')[2].text
                    movies_actors3 = content.find('p',class_='').find_all('a')[3].text
                    movies_actors4 = content.find('p',class_='').find_all('a')[4].text
                elif len(content.find('p',class_='').find_all('a'))==4:
                    movies_actors1 = content.find('p',class_='').find_all('a')[1].text
                    movies_actors2 = content.find('p',class_='').find_all('a')[2].text
                    movies_actors3 = content.find('p',class_='').find_all('a')[3].text
                    movies_actors4 = 'none'
                elif len(content.find('p',class_='').find_all('a'))==3:
                    movies_actors1 = content.find('p',class_='').find_all('a')[1].text
                    movies_actors2 = content.find('p',class_='').find_all('a')[2].text
                    movies_actors3 = 'none'
                    movies_actors4 = 'none'
                elif len(content.find('p',class_='').find_all('a'))==2:
                    movies_actors1 = content.find('p',class_='').find_all('a')[1].text
                    movies_actors2 = 'none'
                    movies_actors3 = 'none'
                    movies_actors4 = 'none'
                elif len(content.find('p',class_='').find_all('a'))==1:
                    movies_actors1 = 'none'
                    movies_actors2 = 'none'
                    movies_actors3 = 'none'
                    movies_actors4 = 'none'
                movie_actors = movies_actors1+', '+movies_actors2+', '+movies_actors3+', '+movies_actors4
                movies_stars.append(movie_actors)
                    
                
                
    elif option == 2:
        for content in serie_contents:
        # The name of the serie
            series_name = content.h3.a.text
            series_names.append(series_name)
        # The year of the serie
            series_year = content.h3.find('span', class_ = 'lister-item-year').text
            series_years.append(series_year)
        # The rating of the serie
            series_imdb = float(content.strong.text)
            series_imdb_ratings.append(series_imdb)
        # The number of votes of the serie
            series_vote = content.find('span', attrs = {'name':'nv'})['data-value']
            series_votes.append(int(series_vote))
        #the Age rating of the serie
            if content.find('span', attrs = {'class':'certificate'}):
                series_age_rating = content.find('span', attrs = {'class':'certificate'}).text
                series_ages.append(series_age_rating)
            else:
                series_age_rating = 'none'
                series_ages.append(series_age_rating)
        #The runtime of the serie
            if content.find('span', attrs = {'class':'runtime'}):
                series_runtime = content.find('span', attrs = {'class':'runtime'}).text.strip(' min')
                series_runtimes.append(series_runtime)
            else:
                series_runtime = 'none'
                series_runtimes.append(series_runtime)
        #The genres of the serie
            series_genre = content.find('span', attrs = {'class':'genre'}).text.strip()
            series_genres.append(series_genre)
        #The director of the serie
            serie_director = content.find('p',class_='').find_all('a')[0].text
            series_directors.append(serie_director)
        #The actors from the serie
            if len(content.find('p',class_='').find_all('a'))>=4:
                series_actors1 = content.find('p',class_='').find_all('a')[0].text
                series_actors2 = content.find('p',class_='').find_all('a')[1].text
                series_actors3 = content.find('p',class_='').find_all('a')[2].text
                series_actors4 = content.find('p',class_='').find_all('a')[3].text
            elif len(content.find('p',class_='').find_all('a'))==3:
                series_actors1 = content.find('p',class_='').find_all('a')[0].text
                series_actors2 = content.find('p',class_='').find_all('a')[1].text
                series_actors3 = content.find('p',class_='').find_all('a')[2].text
                series_actors4 = 'none'
            elif len(content.find('p',class_='').find_all('a'))==2:
                series_actors1 = content.find('p',class_='').find_all('a')[0].text
                series_actors2 = content.find('p',class_='').find_all('a')[1].text
                series_actors3 = 'none'
                series_actors4 = 'none'
            elif len(content.find('p',class_='').find_all('a'))==1:
                series_actors1 = content.find('p',class_='').find_all('a')[0].text
                series_actors2 = 'none'
                series_actors3 = 'none'
                series_actors4 = 'none'
            serie_actors = series_actors1+', '+series_actors2+', '+series_actors3+', '+series_actors4
            series_stars.append(serie_actors)

    elif option == 3:
        for content in game_contents:    
        # The name of the game
            game_name = content.h3.a.text
            games_names.append(game_name)
        # The year of the game
            game_year = content.h3.find('span', class_ = 'lister-item-year').text.strip('( Video Game)')
            games_years.append(game_year)
        # The rating of the game
            game_imdb = float(content.strong.text)
            games_imdb_ratings.append(game_imdb)
        # The number of votes of the game
            game_vote = content.find('span', attrs = {'name':'nv'})['data-value']
            games_votes.append(int(game_vote))
        #the Age rating of the game
            if content.find('span', attrs = {'class':'certificate'}):
                game_age_rating = content.find('span', attrs = {'class':'certificate'}).text
                games_ages.append(game_age_rating)
            else:
                game_age_rating = 'none'
                games_ages.append(game_age_rating)
        #The genres of the game
            if content.find('span', attrs = {'class':'genre'}):
                game_genre = content.find('span', attrs = {'class':'genre'}).text.strip()
                games_genres.append(game_genre)
            else:
                game_genre = 'none'
                games_genres.append(game_genre)
            if content.find('p',class_='').find_all('a'):
                game_director = content.find('p',class_='').find_all('a')[0].text
            else:
                game_director = 'none'
            games_directors.append(game_director)
            


# Here i'm creating an empty array of each entertainment font, and getting the url and adding a loop to call the scrap data and change the url untill the size of the arrays is 1000 

# In[3]:


movie_genre = ''

movies_names = []
movies_years = []
movies_imdb_ratings = []
movies_metascores = []
movies_votes = []
movies_ages = []
movies_runtimes = []
movies_genres = []
movies_directors = []
movies_stars = []

requisition = 0
while len(movies_names) < 1000:
    url_movie = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2015-01-01,2020-12-31&genres='+movie_genre+'&sort=num_votes,desc&count=250&start='+str(requisition)
    movies_req = requests.get(url_movie)
    soup_movie = bs(movies_req.text, 'lxml')
    requisition = requisition+ 251
    movie_contents = soup_movie.find_all('div', class_ = 'lister-item mode-advanced')
    scrap_data(1)


# In[4]:


serie_genre = ''

series_names = []
series_years = []
series_imdb_ratings = []
series_metascores = []
series_votes = []
series_ages = []
series_runtimes = []
series_genres = []
series_directors = []
series_stars = []

requisition = 0
while len(series_names) < 1000:
    url_serie = 'https://www.imdb.com/search/title/?title_type=tv_series&release_date=2015-01-01,2020-12-31&genres='+serie_genre+'&sort=num_votes,desc&count=250&start='+str(requisition)
    series_req = requests.get(url_serie)
    soup_serie = bs(series_req.text, 'lxml')
    requisition = requisition+ 251
    serie_contents = soup_serie.find_all('div', class_ = 'lister-item mode-advanced')
    scrap_data(2)


# In[5]:


game_genre = ''

games_names = []
games_years = []
games_imdb_ratings = []
games_metascores = []
games_votes = []
games_ages = []
games_runtimes = []
games_genres = []
games_directors = []

game_requisition = 0
while len(games_names) < 1000:
    url_game = 'https://www.imdb.com/search/title/?title_type=video_game&release_date=2015-01-01,2019-12-31&genres=&sort=num_votes,desc&count=250&start='+str(game_requisition)
    games_req = requests.get(url_game)
    soup_game = bs(games_req.text, 'lxml')
    game_requisition = game_requisition+ 251
    game_contents = soup_game.find_all('div', class_ = 'lister-item mode-advanced')
    scrap_data(3)


# Adding the arrays to a dataframe

# In[6]:


movies_dataframe = pd.DataFrame({
'name': movies_names,
'year': movies_years,
'imdb': movies_imdb_ratings,
'number_votes': movies_votes,
'age_rating':movies_ages,
'runtime':movies_runtimes,
'genres':movies_genres,
'directors':movies_directors,
'actors':movies_stars
})

series_dataframe = pd.DataFrame({
'name': series_names,
'year': series_years,
'imdb': series_imdb_ratings,
'number_votes': series_votes,
'age_rating':series_ages,
'runtime':series_runtimes,
'genres':series_genres,
'directors':series_directors,
'actors':series_stars
})

games_dataframe = pd.DataFrame({
'name': games_names,
'year': games_years,
'imdb': games_imdb_ratings,
'number_votes': games_votes,
'age_rating':games_ages,
'genres':games_genres,
'directors':games_directors
})


# And look what is in every dataframe

# In[7]:


movies_dataframe.head()


# In[8]:


series_dataframe.head()


# In[9]:


games_dataframe.head()


# And creating a csv with this dataframes

# In[10]:


movies_dataframe.to_csv('imdb_movies.csv')
series_dataframe.to_csv('imdb_series.csv')
games_dataframe.to_csv('imdb_games.csv')

