# π My Fourth Project π

---

##### - Outline : 2022λ 3μ 4μΌ, λ€λ²μ§Έ κ΄ν΅ νλ‘μ νΈλ₯Ό μννμλ€. Djangoλ₯Ό λ°°μ΄ μ§ νλ£¨λ§μ νλ‘μ νΈλ₯Ό νκ² λμ΄ λ§€μ° λΉν©μ€λ¬μ μ§λ§, κ·Έ λμ μ μνμλ νλ‘μ νΈμ μ΄μ μ‘°κΈ λ λ§λΆμΈλ€κ³  μκ°νκ³  μν  μ μμλ€. λ§€μ° λ§λ§νμ§λ§, κ·Έλλ μμ κ°μ κ°μ§κ³  μνλ €κ³  νμλ€. μΉ μ§μμ μμ§ λλ¬΄ μμ§λ§, κ·Έλλ κ΅μλκ»μ μλ €μ£Όμ¨λ κ²λ€μ λλμ΄λ λ³΄μκ³ , κ°μ λ° νμ°λ€κ³Ό νλνμ¬ μ λ§λ¬΄λ¦¬ μ§μ μ μκ² λμλλ°, μ΄ νμΌμμλ λ΄κ° νλ‘μ νΈλ₯Ό μννλ©΄μ λλ μ λ€μ κ΄ν΄ μ μ΄λ³΄λ €κ³  νλ€.

---

<br>


# **< Title : "νλ μμν¬λ₯Ό νμ©ν μΉ νμ΄μ§ κ΅¬ν" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *μκ΅¬μ¬ν­ : μν μΆμ² μλΉμ€ κ°λ°μ μν νλ©΄ κ΅¬μ± λ° μΆμ² κΈ°λ₯ κ°λ° λ¨κ³λ‘, APIλ₯Ό ν΅ν΄ μν λ°μ΄ν°λ₯Ό μ¬μ©ν  μ μλ μ΄νλ¦¬μΌμ΄μμ μμ±μμΌμΌ νλ€. κΈ°μ λμ΄ μλ μ¬ν­λ€μ νμμ μΌλ‘ κ΅¬νν΄μΌ νλ€.*

---

*(νλ‘μ νΈ νμΌμ settings.py, urls.pyμ base.html λ±μ κΈ°λ³Έ μ€μ μ μ μΈνκ³  , μ± νμΌμ κ΄ν΄μλ§ μμ±ν©λλ€.)*

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

  : μ΄ νλ‘μ νΈμμλ μ±μ΄ μ΄ 1κ°κ° μ¬μ©λλ©°, urlμ λ κ°μ κ²½μ°λ§ μ κ³΅ν  μ μκ² λλ€. μ²«μ§Έλ‘λ indexμ recommendations νμ΄μ§μ΄λ€. κ·Έκ²μ λν΄ ν΄λΌμ΄μΈνΈμκ² μ¬λ°λ₯Έ μλ΅μ μ€ μ μλλ‘ urlμ μ‘°μ ν΄ μ£Όμλ€.

<br>

- **movies/views.py**

  ```python
  from django.shortcuts import render
  import requests
  
  def index(request):
      API_KEY = '' # (api_key κ°μ λ§μ§λ§ μμ μ λͺ¨λ μ­μ νμμ΅λλ€.)
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
      # # μμ§νκ³ μ νλ μ λ³΄κ° λ΄κ²¨ μλ URLμ μμ±νμλ€.
      # URL = 'https://api.themoviedb.org/3/movie/popular'
      # # μλμ params λμλλ¦¬λ₯Ό ν΅ν΄ μμ²­ λ³μλ₯Ό κΈ°μ¬ν΄ μ£Όμμ΅λλ€.
      # params = {
      # 'api_key' : '', # (api_key κ°μ λ§μ§λ§ μμ μ λͺ¨λ μ­μ νμμ΅λλ€.)
      # 'language' : 'ko-KR',
      # 'region' : 'KR'
      # }
      # # μμ²­ κ²°κ³Όλ₯Ό μ μ₯νμλ€.
      # response = requests.get(URL, params = params)
      # # data λ³μμ jsonνμμΌλ‘ μ μ₯νμλ€.
      # data = response.json()
      # # λ°νκ°μ μ μ₯ν  λΉ λ¦¬μ€νΈλ₯Ό λ§λ€μ΄μ£Όμλ€.
      # ans_lst = []
      # # 'results'ν­λͺ©μ κ°(μν μ λ³΄λ€)μ data_lstμ λ΄μλ€.
      # data_lst = data.get('results')
      # # λ°λ³΅λ¬Έμ ν΅ν΄ μΈλ±μ€κ° νλνλ κ²ν ν  μ μλλ‘ νμλ€.
      # for index in data_lst:
      #     # μΈλ±μ€κ° μ»μ νμ μ 8μ΄μμΈ κ°λ€λ§ μΆμΆν  μ μλλ‘ νμλ€.
      #     if index.get('vote_average') >= 8:
      #         ans_lst.append(index)
      # # λ΄κ²¨μ§ λ¦¬μ€νΈλ₯Ό λ°ννμλ€.    
      # return render(request, 'movies/recommendation.html')
      return render(request, 'movies/recommendations.html')
  ```

  : views.pyμμλ λ§μ΄ μμΌμ μ΄ νλ‘μ νΈλ₯Ό μμ νκ²λ κ΅¬νν  μ μκ² λμλ€. μ μΌ μ²«λ²μ§Έ λ¬Έμ μ μ API keyλ₯Ό μ΄μ©νμ¬ μλ²μ μλ΅μ μμ²­νλ κ²μ μ΄λ»κ² κ΅¬νν΄μΌ ν  μ§ νμ°Έμ μκ°ν΄λ³΄κ³  μλν΄λ³΄λ€κ° κ²°κ΅­ μ€νμ΄ λμ§ μμκ³ , λλ²μ§Έ λ¬Έμ μ μΌλ‘λ recommendation ν¨μμ κ΅¬μ±μ΄μλ€. λ§€μ° λ³΅μ‘νμκ³ , κ·Έλ‘ μΈν΄ μ΄ νλ‘μ νΈλ₯Ό μ€ν¨νκ² λμλ€. μΌμ£ΌμΌμ΄ μ§λ μ§κΈ, λ€μ ν΄λ³΄λ €κ³  μλν΄λ³΄μμ§λ§ μ΄λ₯Ό ν΄κ²°ν νμ°μκ² λμμ μμ²­ν΄μ κΌ­ μμλ΄μΌ ν  νμκ° μλ€κ³  μκ°νλ€.

<br>

---

## βAfter finishing..

>   γγγλ€ λ²μ§Έ κ΄ν΅ νλ‘μ νΈλ₯Ό μννλ©΄μ κ°μ₯ λ§μ μκ°μ λ€μλ κ² κ°κ³ , μ΄κ²μ μμ±νλ μκ°μ μΌμ£ΌμΌμ΄ μ§λ μμ μΈλ°λ, ν΄κ²°ν  μ μλ λ°©λ²μ΄ λ μ€λ₯΄μ§λ μμκ³  μ΄λ₯Ό κ³ μ³μΌ νλ νμμ±μ λΌμ λ¦¬κ² λλ λΏμ΄λ€. μ²μμΌλ‘ νλ‘μ νΈλ₯Ό μ€ν¨νμ¬ λλ¬΄ μκ΄΄κ°λ ν° κ² κ°λ€. μ€ν¨λ₯Ό κ²ͺκ³  μ΄λ₯Ό λκ³  μΌμ΄λ  κ²μ΄λΌκ³  μ€μ€λ‘ λ€μ§νμλ€.
>
>   γγβ	λ¬΄μλ³΄λ€λ κ°μ§ κ²½νμ΄ μ΄λ° μ€ν¨κ° μλκΉ μΆλ€. ν΄κ²°νμ§ λͺ»ν κ²μ λν μμ¬μ΄ μκΎΈ μκ²¨λλ κ² κ°λ€. λ°°μμΌ ν  κ² λ³΄λ€λ, λ°°μ λ κ²μ λν νμ€ν μμ©μ΄ νμν μμ μμ λλλ€.
>
>   γγβ	λ λμκ°κ³ μ νλ€. λ μ±μ₯νκ³  μΆλ€. κ·Έλ κ² κ°λ§νκ² λ μΌμ£ΌμΌμ΄μλ€.