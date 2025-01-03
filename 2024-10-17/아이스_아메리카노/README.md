# 아이스 아메리카노

[코딩테스트 연습 - 아이스 아메리카노][1] 로 이동

## 문제 설명

머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 `money`가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 제한사항

- 0 < `money` ≤ 1,000,000

## 입출력 예

| money  | result    |
| ------ | --------- |
| 5,500  | [1, 0]    |
| 15,000 | [2, 4000] |

## 입출력 예 설명

입출력 예 #1

- 5,500원은 아이스 아메리카노 한 잔을 살 수 있고 잔돈은 0원입니다.

입출력 예 #2

- 15,000원은 아이스 아메리카노 두 잔을 살 수 있고 잔돈은 4,000원입니다.

## 풀이

첫 번째 요소는 money를 소숫점을 버리는 나눗셈으로 구하고,
두 번째 요소는 money를 나눈 후 몫을 구하면 된다.

```python
def solution(money):
    return [money // 5500, money % 5500]
```

커피의 가격을 상수로 정의해 줄 수 있다.

```python
PRICE = 5500


def solution(money):
    return [money // PRICE, money % PRICE]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120819
