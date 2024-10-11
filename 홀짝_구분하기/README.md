# [홀짝 구분하기][1]

## 문제 설명

자연수 `n`이 입력으로 주어졌을 때 만약 `n`이 짝수이면 "`n` is even"을, 홀수이면 "`n` is odd"를 출력하는 코드를 작성해 보세요.

## 제한사항

- 1 ≤ `n` ≤ 1,000

## 입출력 예

입력 #1

```
100
```

출력 #1

```
100 is even
```

입력 #2

```
1
```

출력 #2

```
1 is odd
```

## 풀이

삼항 연산자를 통해 if - else 문을 간결하게 표현할 수 있다
f 스트링으로 간단한 출력 만들 수 있다

```python
a = int(input())
text = "even" if a % 2 == 0 else "odd"
print(f"{a} is {text}")
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181944
