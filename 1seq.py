n=input('Введите кол-во элементов')
n=int(n)
list=[]
for i in range(0,n):
    x=input(f'Введите {i+1} элемент')
    x=int(x)
    list.append(x)
print(list)