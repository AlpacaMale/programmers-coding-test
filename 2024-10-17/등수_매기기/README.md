# 등수 매기기

[코딩테스트 연습 - 등수 매기기][1] 로 이동

## 문제 설명

영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 `score`가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항

- 0 ≤ `score[0]`, `score[1]` ≤ 100
- 1 ≤ `score`의 길이 ≤ 10
- `score`의 원소 길이는 2입니다.
- `score`는 중복된 원소를 갖지 않습니다.

## 입출력 예

score result
[[80, 70], [90, 50], [40, 70], [50, 80]] [1, 2, 4, 3]
[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]] [4, 4, 6, 2, 2, 1, 7]

## 입출력 예 설명

입출력 예 #1

- 평균은 각각 75, 70, 55, 65 이므로 등수를 매겨 [1, 2, 4, 3]을 return합니다.

입출력 예 #2

- 평균은 각각 75, 75, 40, 95, 95, 100, 20 이므로 [4, 4, 6, 2, 2, 1, 7] 을 return합니다.
- 공동 2등이 두 명, 공동 4등이 2명 이므로 3등과 5등은 없습니다.

## 풀이

공동 n등을 표현하기 위해서 Counter 객체를 사용하였다.
효율을 개선하기 위해서 Counter와 sorted list의 선언부분을 수정할 수 있다.

```python
from collections import Counter


def solution(score):
    total_freq = Counter(eng + math for eng, math in score)
    sorted_total_list = sorted(total_freq, key=lambda x: -x)
    ranks = []
    for eng, math in score:
        my_total_score = eng + math
        rank = 0
        for total_score in sorted_total_list:
            if total_score == my_total_score:
                rank += 1
                break
            else:
                rank += total_freq[total_score]
        ranks.append(rank)
    return ranks
```

이중 for문을 제거하기 위해서 딕셔너리를 사용해서 미리 순위를 계산해서 넣었다.

```python
from collections import Counter


def solution(score):
    total_scores = [eng + math for eng, math in score]
    total_freq = Counter(total_scores)
    sorted_total_list = sorted(total_freq, key=lambda x: -x)
    ranks = {}
    rank = 1
    for total in sorted_total_list:
        ranks[total] = rank
        rank += total_freq[total]

    return [ranks[total] for total in total_scores]
```

[1]: https://school.programmers.co.kr/learn/courses/30/lessons/120882
