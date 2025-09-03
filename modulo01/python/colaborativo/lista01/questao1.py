numbers_list = list()
for i in range(0, 5):
    number = int(input())
    numbers_list.append(number)

for i in range(0, len(numbers_list)):
    print(f'{numbers_list[i]}', end=" ")

print()

for j in reversed(numbers_list):
    print(f'{j}', end=" ")