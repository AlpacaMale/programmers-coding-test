# 가위 바위 보

[코딩테스트 연습 - 가위 바위 보][1] 로 이동

## 문제 설명

가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 `rsp`가 매개변수로 주어질 때, `rsp`에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

## 제한사항

- 0 < `rsp`의 길이 ≤ 100
- `rsp`와 길이가 같은 문자열을 return 합니다.
- `rsp`는 숫자 0, 2, 5로 이루어져 있습니다.

## 입출력 예

## 입출력 예 설명

입출력 예 #1

- "2"는 가위이므로 바위를 나타내는 "0"을 return 합니다.

입출력 예 #2

- "205"는 순서대로 가위, 바위, 보이고 이를 모두 이기려면 바위, 보, 가위를 순서대로 내야하므로 “052”를 return합니다.

## 풀이

문제의 설명대로 코드를 짜면 이렇게 된다.

```python
def solution(rsp):
    result = ""
    for hand in rsp:
        if hand == "2":
            result += "0"
        elif hand == "0":
            result += "5"
        else:
            result += "2"
    return result
```

위의 코드는 문자열에 + 연산으로 문자를 연결한다.
이 때 많은 양의 공간복사가 일어나므로, result를 리스트로 초기화 하고, 마지막에 join() 메소드를 이용해서 문자열로 만들어준다.
wins 딕셔너리를 이용해서 조건문을 없엤다.

```python
def solution(rsp):
    wins = {"2": "0", "0": "5", "5": "2"}
    result = []
    for hand in rsp:
        result.append(wins[hand])
    return "".join(result)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120839
