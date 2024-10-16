# 왼쪽 오른쪽

[코딩테스트 연습 - 왼쪽 오른쪽][1] 로 이동

## 문제 설명

문자열 리스트 `str_list`에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. `str_list`에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. "l"이나 "r"이 없다면 빈 리스트를 return합니다.

## 제한사항

- 1 ≤ `str_list`의 길이 ≤ 20
- `str_list`는 "u", "d", "l", "r" 네 개의 문자열로 이루어져 있습니다.

## 입출력 예

| str_list             | result     |
| -------------------- | ---------- |
| ["u", "u", "l", "r"] | ["u", "u"] |
| ["l"]                | []         |

## 입출력 예 설명

입출력 예 #1

- "r"보다 "l"이 먼저 나왔기 때문에 "l"의 왼쪽에 있는 문자열들을 담은 리스트인 ["u", "u"]를 return합니다.

입출력 예 #2

- "l"의 왼쪽에 문자열이 없기 때문에 빈 리스트를 return합니다.

## 풀이

문자 l과 r중에 찾아야하고, 찾은곳에서 리턴을 하려면 for문을 이용해서 직접 리스트를 순회하고, enumerate() 함수를 이용해서 인덱스에 편하게 접근한 후, 슬라이싱을 해주면 된다.

```python
def solution(str_list):
    for index, char in enumerate(str_list):
        if char == "l":
            return str_list[:index]
        elif char == "r":
            return str_list[index + 1 :]
    return []
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181890
