import csv
import math
import sys
import pandas as pd
from tqdm import tqdm

arquivo_entrada = sys.argv[1]
qtd_entrada = sys.argv[2]

try:
    filename = arquivo_entrada
    handle = open(filename, "r")
    reader = csv.DictReader(handle, delimiter=",")
except:
    sys.exit("Ocorreu uma falha na leitura do arquivo", file=sys.stderr)

i = 0 ; y = 0 ; z = 0

#CONFIG
totalrows = len(open(filename).readlines()) - 1
linesPerFiles = int(qtd_entrada)
totalFilesResult = math.ceil(totalrows / linesPerFiles)

df = pd.DataFrame()
dl = pd.DataFrame(reader)

if (linesPerFiles >= totalrows) :
    print("O Número de linhas por arquivo não pode ser maior ou igual ao total de linhas do arquivo de origem.")
    sys.exit()

onlyFilename = str(filename).split('.')[0]

print("Gerando " + str(totalFilesResult) + " Arquivos com " + str(qtd_entrada) + " linhas")

def separar(row) :
        global i; global z; global y; global df

        if (y == linesPerFiles) :
            print("\n\n [ ✔ ] Arquivo '" + onlyFilename + " part" + str(z) + ".csv' gerado com " + str(y) + " linhas\n\n")
            y = 0
            df.to_csv(onlyFilename + " part" + str(z) + ".csv", sep=";", index=False)
            z = z + 1
            df = pd.DataFrame()

        i = i + 1
        y = y + 1

        if (y <= linesPerFiles) :
            df = df.append(row, ignore_index=True)

            if (i == totalrows) :
                df.to_csv(onlyFilename + " part" + str(z) + ".csv", sep=";", index=False)

for index, row in tqdm(dl.iterrows(), total=dl.shape[0]):
    separar(row)

print("\n\n [ ✔ ] Arquivo '" + onlyFilename + " part" + str(z) + ".csv' gerado com " + str(y) + " linhas\n\n")
print("Finalizado\n\n")
sys.exit()
