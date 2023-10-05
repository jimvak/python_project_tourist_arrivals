import matplotlib.pyplot as plt
import xlrd
import csv

wb2011 = xlrd.open_workbook('./2011.xls')
wb2012 = xlrd.open_workbook('./2012.xls')
wb2013 = xlrd.open_workbook('./2013.xls')
wb2014 = xlrd.open_workbook('./2014.xls')

afikseis_1o_trimino_2011=wb2011.sheet_by_index(2)
afikseis_1o_trimino_2011=round(afikseis_1o_trimino_2011.cell_value(-2,6))

afikseis_aprilios_2011=wb2011.sheet_by_index(3)
afikseis_maios_2011=wb2011.sheet_by_index(4)
afikseis_iounios_2011=wb2011.sheet_by_index(5)

afikseis_aprilios_2011=afikseis_aprilios_2011.cell_value(65,6)
afikseis_maios_2011=afikseis_maios_2011.cell_value(65,6)
afikseis_iounios_2011=afikseis_iounios_2011.cell_value(65,6)

afikseis_2o_trimino_2011=round(afikseis_aprilios_2011+afikseis_maios_2011+afikseis_iounios_2011)

afikseis_ioulios_2011=wb2011.sheet_by_index(6)
afikseis_avgoustos_2011=wb2011.sheet_by_index(7)
afikseis_septemvri_2011=wb2011.sheet_by_index(8)

afikseis_ioulios_2011=afikseis_ioulios_2011.cell_value(65,6)
afikseis_avgoustos_2011=afikseis_avgoustos_2011.cell_value(65,6)
afikseis_septemvri_2011=afikseis_septemvri_2011.cell_value(65,6)

afikseis_3o_trimino_2011=round(afikseis_ioulios_2011+afikseis_avgoustos_2011+afikseis_septemvri_2011)

afikseis_oktovri_2011=wb2011.sheet_by_index(9)
afikseis_noemvri_2011=wb2011.sheet_by_index(10)
afikseis_dekemvri_2011=wb2011.sheet_by_index(11)

afikseis_oktovri_2011=afikseis_oktovri_2011.cell_value(65,6)
afikseis_noemvri_2011=afikseis_noemvri_2011.cell_value(65,6)
afikseis_dekemvri_2011=afikseis_dekemvri_2011.cell_value(65,6)

afikseis_4o_trimino_2011=round(afikseis_oktovri_2011+afikseis_noemvri_2011+afikseis_dekemvri_2011)






afikseis_1o_trimino_2012=wb2012.sheet_by_index(2)
afikseis_1o_trimino_2012=round(afikseis_1o_trimino_2012.cell_value(-2,6))

afikseis_aprilios_2012=wb2012.sheet_by_index(3)
afikseis_maios_2012=wb2012.sheet_by_index(4)
afikseis_iounios_2012=wb2012.sheet_by_index(5)

afikseis_aprilios_2012=afikseis_aprilios_2012.cell_value(65,6)
afikseis_maios_2012=afikseis_maios_2012.cell_value(65,6)
afikseis_iounios_2012=afikseis_iounios_2012.cell_value(65,6)

afikseis_2o_trimino_2012=round(afikseis_aprilios_2012+afikseis_maios_2012+afikseis_iounios_2012)

afikseis_ioulios_2012=wb2012.sheet_by_index(6)
afikseis_avgoustos_2012=wb2012.sheet_by_index(7)
afikseis_septemvri_2012=wb2012.sheet_by_index(8)

afikseis_ioulios_2012=afikseis_ioulios_2012.cell_value(65,6)
afikseis_avgoustos_2012=afikseis_avgoustos_2012.cell_value(65,6)
afikseis_septemvri_2012=afikseis_septemvri_2012.cell_value(65,6)

afikseis_3o_trimino_2012=round(afikseis_ioulios_2012+afikseis_avgoustos_2012+afikseis_septemvri_2012)

afikseis_oktovri_2012=wb2012.sheet_by_index(9)
afikseis_noemvri_2012=wb2012.sheet_by_index(10)
afikseis_dekemvri_2012=wb2012.sheet_by_index(11)

afikseis_oktovri_2012=afikseis_oktovri_2012.cell_value(65,6)
afikseis_noemvri_2012=afikseis_noemvri_2012.cell_value(65,6)
afikseis_dekemvri_2012=afikseis_dekemvri_2012.cell_value(65,6)

afikseis_4o_trimino_2012=round(afikseis_oktovri_2012+afikseis_noemvri_2012+afikseis_dekemvri_2012)



afikseis_1o_trimino_2013=wb2013.sheet_by_index(2)
afikseis_1o_trimino_2013=round(afikseis_1o_trimino_2013.cell_value(-3,6))

afikseis_aprilios_2013=wb2013.sheet_by_index(3)
afikseis_maios_2013=wb2013.sheet_by_index(4)
afikseis_iounios_2013=wb2013.sheet_by_index(5)

afikseis_aprilios_2013=afikseis_aprilios_2013.cell_value(64,6)
afikseis_maios_2013=afikseis_maios_2013.cell_value(64,6)
afikseis_iounios_2013=afikseis_iounios_2013.cell_value(64,6)

afikseis_2o_trimino_2013=round(afikseis_aprilios_2013+afikseis_maios_2013+afikseis_iounios_2013)

afikseis_ioulios_2013=wb2013.sheet_by_index(6)
afikseis_avgoustos_2013=wb2013.sheet_by_index(7)
afikseis_septemvri_2013=wb2013.sheet_by_index(8)

afikseis_ioulios_2013=afikseis_ioulios_2013.cell_value(65,6)
afikseis_avgoustos_2013=afikseis_avgoustos_2013.cell_value(65,6)
afikseis_septemvri_2013=afikseis_septemvri_2013.cell_value(65,6)

afikseis_3o_trimino_2013=round(afikseis_ioulios_2013+afikseis_avgoustos_2013+afikseis_septemvri_2013)

afikseis_oktovri_2013=wb2013.sheet_by_index(9)
afikseis_noemvri_2013=wb2013.sheet_by_index(10)
afikseis_dekemvri_2013=wb2013.sheet_by_index(11)

afikseis_oktovri_2013=afikseis_oktovri_2013.cell_value(65,6)
afikseis_noemvri_2013=afikseis_noemvri_2013.cell_value(65,6)
afikseis_dekemvri_2013=afikseis_dekemvri_2013.cell_value(65,6)

afikseis_4o_trimino_2013=round(afikseis_oktovri_2013+afikseis_noemvri_2013+afikseis_dekemvri_2013)




afikseis_1o_trimino_2014=wb2014.sheet_by_index(2)
afikseis_1o_trimino_2014=round(afikseis_1o_trimino_2014.cell_value(-4,6))

afikseis_aprilios_2014=wb2014.sheet_by_index(3)
afikseis_maios_2014=wb2014.sheet_by_index(4)
afikseis_iounios_2014=wb2014.sheet_by_index(5)

afikseis_aprilios_2014=afikseis_aprilios_2014.cell_value(65,6)
afikseis_maios_2014=afikseis_maios_2014.cell_value(65,6)
afikseis_iounios_2014=afikseis_iounios_2014.cell_value(65,6)

afikseis_2o_trimino_2014=round(afikseis_aprilios_2014+afikseis_maios_2014+afikseis_iounios_2014)

afikseis_ioulios_2014=wb2014.sheet_by_index(6)
afikseis_avgoustos_2014=wb2014.sheet_by_index(7)
afikseis_septemvri_2014=wb2014.sheet_by_index(8)

afikseis_ioulios_2014=afikseis_ioulios_2014.cell_value(65,6)
afikseis_avgoustos_2014=afikseis_avgoustos_2014.cell_value(65,6)
afikseis_septemvri_2014=afikseis_septemvri_2014.cell_value(65,6)

afikseis_3o_trimino_2014=round(afikseis_ioulios_2014+afikseis_avgoustos_2014+afikseis_septemvri_2014)

afikseis_oktovri_2014=wb2014.sheet_by_index(9)
afikseis_noemvri_2014=wb2014.sheet_by_index(10)
afikseis_dekemvri_2014=wb2014.sheet_by_index(11)

afikseis_oktovri_2014=afikseis_oktovri_2014.cell_value(65,6)
afikseis_noemvri_2014=afikseis_noemvri_2014.cell_value(65,6)
afikseis_dekemvri_2014=afikseis_dekemvri_2014.cell_value(65,6)

afikseis_4o_trimino_2014=round(afikseis_oktovri_2014+afikseis_noemvri_2014+afikseis_dekemvri_2014)



data4={'1ο_11':afikseis_1o_trimino_2011,
       '2ο_11':afikseis_2o_trimino_2011,
       '3ο_11':afikseis_3o_trimino_2011,
       '4ο_11':afikseis_4o_trimino_2011,
       '1ο_12': afikseis_1o_trimino_2012,
       '2ο_12': afikseis_2o_trimino_2012,
       '3ο_12': afikseis_3o_trimino_2012,
       '4ο_12': afikseis_4o_trimino_2012,
       '1ο_13': afikseis_1o_trimino_2013,
       '2ο_13': afikseis_2o_trimino_2013,
       '3ο_13': afikseis_3o_trimino_2013,
       '4ο_13': afikseis_4o_trimino_2013,
       '1ο_14': afikseis_1o_trimino_2014,
       '2ο_14': afikseis_2o_trimino_2014,
       '3ο_14': afikseis_3o_trimino_2014,
       '4ο_14': afikseis_4o_trimino_2014,
       }
print(data4)

trimina=list(data4.keys())
afikseis_ana_trimino=list(data4.values())

fig = plt.figure(figsize = (20, 10))
plt.bar(trimina,afikseis_ana_trimino)
plt.xlabel("Τρίμηνα")
plt.ylabel("Αφίξεις")
plt.title("Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για την τετραετία 2011-2014")
plt.show()

