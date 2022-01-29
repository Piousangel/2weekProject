# 사람의 나이 출력하기

# 딕셔너리가 각각의 요소인 리스트가 있을 때, 이름을 넣으면 나이를 돌려주는 함수 만들기

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people :
    print(person['name'], person['age'])

for person in people :
    if person['name'] == 'bob' :
        print(person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당사항 없음..'

print(get_age('bob'))
print(get_age('kay'))