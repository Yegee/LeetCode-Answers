def minWindow(s: str, t: str) -> str:
    hashmapT = {}
    hashmapS = {}
    l,r = 0, len(s)-1
    minl = 0

    

    for i in t:
        hashmapT[i] = 1 + hashmapT.get(i, 0)

    for i in s:
        if i in hashmapT:
            hashmapS[i] = 1 + hashmapS.get(i, 0)
            while hashmapS == hashmapT:
                if s[l] in hashmapS:
                    hashmapS[s[l]] -= 1
                l += 1


                         
            

s = "OUZODYXAZV"
t = "XYZ"

print(minWindow(s, t))