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

afikseis_aeroporikws_2011 = synolikes_afikseis_2011.cell_value(-2,2)
afikseis_sidirodromikws_2011 = synolikes_afikseis_2011.cell_value(-2,3)
afikseis_thalassiws_2011 = synolikes_afikseis_2011.cell_value(-2,4)
afikseis_odikws_2011 = synolikes_afikseis_2011.cell_value(-2,5)

afikseis_aeroporikws_2012 = synolikes_afikseis_2012.cell_value(-2,2)
afikseis_sidirodromikws_2012 = synolikes_afikseis_2012.cell_value(-2,3)
afikseis_thalassiws_2012 = synolikes_afikseis_2012.cell_value(-2,4)
afikseis_odikws_2012 = synolikes_afikseis_2012.cell_value(-2,5)

afikseis_aeroporikws_2013 = synolikes_afikseis_2013.cell_value(-4,2)
afikseis_sidirodromikws_2013 = synolikes_afikseis_2013.cell_value(-4,3)
afikseis_thalassiws_2013 = synolikes_afikseis_2013.cell_value(-4,4)
afikseis_odikws_2013 = synolikes_afikseis_2013.cell_value(-4,5)

afikseis_aeroporikws_2014 = synolikes_afikseis_2014.cell_value(-5,2)
afikseis_sidirodromikws_2014 = synolikes_afikseis_2014.cell_value(-5,3)
afikseis_thalassiws_2014 = synolikes_afikseis_2014.cell_value(-5,4)
afikseis_odikws_2014 = synolikes_afikseis_2014.cell_value(-5,4)




data3={'αεροπορικως': round(afikseis_aeroporikws_2011+afikseis_aeroporikws_2012+afikseis_aeroporikws_2013+afikseis_aeroporikws_2014),
       'σιδηροδρομικως':round(afikseis_sidirodromikws_2011+afikseis_sidirodromikws_2012+afikseis_sidirodromikws_2013+afikseis_sidirodromikws_2014),
       'θαλασσιως':round(afikseis_thalassiws_2011+afikseis_thalassiws_2012+afikseis_thalassiws_2013+afikseis_thalassiws_2014),
       'οδικως':round(afikseis_odikws_2011+afikseis_odikws_2012+afikseis_odikws_2013+afikseis_odikws_2014)}

tropos_taksidiou=list(data3.keys())
afikseis=list(data3.values())


print(data3)

fig = plt.figure(figsize = (10, 5))
plt.bar(tropos_taksidiou,afikseis,width=0.4)
plt.yscale('log')
plt.xlabel("Τρόπος ταξιδιού")
plt.ylabel("Αφίξεις")
plt.title("Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για την τετραετία 2011-2014")
plt.show()

