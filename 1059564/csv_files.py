import xlrd
import csv
import proto_zitoumeno
import deftero_zitoumeno
import trito_zitoumeno
import tetarto_zitoumeno


fields1=proto_zitoumeno.years
rows1=[proto_zitoumeno.afikseis2011,proto_zitoumeno.afikseis2012,proto_zitoumeno.afikseis2013,proto_zitoumeno.afikseis2014]
fields2=['Germany', 'Other_european_countries', 'U.K.', 'France', 'Russia']
rows2=deftero_zitoumeno.megistes_afikseis
fields3=['aeroporikws','sidirodromikws','thalassiws','odikws']
rows3=trito_zitoumeno.afikseis
fields4=['1_11','2_11','3_11','4_11','1_12','2_12','3_12','4_12','1_13','2_13','3_13','4_13','1_14','2_14','3_14','4_14']
rows4=tetarto_zitoumeno.afikseis_ana_trimino

with open('csv_file.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields1)
    csvwriter.writerow(rows1)

    csvwriter.writerow(fields2)
    csvwriter.writerow(rows2)

    csvwriter.writerow(fields3)
    csvwriter.writerow(rows3)

    csvwriter.writerow(fields4)
    csvwriter.writerow(rows4)



