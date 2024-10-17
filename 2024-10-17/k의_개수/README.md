# k의 개수

[코딩테스트 연습 - k의 개수][1] 로 이동

## 문제 설명

1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 `i`, `j`, `k`가 매개변수로 주어질 때, `i`부터 `j`까지 `k`가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

## 제한사항

- 1 ≤ `i` < `j` ≤ 100,000
- 0 ≤ `k` ≤ 9

## 입출력 예

| i   | j   | k   | result |
| --- | --- | --- | ------ |
| 1   | 13  | 1   | 6      |
| 10  | 50  | 5   | 5      |
| 3   | 10  | 2   | 0      |

## 입출력 예 설명

입출력 예 #1

- 본문과 동일합니다.

입출력 예 #2

- 10부터 50까지 5는 15, 25, 35, 45, 50 총 5번 등장합니다. 따라서 5를 return 합니다.

입출력 예 #3

- 3부터 10까지 2는 한 번도 등장하지 않으므로 0을 return 합니다.

## 풀이

count를 이용해서 문자열에 얼마나 자주 등장하는지 확인할 수 있다.

```python
def solution(i, j, k):
    total_frequency = 0
    for number in range(i, j + 1):
        total_frequency += str(number).count(str(k))
    return total_frequency
```

컴프리헨션을 이용해서 더 짧게 풀 수 있다.
k를 미리 문자열로 변환해서 반복당 연산 하나를 줄였다.

```python
def solution(i, j, k):
    k = str(k)
    return (str(number).count(k) for number in range(i, j + 1))
```

문자열을 전부 합친 후에 count(k)를 해줌으로써 반복당 연산 하나를 줄였다.

```python
def solution(i, j, k):
    return "".join(str(number) for number in range(i, j + 1)).count(str(k))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120887
