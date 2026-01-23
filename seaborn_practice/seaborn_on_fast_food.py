import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# load data
data = sns.load_dataset("flights")

# see first rows
print(data.head(10))

# reshape data using pivot
pivot_data = data.pivot(index="month", columns="year", values="passengers")

# set style
sns.set_style("darkgrid")

# draw heatmap
sns.heatmap(pivot_data)

# show plot
plt.show()


sns.lineplot(x='year',y="passengers",hue="month",data=data)
sns.set_style('white')
plt.show()

sns.set_theme('talk')
sns.histplot(x='year',y='month',hue='month',data=data)
sns.set_style('dark')
plt.show()


sns.set_theme('notebook')
sns.kdeplot(x='year',data=data)
plt.show()

sns.set_theme('white')
sns.catplot()



