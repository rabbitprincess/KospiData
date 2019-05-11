import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def printData(title,color,min,max,x1,x2,x3,x4,y):
    ax = plt.subplot(1,1,1)
    for label in ax.xaxis.get_ticklabels() :
        label.set_rotation(45)
    plt.xlabel('DATE')
    plt.ylabel('VALUE')
    plt.title(title)
    plt.plot_date(x1,x2,x3,x4,y,color)
    plt.ylim(min,max)
    plt.show()

def subDate(first,second):
    firstDatetime = datetime.strptime(first,"%Y%m%d") 
    secondDatetime = datetime.strptime(second,"%Y%m%d") 
    return abs((firstDatetime-secondDatetime).days)
    

def interpolation(dataset,s,e):
    data = np.array(dataset[0])
    date = pd.date_range(start = s, end = e)
    dt_list = date.strftime("%Y%m%d").tolist()
    j=1 
    for i in dt_list:
        if dataset[j][1] == int(i):
            data = np.vstack((data,dataset[j]))
            j = j+1
        else:
            tmp = np.array(dataset[0])
            tmp[0] = dataset[j][0]
            tmp[1] = int(i)
            num1 = subDate(str(dataset[j][1]),str(dataset[j-1][1]))
            num2 = subDate(i,str(dataset[j-1][1]))
            num3 = subDate(str(dataset[j][1]),i)
            tmp[2] = round((num3*dataset[j-1][2] + num2*dataset[j][2]) / num1,2)
            tmp[3] = dataset[j][3]        
            tmp[4] = dataset[j][4] 
            tmp[5] = dataset[j][5] #        
            data = np.vstack((data,tmp))
    for idx,i in enumerate(data):
            i[4] = round(float(i[3] / i[2])*100,2) # change_rate
    return data


dataset = pd.read_csv("st_data_koreaIndex.tsv", delimiter = '\t', header = 0)
KOSPI = np.array(dataset[485:646])
xdata = interpolation(KOSPI,'20170101','20181226')

xdate = [datetime.strptime(str(element),"%Y%m%d") for element in xdata[:,1]]
xval = xdata[:,2]
dataset2 = pd.read_csv("st_data_foreignCharge.tsv", delimiter = '\t', header = 0)

INDIA = np.array(dataset2[161:320])
idata = interpolation(INDIA,'20170101','20181226')
idate = [datetime.strptime(str(element),"%Y%m%d") for element in idata[:,1]]
ival = idata[:,2]

RUSSIA = np.array((dataset2[485:648]))
#print(RUSSIA)
rdata = interpolation(RUSSIA,'20170101','20181226')
rdate = [datetime.strptime(str(element),"%Y%m%d") for element in rdata[:,1]]
rval = rdata[:,2]


SANHAI = np.array(dataset2[806:965])
sdata = interpolation(SANHAI,'20170101','20181226')
sdate = [datetime.strptime(str(element),"%Y%m%d") for element in sdata[:,1]]
sval = sdata[:,2]


DAU =  np.array(dataset2[3070:3234])
ddata = interpolation(DAU,'20170101','20181226')
ddate = [datetime.strptime(str(element),"%Y%m%d") for element in ddata[:,1]]
dval = ddata[:,2]


JAPAN = np.array(dataset2[5030:5190])
jdata = interpolation(JAPAN,'20170101','20181226')
jdate = [datetime.strptime(str(element),"%Y%m%d") for element in jdata[:,1]]
jval = jdata[:,2]


NASDAC = np.array(dataset2[7621:7785])

ndata = interpolation(NASDAC,'20170101','20181226')
ndate = [datetime.strptime(str(element),"%Y%m%d") for element in ndata[:,1]]
nval = ndata[:,2]


mydate = pd.date_range(start = '20170101', end = '20181226')



lst = np.vstack((xval,sval,dval,nval,ival,rval,jval)).astype('float64')
#print(lst)
df = pd.DataFrame(lst).T
df.columns = ["KOSPI","SANHAI","DAU","NASDAC","INDIA","RUSSIA","JAPAN"]
#print(df)
corr = df.corr(method = 'pearson')
print(corr)


ax = plt.subplot(1,1,1)
for label in ax.xaxis.get_ticklabels() :
    label.set_rotation(45)
plt.xlabel('DATE')
plt.ylabel('VALUE')
plt.title("비교")
plt.plot_date(xdate,xval/xval[0],'-r',label='KOSPI')
plt.plot_date(sdate,sval/sval[0],'-b',label='SANHAI')
plt.plot_date(ddate,dval/dval[0],'-g',label='DAU')
plt.plot_date(idate,ival/ival[0],'-k',label='INDIA')
plt.plot_date(rdate,rval/rval[0],'-g',label='RUSSIA')
plt.plot_date(jdate,jval/jval[0],'pink',label='JAPAN')
ax.legend(loc='best')
plt.ylim(0.7,1.5)
plt.show()



