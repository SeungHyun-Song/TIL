import requests

class URLMaker():
    base_url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category, feature, **kwargs): # get_url : url 만들어서 반환하라는 역할뿐
        # **kwargs 넣어주는 이유? 인자가 계속해서 바뀌는 경우에 대비 & 어떤 인자가 들어올지 모름 (key, value쌍이 모두 다름)
        url = f'{URLMaker.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'
        return url  # 인자 받아서 url 편하게 만드는 함수


    def movie_id(self, title):
        # /search/movie  search는 category에, movie는 feature에
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie_dict = res.json()

        if movie_dict.get('results'):
            return movie_dict.get('results')[0].get('id')
        else:
            return None

# 위에서 만든 url에서 데이터를 호출하게끔 만든 함수

maker = URLMaker('7108d7a0290beb4c2d99634b041130ba')
# print(maker.get_url('movie', 'top_rated'))
print(maker.get_url('genre', 'movie/list'))
print(maker.movie_id('기생충'))