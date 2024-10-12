# 길이에 따른 연산

[코딩테스트 연습 - 길이에 따른 연산][1] 로 이동

## 문제 설명

정수가 담긴 리스트 `num_list`가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 2 ≤ `num_list`의 길이 ≤ 20
- 1 ≤ `num_list`의 원소 ≤ 9
- `num_list`의 원소를 모두 곱했을 때 2,147,483,647를 넘는 입력은 주어지지 않습니다.

## 입출력 예

| num_list                                | result |
| --------------------------------------- | ------ |
| [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1] | 51     |
| [2, 3, 4, 5]                            | 120    |

## 입출력 예 설명

입출력 예 #1

- 리스트의 길이가 13이므로 모든 원소의 합인 51을 return합니다.

입출력 예 #2

- 리스트의 길이가 4이므로 모든 원소의 곱인 120을 return합니다.

## 풀이

len() 함수를 이용해서 문자열의 길이를 구할 수 있다.
sum() 함수를 이용해서 리스트의 합울 구할 수 있다.

```python
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        total_power = 1
        for num in num_list:
            total_power *= num
        return total_power
```

math 모듈을 임포트하면 prod() 함수를 사용할 수 있다.
prod() 함수는 이터러블의 모든 요소를 곱하는 역할을 한다.
prod() 함수는 최적화가 잘 되있어서 for문으로 직접 곱하는 것 보다 효율적이다

```python
import math


def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return math.prod(num_list)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181879
