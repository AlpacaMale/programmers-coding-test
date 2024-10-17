# 소인수분해

[코딩테스트 연습 - 소인수분해][1] 로 이동

## 문제 설명

소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 x 2 x 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 `n`이 매개변수로 주어질 때 `n`의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 2 ≤ `n` ≤ 10,000

## 입출력 예

| n   | result       |
| --- | ------------ |
| 12  | [2, 3]       |
| 17  | [17]         |
| 420 | [2, 3, 5, 7] |

## 입출력 예 설명

입출력 예 #1

- 12를 소인수분해하면 2 x 2 x 3 입니다. 따라서 [2, 3]을 return합니다.

입출력 예 #2

- 17은 소수입니다. 따라서 [17]을 return 해야 합니다.

입출력 예 #3

- 420을 소인수분해하면 2 x 2 x 3 x 5 x 7 입니다. 따라서 [2, 3, 5, 7]을 return합니다.

## 풀이

set() 자료구조를 이용해서 중복된 값을 걸러내는 코드를 만들 수 있다.

```python
def solution(n):
    current = 2
    result = set()
    while n != 1:
        if n % current == 0:
            n /= current
            result.add(current)
            current = 1
        current += 1
    return sorted(result)
```

current 관련 연산을 개선해서 반복횟수 자체를 줄이고, n을 /로 나누지않고, //로 나누어 불필요한 소수점 연산을 줄였다.

```python
def solution(n):
    current = 2
    result = set()
    while n != 1:
        if n % current == 0:
            n //= current
            result.add(current)
        else:
            current += 1
    return sorted(result)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120852
