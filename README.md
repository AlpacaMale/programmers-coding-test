# 프로그래머스 코딩 테스트 레포지토리

[프로그래머스][1] 사이트에 게시된 문제들을 풀고, 해답을 정리해놓은 레포지토리 입니다

## 목차

- 소개
- 폴더 구조
- 폴더 생성 스크립트
- 문제 풀이
- 사용 언어
- 날짜 포멧

## 소개

프로그래머스 사이트에 게시된 다양한 알고리즘 및 자료구조 문제를 해결하고, 문제별 풀이 방법을 정리하는 레포지토리 입니다. 문제의 이해 및 해답을 제공함으로써, 코딩 테스트 준비와 알고리즘 공부에 도움이 되고자 합니다.

## 폴더 구조

```
├── YYYY-MM-DD/
│   ├── README.md
│   ├── 문제이름1/
│   │   ├── 문제이름1.py
│   │   ├── README.md
│   ├── 문제이름2/
│   │   ├── 문제이름2.py
│   │   ├── README.md
│   └── ...
```

## 폴더 생성 스크립트

리눅스 환경에서

```zsh
./mk2folder.sh 문제이름
```

명령어를 실행하여

```
.
├── 문제이름/
│ ├── 문제이름.py
│ └── README.md # 풀이 설명
```

의 폴더 구조를 생성할 수 있습니다.

## 문제 풀이

각 문제별로 풀이 코드를 제공하며, 문제에 대한 설명과 함께 시간 복잡도 및 해결 방법도 함께 정리합니다.

## 사용 언어

- 파이썬

## 날짜 포멧

커밋 메시지에 사용되는 날짜 포멧은 YYYY-MM-DD 입니다.

[1]: https://school.programmers.co.kr/learn/challenges?order=recent
