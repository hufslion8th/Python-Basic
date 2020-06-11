import random

print("☆★☆★ 로또 번호 자동 생성기 ★☆★☆")

print("게임 수를 입력하세요! ")
number = int(input("게임 수 : "))

lotto = [i for i in range(0,46)]
for i in range(number):
    random.shuffle(lotto)
    print(sorted(lotto[0:6]))

print("☆★☆★ 로또 번호 생성 완료 ★☆★☆")
        
