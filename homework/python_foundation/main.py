'''
Question 1. IO

다음의 실행 결과를 작성하시오

first_num = input('첫번째 숫자 입력 : ')
# (키보드로 숫자 5 입력)
second_num = input('두번째 숫자 입력 : ')
# (키보드로 숫자 3 입력)
print('두 수의 합은 %d 입니다' % (first_num - second_num))
'''

# 첫 번째 숫자와 두 번째 숫자 입력 후, 타입에러가 발생한다.
# 이를 방지하기 위해서는 input() 함수를 int()함수로 묶어 형변환을 시켜줄 필요가 있다.


'''
Question 2. variable definition

이름이 'name'인 변수에 자신의 이름을 저장하고 'age'인 변수에 자신의 나이를 저장한 후에
두 변수를 print 함수를 이용해서 출력하라.
'''

def solution2():
    name = "양재서"
    age = 24
    print(f"이름 : {name}, 나이 : {age}")

#solution2()

'''
Question 3. conditional statements

성적이 90점 이상이면 A, 그게 아니라 80점 이상이면 B, 그게 아니라 70점 이상이면 C
그 외의 성적들에는 D학점을 부여하는 코드를 작성하세요.
'''

def solution3():
    credit = int(input())
    if credit >= 90:
        print("A")
    elif credit >= 80:
        print("B")
    elif credit >= 70:
        print("C")
    else:
        print("D")

#solution3()

'''
Question 4. while loop

코드의 결과값을 서술하시오

num=1                    

while num<10:                    
	if num%5==0:                 
		break                     
	num=num+1  

print("반복문 종료")
'''

# 반복문 종료가 터미널에 출력되고 프로그램은 종료된다.
# 내부적으로 살펴보면 num이 1씩 증가하다가 5가 되면 탈출 조건에 걸려서 빠져나오게 된다.
# 즉 num 변수를 출력해보면 5가 출력될 것이다.

'''
Question 5. for loop with list

코드의 결과값을 서술하시오

color=["빨강","파랑","검정","초록"]    # List

print(color[1])

for x in color:
	print(x)

for x in range(4,8):
	print(x)
'''

# print(color[1]) 에선 1번 인덱스의 "파랑"이 출력
# for x in color: 반복문에서는 "빨강" "파랑" "검정" "초록"이 개행되면서 모두 출력
# for x in range(4,8): 은 4~7이 출력될 것이다.

'''
Question 6. dictionary

다음과 같은 딕셔너리가 있습니다

dict = {'a' : 10, 'b' : 20, 'c' : 30}

여기에 새로운 Key-Value 쌍 'd':40을 추가하고 Key들의 리스트와 Value들의 리스트를 반환하는 
코드를 작성해주세요.
'''

def solution6():
    dict = {'a' : 10, 'b' : 20, 'c' : 30}
    dict.update({'d':40})
    
    # answer 1
    key, value = [], []

    for k, v in dict.items():
        key.append(k)
        value.append(v)

    print(key)
    print(value)

    #return key, value

    # answer 2
    print(list(dict))
    print(list(dict.values()))
    
#solution6()

'''
Question 7. set

집합(set)과 배열(list)의 가장 큰 차이점은 무엇인가요?
'''

# 1. set은 순서가 없다. 따라서 인덱스로 접근할 수 없다. == iterable한 자료형이 아니다.
# 2. 중복이 불가능하다.

'''
Question 8. for loop, list, dict

# 다음과 같이, '운영진의 이름과 나이 정보를 담은 딕셔너리'를 원소로 가지는 리스트가 있어요.
likelion_staffs=[{"name":"김","age":24},{"name":"조","age":25},{"name":"박","age":23}]

# 세 운영진의 나이의 총합을 구하는 코드를 작성하세요.

# 계산한 나이를 출력하세요.
'''

def solution8():
    likelion_staffs = [{"name":"김", "age":24}, {"name":"조", "age":25}, {"name":"박", "age":23}]

    total = 0
    for staff in likelion_staffs:
	    total += staff["age"]
    #print(total)

solution8()
