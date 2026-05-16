def minWindow(s: str, t: str) -> str:
    hashmapT = {}
    hashmapS = {}
    l = 0
    

    for i in t:
        hashmapT[s[i]] = 1 + hashmapT.get(s[i], 0)

    temp = ""
    min = ""
    for i in range(s):
        if i in hashmapT:
            min += i
            

s = "OUZODYXAZV"
t = "XYZ"

print(minWindow(s, t))