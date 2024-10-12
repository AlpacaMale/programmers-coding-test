# 문자열 바꿔서 찾기

[코딩테스트 연습 - 문자열 바꿔서 찾기][1] 로 이동

## 문제 설명

문자 "A"와 "B"로 이루어진 문자열 `myString`과 `pat`가 주어집니다. `myString`의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 `pat`이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

## 제한사항

- 1 ≤ `myString`의 길이 ≤ 100
- 1 ≤ `pat`의 길이 ≤ 10
- `myString`과 `pat`는 문자 "A"와 "B"로만 이루어진 문자열입니다.

## 입출력 예

| myString | pat    | result |
| -------- | ------ | ------ |
| "ABBAA"  | "AABB" | 1      |
| "ABAB"   | "ABAB" | 0      |

## 입출력 예 설명

입출력 예 #1

- "ABBAA"에서 "A"와 "B"를 서로 바꾸면 "BAABB"입니다. 여기에는 부분문자열 "AABB"가 있기 때문에 1을 return 합니다.

입출력 예 #2

- "ABAB"에서 "A"와 "B"를 서로 바꾸면 "BABA"입니다. 여기에는 부분문자열 "BABA"가 없기 때문에 0을 return 합니다.

## 풀이

new_string 이라는 새로운 문자열을 만들어서 그곳에 chractor를 하나씩 더해주며 새로운 문자열을 만들어낼 수 있다

하지만 이런 방식은 메모리를 많이 소모한다

`"A"`라는 문자열에 `"B"`라는 문자열을 더하려면 메모리 복사가 일어나 `"AB"`라는 새로운 문자열이 생겨나기 때문에, 공간 복잡도가 증가한다

공간복잡도가 **O(n^2)**이다

```python
def solution(myString, pat):
    new_string = ""
    for char in myString:
        new_string += "B" if char == "A" else "A"
    return 1 if pat in new_string else 0
```

그러므로 리스트 컨프리헨션과 join() 메서드를 이용해서 한번에 배열을 만들면 공간복잡도를 **O(n)**으로 낮출 수 있다

```python
def solution(myString, pat):
    new_string = "".join('B' if char == 'A' else 'A' for char in myString)
    return 1 if pat in new_string else 0
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181864
