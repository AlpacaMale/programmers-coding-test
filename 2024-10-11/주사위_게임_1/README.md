# 주사위 게임 1
[코딩 테스트 연습 - 주사위 게임 1][1] 로 이동

## 문제 설명

1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 `a`, `b`라고 했을 때 얻는 점수는 다음과 같습니다.

- `a`와 `b`가 모두 홀수라면 `a^2` + `b^2` 점을 얻습니다.
- `a`와 `b` 중 하나만 홀수라면 2 × (`a` + `b`) 점을 얻습니다.
- `a`와 `b` 모두 홀수가 아니라면 |`a` - `b`| 점을 얻습니다.

두 정수 `a`와 `b`가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

## 제한사항

- `a`와 b는 1 이상 6 이하의 정수입니다.

## 입출력 예

| a   | b   | result |
| --- | --- | ------ |
| 3   | 5   | 34     |
| 6   | 1   | 14     |
| 2   | 4   | 2      |

## 입출력 예 설명

입출력 예 #1

- 예제 1번에서 두 주사위 숫자가 모두 홀수이므로 32 + 52 = 9 + 25 = 34점을 얻습니다. 따라서 34를 return 합니다.

입출력 예 #2

- 예제 2번에서 두 주사위 숫자 중 하나만 홀수이므로 2 × (6 + 1) = 2 × 7 = 14점을 얻습니다. 따라서 14를 return 합니다.

입출력 예 #3

- 예제 3번에서 두 주사위 숫자가 모두 홀수가 아니므로 |2 - 4| = |-2| = 2점을 얻습니다. 따라서 2를 return 합니다.

## 풀이

우선 짝수인지 확인하는 코드가 중복되기 때문에 함수화 하고,
check even 함수로 확인한 boolean을 조건문에 대입해서 문제를 풀었다.
두 조건중에 하나만 참일때 실행되는것을 베타적 논리합 이라고 하고, 파이썬에서는 `^`를 이용해서 표현할 수 있다.
절대값은 abs() 함수를 사용해서 만들 수 있다.

```python
def check_even(number):
    return number % 2 == 0


def solution(a, b):
    is_a_even = check_even(a)
    is_b_even = check_even(b)
    if not is_a_even and not is_b_even:
        return a**2 + b**2
    elif is_a_even ^ is_b_even:
        return 2 * (a + b)
    else:
        return abs(a - b)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181839
