# 외계어 사전

[코딩테스트 연습 - 외계어 사전][1] 로 이동

## 문제 설명

PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 `spell`과 외계어 사전 `dic`이 매개변수로 주어집니다. `spell`에 담긴 알파벳을 한번씩만 모두 사용한 단어가 `dic`에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

## 제한사항

- `spell`과 `dic`의 원소는 알파벳 소문자로만 이루어져있습니다.
- 2 ≤ `spell`의 크기 ≤ 10
- `spell`의 원소의 길이는 1입니다.
- 1 ≤ `dic`의 크기 ≤ 10
- 1 ≤ `dic`의 원소의 길이 ≤ 10
- `spell`의 원소를 모두 사용해 단어를 만들어야 합니다.
- `spell`의 원소를 모두 사용해 만들 수 있는 단어는 `dic`에 두 개 이상 존재하지 않습니다.
- `dic`과 `spell` 모두 중복된 원소를 갖지 않습니다.

## 입출력 예

| spell                | dic                                     | result |
| -------------------- | --------------------------------------- | ------ |
| ["p", "o", "s"]      | ["sod", "eocd", "qixm", "adio", "soo"]  | 2      |
| ["z", "d", "x"]      | ["def", "dww", "dzx", "loveaw"]         | 1      |
| ["s", "o", "m", "d"] | ["moos", "dzx", "smm", "sunmmo", "som"] | 2      |

## 입출력 예 설명

입출력 예 #1

- "p", "o", "s" 를 조합해 만들 수 있는 단어가 `dic`에 존재하지 않습니다. 따라서 2를 return합니다.

입출력 예 #2

- "z", "d", "x" 를 조합해 만들 수 있는 단어 "dzx"가 `dic`에 존재합니다. 따라서 1을 return합니다.

입출력 예 #3

- "s", "o", "m", "d" 를 조합해 만들 수 있는 단어가 `dic`에 존재하지 않습니다. 따라서 2을 return합니다.

## 풀이

collections 모듈의 Counter 클래스를 이용해서 쉽게 풀 수 있다.
Counter 객체의 - 연산은 단어가 나타난 빈도를 뺄셈한다.
Counter 객체는 len()을 이용해서 단어가 몇개가 있는지 확인할 수 있다.

```python
from collections import Counter


def solution(spell, dic):
    spell_counter = Counter(spell)
    for word in dic:
        if len(spell_counter - Counter(word)) == 0:
            return 1
    return 2
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120869
