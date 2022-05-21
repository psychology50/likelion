'''
1. HTTP

철수가 네이버 블로그에 **새로운** 글을 작성하고, ‘작성 완료’ 버튼을 눌렀다.
이때, 웹서버에 전달된 HTTP 요청은 무엇인가요?

1️⃣  GET  2️⃣  POST  3️⃣  UPLOAD  4️⃣  DELETE  5️⃣  UPDATE
'''

# answer : (2) Post

# === get VS post === #
# get : 서버 데이터 요청, get으로 요청을 하면 보안에 취약하다. 그래서 데이터 요청에만 사용한다.
# post : 서버 데이터 생성/업데이트. 서버에서 데이터 값을 바꿀 때 이용한다. (로그인도 POST 방식으로 하는 것으로 아는데..모르겟네요.)

'''
2. 디자인 패턴

다음 중 **장고 프레임워크에서 채택한 디자인 패턴**을 선택하고,
각각의 알파벳이 어떤 글자의 약어인지 적으세요.
>> 정답 예시 / 6 MLB , Major League Baseball**)**

1️⃣ MVVM 2️⃣ MVC 3️⃣ MTV 4️⃣ MVP 5️⃣ MBC
'''

# answer : (4) MTV 패턴

# MVVM : Moder-View-View Model 
  # (1) Model : Application에서 사용되는 데이터와 그 데이터를 처리하는 부분
  # (2) View  : 사용자에게 보여지는 UI
  # (3) View Model : View를 표현하기 위해 만든 모델. view를 나타내기 위한 데이터 처리 담당을 한다.
# MVC  : Model-View-Controller
  # (1) Controller : Action을 받고 처리하는 부분.
# MTV  : Model-Template-View
  # (1) Template : 사용자에게 보여지는 화면. html파일이 템플릿을 담당한다. python문법을 활용하면 된다..??는데 해봐야 이해할 수 있을 것 같습니다.
  # (2) View : 웹 요청을 받고 데이터를 해당 Application의 Logic으로 가공하여 겨로가를 템플릿에 렌더링하며 응답한다.
# MVP  : Model-View-Presenter
  # Presenter : View에서 action을 받은 정보로 Model을 가공하여 View에게 다시 전달한다.
# MBC  : ???...The Middle East Broadcasting Center?

'''
3. Django settings

철수가 to do list 프로젝트를 만들기 위해 django 프로젝트를 세팅한 순서가 다음과 같다.

<aside>
💻 애플리케이션을 실행할 디렉토리(폴더)에서 VSCode 터미널 창을 연 후,

1️⃣ lieklion 이라는 이름의 가상환경을 만들고,
2️⃣ 생성된 가상환경을 실행하였다.
3️⃣ 이후, 장고를 설치하고,
4️⃣ todolist라는 이름의 프로젝트를 만들었다.
5️⃣ 자신의 프로필을 세팅하는 profile 애플리케이션을 생성했고,
6️⃣ 일정을 확인할 수 있는 calendar 애플리케이션을 생성했으며,
7️⃣ todolist를 체크하는 home 애플리케이션을 생성했다.
이후 settings.py의 INSTALLED_APP에 생성한 애플리케이션을 추가한 후,
8️⃣서버를 실행해 애플리케이션이 잘 올라갔는지 확인했다.

</aside>

각 번호의 단계에 맞추어 터미널에서 실행해야할 명령어를 적으세요.

>> 정답 예시
1️⃣ ls
2️⃣ cd 

(,,,,)

8️⃣ python —version
'''

# answer
# (1) python -m venv likelion               // 가상환경 세팅
# (2) source likelion/Scripts/activate      // 실행
# (3) pip install django                    // 장고 설치
# (4) django-admin startproject todolist    // 프로젝트 생성
# (5) cd todolist   // manage.py가 있는 프로젝트 디렉토리로 이동
#     python manage.py startapp profile
# (6) python manage.py startapp calendar
# (7) python manage.py startapp home
#     + settings.py의 INSTALLED_APPS에 'profile', 'calender', 'home'을
#       추가해서 인식시켜줌        
# (8) python manage.py runserver            // 서버 실행
#     ctrl + c // 서버 종료
