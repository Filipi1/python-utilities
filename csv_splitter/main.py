import csv
import math
import sys
import pandas as pd

arquivo_entrada = sys.argv[1]

try:
    filename = arquivo_entrada
    handle = open(filename, "r")
    reader = csv.DictReader(handle, delimiter=";")
except:
    sys.exit("Ocorreu uma falha na leitura do arquivo", file=sys.stderr)

i = 0
y = 0
z = 0

#CONFIG
totalrows = len(open(filename).readlines()) - 1
linesPerFiles = 9500
totalFilesResult = math.ceil(totalrows / linesPerFiles)

df = pd.DataFrame()
for row in reader :
    if (y == linesPerFiles) :
        y = 0
        df.to_csv("result " + str(z) + ".csv", sep=";", index=False)
        z = z + 1
        df = pd.DataFrame()

    i = i + 1
    y = y + 1

    if (y <= linesPerFiles) :
        df = df.append(row, ignore_index=True)

        if (i == totalrows) :
            z = z + 1
            df.to_csv("result " + str(z) + ".csv", sep=";", index=False)
   
print("Finalizado")

