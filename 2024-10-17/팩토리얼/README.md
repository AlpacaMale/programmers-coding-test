# 팩토리얼

[코딩테스트 연습 - 팩토리얼][1] 로 이동

## 문제 설명

`i`팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 _ 4 _ 3 _ 2 _ 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

## 제한사항

- 0 < `n` ≤ 3,628,800

## 입출력 예

| n       | result |
| ------- | ------ |
| 3628800 | 10     |
| 7       | 3      |

## 입출력 예 설명

입출력 예 #1

- 10! = 3,628,800입니다. `n`이 3628800이므로 최대 팩토리얼인 10을 return 합니다.
  입출력 예 #2

- 3! = 6, 4! = 24입니다. `n`이 7이므로, 7 이하의 최대 팩토리얼인 3을 return 합니다.

## 풀이

반복문과 조건문을 사용해서 문제를 풀 수 있다.

```python
def solution(n):
    pactorial = 1
    for i in range(1, 12):
        pactorial *= i
        if pactorial > n:
            return i - 1
```

for 문으러 직접 범위를 지정해주는것은 번거로움으로, while문을 사용한다.

```python
def solution(n):
    pactorial = 1
    count = 1
    while pactorial <= n:
        count += 1
        pactorial *= count
    return count - 1
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120848
