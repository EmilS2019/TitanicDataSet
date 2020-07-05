from loadFiles import *
import matplotlib.pyplot as plt
import numpy as np

theFile = getFile()
survived = getRowFromFile(theFile, 1)
pClass = getRowFromFile(theFile, 2)

SurvivedPassengers = [0,0,0]
totalPassangers = [0,0,0]
for i in range(2, len(survived)):
    for j in range(len(SurvivedPassengers)):
        SurvivedPassengers[j] += 1*int(survived[i])*(pClass[i] == str(j+1))
        totalPassangers[j] += 1*(pClass[i]==str(j+1))





#The Plottening
labels = ['First Class', 'Second Class', 'Third Class']
men_means = [SurvivedPassengers[0], SurvivedPassengers[1], SurvivedPassengers[2]]
women_means = [totalPassangers[0], totalPassangers[1], totalPassangers[2]]

x = np.arange(len(labels))  # the label locations
#The plot thickens
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Survived')
rects2 = ax.bar(x + width/2, women_means, width, label='Total')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('People')
ax.set_title('Titanic Survivors based on Class')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()



