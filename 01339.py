try:
    while True:
        flag = True
        li = [0]*100
        in_ = input()
        for a in in_:
            li[ord(a)-41] += 1
        il = [0]*100
        in_ = input()
        for b in in_:
            il[ord(b)-41] += 1
        il.sort(reverse=True)
        li.sort(reverse=True)
        for c in range(len(li)):
            if li[c] == 0:
                break
            elif li[c] != il[c]:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")
except EOFError:
    pass