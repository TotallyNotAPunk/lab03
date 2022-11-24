def MinMaxSort(N, a):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
def MaxMinSort(N, a):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
N = 10
a = []
for i in range(N):
    a.append(float(input("Input number: ")))
choise=0
while choise!=1 and choise!=2:
    choise = int(input("1 - сортировкa по возрастанию\n2 - сортировкa по убыванию\nВаш выбор: "))

print(a)
if choise==1:
    MinMaxSort(N, a)
else:
    MaxMinSort(N, a)
print(a)