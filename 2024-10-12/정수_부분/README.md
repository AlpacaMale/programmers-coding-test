# 정수 부분

[코딩테스트 연습 - 정수 부분][1] 로 이동

## 문제 설명

실수 `flo`가 매개 변수로 주어질 때, `flo`의 정수 부분을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 0 ≤ `flo` ≤ 100

## 입출력 예

| flo   | result |
| ----- | ------ |
| 1.42  | 1      |
| 69.32 | 69     |

## 입출력 예 설명

입출력 예 #1

- 1.42의 정수 부분은 1입니다.

입출력 예 #2

- 69.32의 정수 부분은 69입니다.

## 풀이

math 모듈의 floor() 메소드를 쓰면 쉽게 정수분을 구할 수 있다.
floor()는 소수부분 버린다.

```python
import math


def solution(flo):
    return math.floor(flo)
```

math 모듈을 임포트하기 싫다면 int() 함수를 이용할 수도 있다.

```python
def solution(flo):
    return int(flo)
```

혹은 floor division 연산을 사용할수도 있다
//는 나눗셈의 결과에서 소수를 버린다.

```python
def solution(flo):
    return flo//1
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181850
