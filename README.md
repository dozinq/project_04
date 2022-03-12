# 📌 My Fourth Project 📋

---

##### - Outline : 2022년 3월 4일, 네번째 관통 프로젝트를 수행하였다. Django를 배운 지 하루만에 프로젝트를 하게 되어 매우 당황스러웠지만, 그 동안 제작하였던 프로젝트에 살을 조금 더 덧붙인다고 생각하고 임할 수 있었다. 매우 막막했지만, 그래도 자신감을 가지고 임하려고 하였다. 웹 지식은 아직 너무 얕지만, 그래도 교수님께서 알려주셨던 것들을 되뇌어도 보았고, 같은 반 학우들과 협동하여 잘 마무리 지을 수 있게 되었는데, 이 파일에서는 내가 프로젝트를 수행하면서 느낀 점들에 관해 적어보려고 한다.

---

<br>


# **< Title : "프레임워크를 활용한 웹 페이지 구현" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *요구사항 : 영화 추천 서비스 개발을 위한 화면 구성 및 추천 기능 개발 단계로, API를 통해 영화 데이터를 사용할 수 있는 어플리케이션을 완성시켜야 한다. 기술되어 있는 사항들을 필수적으로 구현해야 한다.*

---

*(프로젝트 파일의 settings.py, urls.py와 base.html 등의 기본 설정은 제외하고 , 앱 파일에 관해서만 작성합니다.)*

<br>

- **movies/urls.py**

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns =[
      path('recommendations/', views.recommendations, name='recommendations'),
      path('', views.index, name="index"),
  ]
  ```

  : 이 프로젝트에서는 앱이 총 1개가 사용되며, url은 두 개의 경우만 제공할 수 있게 된다. 첫째로는 index와 recommendations 페이지이다. 그것에 대해 클라이언트에게 올바른 응답을 줄 수 있도록 url을 조정해 주었다.

<br>

- **movies/views.py**

  ```python
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
  ```

  : views.py에서는 많이 엉켜서 이 프로젝트를 완전하게는 구현할 수 없게 되었다. 제일 첫번째 문제점은 API key를 이용하여 서버에 응답을 요청하는 것을 어떻게 구현해야 할 지 한참을 생각해보고 시도해보다가 결국 실행이 되지 않았고, 두번째 문제점으로는 recommendation 함수의 구성이었다. 매우 복잡하였고, 그로 인해 이 프로젝트를 실패하게 되었다. 일주일이 지난 지금, 다시 해보려고 시도해보았지만 이를 해결한 학우에게 도움을 요청해서 꼭 알아내야 할 필요가 있다고 생각한다.

<br>

---

## ✏After finishing..

>   　　　네 번째 관통 프로젝트를 수행하면서 가장 많은 시간을 들였던 것 같고, 이것을 작성하는 시간은 일주일이 지난 시점인데도, 해결할 수 있는 방법이 떠오르지도 않았고 이를 고쳐야 하는 필요성을 뼈저리게 느낄 뿐이다. 처음으로 프로젝트를 실패하여 너무 자괴감도 큰 것 같다. 실패를 겪고 이를 딛고 일어날 것이라고 스스로 다짐하였다.
>
>   　　​	무엇보다도 값진 경험이 이런 실패가 아닐까 싶다. 해결하지 못한 것에 대한 욕심이 자꾸 생겨나는 것 같다. 배워야 할 것 보다도, 배웠던 것에 대한 확실한 응용이 필요한 시점임을 느낀다.
>
>   　　​	더 나아가고자 한다. 더 성장하고 싶다. 그렇게 갈망하게 된 일주일이었다.