import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def printData(title,color,min,max,x,y):
    ax = plt.subplot(1,1,1)
    for label in ax.xaxis.get_ticklabels() :
        label.set_rotation(45)
    plt.xlabel('DATE')
    plt.ylabel('VALUE')
    plt.title(title)
    plt.plot_date(x,y,color)
    plt.ylim(min,max)
    plt.show()


dataset = pd.read_csv("st_data_itemChargeFull.tsv", delimiter = '\t', header = 0,low_memory = False)
data = np.array(dataset)
j = 0
list = []
for line in data[1:]:
#    print(line)
    if line[2] != 'KOSPI':
        continue
    if line[1] == '넷마블':
        continue
    if line[3] == 20170102:
        x1 = line[14]
    if line[3] == 20171227:
        x2 = line[14]
    if line[3] == 20180104:
        x3 = line[14]
    if line[3] == 20181226:
        x4 = line[14]
        list.append([line[1],x2-x1,x4-x3,round((x2-x1)*100/x1,4),round((x4-x3)*100/x3,4)])
#for line in list:
#    print(line)    
list.sort(key=lambda x: x[1],reverse=True)
dataframe = pd.DataFrame(list[:30],columns = ['종목','2017년 변동량','2018년 변동량','2017년 변동률','2018년 변동률'])
print(dataframe,'\n\n')#상승

list.sort(key=lambda x: x[2])
dataframe = pd.DataFrame(list[:30],columns = ['종목','2017년 변동량','2018년 변동량','2017년 변동률','2018년 변동률'])
print(dataframe)#하락


