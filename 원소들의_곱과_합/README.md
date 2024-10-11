# 원소들의 곱과 합
[코딩 테스트 연습 - 원소들의 곱과 합][1] 로 이동

## 문제 설명

정수가 담긴 리스트 `num_list`가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 2 ≤ `num_list`의 길이 ≤ 10
- 1 ≤ `num_list`의 원소 ≤ 9

## 입출력 예

| num_list        | result |
| --------------- | ------ |
| [3, 4, 5, 2, 1] | 1      |
| [5, 7, 8, 3]    | 0      |

## 입출력 예

입출력 예 #1

- 모든 원소의 곱은 120, 합의 제곱은 225이므로 1을 return합니다.

입출력 예 #2

- 모든 원소의 곱은 840, 합의 제곱은 529이므로 0을 return합니다.

## 풀이

`**` 기호를 사용하면 제곱을 표현할 수 있다

```python
def solution(num_list):
    total_square = sum(num_list) ** 2
    total_power = 1
    for num in num_list:
        total_power *= num
    return 1 if total_square > total_power else 0
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181929
