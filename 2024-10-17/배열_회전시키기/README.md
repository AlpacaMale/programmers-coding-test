# 배열 회전시키기

[코딩테스트 연습 - 배열 회전시키기][1] 로 이동

## 문제 설명

정수가 담긴 배열 `numbers`와 문자열 `direction`가 매개변수로 주어집니다. 배열 `numbers`의 원소를 `direction`방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 3 ≤ `numbers`의 길이 ≤ 20
- `direction`은 "left" 와 "right" 둘 중 하나입니다.

## 입출력 예

| numbers                   | direction | result                    |
| ------------------------- | --------- | ------------------------- |
| [1, 2, 3]                 | "right"   | [3, 1, 2]                 |
| [4, 455, 6, 4, -1, 45, 6] | "left"    | [455, 6, 4, -1, 45, 6, 4] |

## 입출력 예 설명

입출력 예 #1

- `numbers` 가 [1, 2, 3]이고 `direction`이 "right" 이므로 오른쪽으로 한 칸씩 회전시킨 [3, 1, 2]를 return합니다.

입출력 예 #2

- `numbers` 가 [4, 455, 6, 4, -1, 45, 6]이고 `direction`이 "left" 이므로 왼쪽으로 한 칸씩 회전시킨 [455, 6, 4, -1, 45, 6, 4]를 return합니다.

## 풀이

이 문제는 두 가지 방식으로 풀 수 있을 것 같다.
하나는 리스트의 메소드 pop과 insert append 등을 활용한 풀이이고,
하나는 리스트 슬라이싱을 이용한 풀이이다.

```python
def solution(numbers, direction):
    if direction == "right":
        number = numbers.pop()
        numbers.insert(0, number)
    else:
        number = numbers.pop(0)
        numbers.append(number)
    return numbers
```

```python
def solution(numbers, direction):
    if direction == "right":
        numbers = [numbers[-1]] + numbers[:-1]
    else:
        numbers = numbers[1:] + [numbers[0]]
    return numbers
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120844
