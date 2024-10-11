# 문자열로 변환
[코딩 테스트 연습 - 문자열로 변환][1] 로 이동

## 문제 설명

정수 `n`이 주어질 때, `n`을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `n` ≤ 10000

## 입출력 예

| n    | result |
| ---- | ------ |
| 123  | "123"  |
| 2573 | "2573" |

## 입출력 예 설명

입출력 예 #1

- 123을 문자열로 변환한 "123"을 return합니다.

입출력 예 #2

- 2573을 문자열로 변환한 "2573"을 return합니다.

## 풀이

str() 함수를 이용해서 명시적 형변환을 해주었다

```python
def solution(n):
    return str(n)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181845
