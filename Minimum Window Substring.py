def minWindow(s: str, t: str) -> str:
    hashmapT = {}
    hashmapS = {}
    l= 0
    winLen = [-1,-1]

    
    if len(s) == 0:
        return ""

    for i in t:
        hashmapT[i] = 1 + hashmapT.get(i, 0)

     #Keeps duplicates in check
    have  = 0
    need = len(hashmapT)

    for r in range(len(s)):
        if s[r] in hashmapT:
            hashmapS[s[r]] = 1 + hashmapS.get(s[r], 0)
            if hashmapS[s[r]] == hashmapT[s[r]]:
                have += 1
                                
            while have == need:
                if s[l] in hashmapS:
                    if ((r - l) < (winLen[1] - winLen[0])) or (winLen[0] == -1):
                        winLen[1] = r
                        winLen[0] = l

                    hashmapS[s[l]] -= 1
                

                if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                    have -= 1
                l += 1
    
    if len(s) == 0:
        return ""
    else:
        return s[winLen[0]: winLen[1] + 1]


        

s = "aa"

t = "aa"

print(minWindow(s, t))