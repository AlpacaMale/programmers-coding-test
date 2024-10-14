# 이차원 배열 대각선 순회하기

[코딩테스트 연습 - 이차원 배열 대각선 순회하기][1] 로 이동

## 문제 설명

2차원 정수 배열 `board`와 정수 `k`가 주어집니다.

`i` + `j` <= `k`를 만족하는 모든 (`i`, `j`)에 대한 `board[i][j]`의 합을 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `board`의 길이 ≤ 100
- 1 ≤ `board[i]`의 길이 ≤ 100
- 1 ≤ `board[i][j]` ≤ 10,000
- 모든 `board[i]`의 길이는 같습니다.
- 0 ≤ k < board의 길이 + `board[i]`의 길이

## 입출력 예

| board                                     | k   | result |
| ----------------------------------------- | --- | ------ |
| [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]] | 2   | 8      |

## 입출력 예 설명

입출력 예 #1

- 입출력 예 #1의 `board`를 표로 나타내면 다음과 같습니다.

| i \ j | 0   | 1   | 2   |
| ----- | --- | --- | --- |
| 0     | 0   | 1   | 2   |
| 1     | 1   | 2   | 3   |
| 2     | 2   | 3   | 4   |
| 3     | 3   | 4   | 5   |

- `i` + `j`가 2보다 작거나 같은 항들의 합은 0 + 1 + 2 + 1 + 2 + 2 = 8이므로 8을 return 합니다.

## 풀이

2차원 배열을 순회하며 i + j <= k 인 값들을 리스트에 담고 sum() 함수로 더해준다.

```python
def solution(board, k):
    return sum(
        board[i][j]
        for i in range(len(board))
        for j in range(len(board[i]))
        if i + j <= k
    )
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181829
