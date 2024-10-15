# 조건에 맞게 수열 변환하기 2

[코딩테스트 연습 - 조건에 맞게 수열 변환하기 2][1] 로 이동

## 문제 설명

정수 배열 `arr`가 주어집니다. `arr`의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 `x`번 반복한 결과인 배열을 `arr(x)`라고 표현했을 때, `arr(x)` = `arr(x + 1)`인 `x`가 항상 존재합니다. 이러한 `x` 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

## 제한사항

- 1 ≤ `arr`의 길이 ≤ 1,000,000
- 1 ≤ `arr`의 원소의 값 ≤ 100

## 입출력 예

| arr                    | result |
| ---------------------- | ------ |
| [1, 2, 3, 100, 99, 98] | 5      |

## 입출력 예 설명

입출력 예 #1

- 위 작업을 반복하면 다음과 같이 `arr`가 변합니다.

| 반복 횟수 | arr                     |
| --------- | ----------------------- |
| 0         | [1, 2, 3, 100, 99, 98]  |
| 1         | [3, 2, 7, 50, 99, 49]   |
| 2         | [7, 2, 15, 25, 99, 99]  |
| 3         | [15, 2, 31, 51, 99, 99] |
| 4         | [31, 2, 63, 51, 99, 99] |
| 5         | [63, 2, 63, 51, 99, 99] |
| 6         | [63, 2, 63, 51, 99, 99] |

- 이후로 `arr`가 변하지 않으며, `arr(5) = arr(6)`이므로 5를 return 합니다.

## 풀이

설명을 따라 로직을 만든다면 이렇게된다.
for 문을 순회하며 new_arr를 만들어 이전 arr와 비교하고 변한것이 없으면 return 해주는것이다.

```python
def solution(arr):
    count = 0
    while True:
        new_arr = []
        for number in arr:
            if number % 2 == 0 and number >= 50:
                new_arr.append(number / 2)
            elif number % 2 == 1 and number < 50:
                new_arr.append(number * 2 + 1)
            else:
                new_arr.append(number)
        if arr == new_arr:
            return count
        else:
            arr = new_arr
            count += 1
```

하지만 이 코드는 매번 새로운 리스트를 만들어 비교하므로,
공간 복잡도가 증가할 수 있다.

```python
def solution(arr):
    count = 0
    while True:
        changed = False
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                changed = True
                arr[i] /= 2
            elif arr[i] % 2 == 1 and arr[i] < 50:
                changed = True
                arr[i] = arr[i] * 2 + 1
        if not changed:
            return count
        count += 1
```

이 코드는 새로운 배열을 만드는 대신 기존 배열을 변형하여 문제를 해결한다.
하지만 여전이 느리다. 다른 방식으로 구현한다면

```python
def solution(arr):
    count = -1
    while len(arr) != 0:
        new_arr = []
        for number in arr:
            if number >= 50 and number % 2 == 0:
                new_arr.append(number / 2)
            elif number < 50 and number % 2 == 1:
                new_arr.append(number * 2 + 1)
        arr = new_arr
        count += 1
    return count
```

이 방식은 while의 조건문과 number의 변화가 없을때의 조건을 변화시켜 반복하는 리스트의 길이를 점점 줄이고, 매 반복마다 조건문의 개수를 줄였기 때문에 처리해야하는 리스트의 크기가 커질수록 유리하다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181881
