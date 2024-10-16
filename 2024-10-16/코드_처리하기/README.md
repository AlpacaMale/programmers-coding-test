# 코드 처리하기

[코딩테스트 연습 - 코드 처리하기][1] 로 이동

## 문제 설명

문자열 `code`가 주어집니다.
`code`를 앞에서부터 읽으면서 만약 문자가 "1"이면 `mode`를 바꿉니다. `mode`에 따라 `code`를 읽어가면서 문자열 `ret`을 만들어냅니다.

`mode`는 0과 1이 있으며, `idx`를 0 부터 `code의 길이 - 1` 까지 1씩 키워나가면서 `code[idx]`의 값에 따라 다음과 같이 행동합니다.

- `mode`가 0일 때
  - `code[idx]`가 "1"이 아니면 `idx`가 짝수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
  - `code[idx]`가 "1"이면 `mode`를 0에서 1로 바꿉니다.
- `mode`가 1일 때
  - `code[idx]`가 "1"이 아니면 `idx`가 홀수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
  - `code[idx]`가 "1"이면 `mode`를 1에서 0으로 바꿉니다.

문자열 `code`를 통해 만들어진 문자열 `ret`를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 `mode`는 0이며, return 하려는 `ret`가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

## 제한사항

- 1 ≤ `code`의 길이 ≤ 100,000
- `code`는 알파벳 소문자 또는 "1"로 이루어진 문자열입니다.

## 입출력 예

| code          | result  |
| ------------- | ------- |
| "abc1abc1abc" | "acbac" |

## 입출력 예 설명

입출력 예 #1

- code의 각 인덱스 i에 따라 다음과 같이 mode와 ret가 변합니다.

| i   | code[i] | mode | ret     |
| --- | ------- | ---- | ------- |
| 0   | "a"     | 0    | "a"     |
| 1   | "b"     | 0    | "a"     |
| 2   | "c"     | 0    | "ac"    |
| 3   | "1"     | 1    | "ac"    |
| 4   | "a"     | 1    | "ac"    |
| 5   | "b"     | 1    | "acb"   |
| 6   | "c"     | 1    | "acb"   |
| 7   | "1"     | 0    | "acb"   |
| 8   | "a"     | 0    | "acba"  |
| 9   | "b"     | 0    | "acba"  |
| 10  | "c"     | 0    | "acbac" |

- 따라서 "acbac"를 return 합니다.

## 풀이

mode를 boolean으로 설정하고, code가 "1"이면 mode값을 토글시키고, 그렇지 않을 경우에는 모드 값에 따라 홀짝을 구별해서 새로운 문자열 ret에 새로운 문자를 붙여준다.

문자열의 불필요한 공간복사를 방지하기 위해서 리스트로 만들고, ''.join() 메소드를 사용하였다.

```python
def solution(codes):
    ret = []
    mode = False
    for index, code in enumerate(codes):
        if code == "1":
            mode = not mode
        elif index % 2 == int(mode):
            ret.append(code)
    return "".join(ret) or "EMPTY"
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181932
