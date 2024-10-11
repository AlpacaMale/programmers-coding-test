# 꼬리 문자열
[코딩 테스트 연습 - 꼬리 문자열][1] 로 이동

## 문제 설명

문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.

문자열 리스트 `str_list`와 제외하려는 문자열 `ex`가 주어질 때, `str_list`에서 `ex`를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 2 ≤ `str_list`의 길이 ≤ 10
- 1 ≤ `str_list`의 원소의 길이 ≤ 10
- 1 ≤ `ex`의 길이 ≤ 5

## 입출력 예

| str_list              | ex   | result   |
| --------------------- | ---- | -------- |
| ["abc", "def", "ghi"] | "ef" | "abcghi" |
| ["abc", "bbc", "cbc"] | "c"  | ""       |

## 입출력 예 설명

입출력 예 #1

- 본문과 동일합니다.

입출력 예 #2

- 리스트 안의 모든 문자열이 "c"를 포함하므로 빈 문자열을 return합니다.

## 풀이

제너레이터 컴프리헨션과 if문을 이용해서 특정 조건의 요소로만 리스트를 생성할 수 있다.
join 메소드를 사용해서 리스트 안의 문자열을 합칠 수 있다.

```python
def solution(str_list, ex):
    return "".join(str for str in str_list if ex not in str)
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/181841
