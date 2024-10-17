# 중복된 문자 제거

[코딩테스트 연습 - 중복된 문자 제거][1] 로 이동

## 문제 설명

문자열 `my_string`이 매개변수로 주어집니다. `my_string`에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `my_string` ≤ 110
- `my_string`은 대문자, 소문자, 공백으로 구성되어 있습니다.
- 대문자와 소문자를 구분합니다.
- 공백(" ")도 하나의 문자로 구분합니다.
- 중복된 문자 중 가장 앞에 있는 문자를 남깁니다.

## 입출력 예

| my_string          | result        |
| ------------------ | ------------- |
| "people"           | "peol"        |
| "We are the world" | "We arthwold" |

## 입출력 예 설명

입출력 예 #1

- "people"에서 중복된 문자 "p"와 "e"을 제거한 "peol"을 return합니다.

입출력 예 #2

- "We are the world"에서 중복된 문자 "e", " ", "r" 들을 제거한 "We arthwold"을 return합니다.

## 풀이

새로운 문자열 new_string에 charactor가 있는지 검사하고, 없으면 new_string에 append 해준다.

```python
def solution(my_string):
    new_string = []
    for char in my_string:
        if char not in new_string:
            new_string.append(char)
    return "".join(new_string)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120888
