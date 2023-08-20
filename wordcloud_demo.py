from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Specify the font path for "標楷體"
font_path = 'C:\\Windows\\Fonts\\msjh.ttc'

# Set the font properties using rcParams
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # For 標楷體 on Windows

# Keywords for each category
keywords = {
    "Product name - high price": ["Rolex", "Omega", "機械", "自動", "GPS", "限量", "瑞士", "金屬", "手工", "豪華"],
    "Product name - low price": ["電子", "石英", "塑膠", "便宜", "時尚", "日常", "運動", "小巧", "輕便", "學生"],
    "Comment - high price": ["有質感", "品質優良", "精緻", "保卡", "豪華", "尊貴", "高級", "值得", "美觀", "經典"],
    "Comment - low price": ["物超所值", "輕便", "適合日常", "運動", "易用", "便宜", "實用", "時尚", "舒適", "功能多"]
}

# Generate word clouds
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()

for i, (key, words) in enumerate(keywords.items()):
    text = ' '.join(words)
    wordcloud_instance = WordCloud(font_path=font_path, width=400, height=400, background_color='white').generate(text)
    axes[i].imshow(wordcloud_instance, interpolation='bilinear')
    axes[i].axis('off')
    axes[i].set_title(key)

plt.tight_layout()
plt.show()
