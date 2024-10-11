# 홀수 vs 짝수
[코딩 테스트 연습 - 홀수 vs 짝수][1] 로 이동

## 문제 설명

정수 리스트 `num_list`가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

## 제한사항

- 5 ≤ `num_list`의 길이 ≤ 50
- -9 ≤ `num_list`의 원소 ≤ 9

## 입출력 예

| num_list           | result |
| ------------------ | ------ |
| [4, 2, 6, 1, 7, 6] | 17     |
| [-1, 2, 5, 6, 3]   | 8      |

## 입출력 예 설명

입출력 예 #1

- 홀수 번째 원소들의 합은 4 + 6 + 7 = 17, 짝수 번째 원소들의 합은 2 + 1 + 6 = 9 이므로 17을 return합니다.

입출력 예 #2

- 홀수 번째 원소들의 합은 -1 + 5 + 3 = 7, 짝수 번째 원소들의 합은 2 + 6 = 8 이므로 8을 return합니다.

## 풀이

enumerate 함수는 이터러블 객체의 인덱스와 밸류를 튜플의 형태로 저장한 리스트를 반환한다.

for문과 enumerate 함수를 이용해서 홀수 인덱스, 짝수 인덱스를 구분한다.

홀수번째 인덱스의 값의 합을 저장하는 변수와 짝수번째 인덱스의 값의 합을 저장하는 변수를 따로 만들고 각각 더해준다.

max를 이용해서 큰 값을 리턴해준다.

```python
def solution(num_list):
    sum_of_value_of_even_index = 0
    sum_of_value_of_odd_index = 0
    for index, num in enumerate(num_list):
        if index % 2 == 0:
            sum_of_value_of_odd_index += num
        else:
            sum_of_value_of_even_index += num
    return max(sum_of_value_of_even_index, sum_of_value_of_odd_index)
```

밑의 풀이는 다른 사람의 풀이에서 가장 많은 좋아요를 받은 풀이이다.

슬라이싱을 이용해서 원하는 범위의 인덱스를 찾았다.

하지만 이런 방식은 리스트를 두번 순회하고, 리스트와 같은 사이즈의 리스트를 메모리에 복사하기 때문에 시간 복잡도와 공간 복잡도가 증가한다.

시간 복잡도가 증가했지만 big O 표기법으로는 위의 코드와 아래의 코드 모두 **O(n)** 으로 같다

공간 복잡도는 위의 코드가 **O(1)** 이며, 아래의 코드가 **O(n)**이다.

```python
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181887
