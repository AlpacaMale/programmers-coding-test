# 소문자로 바꾸기

[코딩테스트 연습 - 소문자로 바꾸기][1] 로 이동

## 문제 설명

알파벳으로 이루어진 문자열 `myString`이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `myString`의 길이 ≤ 100,000
- `myString`은 알파벳으로 이루어진 문자열입니다.

## 입출력 예

| myString  | result    |
| --------- | --------- |
| "aBcDeFg" | "abcdefg" |
| "aaa"     | "aaa"     |

## 풀이

lower() 메소드를 이용하면 쉽게 풀 수 있다.

```python
def solution(myString):
    return myString.lower()
```

[1]:
