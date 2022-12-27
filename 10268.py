try:
    while True:
        x = int(input())
        in_ = list(map(int,input().split()))
        ans = []

        for a in range(len(in_),1,-1):
            if a == 2:
                ans.append(in_[-a])
            else:    
                ans.append(in_[-a]*in_[-a+1]*(a-1))
        ans.reverse()
        n = 0
        if len(ans)>1:
            for i in range(len(ans)):
                n += x**i*ans[i]
            print(n)
        else: 
            print(ans[0])
except:
    pass


# a = [0,1,2]
# print(a[-2]) Output 1