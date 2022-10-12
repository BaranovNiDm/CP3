print('введите число лет')
let=int(input())
minut=(let*365+let//4)*24*60
kartin=minut//5
print("будет просмотрено",kartin,'экспонатов')
print("введите число экспонатов")
ekspon=int(input())
minuti=ekspon*5
lett=(minuti/24/60)//365
#мог бы продолжить с високосными годами, но уже очень поздно, простите
minuti=minuti-lett*365
dni=minuti/60/24
chasi=dni%1*24
dni=int(dni)
minuti=chasi%1*60
chasi=int(chasi)
print('будет затрачено',int(lett),"лет",dni,'дней',chasi,'часов',int(minuti) ,'минут')