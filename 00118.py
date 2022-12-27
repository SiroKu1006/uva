def Ri(n:str):
    c =["N","E","S","W"]
    n = c.index(n)
    if n == 3:
        return c[0]
    else:
        return c[n+1]
def le(n:str):
    c =["N","E","S","W"]
    n = c.index(n)
    if n == 0:
        return c[3]
    else:
        return c[n-1]
def walk(x,y,ca):
    c =["N","E","S","W"]
    a = c.index(ca)
    if a == 0:
        return [x,y+1,ca]
    elif a == 1:
        return [x+1,y,ca]
    elif a == 2:
        return [x,y-1,ca]
    else:
        return [x-1,y,ca]
x,y = map(int,input().split())
flag = []
while True:
    try:
        mew = list(map(str,input().split()))
        for kk in range(2):
            mew[kk] = int(mew[kk])
        case = input()
        for do in case:
            if do == "L":
                new = [mew[0],mew[1],le(mew[2])]
                mew = new
            elif do == "R":
                new = [mew[0],mew[1],Ri(mew[2])]
                mew = new
            else:
                new = walk(mew[0],mew[1],mew[2])
                if new[0] > x or new[0] < 0 or new[1] > y or new[1] < 0:
                    if [mew[0],mew[1]] in flag:
                        pass
                    else:
                        print(f"{mew[0]} {mew[1]} {mew[2]} LOST")
                        flag.append([mew[0],mew[1]])
                        break
                else:
                    mew = new
        else:
            print(f"{mew[0]} {mew[1]} {mew[2]}")
    except EOFError:
        break