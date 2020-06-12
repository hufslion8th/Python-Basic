import random
import math

print('☆★☆★ 로또 번호 자동 생성기 ★☆★☆')

game_num = int(input('게임 수를 입력하세요! : '))
print('게임 수 : ',game_num)


def I_am_fxxking_Rich(num):

    for i in range(0,num):
        Rich = random.sample(range(1,47),6)
        Rich.sort()
        print(Rich)

I_am_fxxking_Rich(game_num)  
print('----------------------')
print('!!!!!부자 되세요!!!!!')