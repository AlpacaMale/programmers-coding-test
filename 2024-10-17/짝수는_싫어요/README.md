# 짝수는 싫어요

[코딩테스트 연습 - 짝수는 싫어요][1] 로 이동

## 문제 설명

정수 `n`이 매개변수로 주어질 때, `n` 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `n` ≤ 100

## 입출력 예

| n   | result                      |
| --- | --------------------------- |
| 10  | [1, 3, 5, 7, 9]             |
| 15  | [1, 3, 5, 7, 9, 11, 13, 15] |

## 입출력 예 설명

입출력 #1

- 10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.

입출력 #1

- 15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.

## 풀이

list() 함수와 range() 함수를 사용하여 쉽게 구할 수 있다.

```python
def solution(n):
    return list(range(1, n + 1, 2))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120813
