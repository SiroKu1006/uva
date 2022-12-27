in_ = [-1,-1]
while in_[0]!=0 and in_[1]!=0:
    in_ = list(map(int,input().split()))
    if in_[0]==0 and in_[1]==0 :
        break
    elif in_[1]==0:
        continue
    ans = f"{in_[0]}"

    while in_[0] > 1 :
        if in_[0] % in_[1] == 0 :
            de = in_[0] // in_[1]
            ans += f" {de}"
            in_[0] = de
        else:
            ans = "Boring!"
            break
    if ans != 0:
        print(ans)