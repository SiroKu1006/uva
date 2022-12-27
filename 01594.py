times = int(input())
for i in range(times):
    n = int(input())
    done = []
    case = list(map(int,input().split()))
    while True:
        c = []
        if sum(case) == 0:
            print("ZERO")
            break
        elif case in done:
            print("LOOP")
            break
        done.append(case)
        for k in range(n):
            if k < n-1:
                c.append(abs(case[k]-case[k+1]))
            else:
                c.append(abs(case[k]-case[0]))
        case = c
