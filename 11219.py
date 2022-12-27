times = int(input())+1
for i in range(1,times):
    fkkkkk = input()
    date = list(map(int,input().split("/")))
    birthdate = list(map(int,input().split("/")))
    y = date[2] - birthdate[2]
    m = date[1] - birthdate[1]
    d = date[0] - birthdate[0]
    if y < 0:
        print(f"Case #{i}: Invalid birth date")
    elif y == 0 :
        if m < 0 :
            print(f"Case #{i}: Invalid birth date")
        elif m == 0:
            if d < 0:
                print(f"Case #{i}: Invalid birth date")
            else:
                print(f"Case #{i}: 0")
        else:
            print(f"Case #{i}: 0")
    elif y > 0 :
        age = y
        if m < 0:
            age -= 1
        elif m == 0 : 
            if d < 0:
                age -= 1

        if age <= 130:
            print(f"Case #{i}: {age}")
        else:
            print(f"Case #{i}: Check birth date")



        # print(f"Case #{i}: Check birth date")
        # print(f"Case #{i}: Invalid birth date")



