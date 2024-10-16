# 대소문자 바꿔서 출력하기

[코딩테스트 연습 - 대소문자 바꿔서 출력하기][1] 로 이동

## 문제 설명

영어 알파벳으로 이루어진 문자열 `str`이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

## 제한사항

- 1 ≤ `str`의 길이 ≤ 20
- `str`은 알파벳으로 이루어진 문자열입니다.

## 입출력 예

입력 #1

```
aBcDeFg
```

출력 #1

```
AbCdEfG
```

## 풀이

파이썬의 swapcase() 메소드를 이용하면 쉽게 풀 수 있다.

```python
str = input()
print(str.swapcase())
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181949
