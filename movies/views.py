from django.shortcuts import render
import requests

def index(request):
    API_KEY = '' # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
    IMAGE_URL = 'https://image.tmdb.org/t/p/original'

    params = {
        'api_key': API_KEY,
        'page': 1,
        'language': 'ko',
    }

    response = requests.get(BASE_URL, params=params).json()
    movie_list = response.get('results')[:6]

    context = {
        'movie_list': movie_list,
        'image_url': IMAGE_URL,
    }
    
    return render(request, 'movies/index.html', context)

def recommendations(request):
    # # 수집하고자 하는 정보가 담겨 있는 URL을 작성하였다.
    # URL = 'https://api.themoviedb.org/3/movie/popular'
    # # 아래의 params 딕셔녀리를 통해 요청 변수를 기재해 주었습니다.
    # params = {
    # 'api_key' : '', # (api_key 값은 마지막 시점에 모두 삭제하였습니다.)
    # 'language' : 'ko-KR',
    # 'region' : 'KR'
    # }
    # # 요청 결과를 저장하였다.
    # response = requests.get(URL, params = params)
    # # data 변수에 json형식으로 저장하였다.
    # data = response.json()
    # # 반환값을 저장할 빈 리스트를 만들어주었다.
    # ans_lst = []
    # # 'results'항목의 값(영화 정보들)을 data_lst에 담았다.
    # data_lst = data.get('results')
    # # 반복문을 통해 인덱스가 하나하나 검토할 수 있도록 하였다.
    # for index in data_lst:
    #     # 인덱스가 얻은 평점을 8이상인 값들만 추출할 수 있도록 하였다.
    #     if index.get('vote_average') >= 8:
    #         ans_lst.append(index)
    # # 담겨진 리스트를 반환하였다.    
    # return render(request, 'movies/recommendation.html')
    return render(request, 'movies/recommendations.html')