# 가장 큰 수 찾기

[코딩테스트 연습 - 가장 큰 수 찾기][1] 로 이동

## 문제 설명

정수 배열 `array`가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 제한사항

- 1 ≤ `array`의 길이 ≤ 100
- 0 ≤ `array` 원소 ≤ 1,000
- `array`에 중복된 숫자는 없습니다.

## 입출력 예

| array          | result  |
| -------------- | ------- |
| [1, 8, 3]      | [8, 1]  |
| [9, 10, 11, 8] | [11, 2] |

## 입출력 예 설명

입출력 예 #1

- 1, 8, 3 중 가장 큰 수는 8이고 인덱스 1에 있습니다.

입출력 예 #2

- 9, 10, 11, 8 중 가장 큰 수는 11이고 인덱스 2에 있습니다.

## 풀이

파이써닉한 코드를 사용한다면 코드를 한줄로 작성할 수 있다.
max() 함수와 index() 메소드를 같이 이용해서 값을 찾을 수 있다.

```python
def solution(array):
    return [max(array), array.index(max(array))]

```

하지만 위의 코드는 배열을 여러번 순회하기 때문에 비효율적일수있다.

```python
def solution(array):
    max_number, max_index = 0, 0
    for index, number in enumerate(array):
        if max_number < number:
            max_number = number
            max_index = index
    return [max_number, max_index]
```

이 코드는 직접 for문을 사용하여 max_number와 max_index를 업데이트해주는 코드다.
for문을 한번만 돌리기 때문에 효율이 좋다.

성능이 문제되지 않는다면 첫 번째 코드를 사용하고,
성능이 중요하다면 아래 코드를 사용하는것이 좋다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120899
