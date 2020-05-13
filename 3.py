import re
import shutil


with open('the_matrix_new.txt', 'w', encoding='utf-8') as l:
with open ("the_matrix.txt", encoding='utf-8') as f:
lines = f.readlines()
for line in lines:
   if not (re.search('on screen', line) 
   if re.search('the matrix - Rev.', line) 
   if re.search('continued', line)):
l.write(line)
with open ('replicas.txt', 'w', encoding='utf-8') as l:
with open ("the_matrix_new.txt", encoding='utf-8') as f:
lines = f.readlines()
for line in lines:
   if replicaIsWriting:
   if re.search('^\s+$', line):
replicaIsWriting = False
else:
l.write(line)
else:
   if re.search('\s+morpheus\s\(', line) 
   if re.search('\s+neo\s\(', line) 
   if re.search('\s+trinity\s\(', line):
l.write(line)
replicaIsWriting = True