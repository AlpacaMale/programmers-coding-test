# 외계행성의 나이

[코딩테스트 연습 - 외계행성의 나이][1] 로 이동

## 문제 설명

우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 `age`가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

## 제한사항

`age`는 자연수입니다.
`age` ≤ 1,000
PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.

## 입출력 예

| age | result |
| --- | ------ |
| 23  | "cd"   |
| 51  | "fb"   |
| 100 | "baa"  |

## 입출력 예 설명

입출력 예 #1

`age`가 23이므로 "cd"를 return합니다.
입출력 예 #2

`age`가 51이므로 "fb"를 return합니다.
입출력 예 #3

`age`가 100이므로 "baa"를 return합니다.

## 풀이

'abcdefghij' 문자열을 만들고, 인덱스 각 자리수의 숫자를 인덱스로 집어넣어서 문자열을 만들 수 있다.

```python
def solution(age):
    numbers = "abcdefghij"
    return "".join(numbers[int(index)] for index in str(age))
```

혹은 문자열이 아닌 딕셔너리로 숫자와 알파벳을 매핑하여 사용할 수 있다.
반복당 형변환 횟수를 한번 줄일 수 있다.

```python
def solution(age):
    numbers = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h",
        "8": "i",
        "9": "j",
    }
    return "".join(numbers[char] for char in str(age))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120834
