def sumAndMultiply(s: str, queries: List[List[int]]) -> List[int]:
    answer = []
    
    for queue in queries:
        temp = int(s[queue[0]:queue[1] + 1])
        if temp == 0:
            answer.append(0)
            continue
        
        array = []
        while temp > .9:
            if temp%10 >= 1:
                array.insert(0, int(temp%10))
            temp //= 10        
        digit_sum = 0
        num = ""
        for i in array:
            digit_sum += i
            num += str(i)

        num = int(num)
        answer.append((num * digit_sum) % (10**9 + 7))
    
    return answer

s = "900"
queries = [[0,0],[0,1],[0,2],[1,1],[1,2],[2,2]]


print(sumAndMultiply(s,queries))
