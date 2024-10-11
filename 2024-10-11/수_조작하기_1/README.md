# 수 조작하기 1
[코딩 테스트 연습 - 수 조작하기 1][1] 로 이동

## 문제 설명

정수 `n`과 문자열 `control`이 주어집니다. `control`은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, `control`의 앞에서부터 순서대로 문자에 따라 `n`의 값을 바꿉니다.

- "w" : `n`이 1 커집니다.
- "s" : `n`이 1 작아집니다.
- "d" : `n`이 10 커집니다.
- "a" : `n`이 10 작아집니다.
  위 규칙에 따라 `n`을 바꿨을 때 가장 마지막에 나오는 `n`의 값을 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- -100,000 ≤ `n` ≤ 100,000
- 1 ≤ `control`의 길이 ≤ 100,000
  - `control`은 알파벳 소문자 "w", "a", "s", "d"로 이루어진 문자열입니다.

## 입출력 예

| n   | control       | result |
| --- | ------------- | ------ |
| 0   | "wsdawsdassw" | -1     |

## 입출력 예 설명

입출력 예 #1

- 수 `n`은 `control`에 따라 다음과 같은 순서로 변하게 됩니다.
- 0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1
- 따라서 -1을 return 합니다.

## 풀이

문자열은 iterable 객체이므로, for문을 이용해서 순회할 수 있다.
for문을 이용해서 각 charactor를 이용해서 로직을 처리할 수 있다.

```python
def solution(n, control):
    for c in control:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        else:
            n -= 10
    return n
```

if문을 사용하는 대신 딕셔너리를 이용해서 n에 더해줄 숫자를 정의할 수도 있다.

```python
def solution(n, control):
    control_dict = {"w": 1, "s": -1, "d": 10, "a": -10}
    for c in control:
        n += control_dict[c]
    return n
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181926
