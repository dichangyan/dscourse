#从youtube csv 中读取评论数量的直方图
import numpy as np
from matplotlib import pyplot as plt
uk_data_path="youtube_video_data/GB_video_data_numbers.csv"
us_data_path="youtube_video_data/US_video_data_numbers.csv"
us_data=np.loadtxt(us_data_path,delimiter=",",dtype=int)
uk_data=np.loadtxt(uk_data_path,delimiter=",",dtype=int)
#取评论的数据
us_comments=us_data[0:,-1]
#清洗数据，去除》5000的
us_comments=us_comments[us_comments<5000]
print(us_comments.max(),us_comments.min())
d=50
bin_num=(us_comments.max()-us_comments.min())//d

plt.figure(figsize=(20,8),dpi=80)
plt.hist(us_comments,bin_num)
plt.show()
