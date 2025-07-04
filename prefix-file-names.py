import glob
import os

while True:
 local = input('local = ')
 
 tudo = glob.glob(local + '\\*')
 print(tudo)
 
 nova = input('word = ')         # the word you want to add
 
 for i in range(len(tudo)):
 
  arqu = os.path.basename(tudo[i])  # receive 1 file from the list (only name without path)             
  f = nova + arqu
 
  fim = local + '\\' + f
 
  os.rename(tudo[i], fim)


