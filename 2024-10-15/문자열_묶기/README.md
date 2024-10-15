# 문자열 묶기

[코딩테스트 연습 - 문자열 묶기][1] 로 이동

## 문제 설명

문자열 배열 `strArr`이 주어집니다. `strArr`의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

## 제한사항

- 1 ≤ `strArr`의 길이 ≤ 100,000
- 1 ≤ `strArr`의 원소의 길이 ≤ 30
- `strArr`의 원소들은 알파벳 소문자로 이루어진 문자열입니다.

## 입출력 예

| strArr                    | result |
| ------------------------- | ------ |
| ["a","bc","d","efg","hi"] | 2      |

## 입출력 예 설명

입출력 예 #1

- 각 문자열들을 길이에 맞게 그룹으로 묶으면 다음과 같습니다.

| 문자열 길이 | 문자열      | 목록 개수 |
| ----------- | ----------- | --------- |
| 1           | ["a","d"]   | 2         |
| 2           | ["bc","hi"] | 2         |
| 3           | ["efg"]     | 1         |

- 개수의 최댓값은 2이므로 2를 return 합니다.

## 풀이

문자열로 되어있는 배열을 이용해서 문자열의 길이를 표시하는 리스트를 새로 생성한다.
빈도수를 구하기 위해서 set을 이용해 length를 길이별로 분류한다.
set 을 순회하며 length_arr의 요소가 length_set의 요소를 몇번가졌는지 확인한다.

```python
def solution(strArr):
    length_arr = [len(string) for string in strArr]
    length_set = set(length_arr)
    return max(length_arr.count(count) for count in length_set)
```

이 코드는 파이써닉하지만 많이 느린 코드이며, 대용량 데이터를 처리할때 심각한 성능 문제가 발생할 수 있다.

```python
def solution(strArr):
    length_count = {}
    for string in strArr:
        length = len(string)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    return max(length_count.values())
```

대신 length와 count를 key value 형식으로 매핑하는 딕셔너리를 만들어서 속도를 개선할 수 있다.

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181855
