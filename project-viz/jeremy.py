import json, urllib, pandas as pd, numpy as np
from matplotlib import pyplot as plt
from pylab import *
from collections import Counter

url = "https://itunes.apple.com/us/rss/customerreviews/id=874498884/sortBy=mostRecent/json"
response = urllib.urlopen(url);
reviews = json.load(response)
revs = reviews['feed']['entry']
review_content = []

review_data = pd.read_json(url)

for rev in revs[1:]:
    current_review = rev['content']['label']
    review_content.append(current_review)

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']


review_content = str(review_content)
review_content = review_content.split()
review_content_lowercase = [i.lower() for i in review_content ]
review_content_without_stopwords = [i for i in review_content_lowercase if i not in stopwords]
c = Counter(review_content_without_stopwords)
unique_word_count = c.most_common() 

print review_data.head()
print unique_word_count[1:20]

counts = []
words = []

for i in unique_word_count[1:10]:
    words.append(i[0])
    counts.append(i[1])  

plt.bar(arange(len(counts)), counts)
plt.xticks(arange(len(words)),words, rotation=80)
plt.suptitle('Word count in most 50 recent iTunes reviews')
plt.xlabel('Word')
plt.ylabel('Instances')
plt.tight_layout()
plt.show()

star_ratings = []
star_counts = []

for rev in revs[1:]:
    current_rating = rev['im:rating']['label']
    star_ratings.append(current_rating)

for i in star_ratings:
    str(i)
    star_counts.append(i)

star_counter = Counter(star_counts)
unique_star_counter = star_counter.most_common()

num_stars = range(1,6)
num_stars = num_stars[::-1]
count_stars = []

for i in unique_star_counter:
    str(i)
    count_stars.append(i[1])

plt.bar(arange(len(count_stars)), count_stars)
plt.xticks(arange(len(num_stars)),num_stars, rotation=80)
plt.suptitle('Distribution of star ratings in 50 most recent iTunes reviews')
plt.xlabel('Star Rating')
plt.ylabel('Instances')
plt.show()
