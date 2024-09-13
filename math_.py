import random
print("Welcome To")
print("!!! Math Quiz !!!")
correct = 0
question = 5
for i in range(question):
  num1 = random.randint(1, 9) 
  num2 = random.randint(1, 9) 
  num3 = random.randint(1, 9)
  answer = num1 * num2 - num3 
  user_input = int(input(f"{num1} x {num2} - {num3} ="))
  if answer==user_input:
    print("정답입니다.")
    correct += 1
  else:
    print(f"아쉽네요. 정답은 {answer}입니다.")
print(f"{question}개 중 {correct}개를 맞췄습니다.")