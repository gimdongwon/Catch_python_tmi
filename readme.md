# Catch_Python_Tmi

파이썬 코딩테스트를 위한 알고리즘 스터디 모임입니다.

[스터디 노션 페이지](https://www.notion.so/cd77d4ca02c746eeb00e8d8fc0560b59)

## 팀원

1. 김동원
2. 김진현(👑)
3. 나채빈
4. 안우진

## 모임시간

매주 화요일 오후 12시, 2시간, [서울역 아지트](https://map.naver.com/v5/entry/address/14133799.37361801,4516399.126125481,%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%9A%A9%EC%82%B0%EA%B5%AC%20%EC%84%9C%EA%B3%84%EB%8F%99%2033-157,jibun?c=14133770.1967795,4516399.9264848,19,0,0,0,dh)

## 스터디 진행방식

1. 온라인
   - 코드리뷰 (매 pr 마다 코멘트 남기기(필수))
   - 매주 부여된 과제 해결(매주 일요일 자정까지)
2. 오프라인
   - 돌아가며 풀이 발표

## PR 규칙

1. 해당 Repo를 Clone을 받고
2. main branch에서 자기 이름을 가진 branch 생성
3. 폴더 구조(자기 이름폴더)에 따라 주차에 맞는 문제 풀기
4. 작업완료 후 자신의 브랜치에서 Commit 완료 후 remote에 자신의 branch로 push
5. github repo에 pull request 페이지에서 new pull request 생성
6. 코드리뷰 진행 후
7. 오프라인 스터디가 끝나면 일괄 pr 승인으로 main merge.
8. pr 메시지는 "[동원] 1주차 문제 풀이"

## 과제

- 1st (카카오 기출)
  + 신규아이디 추천
  + 메뉴 리뉴얼
- 2nd (카카오 기출)
  + 튜플
  + 수식 최대화
- 3rd (그리디 홀수번)
   + 모험가 길드
   + 문자열 뒤집기
   + 볼링공 고르기
- 4th (그리디 짝수번)
   + 곱하기 혹은 더하기
   + 만들 수 없는 금액
   + 무지의 먹방 라이브
- 5th (구현 홀수번)
   + 럭키 스트레이트
   + 문자열 압축
   + 뱀
   + 치킨 배달
- 6th (구현 짝수번)
   + 문자 재정렬
   + 자물쇠와 열쇠
   + 기둥과 보 설치
   + 외벽 점검
- 7th (DFS/BFS 홀수번)
   + 특정한 거리의 도시 찾기
   + 경쟁적 전염
   + 연산자 끼워 넣기
   + 인구 이동
- 8th (DFS/BFS 짝수번)
   + 연구소
   + 괄호 변환
   + 감시 피하기
   + 블록 이동하기
- 9th (네이버웹툰 기출)
- 10th (정렬)
   + 국영수
   + 안테나
   + 실패율
   + 카드 정렬하기
- 11th (이진탐색)
   + 정렬된 배열에서 특정 수의 개수 구하기
   + 고정점 찾기
   + 공유기 설치
   + 가사 검색
   
## 참고 문서

- [Code Review](https://ehddnjs8989.medium.com/%EC%BD%94%EB%93%9C%EB%A6%AC%EB%B7%B0-code-review-ec557ae8168)
- [Code Review 요약 및 구체적 방안](https://ehddnjs8989.medium.com/%EC%BD%94%EB%93%9C%EB%A6%AC%EB%B7%B0-code-review-%EC%9D%98-%EA%B5%AC%EC%B2%B4%EC%A0%81%EC%9D%B8-%EB%B0%A9%EC%95%88-%EB%B0%8F-%EC%A0%81%EC%9A%A9-ad4bd465391b)

## 입출력 제한 확인하기.

1. 입력이 100 이하인 경우

- 완전탐색
- 백트래킹

2. 10,000 이하인 경우

- O(n^2) 이내로 끝내야 함.
- 문제에 따라 O(n^2 log n) 까지 가능 하기도 함
- n^n 2차원 리스트 순회하는 문제가 많음.

3. 1,000,000 이하인 경우

- O(n log n) 이하로 끝내야 함.
- 힙, 우선순위 큐
- 정렬
- 다익스트라
- 위상정렬
- 동적 계획법

4. 100,000,000 이하인 경우

- 최대 O(n)으로 끝내야 함
- 동적 계획법
- 그리디

5. 그 이상인 경우

- O(log n)으로 끝내야 함
- 이진 탐색
