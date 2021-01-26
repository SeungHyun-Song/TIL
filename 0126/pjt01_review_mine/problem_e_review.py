import json

def dec_movies(movies):
    result = []   # 12월에 개봉한 영화 리스트

    for movie in movies:
        # movie id를 기준으로 movie 상세정보 파일 읽기 (movie_id.json 파일)
        movie_id = movie.get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_detail = json.load(movie_json)

        # 12월에 개봉한 movie title 찾기
        movie_release_date = movie_detail['release_date']
        if movie_release_date[5:7] == '12':
            movie_title = movie['title']
            result.append(movie_title)

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))