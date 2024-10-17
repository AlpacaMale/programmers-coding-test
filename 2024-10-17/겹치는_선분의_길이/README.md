# 겹치는 선분의 길이

[코딩테스트 연습 - 겹치는 선분의 길이][1] 로 이동

## 문제 설명

선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 `lines`가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

`lines`가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

![](image.png)

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

## 제한사항

- `lines`의 길이 = 3
- `lines`의 원소의 길이 = 2
- 모든 선분은 길이가 1 이상입니다.
- `lines`의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
- -100 ≤ a < b ≤ 100

## 입출력 예

| lines                     | result |
| ------------------------- | ------ |
| [[0, 1], [2, 5], [3, 9]]  | 2      |
| [[-1, 1], [1, 3], [3, 9]] | 0      |
| [[0, 5], [3, 9], [1, 10]] | 8      |

## 입출력 예 설명

입출력 예 #1

- 두 번째, 세 번째 선분 [2, 5], [3, 9]가 [3, 5] 구간에 겹쳐있으므로 2를 return 합니다.

입출력 예 #2

- 겹친 선분이 없으므로 0을 return 합니다.

입출력 예 #3

- 첫 번째와 두 번째 선분이 [3, 5] 구간에서 겹칩니다.
- 첫 번째와 세 번째 선분 [1, 5] 구간에서 겹칩니다.
- 두 번째와 세 번째 선분 [3, 9] 구간에서 겹칩니다.
- 따라서 [1, 9] 구간에 두 개 이상의 선분이 겹쳐있으므로, 8을 return 합니다.

## 풀이

먼저 수색 범위를 줄이기 위해 set을 이용해서 선분이 지나가는 숫자를 찾고, 현재 숫자와 다음 숫자가 모두 라인에 곂치면, count가 하나 올라가고 count가 두개면 2개 이상 곂쳤다고 판단하여 result가 1 올라간다.

```python
def solution(lines):
    numbers = set()
    result = 0
    for start, end in lines:
        for number in range(start, end + 1):
            numbers.add(number)

    for number in numbers:
        count = 0
        for start, end in lines:
            if start <= number <= end and start <= number + 1 <= end:
                count += 1
        if count >= 2:
            result += 1
    return result
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120876
