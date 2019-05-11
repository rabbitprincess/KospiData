import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


#%matplotlib auto

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

dataset = pd.read_csv("st_data_koreaIndex.tsv", delimiter = '\t', header = 0)
KOSDAQ = np.array(dataset[0:323])
KOSPI = np.array(dataset[324:646])
KP200 = np.array(dataset[647:])

KOSDAQ2018 = np.array(dataset[165:323])
KOSPI2018 = np.array(dataset[488:646])
KP2002018 = np.array(dataset[731:])

xdate = [datetime.datetime.strptime(str(element),"%Y%m%d") for element in KOSPI[:,1]]
ydate = [datetime.datetime.strptime(str(element),"%Y%m%d") for element in KOSDAQ[:,1]]
zdate = [datetime.datetime.strptime(str(element),"%Y%m%d") for element in KP200[:,1]]

xval = KOSPI[:,2]
yval = KOSDAQ[:,2]
zval = KP200[:,2]

printData("KOSPI","r-",170000,280000,xdate,xval)
printData("KOSDAQ","b-",50000,100000,ydate,yval)
printData("KP200","g-",20000,35000,zdate,zval)

dataset2 = pd.read_csv("st_data_foreignCharge.tsv", delimiter = '\t', header = 0)

SANHAI = np.array(dataset2[650:965])
sdate = [datetime.datetime.strptime(str(element),"%Y%m%d") for element in SANHAI[:,1]]
sval = SANHAI[:,2]

printData("SANHAI","b-",2200,5300,sdate,sval)

NASDAC = np.array(dataset2[7456:7785])
ndate = [datetime.datetime.strptime(str(element),"%Y%m%d") for element in NASDAC[:,1]]
nval = NASDAC[:,2]
printData("NASDAC","y-",4000,8500,ndate,nval)