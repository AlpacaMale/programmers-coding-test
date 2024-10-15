# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

[코딩테스트 연습 - 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기][1] 로 이동

## 문제 설명

문자열 `myString`과 `pat`가 주어집니다. `myString`의 부분 문자열중 `pat`로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 5 ≤ `myString` ≤ 20
- 1 ≤ `pat` ≤ 5
- `pat`은 반드시 `myString`의 부분 문자열로 주어집니다.
- `myString`과 `pat`에 등장하는 알파벳은 대문자와 소문자를 구분합니다.

## 입출력 예

| myString   | pat  | result     |
| ---------- | ---- | ---------- |
| "AbCdEFG"  | "dE" | "AbCdE"    |
| "AAAAaaaa" | "a"  | "AAAAaaaa" |

## 입출력 예 설명

입출력 예 #1

- "AbCdEFG"에서 "dE"는 한 번 등장하며 처음부터 해당 위치까지 잘라내면 "AbCdE"가 됩니다. 따라서 이 문자열이 "dE"로 끝나는 가장 긴 문자열이며, "AbCdE"를 return 합니다.

입출력 예 #2

- "AAAAaaaa"에서 "a"는 총 네 번 등장하며 이 중 가장 마지막에 있는 위치까지 잘라내면 "AAAAaaaa"가 됩니다. 따라서 이 문자열이 "a"로 끝나는 가장 긴 문자열이며, "AAAAaaaa"를 return 합니다.

## 풀이

오른쪽에서부터 요소를 찾아야 하므로, rindex를 이용해서 찾을 수 있다.
rindex는 찾으려는 요소가 문자열 안에 없으면 value error를 일으키므로,
만약 pat이 myString의 부분문자열로 반드시 주어지는게 아니라면, rfind를 이용해서 찾을 수 있다.

```python
def solution(myString, pat):
    e = myString.rindex(pat) + len(pat)
    return myString[:e]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181872
