import random

print("★☆★☆로또 번호 자동 생성기★☆★☆\n")
print("게임의 수를 입력하세요!")
play = int(input("게임 수: "))
print('-'*30)

for i in range(play):
    num = random.sample(range(1, 46), 6)
    print(num)

print('-'*30)
print("\n★☆★☆로또 번호 생성 완료★☆★☆\n")
