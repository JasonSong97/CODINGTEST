def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(1, n + 1):
            if i % 2 != 0:
                answer += i
        return answer
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                answer += (i * i)
        return answer