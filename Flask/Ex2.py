# 과일 갯수 세기 함수 특정 과일이 몇개 들어있는지 세는 함수를 만들어봅시다.

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

cnt = 0
for i in range(len(fruits)) :
    fruit = fruits[i]
    if fruit == '사과' :
        cnt += 1
        
print(cnt)


def cnt_fruits(target):
    cnt = 0
    for fruit in fruits:
        if fruit == target:
            cnt += 1
    return cnt

subak_cnt = cnt_fruits('수박')
print(subak_cnt)

gam_cnt = cnt_fruits('감')
print(gam_cnt)