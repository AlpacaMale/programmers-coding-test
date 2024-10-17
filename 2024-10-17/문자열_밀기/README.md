# 문자열 밀기

[코딩테스트 연습 - 문자열 밀기][1] 로 이동

## 문제 설명

문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 `A`와 `B`가 매개변수로 주어질 때, `A`를 밀어서 `B`가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 `B`가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

## 제한사항

- 0 < `A`의 길이 = `B`의 길이 < 100
- `A`, `B`는 알파벳 소문자로 이루어져 있습니다.

## 입출력 예

| A       | B       | result |
| ------- | ------- | ------ |
| "hello" | "ohell" | 1      |
| "apple" | "elppa" | -1     |
| "atat"  | "tata"  | 1      |
| "abc"   | "abc"   | 0      |

## 입출력 예 설명

입출력 예 #1

- "hello"를 오른쪽으로 한 칸 밀면 "ohell"가 됩니다.

입출력 예 #2

- "apple"은 몇 번을 밀어도 "elppa"가 될 수 없습니다.

입출력 예 #3

- "atat"는 오른쪽으로 한 칸, 세 칸을 밀면 "tata"가 되므로 최소 횟수인 1을 반환합니다.

입출력 예 #4

- "abc"는 밀지 않아도 "abc"이므로 0을 반환합니다.

## 풀이

슬라이싱을 이용해서 풀 수 있다.
하지만 for문을 사용하며 슬라이싱을 이용해서 새로운 문자열을 만들어내기 때문에 시간 공간복잡도가 높다.

```python
def solution(A, B):
    for offset in range(len(A)):
        if B == A[-offset:] + A[:-offset]:
            return offset
    return -1
```

위의 문제들은 아래처럼 해결할 수 있다.

A가 B \* 2 의 부분문자열이면, 인덱스를 반환하고, 그렇지 않다면 -1을 반환한다.

```python
def solution(A, B):
    return (B * 2).find(A)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120921
