# 수 조작하기 2

[코딩테스트 연습 - 수 조작하기 2][1] 로 이동

## 문제 설명

정수 배열 `numLog`가 주어집니다. 처음에 `numLog[0]`에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

- "w" : 수에 1을 더한다.
- "s" : 수에 1을 뺀다.
- "d" : 수에 10을 더한다.
- "a" : 수에 10을 뺀다.

그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 `numLog`입니다. 즉, `numLog[i]`는 `numLog[0]`로부터 총 `i`번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 `numLog`에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 2 ≤ `numLog`의 길이 ≤ 100,000
- -100,000 ≤ `numLog[0]` ≤ 100,000
- 1 ≤ `i` ≤ `numLog`의 길이인 모든 `i`에 대해 `|numLog[i] - numLog[i - 1]|`의 값은 1 또는 10입니다.

## 입출력 예

| numLog                                    | result        |
| ----------------------------------------- | ------------- |
| [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1] | "wsdawsdassw" |

## 입출력 예 설명

입출력 예 #1

- result인 "wsdawsdassw"를 따라 `numLog[0]`에서부터 시작해 조작을 하면 `numLog`의 값과 순서대로 일치합니다. 따라서 "wsdawsdassw"를 return 합니다.

## 풀이

수 조작하기 1의 변형버전으로, 리스트의 내용을 보고 과거에 어떤 문자열을 입력했는지 찾아내는 코드를 작성하면 된다

enumerate() 함수를 이용해서 이전 인덱스를 찾아내고, 문자를 하나씩 더해서 완성시킨다.

```python
def solution(numLog):
    control = ""
    for index, num in enumerate(numLog):
        if index == 0:
            continue
        prev_num = numLog[index - 1]
        if num - prev_num == 1:
            control += "w"
        elif num - prev_num == -1:
            control += "s"
        elif num - prev_num == 10:
            control += "d"
        else:
            control += "a"
    return control
```

문자열을 만드는 과정에서 공간 복잡도를 신경쓴다면 리스트를 전부 만든 뒤 "".join() 함수를 쓸 수도 있다.

```python
def solution(numLog):
    control = []
    for index, num in enumerate(numLog):
        if index == 0:
            continue
        prev_num = numLog[index - 1]
        if num - prev_num == 1:
            control.append("w")
        elif num - prev_num == -1:
            control.append("s")
        elif num - prev_num == 10:
            control.append("d")
        else:
            control.append("a")
    return "".join(control)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181925
