from operator import truediv


myname = 'kim'
print(myname)
print(myname.upper())

print('Hello, jungle')

# a**2 a의 거듭제곱

# 문자열나누기
myemail = 'test@gmail.com'
result = myemail.split('@')
print(result[0])
print(result[1])

result2 = result[1].split('.')
print(result2[0] + ' ' + result2[1])
#한줄로
myemail.split('@')[1].split('.')[0]

# 특정 문자를 다른 문자로 치환
txt = '서울시-마포구-망원동'
result = txt.replace('-','>')

# 불(bool) 자료형 불형 자료형에는 논리연산자를 이용할 수 있습니다.
x = True
y = False
# z= true 에러

# 리스트와 딕셔너리 

a_list = []
a_list.append(1)
a_list.append([2,3])

a_list
len(a_list)
a_list[0]
a_list[1]
a_list[1][0]

a_dict = {}
a_dict = {'name' : 'bob' , 'age' : 21}
a_dict =['height'] = 178

people = [{'name':'bob','age':20},{'name':'carry','age':38}]
person = {'name' : 'john', 'age' : 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'

a = [3,3,1]
b = [5,2]

# a+b = [3,3,1,5,2]
# a*2 = [3,3,1,3,3,1]

def f(x) :
    return 2*x+3

# 조건문 else if == elif로 줄여씁니다.

def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

# 반복문

fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)) :
    fruit = fruits[i]
    print(fruit)