import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Read Excel
df = pd.read_excel('indo_12_1.xls', na_values = ['-'])
# print(df)

# # # Rearrangement # # #
# print(df.iloc[3:37].values)
rapih1 = df.iloc[3:37].values

dfRapih1 = pd.DataFrame(rapih1, columns = ['prov',1970,1980,1990,1995,2000,2010])
# print(dfRapih1.values)

# # Check out the values
# for check in dfRapih1.values:
#     print(check[0])
# print(len(dfRapih1.values))

# Replacing province names with digits
''' Better check the names in order by index'''
provinsi = []
provinsi.append('tahun')
for a in range(len(dfRapih1.values)):
    provinsi.append(a)
print(provinsi)

t70 = []
t70.append(1970)
t80 = []
t80.append(1980)
t90 = []
t90.append(1990)
t95 = []
t95.append(1995)
t200 = []
t200.append(2000)
t210 = []
t210.append(2010)
for b in dfRapih1.values:
    t70.append(b[1])
    t80.append(b[2])
    t90.append(b[3])
    t95.append(b[4])
    t200.append(b[5])
    t210.append(b[6])

dfRapih2 = pd.DataFrame(
    [t70,t80,t90,t95,t200,t210],
    columns = provinsi
)

# Making sure everything is in order
print(dfRapih1)
print(dfRapih2)

# Preparation for plotting
namaProv = []
for x in dfRapih1.values:
    namaProv.append(x[0])
print(namaProv)
dfNP = pd.DataFrame(namaProv, columns = ['name'])
print(dfNP)
# Plot everthing

plt.figure('soal1_1_plot', figsize = (40,70))
plt.style.use('ggplot')
plt.plot(
    dfRapih2['tahun'],
    dfRapih2[11],
    'g-'
)
plt.plot(
    dfRapih2['tahun'],
    dfRapih2[6],
    'b-'
)
plt.plot(
    dfRapih2['tahun'],
    dfRapih2[33],
    'r-'
)
plt.scatter(
    dfRapih2['tahun'],
    dfRapih2[11],
    marker = 'o',
    color = 'g'
)
plt.scatter(
    dfRapih2['tahun'],
    dfRapih2[6],
    marker = 'o',
    color = 'b'
)
plt.scatter(
    dfRapih2['tahun'],
    dfRapih2[33],
    marker = 'o',
    color = 'r'
)
plt.title('Jumlah Penduduk {} (1970 - 2010)'.format(dfNP['name'][33]))
plt.legend([dfNP['name'][11],dfNP['name'][6],dfNP['name'][33]])
plt.xlabel('Tahun')
plt.show()