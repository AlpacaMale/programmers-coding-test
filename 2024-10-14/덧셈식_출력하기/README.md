# 덧셈식 출력하기

[코딩테스트 연습 - 덧셈식 출력하기][1] 로 이동

## 문제 설명

두 정수 `a`, `b`가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

```
a + b = c
```

## 제한사항

- 1 ≤ `a`, `b` ≤ 100

## 입출력 예

입력 #1

```
4 5
```

출력 #1

```
4 + 5 = 9
```

## 풀이

f스트링을 이용해서 쉽게 풀 수 있다.

```python
a, b = map(int, input().strip().split(" "))
print(f"{a} + {b} = {a + b}")
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181947
