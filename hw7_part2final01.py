import json

def find_movies_in_range(movies, min_year, max_year):
    ''' find movies in range of min year and max year '''
    m = {}
    for id, info in movies.items():
        movie_year = info['movie_year']
        if min_year <= movie_year <= max_year:
            m[id] = info
    return m


def find_movies_of_genre(movies, genre):
    ''' find movies of genre '''
    m = {}
    for id, info in movies.items():
        genres = info['genre']
        for g in genres:
            if g.lower() == genre.lower() and id not in m:
                m[id] = info
    return m


def score_movies(movies, ratings, w1, w2):
    ''' score the movies '''
    m = []
    for id, info in movies.items():
        if id not in ratings or len(ratings[id]) < 3:
            continue
        score = (w1 * info['rating'] + w2 * (sum(ratings[id]) / len(ratings[id]))) / (w1 + w2)
        m.append((score, id))
    if not m:
        return False
    m.sort(reverse=True)
    print('Best:')
    best_movie = movies[m[0][1]]
    print('        Released in %d, %s has a rating of %.2f' % (best_movie['movie_year'], best_movie['name'], m[0][0]))
    print()
    print('Worst:')
    worst_movie = movies[m[-1][1]]
    print('        Released in %d, %s has a rating of %.2f' % (worst_movie['movie_year'], worst_movie['name'], m[-1][0]))
    return True

def get_genre(genre):
    if genre.lower() == 'sci-fi':
        return 'Sci-Fi'
    else:
        return genre[0].upper() + genre[1:].lower()

if __name__ == '__main__':
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    min_year = input('Min year => ').strip()
    print(min_year)
    min_year = int(min_year)
    max_year = input('Max year => ').strip()
    print(max_year)
    max_year = int(max_year)
    imdb = input('Weight for IMDB => ').strip()
    print(imdb)
    imdb = float(imdb)
    twitter = input('Weight for Twitter => ').strip()
    print(twitter)
    twitter = float(twitter)

    genre = input('\nWhat genre do you want to see? ').strip()
    genre1 = get_genre(genre)
    while genre.lower() != 'stop':
        print(genre)
        print()
        m = find_movies_in_range(movies, min_year, max_year)
        m = find_movies_of_genre(m, genre1)
        if len(m) == 0:
            print('No %s movie found in %d through %d' % (genre1, min_year, max_year))
        else:
            if not score_movies(m, ratings, imdb, twitter):
                print('No %s movie found in %d through %d' % (genre1, min_year, max_year))
        genre = input('\nWhat genre do you want to see? ').strip()
        genre1 = get_genre(genre)  
    while genre.lower() == 'stop':
        print(genre)
        break

