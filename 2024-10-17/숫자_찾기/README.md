# 숫자 찾기

[코딩테스트 연습 - 숫자 찾기][1] 로 이동

## 문제 설명

정수 `num`과 `k`가 매개변수로 주어질 때, `num`을 이루는 숫자 중에 `k`가 있으면 `num`의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

## 제한사항

- 0 < `num` < 1,000,000
- 0 ≤ `k` < 10
- `num`에 `k`가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.

## 입출력 예

| num    | k   | result |
| ------ | --- | ------ |
| 29183  | 1   | 3      |
| 232443 | 4   | 4      |
| 123456 | 7   | -1     |

## 입출력 예 설명

입출력 예 #1

- 29183에서 1은 3번째에 있습니다.

입출력 예 #2

- 232443에서 4는 4번째에 처음 등장합니다.

입출력 예 #3

- 123456에 7은 없으므로 -1을 return 합니다.

## 풀이

num을 str() 함수로 형변환 해준 후에 enumerate() 함수를 사용해서 char가 일치하는 index를 반환해준다.

```python
def solution(num, k):
    for index, char in enumerate(str(num)):
        if int(char) == k:
            return index + 1
    return -1
```

매 반복마다 int()를 사용하지 않고 k를 str() 로 형변환해줘서 반복간에 연산횟수를 줄일 수 있다.

```python
def solution(num, k):
    k = str(k)
    for index, char in enumerate(str(num)):
        if char == k:
            return index + 1
    return -1
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120904
