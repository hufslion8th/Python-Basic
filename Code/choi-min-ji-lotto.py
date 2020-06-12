import random

print("☆ ★ ☆ ★ 로또 번호 자동 생성기 ☆ ★ ☆ ★")
print('-'*30)
print("게임 수를 입력하세요!")
a = (input("게임 수: "))
print('-'*30)

def lotto(game):
    for i in range(int(game)):
        num = random.sample(range(1,46),6)
        num.sort()
        print(num)

lotto(a)
print('-'*30)
print("☆ ★ ☆ ★ 로또 번호 생성 완료 ☆ ★ ☆ ★")
print('-'*30)