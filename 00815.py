times = 1
while True:
    percent = 0
    m,n = map(int,input().split())
    if n == 0 or m == 0:
        break
    start = 10**18
    case = []
    flag = [0]*(m*n)
    for i in range(m):
        in_ = list(map(int,input().split()))
        for k in in_:
            case.append(k)
    water = int(input())
    case.sort()
    height = case[0]
    temp = 0
    for o in range(m*n):
        if o == m*n-1 :
            flag[o] = 1
            break
        elif water < ((case[o+1]-case[o])*100*(o+1)):
            break
        elif water >= ((case[o+1]-case[o])*100*(o+1)):
            water -= ((case[o+1]-case[o])*100*(o+1))
            flag[o] = 1
            height = case[o+1]
    if water/(100*(o+1)) > 0:
        flag[o] = 1
    elif water/(100*(o+1)) == 0:
        flag[o-1] = 0
    height += water/(100*(o+1))
    percent = flag.count(1)/len(case)*100
    print(f"Region {times}")
    print("Water level is %.2f meters."%round(height,2))
    print("%.2f percent of the region is under water."%round(percent,2))
    print("")
    times+=1