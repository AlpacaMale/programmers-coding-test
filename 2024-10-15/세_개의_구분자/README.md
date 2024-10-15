# 세 개의 구분자

[코딩테스트 연습 - 세 개의 구분자][1] 로 이동

## 문제 설명

임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 `myStr`이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.

## 제한사항

- 1 ≤ `myStr`의 길이 ≤ 1,000,000
- `myStr`은 알파벳 소문자로 이루어진 문자열 입니다.

## 입출력 예

| myStr                | result                    |
| -------------------- | ------------------------- |
| "baconlettucetomato" | ["onlettu", "etom", "to"] |
| "abcd"               | ["d"]                     |
| "cabab"              | ["EMPTY"]                 |

## 입출력 예 설명

입출력 예 #1

문제 설명의 예시와 같습니다.

입출력 예 #2

- "c" 이전에는 "a", "b", "c" 이외의 문자가 없습니다.
- "c" 이후에 문자열 "d"가 있으므로 "d"를 저장합니다.
- 따라서 ["d"]를 return 합니다.

입출력 예 #3

- "a", "b", "c" 이외의 문자가 존재하지 않습니다. 따라서 저장할 문자열이 없습니다.
- 따라서 ["EMPTY"]를 return 합니다.

## 풀이

정규 표현식을 이용해서 풀수 있지만, 정규 표현식을 사용하려면 추가적인 컴파일 단계와 패턴 매칭 단계가 필요하기 때문에 처리속도가 느려질 수 있다.

```python
import re


def solution(myStr):
    new_array = [string for string in re.split("[a,b,c]", myStr) if string]
    return new_array or ["EMPTY"]
```

코드가 지저분하게 보일 수 있지만 밑의 코드가 많이 빠르다.

```python
def solution(myStr):
    new_string = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
    return new_string or ["EMPTY"]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181862
