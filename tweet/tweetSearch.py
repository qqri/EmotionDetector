# 가져올 범위를 정의

import GetOldTweets3 as got
import datetime
import time

days_range = []

start = datetime.datetime.strptime("2020-01-12","%Y-%m-%d")
end = datetime.datetime.strptime("2020-01-13","%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0,(end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

print("설정된 트윗 수집 기간은 {}에서 {}까지 입니다.".format(days_range[0],days_range[-1]))
print("총 {}일간의 데이터 수집!".format(len(days_range)))

# 특정 검색어가 포함된 트윗 검색! (quary search)
# str 변수가 검색어임
str = "오늘"

print("검색 단어는 [ %s ] 입니다." %str)

#수집 기간을 맞추자
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d")
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# setUntil이 끝을 포함하지 않으므로, day + 1

#트윗 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(str)\
    .setSince(start_date)\
    .setUntil(end_date)\
    .setMaxTweets(-1)

#수집 with GetOldTweet3
print("{} 에서 {} 까지 검색 시작...".format(days_range[0], days_range[-1]))
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("Collecting data end.. {0:0.2f} Minutes".format((time.time() - start_time)/60))
print("=== Total num of tweets is {} ===".format(len(tweet)))