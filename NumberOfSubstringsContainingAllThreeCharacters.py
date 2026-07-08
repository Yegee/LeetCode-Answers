def numberOfSubstrings(s: str) -> int:

    arrS = [0] * 3
    n = len(s)
    l = 0
    count = 0


    for r in range(n):
        arrS[ord(s[r]) - ord('a')] += 1

        while arrS[0] and arrS[1] and arrS[2]:
            count += n - r
            arrS[ord(s[l]) - ord('a')] -= 1
            l += 1

    return count

s = "abcabc"
print(numberOfSubstrings(s))