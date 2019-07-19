## Percentage of all the students who were admitted and rejected
import pandas as pd

data=pd.read_csv('Berkeley.csv')
print(data)

print(data['Freq'].sum())
#4526

#to find the total admitted students
a='Admitted'
total_admit=data[data['Admit']==a]
print(total_admit)
print(total_admit['Freq'].sum())
#1755

p1=(total_admit['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')

#to find the total rejected students
b='Rejected'
total_reject=data[data['Admit']==b]
print(total_reject)
print(total_reject['Freq'].sum())
#2771

p1=(total_reject['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')


## Percentage of male and female admitted and rejected

Part1:  percentage of male and female admitted

#to find the total male admitted students
a='Admitted'
c='Male'
total_admit=data[(data['Admit']==a) & (data['Gender']==c)]
print(total_admit)
print(total_admit['Freq'].sum())
#1198

p1=(total_admit['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')


#to find the total female admitted students
a='Admitted'
d='Female'
total_admit=data[(data['Admit']==a) & (data['Gender']==d)]
print(total_admit)
print(total_admit['Freq'].sum())
#557

p1=(total_admit['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')




Part 2: percentage of male and female rejected
#to find the total male rejected students
b='Rejected'
c='Male'
total_reject=data[(data['Admit']==b) & (data['Gender']==c)]
print(total_reject)
print(total_reject['Freq'].sum())
#1493

p1=(total_reject['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')


#to find the total female rejected students
b='Rejected'
d='Female'
total_reject=data[(data['Admit']==b) & (data['Gender']==d)]
print(total_reject)
print(total_reject['Freq'].sum())
#1278

p1=(total_reject['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')







## Percentage of males and females from every Dept who were admitted and rejected

? for male and  female admitted in dept A
a='Admitted'
c='Male'
z='A'.o
total_admit=data[(data['Admit']==a) & (data['Gender']==c) & (data['Dept']==z)]
print(total_admit)
print(total_admit['Freq'].sum())

p1=(total_admit['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')

#female
a='Admitted'
d='Female'
z='A'
total_admit=data[(data['Admit']==a) & (data['Gender']==d) & (data 
['Dept']==z)]
print(total_admit)
print(total_admit['Freq'].sum())
#557

p1=(total_admit['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')



? male and female rejected in dept A
#to find the total male rejected students
b='Rejected'
c='Male'
z='A'
total_reject=data[(data['Admit']==b) & (data['Gender']==c) & (data 
['Dept']==z)]
print(total_reject)
print(total_reject['Freq'].sum())
#1493

p1=(total_reject['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')


#to find the total female rejected students
b='Rejected'
d='Female'
z='A'
total_reject=data[(data['Admit']==b) & (data['Gender']==d) & (data 
['Dept']==z)]
print(total_reject)
print(total_reject['Freq'].sum())
#1278

p1=(total_reject['Freq'].sum())/(data['Freq'].sum())*100
p1=p1.round(3)
print(p1,'%')

