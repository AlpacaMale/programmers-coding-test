# 문자열 여러 번 뒤집기

[코딩테스트 연습 - 문자열 여러 번 뒤집기][1] 로 이동

## 문제 설명

문자열 `my_string`과 이차원 정수 배열 `queries`가 매개변수로 주어집니다. `queries`의 원소는 [s, e] 형태로, `my_string`의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. `my_string`에 `queries`의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

## 제한사항

- `my_string`은 영소문자로만 이루어져 있습니다.
- 1 ≤ `my_string`의 길이 ≤ 1,000
- `queries`의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < `my_string`의 길이를 만족합니다.
- 1 ≤ `queries`의 길이 ≤ 1,000

## 입출력 예

| my_string     | queries                           | result        |
| ------------- | --------------------------------- | ------------- |
| "rermgorpsam" | [[2, 3], [0, 7], [5, 9], [6, 10]] | "programmers" |

## 입출력 예 설명

- 예제 1번의 `my_string`은 "rermgorpsam"이고 주어진 `queries`를 순서대로 처리하면 다음과 같습니다.

| queries | my_string     |
| ------- | ------------- |
|         | "rermgorpsam" |
| [2, 3]  | "remrgorpsam" |
| [0, 7]  | "progrmersam" |
| [5, 9]  | "prograsremm" |
| [6, 10] | "programmers" |

- 따라서 "programmers"를 return 합니다.

## 풀이

문자열 슬라이싱을 이용해서 풀 수 있다.

```python
def solution(my_string, queries):
    for [s, e] in queries:
        my_string = my_string[:s] + my_string[s : e + 1][::-1] + my_string[e + 1 :]
    return my_string
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181913
