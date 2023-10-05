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

krati=[]
afikseis2011=[]
afikseis2012=[]
afikseis2013=[]
afikseis2014=[]



#afikseis apo evropaika krati
for i in range(78,112):
    krati.append(synolikes_afikseis_2014.cell_value(i,1))
    afikseis2011.append(round(synolikes_afikseis_2011.cell_value(i-2,6)))
    afikseis2012.append(round(synolikes_afikseis_2012.cell_value(i,6)))
    afikseis2013.append(round(synolikes_afikseis_2013.cell_value(i,6)))
    afikseis2014.append(round(synolikes_afikseis_2014.cell_value(i,6)))
    if(i>=109):
        afikseis2011.append(0)
    if(i==111):
        afikseis2012.append(0)

#afikseis apo asiatika krati
for i in range(113,122):
    krati.append(synolikes_afikseis_2014.cell_value(i, 1))
    afikseis2011.append(round(synolikes_afikseis_2011.cell_value(i-3, 6)))
    afikseis2012.append(round(synolikes_afikseis_2012.cell_value(i-1, 6)))
    afikseis2013.append(round(synolikes_afikseis_2013.cell_value(i, 6)))
    afikseis2014.append(round(synolikes_afikseis_2014.cell_value(i, 6)))

#afikseis apo krati tis afrikis
for i in range(123,126):
    krati.append(synolikes_afikseis_2014.cell_value(i, 1))
    afikseis2011.append(round(synolikes_afikseis_2011.cell_value(i-3, 6)))
    afikseis2012.append(round(synolikes_afikseis_2012.cell_value(i-1, 6)))
    afikseis2013.append(round(synolikes_afikseis_2013.cell_value(i, 6)))
    afikseis2014.append(round(synolikes_afikseis_2014.cell_value(i, 6)))

#afikseis apo krati tis amerikis
for i in range(127,133):
    krati.append(synolikes_afikseis_2014.cell_value(i, 1))
    afikseis2011.append(round(synolikes_afikseis_2011.cell_value(i-3, 6)))
    afikseis2012.append(round(synolikes_afikseis_2012.cell_value(i-1, 6)))
    afikseis2013.append(round(synolikes_afikseis_2013.cell_value(i, 6)))
    afikseis2014.append(round(synolikes_afikseis_2014.cell_value(i, 6)))

#afikseis apo krati tis okeanias
for i in range(134,136):
    krati.append(synolikes_afikseis_2014.cell_value(i, 1))
    afikseis2011.append(round(synolikes_afikseis_2011.cell_value(i - 3, 6)))
    afikseis2012.append(round(synolikes_afikseis_2012.cell_value(i - 1, 6)))
    afikseis2013.append(round(synolikes_afikseis_2013.cell_value(i, 6)))
    afikseis2014.append(round(synolikes_afikseis_2014.cell_value(i, 6)))

meg_afikseis=[]

for i in range(len(krati)):
    meg_afikseis.append(afikseis2011[i]+afikseis2012[i]+afikseis2013[i]+afikseis2014[i])

krati_proelevsis_me_megal_meridio_afiksewn=[]
etos_me_peris_afikseis=[]
megistes_afikseis=[]
index=[]

for i in range(5):
    maximum=max(meg_afikseis)
    index.append(meg_afikseis.index(maximum))
    megistes_afikseis.append(maximum)
    meg_afikseis[index[i]]=-1
    krati_proelevsis_me_megal_meridio_afiksewn.append(krati[index[i]])

data2=krati_proelevsis_me_megal_meridio_afiksewn,megistes_afikseis
print(data2)

fig = plt.figure(figsize = (10, 5))
plt.barh(krati_proelevsis_me_megal_meridio_afiksewn,megistes_afikseis)
plt.ylabel("Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις ")
plt.xlabel("Αριθμός αφίξεων")
plt.title("Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα για την τετραετία 2011-2014")
plt.show()

