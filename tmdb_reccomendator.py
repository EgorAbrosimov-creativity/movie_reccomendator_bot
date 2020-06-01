from tmdbv3api import TMDb, Movie, Discover
import omdb_parse

tmdb = TMDb()
tmdb.api_key = 'b708e47bb2b4e1f533b18723ce7234bf'

tmdb.language = 'en'

discover = Discover()
movie = Movie()

def popular_list():
    ids_popular = []
    popular_titles = movie.popular()
    for p in popular_titles:
        id_popular = omdb_parse.title_search(p.title)[0]
        ids_popular.append(id_popular)
    return ids_popular
""""""
def top_family_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [10751]
    })
    for i in range(20):
        id = omdb_parse.title_search(mov[i])
        ids.append(id)
    print(ids)
    return ids

def top_comedies_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [35]
    })
    for i in mov:
        id = omdb_parse.title_search(mov.title)[0]
        ids.append(id)
    return ids


def top_romantic_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [10749]
    })
    for i in mov:
        id = omdb_parse.title_search(mov.title)[0]
        ids.append(id)
    return ids

def top_horror_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [27]
    })
    for i in mov:
        id = omdb_parse.title_search(mov.title)[0]
        ids.append(id)
    return ids

def top_documentaries_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [99]
    })
    for i in mov:
        id = omdb_parse.title_search(mov.title)[0]
        ids.append(id)
    return ids

def top_scifi_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [878]
    })
    for i in mov:
        id = omdb_parse.title_search(str(i))
        ids.append(id)
    return ids

def top_war_list():
    ids = []
    mov = discover.discover_movies({
        'sort_by': 'popularity.desc',
        'genre_ids': [10752]
    })
    for i in mov:
        id = omdb_parse.title_search(mov.title)[0]
        ids.append(id)
    return ids

""""""
discover = Discover()
mov_ = discover.discover_movies({
    'sort_by': 'popularity.desc',
    'genre_ids': [1,2, 4]
})

print(mov_)
"""
genres' id's
action 28
animated 16
documentary 99
drama 18
family 10751
fantasy 14
history 36
comedy 35
war 10752
crime 80
music 10402
mystery 9648
romance 10749
sci fi 878
horror 27
TV movie 10770
thriller 53
western 37
adventure 12
"""