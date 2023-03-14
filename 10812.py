num = int(int(input()))
cas = []
for i in range(num):
    s,d = list(map(int,input().split()))
    if s < 0 or d < 0 or s < d or (s+d)%2==1  :
        print("impossible")
        continue
    else:
        print(f'{(s+d)//2} {s-(s+d)//2}')
