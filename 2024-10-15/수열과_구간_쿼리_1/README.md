# 수열과 구간 쿼리 1

[코딩테스트 연습 - 수열과 구간 쿼리 1][1] 로 이동

## 문제 설명

정수 배열 `arr`와 2차원 정수 배열 `queries`이 주어집니다. `queries`의 원소는 각각 하나의 `query`를 나타내며, `[s, e]` 꼴입니다.

각 `query`마다 순서대로 `s` ≤ `i` ≤ `e`인 모든 `i`에 대해 `arr[i]`에 1을 더합니다.

위 규칙에 따라 `queries`를 처리한 이후의 `arr`를 return 하는 solution 함수를 완성해 주세요.

단, 빈 문자열은 반환할 배열에 넣지 않습니다.

## 제한사항

_ 1 ≤ `arr`의 길이 ≤ 1,000
_ 0 ≤ `arr`의 원소 ≤ 1,000,000
_ 1 ≤ `queries`의 길이 ≤ 1,000
_ 0 ≤ s ≤ e < `arr`의 길이

## 입출력 예

| arr             | queries                | result          |
| --------------- | ---------------------- | --------------- |
| [0, 1, 2, 3, 4] | [[0, 1],[1, 2],[2, 3]] | [1, 3, 4, 4, 4] |

## 입출력 예 설명

입출력 예 #1

입출력 예 #1

- 각 쿼리에 따라 `arr`가 다음과 같이 변합니다.

| i   | queries[i] | arr             |
| --- | ---------- | --------------- |
| -   | -          | [0, 1, 2, 3, 4] |
| 0   | [0,1]      | [1, 2, 2, 3, 4] |
| 1   | [1,2]      | [1, 3, 3, 3, 4] |
| 2   | [2,3]      | [1, 3, 4, 4, 4] |

- 따라서 [1, 3, 4, 4, 4]를 return 합니다.

## 풀이

이중 for문을 이용하거나, 리스트 컴프리헨션을 이용해서 풀 수 있다.

```python
def solution(arr, queries):
    for s, e in queries:
        arr[s : e + 1] = [value + 1 for value in arr[s : e + 1]]
    return arr
```

```python
def solution(arr, queries):
    for s, e in queries:
        for index in range(s, e + 1):
            arr[index] += 1
    return arr
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181866
