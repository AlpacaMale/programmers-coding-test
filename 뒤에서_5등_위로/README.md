# 뒤에서 5등 위로
[코딩 테스트 연습 - 뒤에서 5등 위로][1] 로 이동

## 문제 설명

정수로 이루어진 리스트 `num_list`가 주어집니다. `num_list`에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 6 ≤ `num_list`의 길이 ≤ 30
- 1 ≤ `num_list`의 원소 ≤ 100

## 입출력 예

| num_list                               | result               |
| -------------------------------------- | -------------------- |
| [12, 4, 15, 46, 38, 1, 14, 56, 32, 10] | [15, 32, 38, 46, 56] |

## 입출력 예 설명

입출력 예 #1

- [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]를 정렬하면 [1, 4, 10, 12, 14, 15, 32, 38, 46, 56]이 되고, 앞에서 부터 6번째 이후의 수들을 고르면 [15, 32, 38, 46, 56]가 됩니다.

## 풀이

sort() 메소드를 이용해서 리스트를 정렬할 수 있다 이 때, sort() 메소드를 사용한 리스트를 `num_list = num_list.sort()` 로 대입하면 안된다.

sort() 메소드는 None을 반환한다

```python
def solution(num_list):
    num_list.sort()
    return num_list[5:]
```

만약 대입하고싶으면 sorted() 함수를 사용하면된다.

```python
def solution(num_list):
    return sorted(num_list)[5:]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181852
