import random

print("☆★☆★ 로또 생성기 ★☆★☆")
print('-'*30)

print("게임 수를 입력하세요!")
n = int(input("게임 수: "))

def lottery(num):
    for i in range(num):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        print(numbers)

lottery(n)

print('-'*30)
print("☆★☆★ 로또 번호 생성 완료 ★☆★☆")