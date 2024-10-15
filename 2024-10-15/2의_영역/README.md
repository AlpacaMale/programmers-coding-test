# 2의 영역

[코딩테스트 연습 - 2의 영역][1] 로 이동

## 문제 설명

정수 배열 `arr`가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, `arr`에 2가 없는 경우 [-1]을 return 합니다.

## 제한사항

- 1 ≤ `arr`의 길이 ≤ 100,000
- 1 ≤ `arr`의 원소 ≤ 10

## 입출력 예

| arr                       | result              |
| ------------------------- | ------------------- |
| [1, 2, 1, 4, 5, 2, 9]     | [2, 1, 4, 5, 2]     |
| [1, 2, 1]                 | [2]                 |
| [1, 1, 1]                 | [-1]                |
| [1, 2, 1, 2, 1, 10, 2, 1] | [2, 1, 2, 1, 10, 2] |

## 입출력 예 설명

입출력 예 #1

- 2가 있는 인덱스는 1번, 5번 인덱스뿐이므로 1번부터 5번 인덱스까지의 부분 배열인 [2, 1, 4, 5, 2]를 return 합니다.

입출력 예 #2

- 2가 한 개뿐이므로 [2]를 return 합니다.

입출력 예 #3

- 2가 배열에 없으므로 [-1]을 return 합니다.

입출력 예 #4

- 2가 있는 인덱스는 1번, 3번, 6번 인덱스이므로 1번부터 6번 인덱스까지의 부분 배열인 [2, 1, 2, 1, 10, 2]를 return 합니다.

## 풀이

리스트에는 rindex가 없으므로, arr를 뒤집은 후에 구해줄 수 있다.

```python
def solution(arr):
    if 2 not in arr:
        return [-1]
    start = arr.index(2)
    end = len(arr) - arr[::-1].index(2)
    return arr[start:end]
```

하지만 len(), 슬라이싱, index 함수 두번 이용 등으로 인해 코드가 느리다.

```python
def solution(arr):
    if 2 not in arr:
        return [-1]
    start, end = 99999, 0
    for index, number in enumerate(arr):
        if number == 2:
            start = min(index, start)
            end = max(index + 1, end)
    return arr[start:end]
```

이렇게 리스트를 in, for를 각각 한번만써서 시간복잡도를 줄일 수 있다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181894
