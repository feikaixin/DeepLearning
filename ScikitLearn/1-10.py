"""
sklearn中如何查看模型评估招标
"""

from sklearn import metrics

scores = sorted(metrics.SCORERS.keys())

print(scores)