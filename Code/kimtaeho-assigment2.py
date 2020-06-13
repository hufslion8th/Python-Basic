import random
import math

print('☆★☆★ 로또 번호 자동 생성기 ★☆★☆')
print('게임 수를 입력하세요!')
num_game = int(input('게임 수 : '))
print('-'*32)

def lotto(n):
    for i in range(n):
        numbers = random.sample(range(1,47),6)
        numbers.sort()
        print(numbers)

lotto(num_game)
print('-'*32)