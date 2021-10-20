import pandas as pd
import csv 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("StudentsPerformance.csv")
data_list=df["reading score"].to_list()

data_mean=statistics.mean(data_list)
data_median=statistics.median(data_list)
data_mode=statistics.mode(data_list)
data_std_deviation=statistics.stdev(data_list)

first_std_deviation_start, first_std_deviation_end = data_mean-data_std_deviation, data_mean+data_std_deviation
second_std_deviation_start, second_std_deviation_end = data_mean-(2*data_std_deviation), data_mean+(2*data_std_deviation)
third_std_deviation_start, third_std_deviation_end = data_mean-(3*data_std_deviation), data_mean+(3*data_std_deviation)

thin_1_std_deviation = [result for result in data_list if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in data_list if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in data_list if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of this data is : " , data_mean)
print("Median of this data is : " , data_median)
print("Mode of this data is : " , data_mode)
print("Standard deviation of this data is : " , data_std_deviation)

print("{}% of data lies within 1 standard deviation".format(len(thin_1_std_deviation)*100.0/len(data_list)))
print("{}% of data lies within 2 standard deviation".format(len(thin_2_std_deviation)*100.0/len(data_list)))
print("{}% of data lies within 3 standard deviation".format(len(thin_3_std_deviation)*100.0/len(data_list)))


fig = ff.create_distplot([data_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[data_mean, data_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()