from collections import Counter
ti = int(input())
ans = []
for i in range(ti):
    in_ = input()
    for a in in_:
        try:
            k = a.upper()
            if k.isupper():
                ans.append(k)
        except:
            continue
ans = Counter(ans)
case = []
for k, v in ans.items():
    case.append([v,k])
case.sort(key= lambda x :x[1])
case.sort(key= lambda y : -y[0])
for b in range(len(case)):
    print(case[b][1],case[b][0])
