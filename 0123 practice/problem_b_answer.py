import json
from pprint import pprint


def movie_info(movie, genres):
    # movie에 있는 genre_ids 를 genres에 있는 genre_names로 바꿔야한다.
    result = {}      # result 초기화

    genre_ids = movie['genre_ids'] # movie['genre_ids']를 바꿔주기위해 다른 변수로
    convert = {}

    for i in genres:
        convert[i['id']] = i['name']

    genre_names = []
    for j in genre_ids:
        genre_names += [convert[j]] 

    result['genre_names'] = genre_names
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['poster_path'] = movie['poster_path']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']
    return result


        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))