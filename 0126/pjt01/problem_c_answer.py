import json
from pprint import pprint


def movie_info(movies, genres):
    '''
    {
        'adult': False,
        'backdrop_path': '/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg',
        'genre_ids': [18, 80],
        'id': 278,
        'original_language': 'en',
        'original_title': 'The Shawshank Redemption',
        'overview': '.............,
        'popularity': 67.931,
        'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
        'release_date': '1995-01-28',
        'title': '쇼생크 탈출',
        'video': False,
        'vote_average': 8.7,
        'vote_count': 18040
    }

    {'id': 28, 'name': 'Action'},
    '''
    # 1. 결과값 변수 초기화
    result = []

    # 2. movies 리스트 순회 -> 원하는 정보만 추출
    for movie in movies:
        # 3. 원하는 데이터만 추출한 new_movie 딕셔너리 생성
        new_movie = {
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'poster_path': movie.get('poster_path'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average'),
            'genre_names': [],
        }

        # 4. new_movie의 genre_names 리스트 만들기
        genre_ids = movie.get('genre_ids')
        for genre in genres:
            # for genre_id in genre_ids:
            if genre['id'] in genre_ids:
                new_movie['genre_names'].append(genre['name'])

        # 5. 가공이 끝난 new_movie 딕셔너리를 결과값 리스트에 추가
        result.append(new_movie)
    
    # 6. for문을 빠져나와 가공이 끝난 영화 데이터들이 담겨있는 result 리스트를 Return
    return result
    
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))