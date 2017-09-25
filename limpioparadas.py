import csv
with open('/home/fede/Datos/Datos-Tp/ParadasNAC.csv', newline='') as csvfile:
    colectivos = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('/home/fede/Datos/Datos-Tp/Paradas3decimales.csv', 'a', newline='') as csvfile2:
        i = 0
        for row in colectivos:
            if i==0:
                spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(row)
                i=1
            else:
                spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                row[0] = str(round(float(row[0]),3))
                row[1] = str(round(float(row[1]),3))
                spamwriter.writerow(row)
                print(row)
with open('/home/fede/Datos/Datos-Tp/ParadasPBA.csv', newline='') as csvfile:
    colectivos = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('/home/fede/Datos/Datos-Tp/Paradas3decimales.csv', 'a', newline='') as csvfile2:
        i = 0
        for row in colectivos:
            if i==0:
                i=1
            else:
                spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                row[0] = str(round(float(row[0]),3))
                row[1] = str(round(float(row[1]),3))
                spamwriter.writerow(row)
                print(row)

with open('/home/fede/Datos/Datos-Tp/Paradas_MUN.csv', newline='') as csvfile:
    colectivos = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('/home/fede/Datos/Datos-Tp/Paradas3decimales.csv', 'a', newline='') as csvfile2:
        i = 0
        for row in colectivos:
            if i==0:
                i=1
            else:
                spamwriter = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                row[0] = str(round(float(row[0]),3))
                row[1] = str(round(float(row[1]),3))
                spamwriter.writerow(row)
                print(row)
