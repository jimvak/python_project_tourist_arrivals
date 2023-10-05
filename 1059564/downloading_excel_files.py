import wget

print('Start downloading excel files')


url2011 = 'https://1drv.ms/x/s!AkPjUu0qYEdijEMZqh84gek2ypHV?e=1TYscX'
wget.download(url2011, './2011.xls')

url2012 = 'https://1drv.ms/x/s!AkPjUu0qYEdijEWM-mtbehHDdZRo?e=obuIKB'
wget.download(url2012, './2012.xls')

url2013 = 'https://1drv.ms/x/s!AkPjUu0qYEdijEYGJ5DQ4GCSXqsM?e=JTQDzv'
wget.download(url2013, './2013.xls')

url2014 = 'https://1drv.ms/x/s!AkPjUu0qYEdijEh8cQB4i_-SLBOh?e=F38R1G'
wget.download(url2014, './2014.xls')



print(url2011)
print(url2012)
print(url2013)
print(url2014)

print('Downloading ready')

