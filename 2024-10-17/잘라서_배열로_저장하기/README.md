# 잘라서 배열로 저장하기

[코딩테스트 연습 - 잘라서 배열로 저장하기][1] 로 이동

## 문제 설명

문자열 `my_str`과 `n`이 매개변수로 주어질 때, `my_str`을 길이 `n`씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `my_str`의 길이 ≤ 100
- 1 ≤ `n` ≤ `my_str`의 길이
- `my_str`은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.

## 입출력 예

| my_str             | n   | result                       |
| ------------------ | --- | ---------------------------- |
| "abc1Addfggg4556b" | 6   | ["abc1Ad", "dfggg4", "556b"] |
| "abcdef123"        | 3   | ["abc", "def", "123"]        |

## 입출력 예 설명

입출력 예 #1

- "abc1Addfggg4556b" 를 길이 6씩 잘라 배열에 저장한 ["abc1Ad", "dfggg4", "556b"]를 return해야 합니다.

입출력 예 #2

- "abcdef123" 를 길이 3씩 잘라 배열에 저장한 ["abc", "def", "123"]를 return해야 합니다.

## 풀이

슬라이싱과 컴프리헨션을 이용해서 풀 수 있다.

```python
def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120913
