# 분수의 덧셈

[코딩테스트 연습 - 분수의 덧셈][1] 로 이동

## 문제 설명

첫 번째 분수의 분자와 분모를 뜻하는 `numer1`, `denom1`, 두 번째 분수의 분자와 분모를 뜻하는 `numer2`, `denom2`가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 제한사항

- 0 < `numer1`, `denom1`, `numer2`, `denom2` < 1,000

## 입출력 예

| numer1 | denom1 | numer2 | denom2 | result  |
| ------ | ------ | ------ | ------ | ------- |
| 1      | 2      | 3      | 4      | [5, 4]  |
| 9      | 2      | 1      | 3      | [29, 6] |

## 입출력 예 설명

입출력 예 #1

- 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.

입출력 예 #2

- 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

## 풀이

분모와 분자를 상대 분모로 곱한값을 분자끼리 더해주고, Counter 모듈을 사용해서 공통으로 곂치는 약수를 나눠주면 된다.

```python
from collections import Counter
from math import prod


def get_counter(number):
    counter = 2
    array = []
    while number != 1:
        if number % counter == 0:
            number //= counter
            array.append(counter)
        else:
            counter += 1
    return Counter(array)


def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom2 * denom1
    numer_counter = get_counter(numer)
    denom_counter = get_counter(denom)
    divide = prod((numer_counter & denom_counter).elements())
    return [numer // divide, denom // divide]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120808
