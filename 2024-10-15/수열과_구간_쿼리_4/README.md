# 수열과 구간 쿼리 4

[코딩테스트 연습 - 수열과 구간 쿼리 4][1] 로 이동

## 문제 설명

정수 배열 `arr`와 2차원 정수 배열 `queries`이 주어집니다. `queries`의 원소는 각각 하나의 `query`를 나타내며, `[s, e, k]` 꼴입니다.

각 `query`마다 순서대로 `s` ≤` i` ≤ `e`인 모든 `i`에 대해 `i`가 `k`의 배수이면 `arr[i]`에 1을 더합니다.

위 규칙에 따라 `queries`를 처리한 이후의 `arr`를 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `arr`의 길이 ≤ 1,000
- 0 ≤ `arr`의 원소 ≤ 1,000,000
- 1 ≤ `queries`의 길이 ≤ 1,000
- 0 ≤ s ≤ e < `arr`의 길이
- 0 ≤ k ≤ 5

## 입출력 예

| arr             | queries                         | result          |
| --------------- | ------------------------------- | --------------- |
| [0, 1, 2, 4, 3] | [[0, 4, 1],[0, 3, 2],[0, 3, 3]] | [3, 2, 4, 6, 4] |

## 입출력 예 설명

입출력 예 #1

- 각 쿼리에 따라 `arr`가 다음과 같이 변합니다.

| arr             |
| --------------- |
| [0, 1, 2, 4, 3] |
| [1, 2, 3, 5, 4] |
| [2, 2, 4, 5, 4] |
| [3, 2, 4, 6, 4] |

- 따라서 [3, 2, 4, 6, 4]를 return 합니다.

## 풀이

조건문과 리스트 컴프리헨션을 이용해서 풀 수 있다.

```python
def solution(arr, queries):
    for [s, e, k] in queries:
        arr = [
            value + 1 if s <= index and index <= e and index % k == 0 else value
            for index, value in enumerate(arr)
        ]
    return arr
```

불필요한 반복을 줄여서 시간복잡도를 개선한다면,

```python
def solution(arr, queries):
    for [s, e, k] in queries:
        start = s if s % k == 0 else s + (k - s % k)
        end = e + 1
        for index in range(start, end, k):
            arr[index] += 1
    return arr
```

시작 인덱스와 끝 인덱스를 교환한 후에 값을 바꿔줄 인덱스에만 접근해서 값을 변경해주면 된다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181922
