area = []
def d(x,y,va):
    global area
    if area[x][y] == va:
        area[x][y] = 0
        if x == 0 or y == 0:
            if y == 0:
                d(x+1,y,va)
                d(x,y+1,va)
            else:
                d(x,y-1,va)
                d(x+1,y,va)
                d(x,y+1,va)
        elif x == len(area[0])-1 or y == len(area)-1:
            if y == len(area)-1:
                d(x,y-1,va)
                d(x-1,y,va)
            else:
                d(x,y-1,va)
                d(x-1,y,va)
        else:
                d(x,y-1,va)
                d(x+1,y,va)
                d(x,y+1,va)
                d(x-1,y,va)

times = int(input())
for i in range(times):
    name = []
    n = list(map(int,input().split()))
    cheak = [[0]*n[1]]*n[0]
    for k in range(n[0]):
        case = []
        m = input()
        for a in m:
            if a not in name:
                name.append(a)
            case.append(a)
        area.append(case)
    for j in name(len(name)):
        print(name[j],area.count(name[j]))
        while False:
            pass


    print(area)
