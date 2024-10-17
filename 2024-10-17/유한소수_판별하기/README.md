# 유한소수 판별하기

[코딩테스트 연습 - 유한소수 판별하기][1] 로 이동

## 문제 설명

소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 `a`와 `b`가 매개변수로 주어질 때, `a`/`b`가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

## 제한사항

- `a`, `b`는 정수
- 0 < `a` ≤ 1,000
- 0 < `b` ≤ 1,000

## 입출력 예

| a   | b   | result |
| --- | --- | ------ |
| 7   | 20  | 1      |
| 11  | 22  | 1      |
| 12  | 21  | 2      |

## 입출력 예 설명

입출력 예 #1

- 분수 7/20은 기약분수 입니다. 분모 20의 소인수가 2, 5 이기 때문에 유한소수입니다. 따라서 1을 return합니다.

입출력 예 #2

- 분수 11/22는 기약분수로 나타내면 1/2 입니다. 분모 2는 소인수가 2 뿐이기 때문에 유한소수 입니다. 따라서 1을 return합니다.

입출력 예 #3

- 분수 12/21는 기약분수로 나타내면 4/7 입니다. 분모 7은 소인수가 7 이므로 무한소수입니다. 따라서 2를 return합니다.

## 풀이

Counter의 - 연산을 이용해서 답을 구할 수 있다.
중복되는 부분은 함수로 처리하였다.

```python
from collections import Counter


def find_divisors(number):
    divisors = []
    current = 2
    while number != 1:
        if number % current == 0:
            number //= current
            divisors.append(current)
        else:
            current += 1
    return Counter(divisors)


def solution(a, b):
    divisor_a = find_divisors(a)
    divisor_b = find_divisors(b)
    return (
        1
        if all(
            divisor == 2 or divisor == 5
            for divisor in (divisor_b - divisor_a).elements()
        )
        else 2
    )
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120878
