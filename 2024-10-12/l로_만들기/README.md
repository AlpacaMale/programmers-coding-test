# l로 만들기

[코딩테스트 연습 - l로 만들기][1] 로 이동

## 문제 설명

알파벳 소문자로 이루어진 문자열 `myString`이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `myString` ≤ 100,000
- `myString`은 알파벳 소문자로 이루어진 문자열입니다.

## 입출력 예

| myString     | result       |
| ------------ | ------------ |
| "abcdevwxyz" | "lllllvwxyz" |
| "jjnnllkkmm" | "llnnllllmm" |

## 입출력 예 설명

입출력 예 #1

- 0 ~ 4번 인덱스의 문자 "a","b","c","d","e"는 각각 "l"보다 앞서는 문자입니다. 따라서 "l"로 고쳐줍니다.
- 그 외의 문자는 모두 "l"보다 앞서지 않는 문자입니다. 따라서 바꾸지 않습니다.
- 따라서 "lllllvwxyz"을 return 합니다.

입출력 예 #2

- 0번, 1번, 6번, 7번 인덱스의 문자 "j","j","k","k"는 각각 "l"보다 앞서는 문자입니다. 따라서 "l"로 고쳐줍니다.
- 그 외의 문자는 모두 "l"보다 앞서지 않는 문자입니다. 따라서 바꾸지 않습니다.
- 따라서 "llnnllllmm"을 return 합니다.

## 풀이

알파벳 순서를 따졌을때 l보다 순서가 빠른 알파벳을 l로 바꾸는 내용이다
ord() 함수를 이용해서 알파벳의 아스키 코드를 얻을 수 있다.
공간복잡도를 줄이기 위해서 join() 메소드와 리스트 컴프리헨션을 함께 사용하여 문자열을 만들어냈다.

```python
def solution(myString):
    ascii_l = ord("l")
    return "".join("l" if ascii_l > ord(char) else char for char in myString)
```

하지만 아스키 코드로 바꾸지 않고도 비교할 수 있다
코드상에서 명시적으로 바꾸지 않더라도 파이썬에서 문자의 비교는 아스키코드를 기반으로 이루어진다

따라서

```python
def solution(myString):
    return "".join("l" if 'l' > char else char for char in myString)

```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181834
