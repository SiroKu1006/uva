times = int(input())
m = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for i in range(times):
    date = list(map(int,input().split()))
    day = sum(m[:date[0]-1])+date[1]+5
    day %= 7
    print(week[day])