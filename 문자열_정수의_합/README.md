# [문자열 정수의 합][1]

## 문제 설명

한 자리 정수로 이루어진 문자열 `num_str`이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 3 ≤ `num_str` ≤ 100

## 입출력 예

| num_str     | result |
| ----------- | ------ |
| "123456789" | 45     |
| "1000000"   | 1      |

## 입출력 예 설명

입출력 예 #1

- 문자열 안의 모든 숫자를 더하면 45가 됩니다.

입출력 예 #2

- 문자열 안의 모든 숫자를 더하면 1이 됩니다.

## 풀이

제너레이터 컴프리헨션과 명시적 형변환 int() 함수를 사용해서 숫자로 표현된 문자열의 각 자리수를 더할 수 있다.

```python
def solution(num_str):
    return sum(int(num) for num in num_str)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181849
