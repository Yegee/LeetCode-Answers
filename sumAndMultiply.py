def sumAndMultiply(s: str, queries: List[List[int]]) -> List[int]:
    array = []
    while n > .9:
        if n%10 >= 1:
            array.insert(0, int(n%10))
        n = n/10
    
    sum = 0
    num = ""
    for i in array:
        sum += i
        num += str(i)

    return int(num) * sum

x = 10203004
queries = [[0,7],[1,3],[4,6]]
print(sumAndMultiply(x, queries))