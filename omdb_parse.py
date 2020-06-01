import omdb

API_KEY = "fff3e250"

omdb.set_default('apikey', API_KEY)

def title_search(title):
    results = omdb.search(title)
    result_ids = []
    for i in results:
        result_ids.append(i['imdb_id'])
    return result_ids


def title_year_search(title, year):                         # ТУТ ПОФИКСИТЬ РАЗБИЕНИЕ
    results = omdb.search(title, year=year)
    result_ids = []
    for i in results:
        result_ids.append(results[i]['imdb_id'])            #ТУТ ПОФИКСИТЬ ИНДЕКСАЦИЮ
    return result_ids


def get_by_id(id_movie):
    return omdb.imdbid(id_movie, fullplot=True, tomatoes=True)


def construct_movie_description(id_movie):
    mov = get_by_id(id_movie)
    desc_title = mov['title'] + '\n'
    desc_country = mov['country'] + '\n'
    desc_genre = mov['genre'] + '\n'
    desc_language = mov['language'] + '\n'
    desc_year = 'Year: ' + mov['year'] + '\n'
    desc_director = 'Directed: ' + mov['director'] + '\n'
    desc_scores_imdb = 'Scores:\n' + 'IMDB rating: ' + mov['imdb_rating'] + '⭐ \ 10' + '\n'
    desc_scores_tomatoes = '🍅 Rotten tomatoes rating: ' + mov['tomato_rating'] + '\n'
    desc_plot = mov['plot']
    desc_poster = 'Poster link: ' + mov['poster'] + '\n'

    desc = desc_title + desc_country + desc_genre + desc_language + desc_year + desc_director + desc_scores_imdb +\
           desc_scores_tomatoes + desc_plot +desc_poster
    return desc


def construct_following_info(id_movie):
    mov = get_by_id(id_movie)
    first_line = 'Further information: \n'
    second_line = 'Website: ' + mov['website'] + '\n'
    third_line = 'Poster link: ' + mov['poster'] + '\n'
    following_info = first_line + second_line + third_line
    return following_info


