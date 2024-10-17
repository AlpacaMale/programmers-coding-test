# 최빈값 구하기

[코딩테스트 연습 - 최빈값 구하기][1] 로 이동

## 문제 설명

최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 `array`가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

## 제한사항

- 0 < `array`의 길이 < 100
- 0 ≤ `array`의 원소 < 1000

## 입출력 예

| array              | result |
| ------------------ | ------ |
| [1, 2, 3, 3, 3, 4] | 3      |
| [1, 1, 2, 2]       | -1     |
| [1]                | 1      |

## 입출력 예 설명

입출력 예 #1

- [1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.

입출력 예 #2

- [1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.

입출력 예 #3

- [1]에는 1만 있으므로 최빈값은 1입니다.

## 풀이

Counter를 이용해서 풀 수 있다.
가장 높은 빈도수의 값을 찾은 다음 value가 max_freq인 key값을 찾아주면 된다.

```python
from collections import Counter


def solution(array):
    array_count = Counter(array)
    max_freq = max(array_count.values())
    most_common = [key for key, count in array_count.items() if count == max_freq]
    return most_common[0] if len(most_common) == 1 else -1
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120812
