'''
twitter 크롤링
'''

import tweepy

# 트위터 앱의 Keys and Access Tokens 탭 참조(자신의 설정 값을 넣어준다)
consumer_key = 'mykey'
consumer_secret = 'mykey'

# 1. 인증요청(1차) : 개인 앱 정보
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = 'mykey'
access_token_secret= 'mykey'

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)

keyword = "🙁","ㅠ";     # 자신이 검색하고 싶은 키워드 입력 > 저희는 이 키워드로 크롤링 했습니다.
search = [] # 크롤링 결과 저장할 변수

cnt = 1
while(cnt <= 30):   # 10page 대상으로 크롤링
   tweets = api.search(keyword)
   for tweet in tweets:
       search.append(tweet)
   cnt += 1

#전체 문서 보기

data = {}   # 전체 문서 추가
i = 0       # 문서 번호
for tweet in search:
    data['text'] = tweet.text   # text키에 text문서 저장
    print(i, " : ", data)   # 문서번호 : 문서내용
    i += 1

print(len(search)) # 문서 길이
print(search[0]) # 첫번째 text 보기