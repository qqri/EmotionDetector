from konlpy.tag import Twitter
from collections import Counter
from konlpy.tag import Twitter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nlpy = Twitter()
# 입력변수- text : 댓글, ntags : 표시할 단어수, multiplier : 크기가중치
def get_tags(text, ntags=30, multiplier=2):
    t = Twitter()
    nouns = []

emotion = []
file = open('depression.txt', 'r',  encoding= 'unicode_escape')
lines = file.readlines()

wordcloud = WordCloud(
  font_path = 'C:/Windows/Fonts/Hancom Gothic Bold.ttf',
  background_color='white',
  max_words=2000,
).generate(' '.join(nouns))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()