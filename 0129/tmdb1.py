class URLMaker():
    base_url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category, feature): # get_url : url 만들어서 반환하라는 역할뿐
        url = f'{URLMaker.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'
        return url

maker = URLMaker('7108d7a0290beb4c2d99634b041130ba')
print(maker.get_url('movie', 'top_rated'))
print(maker.get_url('movie', 'popular'))