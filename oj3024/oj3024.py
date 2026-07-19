""""GDSGSDGSDGSDG"""
lnw = float(input())
za = float(input())
if 0 <= lnw <= 30:
    if lnw - za >= za:
        second = za
        o = (lnw - za) - second
        hee = za - o
        if hee <= 2:
            print("Not surprising")
        else:
            print("Surprising")
    elif lnw - za < za:
        second = lnw - za
        o = (lnw - za) - second
        hee = za - o
        if hee <= 2:
            print("Not surprising")
        else:
            print("Surprising")
