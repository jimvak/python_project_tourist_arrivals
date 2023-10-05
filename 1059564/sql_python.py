import xlrd
import csv
import mysql.connector as mysql
import proto_zitoumeno
import deftero_zitoumeno
import trito_zitoumeno
import tetarto_zitoumeno

eti=proto_zitoumeno.years
afik=proto_zitoumeno.afikseis
kor_xwres=deftero_zitoumeno.krati_proelevsis_me_megal_meridio_afiksewn
max_afikseis=deftero_zitoumeno.megistes_afikseis
tropos_metaforas = trito_zitoumeno.tropos_taksidiou
arrivals=trito_zitoumeno.afikseis
trim=tetarto_zitoumeno.trimina
af_ana_trim=tetarto_zitoumeno.afikseis_ana_trimino


# connecting to the database
db = mysql.connect(host="localhost",user="root",passwd="11061998",database="python")

# creating cursor
mycursor = db.cursor()

# create tables
mycursor.execute("CREATE TABLE IF NOT EXISTS afikseis_ana_etos(etos int(25),afikseis int(25))")
mycursor.execute("CREATE TABLE IF NOT EXISTS korifaies_xwres_proelevsis(kratos text,ar_afiksewn int(5))")
mycursor.execute("CREATE TABLE IF NOT EXISTS afikseis_me_mesa(tropos_metaforas varchar(25),afikseis int(5))")
mycursor.execute("CREATE TABLE IF NOT EXISTS afikseis_ana_trimino(trimino int(25),afikseis int(25))")


# insert into tables
mycursor.execute("INSERT INTO afikseis_ana_etos(etos,afikseis) VALUES('2011','16427247'),('2012','15517622'),('2013','17919580'),('2014','22033462')")
mycursor.execute("INSERT INTO korifaies_xwres_proelevsis(kratos,ar_afiksewn) VALUES('Germany','7566365'),('other european countries','6403936'),('U.K.','5693955'),('France','3764763'),('Russia','3295134')")
mycursor.execute("INSERT INTO afikseis_me_mesa(tropos_metaforas,afikseis) VALUES('aeroporikws','49023722'),('sidirodromikws','10659'),('thalassiws','3246623'),('odikws','13050246')")
mycursor.execute("INSERT INTO afikseis_ana_trimino(trimino,afikseis) VALUES('12011','1108387'),('22011','4195768'),('32011','8925699'),('42011','2197393'),('12012','978559'),('22012','3849245'),('32012','8655186'),('42012','2034632'),('12013','1023354'),('22013','4397477'),('32013','10113076'),('42013','2385673'),('12014','1186900'),('22014','5077136'),('32014','12722925'),('42014','3046501')")

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
db.commit()

# close the connection
db.close()
