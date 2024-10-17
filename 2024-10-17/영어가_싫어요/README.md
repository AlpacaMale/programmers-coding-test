# 영어가 싫어요

[코딩테스트 연습 - 영어가 싫어요][1] 로 이동

## 문제 설명

영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 `numbers`가 매개변수로 주어질 때, `numbers`를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

## 제한사항

`numbers`는 소문자로만 구성되어 있습니다.
`numbers`는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
1 ≤ `numbers`의 길이 ≤ 50
"zero"는 `numbers`의 맨 앞에 올 수 없습니다.

## 입출력 예

| numbers                                | result    |
| -------------------------------------- | --------- |
| "onetwothreefourfivesixseveneightnine" | 123456789 |
| "onefourzerosixseven"                  | 14067     |

## 입출력 예 설명

입출력 예 #1

- "onetwothreefourfivesixseveneightnine"를 숫자로 바꾼 123456789를 return합니다.

입출력 예 #1

- "onefourzerosixseven"를 숫자로 바꾼 14067를 return합니다.

## 풀이

딕셔너리에 문자열을 숫자로 매핑하고, 이것을 이용해서 문자열 표현을 숫자로 변경하였다.

```python
string_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(numbers):
    for string in string_to_number.keys():
        numbers = numbers.replace(string, string_to_number[string])
    return int(numbers)
```

number.keys()를 사용하는 대신 items()를 사용하여 가독성을 높일 수 있다.

```python
string_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(numbers):
    for string, number in string_to_number.items():
        numbers = numbers.replace(string, number)
    return int(numbers)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120894
