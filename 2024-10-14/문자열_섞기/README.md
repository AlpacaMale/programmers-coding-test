# 문자열 섞기

[코딩테스트 연습 - 문자열 섞기][1] 로 이동

## 문제 설명

길이가 같은 두 문자열 `str1`과 `str2`가 주어집니다.

두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `str1`의 길이 = `str2`의 길이 ≤ 10
- `str1`과 `str2`는 알파벳 소문자로 이루어진 문자열입니다.

## 입출력 예

| str1    | str2    | result       |
| ------- | ------- | ------------ |
| "aaaaa" | "bbbbb" | "ababababab" |

## 풀이

join() 함수와 zip() 함수를 사용해서 쉽게 풀 수 있다.

```python
def solution(str1, str2):
    return "".join(char1 + char2 for char1, char2 in zip(str1, str2))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181942
