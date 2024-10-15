# 문자열이 몇 번 등장하는지 세기

[코딩테스트 연습 - 문자열이 몇 번 등장하는지 세기][1] 로 이동

## 문제 설명

문자열 `myString`과 `pat`이 주어집니다. `myString`에서 `pat`이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `myString` ≤ 1000
- 1 ≤ `pat` ≤ 10

## 입출력 예

| myString | pat   | result |
| -------- | ----- | ------ |
| "banana" | "ana" | 2      |
| "aaaa"   | "aa"  | 3      |

## 입출력 예 설명

입출력 예 #1

- "banana"에서 1 ~ 3번 인덱스에서 한 번, 3 ~ 5번 인덱스에서 또 한 번 "ana"가 등장해서 총 두 번 등장합니다. 따라서 2를 return 합니다.

입출력 예 #2

- "aaaa"에서 0 ~ 2번 인덱스에서 한 번, 1 ~ 3번 인덱스에서 한 번, 2 ~ 4번 인덱스에서 한 번 "aa"가 등장해서 총 세 번 등장합니다. 따라서 3을 return 합니다.

## 풀이

count() 메소드로 세고 싶지만, count는 banana에 ana를 세고 나면, 그 다음 문자열인 na부터 확인하는 것 같다.
직접 for문을 순회하며 startswith 메소드로 pat으로 시작하는 횟수를 세서, 몇번 등장하는지 알 수 있다.

```python
def solution(myString, pat):
    count = 0
    for index in range(len(myString)):
        if myString[index:].startswith(pat):
            count += 1
    return count
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181871
