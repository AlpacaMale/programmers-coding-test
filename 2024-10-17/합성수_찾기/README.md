# 합성수 찾기

[코딩테스트 연습 - 합성수 찾기][1] 로 이동

## 문제 설명

약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 `n`이 매개변수로 주어질 때 `n`이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `n` ≤ 100

## 입출력 예

| n   | result |
| --- | ------ |
| 10  | 5      |
| 15  | 8      |

## 입출력 예 설명

입출력 예 #1

- 10 이하 합성수는 4, 6, 8, 9, 10 로 5개입니다. 따라서 5를 return합니다.

입출력 예 #1

- 15 이하 합성수는 4, 6, 8, 9, 10, 12, 14, 15 로 8개입니다. 따라서 8을 return합니다.

## 풀이

로직에 따라 풀어보면 아래처럼 나온다.
나눠지는 횟수가 3번 이상이면 약수가 3개 이상이므로 numbers 리스트에 넣고, numbers의 length를 구하면 풀 수 있다.

```python
def solution(n):
    numbers = []
    for num in range(1, n + 1):
        count = 1
        current = 2
        a = num
        while a != 1:
            if a % current == 0:
                a /= current
                count += 1
                current = 1
            current += 1
        if count >= 3:
            numbers.append(num)
    return len(numbers)
```

numbers의 length를 구하는 대신 total_composite를 카운터로 써서 풀었다.

```python
def solution(n):
    total_composite = 0
    for num in range(1, n + 1):
        count = 1
        current = 2
        a = num
        while a != 1:
            if a % current == 0:
                a /= current
                count += 1
                current = 2
            else:
                current += 1
        if count >= 3:
            total_composite += 1
    return total_composite
```

반복을 num / 2 까지만 반복해서 성능을 개선할 수 있다.

```python
import math


def solution(n):
    total_composite = 0

    for num in range(1, n + 1):
        divisor_count = 1
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisor_count += 1
        if divisor_count >= 3:
            total_composite += 1

    return total_composite
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120846
