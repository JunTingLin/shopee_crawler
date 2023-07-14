import pandas as pd
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ------統計商品資料--------

# 讀取 CSV 檔案
df = pd.read_csv('廚具_商品資料.csv')

# 讀取停用詞列表
stopwords = pd.read_csv('stop.txt', header=None, sep='\t', names=['stopword'])

# 提取商品名稱的關鍵字
keywords = []
for name in df['商品名稱']:
    seg_list = jieba.cut(name)
    for word in seg_list:
        if word not in stopwords['stopword'].values and word != ' ': # 過濾掉停用詞和空格
            keywords.append(word)

# 計算關鍵字的出現次數
keyword_counts = Counter(keywords)

# 取得前10項最常出現的關鍵字
top_keywords = keyword_counts.most_common(10)

# 繪製圓餅圖
labels = [kw[0] for kw in top_keywords]
sizes = [kw[1] for kw in top_keywords]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 使用中文字體
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Top 10 Keywords')
plt.show()


# -----統計單價、收益資料--------
