import matplotlib.pyplot as plt
import xlrd
import csv

wb2011 = xlrd.open_workbook('./2011.xls')
wb2012 = xlrd.open_workbook('./2012.xls')
wb2013 = xlrd.open_workbook('./2013.xls')
wb2014 = xlrd.open_workbook('./2014.xls')

synolikes_afikseis_2011 = wb2011.sheet_by_index(-1)
synolikes_afikseis_2012 = wb2012.sheet_by_index(-1)
synolikes_afikseis_2013 = wb2013.sheet_by_index(-1)
synolikes_afikseis_2014 = wb2014.sheet_by_index(-1)


afikseis2011 = round(synolikes_afikseis_2011.cell_value(-2,6))
afikseis2012 = round(synolikes_afikseis_2012.cell_value(-2,6))
afikseis2013 = round(synolikes_afikseis_2013.cell_value(-4,6))
afikseis2014 = round(synolikes_afikseis_2014.cell_value(-5,6))


data = {2011:afikseis2011,2012:afikseis2012,2013:afikseis2013,2014:afikseis2014}
print(data)
years = list(data.keys())
afikseis = list(data.values())

fig = plt.figure(figsize = (10, 5))
plt.bar(years,afikseis,width=0.4)
plt.xlabel("'Ετη")
plt.ylabel("Αφίξεις")
plt.title("Συνολικές αφίξεις τουριστών στην Ελλάδα για την τετραετία 2011-2014")
plt.show()


