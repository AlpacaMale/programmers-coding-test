# 조건 문자열

[코딩테스트 연습 - 조건 문자열][1] 로 이동

## 문제 설명

문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

- 두 수가 `n`과 `m`이라면
- ">", "=" : `n` >= `m`
- "<", "=" : `n` <= `m`
- ">", "!" : `n` > `m`
- "<", "!" : `n` < `m`

두 문자열 `ineq`와 `eq`가 주어집니다. `ineq`는 "<"와 ">"중 하나고, `eq`는 "="와 "!"중 하나입니다. 그리고 두 정수 `n`과 `m`이 주어질 때, `n`과 `m`이 `ineq`와 `eq`의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `n`, `m` ≤ 100

## 입출력 예

| ineq | eq  | n   | m   | result |
| ---- | --- | --- | --- | ------ |
| "<"  | "=" | 20  | 50  | 1      |
| ">"  | "!" | 41  | 78  | 0      |

## 입출력 예 설명

입출력 예 #1

- 20 <= 50은 참이기 때문에 1을 return합니다.

입출력 예 #2

- 41 > 78은 거짓이기 때문에 0을 return합니다.

## 풀이

eval을 쓰지 않고 이 문제를 푸는 방법은 if문을 사용하는것이다.
리턴 형태를 확실하게 명시하기 위해서 별도의 변수와 함께 사용하였다.

```python
def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        flag = n >= m
    elif ineq == "<" and eq == "=":
        flag = n <= m
    elif ineq == ">":
        flag = n > m
    else:
        flag = n < m
    return 1 if flag else 0
```

혹은 삼항 연산자를 사용해서 라인을 줄일 수도 있다.

```python
def solution(ineq, eq, n, m):
    if eq == "=":
        flag = n >= m if ineq == ">" else n <= m
    else:
        flag = n > m if ineq == ">" else n < m
    return 1 if flag else 0
```

좋다고 생각하는 방법으로 하면 된다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181934
