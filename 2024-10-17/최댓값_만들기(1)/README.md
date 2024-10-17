# 최댓값 만들기(1)

[코딩테스트 연습 - 최댓값 만들기(1)][1] 로 이동

## 문제 설명

정수 배열 `numbers`가 매개변수로 주어집니다. `numbers`의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 0 ≤ `numbers`의 원소 ≤ 10,000
- 2 ≤ `numbers`의 길이 ≤ 100

## 입출력 예

| numbers               | result |
| --------------------- | ------ |
| [1, 2, 3, 4, 5]       | 20     |
| [0, 31, 24, 10, 1, 9] | 744    |

## 입출력 예 설명

입출력 예 #1

- 두 수의 곱중 최댓값은 4 \* 5 = 20 입니다.

입출력 예 #1

- 두 수의 곱중 최댓값은 31 \* 24 = 744 입니다.

## 풀이

아래의 코드는 numbers를 정렬한 후에, 가장 큰 수 두개를 찾아서 math 모듈의 prod() 함수를 이용해서 두 값을 곱해주는 코드이다.
리스트를 정렬하는것은 엄청난 시간이 소요된다.

```python
import math


def solution(numbers):
    return math.prod(sorted(numbers, key=lambda x: -x)[:2])
```

위의 코드를 개선하면 밑의 코드가 나온다.

```python
def solution(numbers):
    max1, max2 = 0, 0
    for number in numbers:
        if number > max1:
            max1, max2 = number, max1
        elif number > max2:
            max2 = number
    return max1 * max2
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120847
