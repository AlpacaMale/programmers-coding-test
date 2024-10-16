# 배열 만들기 2

[코딩테스트 연습 - 배열 만들기 2][1] 로 이동

## 문제 설명

정수 `l`과 `r`이 주어졌을 때, `l` 이상 `r`이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

## 제한사항

- 1 ≤ `l` ≤ `r` ≤ 1,000,000

## 입출력 예

| l   | r   | result                          |
| --- | --- | ------------------------------- |
| 5   | 555 | [5, 50, 55, 500, 505, 550, 555] |
| 10  | 20  | [-1]                            |

## 입출력 예 설명

입출력 예 #1

- 5 이상 555 이하의 0과 5로만 이루어진 정수는 작은 수부터 5, 50, 55, 500, 505, 550, 555가 있습니다. 따라서 [5, 50, 55, 500, 505, 550, 555]를 return 합니다.

입출력 예 #2

- 10 이상 20 이하이면서 0과 5로만 이루어진 정수는 없습니다. 따라서 [-1]을 return 합니다.

## 풀이

푸는 방법은 두가지가 있을 것 같다.
5의 배수인 숫자를 start와 end값을 구한 후, range() 함수를 이용해서 많은 숫자를 생성하고, 그중 5와 0만 포함된 숫자들을 골라내는것이다.

그리고 다른 방법은 리스트에 이미 있는 요소의 맨 뒤에 0, 5를 붙인 숫자를 새로 추가해주는것이다.

0, 5를 추가한 숫자를 계속 더하는 코드이다.

```python
def solution(l, r):
    numbers = [5]
    new_numbers = [5]
    while max(numbers) < r:
        current = new_numbers
        new_numbers = []
        for number in current:
            string = str(number)
            new_numbers.append(int(string + "0"))
            new_numbers.append(int(string + "5"))
        numbers.extend(new_numbers)

    return [number for number in numbers if l <= number <= r] or [-1]
```

all 함수를 이용해서 모든 요소가 조건에 일치하는지 확인할 수 있다.

```python
def solution(l, r):
    start = 5 * (l // 5)
    end = 5 * (r // 5) + 1
    return [
        number
        for number in range(start, end, 5)
        if l <= number <= r and all(c in "05" for c in str(number))
    ] or [-1]
```

두번째 코드는 엄청난 숫자를 만들어내고 반복도 많이하기 때문에 느리다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181921
