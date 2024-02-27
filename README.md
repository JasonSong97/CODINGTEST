# Coding Test

## Algorithm

알고리즘 및 자료구조

> - 1. 그리디 알고리즘
>   - 우선순위 큐
>     - import heapq
>
> - 2. 구현
>
> - 3. BFS/DFS
>   - BFS
>     - Queue
>     - 너비 우선 탐색이라는 의미입니다. 가까운 노드부터 탐색하는 알고리즘
>   - DFS
>     - Stack, Recursion
>     - 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
> 
> - 4. 정렬
>   - 선택정렬
>   - 삽입정렬
>   - 퀵정렬
>   - 계수정렬
>
> - 5. 이진탐색
>   - 파라메트릭 서치
>   - 라이브러리 활용
>     - from bisect import bisect_left, bisect_right
> 
> - 6. DP

---

## 성능 확인 코드

```python
import resource
import time

start_time = time.time()
start_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# 여기에 코딩테스트 코드 작성

end_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
end_time = time.time()

execution_time = end_time - start_time

# 메모리 사용량 변환 (KB -> MB)
memory_usage_MB = (end_memory_usage - start_memory_usage) / 1024
print("메모리 사용량: {} MB".format(memory_usage_MB))
print("실행 시간: {:.6f} 초".format(execution_time))
```

---

## 참고

[이것이 취업을 위한 코딩 테스트다](https://github.com/ndb796/python-for-coding-test)

[leetcode](https://leetcode.com/)

[codeup](https://codeup.kr/problemsetsol.php?psid=33)
