# 짝수의 합

[코딩테스트 연습 - 짝수의 합][1] 로 이동

## 문제 설명

정수 `n`이 주어질 때, `n`이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- 0 < `n` ≤ 1000

## 입출력 예

| n   | result |
| --- | ------ |
| 10  | 30     |
| 4   | 6      |

## 입출력 예 설명

입출력 예 #1

- `n`이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.

입출력 예 #2

- `n`이 4이므로 2 + 4 = 6을 return 합니다.

## 풀이

제너레이터 컴프리헨션과 sum() 함수를 이용해서 쉽게 풀 수 있다.

```python
def solution(n):
    return sum(number for number in range(0, n + 1, 2))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120831
