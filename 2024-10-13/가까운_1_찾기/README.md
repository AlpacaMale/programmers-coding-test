# 가까운 1 찾기

[코딩테스트 연습 - 가까운 1 찾기][1] 로 이동

## 문제 설명

정수 배열 `arr`가 주어집니다. 이때 `arr`의 원소는 1 또는 0입니다. 정수 `idx`가 주어졌을 때, `idx`보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.

단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

## 제한사항

- 3 ≤ `arr`의 길이 ≤ 100'000
- `arr`의 원소는 전부 1 또는 0입니다.

## 입출력 예

| arr                | idx | result |
| ------------------ | --- | ------ |
| [0, 0, 0, 1]       | 1   | 3      |
| [1, 0, 0, 1, 0, 0] | 4   | -1     |
| [1, 1, 1, 1, 0]    | 3   | 3      |

## 입출력 예 설명

입출력 예 #1

- 1보다 크면서 원소가 1인 가장 작은 인덱스는 3입니다. 따라서 3을 return 합니다.

입출력 예 #2

- 4번 인덱스 이후에 1은 등장하지 않습니다. 따라서 -1을 return 합니다.

입출력 예 #3

- 3번 인덱스의 값이 1입니다. 따라서 3을 return 합니다.

## 풀이

index() 함수로 원하는 값을 가진 요소의 인덱스를 구할 수 있다.
하지만 리스트 안에 찾는 값이 없다면 value error를 일으키기 때문에,
in을 이용해서 먼저 값이 있는지 찾거나, try - exept를 이용해서 예외처리를 해준다.

```python
def solution(arr, idx):
    if 1 in arr[idx:]:
        return arr[idx:].index(1) + idx
    else:
        return -1
```

```python
def solution(arr, idx):
    try:
        return arr[idx  :].index(1) + idx
    except:
        return -1
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181898
