A="Billy"
B="Brown"
C=2004

#меняем через доп. переменную, чтобы не морочиться
D=A
A=B
B=D
C+=60
print(A,B,C,sep="_")