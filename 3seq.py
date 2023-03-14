n=input('Введите кол-во элементов')
n=int(n)
list_1=[]
for i in range(0,n):
    x=input(f'Введите {i+1} элемент')
    x=int(x)
    list_1.append(x)
seq=input('Введите последовательность')
list_2=seq.replace(',',' ').replace(';',' ').replace('/',' ').split()
list_3=[int(i) for i in list_2]
for i in list_3:
    if i in list_1:list_1.remove(i)
print(list_1)
