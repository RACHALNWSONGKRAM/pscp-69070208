"""GDSGSDGSDGSG"""
raka = int(input())
total = 50 + raka + (((50 + raka) / 100) * 7)
total2 = (raka / 10) + raka + ((((raka / 10) + raka) / 100) * 7)
total3 = (1000 + raka) + (((1000 + raka) / 100) * 7)
if raka / 10 <= 50:
    print(f"{total:.2f}")
elif raka / 10 > 50 and raka / 10 < 1000:
    print(f"{total2:.2f}")
elif raka / 10 >= 1000:
    print(f"{total3:.2f}")
