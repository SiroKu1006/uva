


cas = 1
while True:
    height = 0
    stock = []
    n = int(input())
    if n == 0 :
        break
    for i in range(n):
        in_ = list(map(int,input().split()))
        in_.sort()
        stock.append(in_)
    stock.sort()
    print(stock)




    print(f"Case {cas}: maximum height = {height}")
    cas += 1


