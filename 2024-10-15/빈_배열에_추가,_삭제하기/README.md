# 빈 배열에 추가, 삭제하기

[코딩테스트 연습 - 빈 배열에 추가, 삭제하기][1] 로 이동

## 문제 설명

아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 길이가 같은 정수 배열 `arr`과 boolean 배열 `flag`가 매개변수로 주어질 때, `flag`를 차례대로 순회하며 `flag[i]`가 true라면 X의 뒤에 `arr[i]`를 `arr[i]` × 2 번 추가하고, `flag[i]`가 false라면 X에서 마지막 `arr[i]`개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

## 제한사항

- 1 ≤ arr의 길이 = flag의 길이 ≤ 100
- arr의 모든 원소는 1 이상 9 이하의 정수입니다.
- 현재 X의 길이보다 더 많은 원소를 빼는 입력은 주어지지 않습니다.

## 입출력 예

| arr             | flag                              | result                   |
| --------------- | --------------------------------- | ------------------------ |
| [3, 2, 4, 1, 3] | [true, false, true, false, false] | [3, 3, 3, 3, 4, 4, 4, 4] |

## 입출력 예 설명

입출력 예 #1

- 예제 1번에서 X의 변화를 표로 나타내면 다음과 같습니다

| i   | flag[i] | arr[i] | X                                    |
| --- | ------- | ------ | ------------------------------------ |
|     |         |        | []                                   |
| 0   | true    | 3      | [3, 3, 3, 3, 3, 3]                   |
| 1   | false   | 2      | [3, 3, 3, 3]                         |
| 2   | true    | 4      | [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4] |
| 3   | false   | 1      | [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]    |
| 4   | false   | 3      | [3, 3, 3, 3, 4, 4, 4, 4]             |

- 따라서 [3, 3, 3, 3, 4, 4, 4, 4]를 return 합니다.

## 풀이

arr와 flag를 순회하며 조건에 맞는 연산을 해주면 된다.

```python
def solution(arr, flag):
    new_arr = []
    for number, is_true in zip(arr, flag):
        if is_true:
            new_arr += [number] * number * 2
        else:
            new_arr = new_arr[:-number]
    return new_arr
```

리스트의 + 연산은 기존 리스트를 복사한 뒤 새로운 요소를 추가하는 방식이므로,
메모리 복사가 발생해서 성능에 영향을 줄 수 있다.
따라서 += 연산을 사용하지 않고 extend() 메소드를 사용한다.

```python
def solution(arr, flag):
    new_arr = []
    for number, is_true in zip(arr, flag):
        if is_true:
            new_arr.extend([number] * number * 2)
        else:
            new_arr = new_arr[:-number]
    return new_arr
```

new_arr = new_arr[:-number] 는 슬라이싱을 이용해서 새로운 리스트를 만들어서 다시 할당하는 방식으로, 메모리 복사가 일어난다.
del을 사용하여 효과적으로 요소를 제거할 수 있다.

```python
def solution(arr, flag):
    new_arr = []
    for number, is_true in zip(arr, flag):
        if is_true:
            new_arr.extend([number] * number * 2)
        else:
            del new_arr[-number:]
    return new_arr
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181860
