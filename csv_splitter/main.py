import csv
import math
import sys
import pandas as pd

arquivo_entrada = sys.argv[1]
qtd_entrada = sys.argv[2]

try:
    filename = arquivo_entrada
    handle = open(filename, "r")
    reader = csv.DictReader(handle, delimiter=",")
except:
    sys.exit("Ocorreu uma falha na leitura do arquivo", file=sys.stderr)

i = 0
y = 0
z = 0

#CONFIG
totalrows = len(open(filename).readlines()) - 1
linesPerFiles = int(qtd_entrada)
totalFilesResult = math.ceil(totalrows / linesPerFiles)

df = pd.DataFrame()

if (linesPerFiles >= totalrows) :
    print("O Número de linhas por arquivo não pode ser maior ou igual ao total de linhas do arquivo de origem.")
    sys.exit()

onlyFilename = str(filename).split('.')[0]

for row in reader :
    if (y == linesPerFiles) :
        y = 0
        df.to_csv(onlyFilename + " part" + str(z) + ".csv", sep=";", index=False)
        z = z + 1
        df = pd.DataFrame()

    i = i + 1
    y = y + 1

    if (y <= linesPerFiles) :
        df = df.append(row, ignore_index=True)

        if (i == totalrows) :
            z = z + 1
            df.to_csv(onlyFilename + " part" + str(z) + ".csv", sep=";", index=False)
   
print("Finalizado")
sys.exit()
