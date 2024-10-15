# 1로 만들기

[코딩테스트 연습 - 1로 만들기][1] 로 이동

## 문제 설명

정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

- 10 / 2 = 5
- (5 - 1) / 2 = 2
- 2 / 2 = 1

위와 같이 3번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 `num_list`가 주어질 때, `num_list`의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 3 ≤ `num_list`의 길이 ≤ 15
- 1 ≤ `num_list`의 원소 ≤ 30

## 입출력 예

| num_list           | result |
| ------------------ | ------ |
| [12, 4, 15, 1, 14] | 11     |

## 입출력 예 설명

입출력 예 #1

- 12는 3번, 4는 2번, 15는 3번, 1은 0번, 14는 3번의 연산이 필요하기 때문에 총 11번의 연산이 필요합니다.

## 풀이

while문을 이용해서 num이 1이 될때까지 연산을 반복할 수 있다.
전역변수 count를 이용해서 전체 카운트의 횟수를 알 수 있다.

```python
def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = (num - 1) / 2
            count += 1
    return count
```

`(num - 1) / 2` 은 `num // 2`로 바꿀 수 있다.
//은 소수부분을 없에는 floor같은 연산이다.

```python
def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = num // 2
            count += 1
    return count
```

```python
if num % 2 == 0:
    num /= 2
else:
    num = num // 2
```

이 부분은

num //= 2 로 바꿀 수 있다.
어차피 소수가 남지 않는 나누기를 하는것이 목표이다.

```python
def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            num //= 2
            count += 1
    return count
```

최종 코드다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181880
