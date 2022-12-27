def add(n:int):
    if len(str(n)) == 1:
        return n
    n = str(n)
    k = 0
    for i in n:
        k += int(i)
    return add(k)
        

while True:
    n = int(input())
    if n == 0 :
        break
    print(add(n))
