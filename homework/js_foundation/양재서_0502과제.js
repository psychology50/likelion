/* ==================================================================================
Question 1.

let object = {name: "likelion", color: "yellow"};
________(object);

(1) 빈칸은 인수로 설정한 값을 디버거 콘솔에 표시하는 함수이다. 빈칸을 채우시오
(2) 실행 결과를 적으시오
================================================================================== */

// Answer 1.
let object = {name: "likelion", color: "yellow"};
console.log(object)

// Answer 2.
// : Object의 정보가 크롬 개발자 도구 콘솔창에서 다음과 같이 출력된다.
//  output
//  {name: "likelion", color: "yellow"}



/* ==================================================================================
Question 2.

let likelion = {
    1: {"name" : "김대연", "mbti" : "ENFJ"},
    2: {"name" : "김지혜", "mbti" : "INTJ"},
    3: {"name" : "조나원", "mbti" : "ENFP"},
}

(1) 해당 객체에서 ENFP를 출력시키는 코드를 작성하시오
(2) likelion[1]["name"]의 실행 결과를 적으시오
================================================================================== */ 

// Answer (1)
let likelion = {
    1: {"name" : "김대연", "mbti" : "ENFJ"},
    2: {"name" : "김지혜", "mbti" : "INTJ"},
    3: {"name" : "조나원", "mbti" : "ENFP"},
}

// EX 1) (문제의 의도가 이게 아닌 거 같아서 2번까지 했습니다..)
let mbti = "ENFP";
console.log(mbti); // ENFP 출력

// EX 2)
for (var i in likelion) {
    if (likelion[i]["mbti"] == mbti) {
        document.write(mbti + '\n');
        document.write(likelion[i]["name"]);
    }
}

// Answer 2.
// : 현재 객체의 구조는 다음과 같다.
//   ObjectType likelion = {key1 : value1 = {key2 : value2, key3 : value3}}
//                     key1 == 1, 2, 3  /  key2 == "name"  /  key3 == "mbti"
//   likelion[1]["name"]은 key1의 1번 value에 접근하여, key2에 해당하는 "name"의 value를 가져오는 것이므로 결과는
//   String Type의 "김대연" 이라는 정보를 가져온다. (따로 명령을 하지 않았으므로, 가져오기만 하고 딱히 육안으로 확인되는 실행 결과는 없다.)



/* ==================================================================================
Question 3.

세렝게티에서 사용한 jQuery 함수입니다. 빈칸에 함수 이름을 적어주세요.

(1) __: 일치하는 요소 집합에서 첫 번째 요소의 현재 값을 가져오거나 일치하는 모든 요소의 값을 설정하는 함수
(2) __: 선택한 요소 안의 내용을 가져오거나, 다른 내용으로 바꾸는 함수
(3) __: String형을 숫자형으로 바꿔주는 함수
(4) __: 태그의 속성을 바꿔주는 함수
================================================================================== */

// Answer 1.
// (1) $(Selector).html()
//     $(Selector).val()   -> 요소의 '값'이라고 되어 있어서 val()이 맞는 거 같은데 혹시 몰라서 .html() 메서드도 적어봅니다..ㅎ
// (2) $(Selector).text() 
// (3) parseInt(String)
// (4) .attr('속성', '변경 값')



/* ==================================================================================
Question 4.

<!-- 요소에 id 속성이 있으면 위치에 상관없이 메서드 document.getElementById(id)를 이용해 접근할 수 있다. -->

<div id="elem">
    <div id="elem-content">Element</div>
</div>

<script>
    let elemtext = document.getElementById('elem');
    _______________________
</script>

(1) 빈칸에 변수 elemtext를 사용해 중앙 정렬하는 코드를 작성하시오
================================================================================== */

// Answer 1.
let elemtext = document.getElementById('elem');
elemtext.style.textAlign = "center";
// variable elemtext가 가리키는 elem id값의 css값으로 textAlign:center 속성값을 추가해준다.



/* ==================================================================================
Question 5.

<!-- elem.querySelectorAll(css)은 요소검색 메서드이다. elem의 자식 요소 중 주어진 CSS 선택자에 대응하는 요소 모두를 반환한다. -->

<ul>
    <li>1-1</li>
    <li>1-2</li>
</ul>
<ul>
    <li>2-1</li>
    <li>2-2</li>
</ul>
<script>
    let elements = document.querySelectorAll('ul > li:last-child');

    for (let elem of elements) {
        alert(elem.innerHTML);
    }
</script>

(1) for문의 실행 결과를 서술하시오.
================================================================================== */

// Answer 1.
// : variable elements가 저장한 값은 모든 ul 태그 안에 있는 li 중에서도 마지막 요소의 정보를 저장한다. (:last-child 때문)
//   즉, 현재 elements에 저장된 값은 1-2, 2-2이다.
//   alert() 함수는 괄호 안의 정보를 경고창에 띄우는 함수이다.
//   for (let elem of elements)는 Python으로 따지면 for elem in elements와 비슷하고,
//   다른 방식으로 표현하자면 for (let elem = 0; elem < elements.length ; elem++) { alert(elements[elem].innerHTML); }와 동일하게 기능한다.
//   따라서 for문의 실행 결과는 경고창으로 1-2, 2-2 출력이 된다.