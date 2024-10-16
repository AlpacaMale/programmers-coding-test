# 정수를 나선형으로 배치하기

[코딩테스트 연습 - 정수를 나선형으로 배치하기][1] 로 이동

## 문제 설명

양의 정수 `n`이 매개변수로 주어집니다. `n` × `n` 배열에 1부터 `n^2` 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

## 제한사항

- 1 ≤ `n` ≤ 30

## 입출력 예

| n   | result                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------- |
| 4   | [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]                                       |
| 5   | [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]] |

## 입출력 예 설명

입출력 예 #1

- 예제 1번의 `n`의 값은 4로 4 × 4 배열에 다음과 같이 1부터 16까지 숫자를 채울 수 있습니다.

| 행 \ 열 | 0   | 1   | 2   | 3   |
| ------- | --- | --- | --- | --- |
| 0       | 1   | 2   | 3   | 4   |
| 1       | 12  | 13  | 14  | 5   |
| 2       | 11  | 16  | 15  | 6   |
| 3       | 10  | 9   | 8   | 7   |

- 따라서 [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]를 return 합니다.

입출력 예 #2

- 예제 2번의 `n`의 값은 5로 5 × 5 배열에 다음과 같이 1부터 25까지 숫자를 채울 수 있습니다.

| 행 \ 열 | 0   | 1   | 2   | 3   | 4   |
| ------- | --- | --- | --- | --- | --- |
| 0       | 1   | 2   | 3   | 4   | 5   |
| 1       | 16  | 17  | 18  | 19  | 6   |
| 2       | 15  | 24  | 25  | 20  | 7   |
| 3       | 14  | 23  | 22  | 21  | 8   |
| 4       | 13  | 12  | 11  | 10  | 9   |

- 따라서 [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]를 return 합니다.

## 풀이

right, down, left, up 의 방향을 설정하고, 방향이 정해졌다면 현재까지 실행한 count를 마킹하며 x, y 좌표를 이동하는 코드이다.

가장 처음 n \* n의 2차원 배열을 만들고 이후에 값을 변경하는 방법으로 한다.

```python
def solution(n):
    array = [[0] * n for _ in range(n)]
    direction = "right"
    x, y = 0, 0
    counter = 1
    while True:
        if counter != n**2:
            if direction == "right":
                if x + 1 == n or array[y][x + 1] != 0:
                    direction = "down"
                else:
                    array[y][x] = counter
                    counter += 1
                    x += 1
            elif direction == "down":
                if y + 1 == n or array[y + 1][x] != 0:
                    direction = "left"
                else:
                    array[y][x] = counter
                    counter += 1
                    y += 1
            elif direction == "left":
                if x - 1 < 0 or array[y][x - 1] != 0:
                    direction = "up"
                else:
                    array[y][x] = counter
                    counter += 1
                    x -= 1
            else:
                if array[y - 1][x] != 0:
                    direction = "right"
                else:
                    array[y][x] = counter
                    counter += 1
                    y -= 1
        else:
            array[y][x] = counter
            break
    return array
```

위의 코드에서 문자열 right 등을 상수로 정의하며, 코드에 쓸모가 있도록 x, y의 변화값을 넣어주었다.
while 안에서 if로 체크하던 조건을 while문의 조건으로 만들고 마지막 정수를 배치하는 코드를 while문 밖으로 빼주었다.

if문을 줄이기 위해서 조건문을 변경하였다.

```python
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)


def solution(n):
    matrix = [[0] * n for _ in range(n)]
    direction = RIGHT
    x, y = 0, 0
    counter = 1

    while counter != n**2:
        if (
            0 <= y + direction[0] < n
            and 0 <= x + direction[1] < n
            and matrix[y + direction[0]][x + direction[1]] == 0
        ):
            matrix[y][x] = counter
            y += direction[0]
            x += direction[1]
            counter += 1
        else:
            if direction == RIGHT:
                direction = DOWN
            elif direction == DOWN:
                direction = LEFT
            elif direction == LEFT:
                direction = UP
            else:
                direction = RIGHT
    matrix[y][x] = counter

    return matrix
```

위의 코드에서 next_x, y 를 미리 계산해서 연산 횟수를 줄이고, directions 리스트를 만들어서 if문의 개수를 줄였다.

```python
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)


def solution(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [RIGHT, DOWN, LEFT, UP]
    direction_index = 0
    x, y = 0, 0
    counter = 1

    while counter != n**2:
        next_y = y + directions[direction_index][0]
        next_x = x + directions[direction_index][1]

        if 0 <= next_y < n and 0 <= next_x < n and matrix[next_y][next_x] == 0:
            matrix[y][x] = counter
            counter += 1
            y = next_y
            x = next_x
        else:
            direction_index = (direction_index + 1) % 4
    matrix[y][x] = counter

    return matrix
```

위의 코드에서 반복문의 조건을 바꾸고 코드의 가독성을 개선하면 아래처럼 바뀐다.

```python
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)


def solution(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [RIGHT, DOWN, LEFT, UP]
    direction_index = 0
    x, y = 0, 0
    counter = 1

    while counter <= n**2:
        matrix[y][x] = counter
        counter += 1

        next_y = y + directions[direction_index][0]
        next_x = x + directions[direction_index][1]

        if not (0 <= next_y < n and 0 <= next_x < n and matrix[next_y][next_x] == 0):
            direction_index = (direction_index + 1) % 4
            next_y = y + directions[direction_index][0]
            next_x = x + directions[direction_index][1]

        x, y = next_x, next_y

    return matrix
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181832
