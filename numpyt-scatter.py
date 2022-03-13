#从youtube csv 中读取，绘制相关散点图
import numpy as np
from matplotlib import pyplot as plt
uk_data_path="youtube_video_data/GB_video_data_numbers.csv"
us_data_path="youtube_video_data/US_video_data_numbers.csv"

uk_data=np.loadtxt(uk_data_path,delimiter=",",dtype=int)

uk_data=uk_data[uk_data[:,-1]<5000]
data_comment=uk_data[:,-1]#评论数

data_like=uk_data[:,1]#喜欢数
plt.figure(figsize=(10,8),dpi=80)
plt.scatter(data_comment,data_like)
plt.xlabel("comment")
plt.ylabel("like")
plt.show()


