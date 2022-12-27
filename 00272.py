while True:
    try:
        a = input()
        flag1 = False
        flag2 = False
        ans = ""
        for i in a:
            if i == "\"":
                if flag1:
                    ans+= "``"
                    flag1 = False
                else:
                    flag1 = True
                    ans += i
            elif i == "\'":
                if flag2:
                    ans+= "``"
                    flag1 = False
                else:
                    flag1 = True
                    ans += i
    except EOFError:
        break