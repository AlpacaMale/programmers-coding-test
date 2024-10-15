# 글자 지우기

[코딩테스트 연습 - 글자 지우기][1] 로 이동

## 문제 설명

문자열 `my_string`과 정수 배열 `indices`가 주어질 때, `my_string`에서 `indices`의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

## 제한사항

- 1 ≤ `indices`의 길이 < `my_string`의 길이 ≤ 100
- `my_string`은 영소문자로만 이루어져 있습니다
- 0 ≤ indices의 원소 < `my_string`의 길이
- indices의 원소는 모두 서로 다릅니다.

## 입출력 예

| my_string             | indices                      | result        |
| --------------------- | ---------------------------- | ------------- |
| "apporoograpemmemprs" | [1, 16, 6, 15, 0, 10, 11, 3] | "programmers" |

## 입출력 예 설명

입출력 예 #1

- 예제 1번의 `my_string`의 인덱스가 잘 보이도록 표를 만들면 다음과 같습니다.

| index     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| my_string | a   | p   | p   | o   | r   | o   | o   | g   | r   | a   | p   | e   | m   | m   | e   | m   | p   | r   | s   |

- `indices`에 있는 인덱스의 글자들을 지우고 이어붙이면 "programmers"가 되므로 이를 return 합니다.

## 풀이

join() 메소드와 제너레이터 컴프리헨션으로 풀 수 있다.

```python
def solution(my_string, indices):
    return "".join(char for index, char in enumerate(my_string) if index not in indices)
```

컴프리헨션과 join을 사용하는 이유는 for문을 반복하여 문자열을 만들어내는 것보다 공간 복잡도가 낮아서 그렇다.

```python
def solution(my_string, indices):
    new_string = ""
    for index, char in enumerate(my_string):
        if index not in indices:
            new_string += char
            print(new_string)
    return new_string
```

이 코드를 실행하게되면

p
pr
pro
prog
progr
progra
program
programm
programme
programmer
programmers

라는 출력이 찍히게된다 .
파이썬에서 문자열은 고유한 값으로써 존재하며,
만약 글자 하나라도 달라진다면 새로운 문자열이 생성된다.
char를 더해서 new_string을 업데이트할때마다 새로운 공간복사가 일어나고 공간을 많이 차지하게된다.

두 개의 코드 중 첫 번째의 코드는 O(n)의 공간 복잡도를 가지지만,
두번째 코드는 O(n^2)의 공간 복잡도를 가진다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181900
