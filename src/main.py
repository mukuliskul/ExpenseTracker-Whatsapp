import datetime
now=datetime.datetime.now()
cmonth=str(now.month)

spending=[]
received=0
num=(0,1,2,3,4,5,6,7,8,9)
entrylist=[]


f=open(r'/Users/mukulsharma/Downloads/WhatsApp Chat with Hum.txt','r') #exported chat(.txt)
chat=f.readlines()
for i in chat:
    if i[0]==cmonth:
        entry=i.split()     
#expenditure
#format(xxx cash abc)
        if "cash" in entry:
            cashspent=entry
            csvar=int(cashspent[4])
            spending.append(csvar)
#received  
#format(xxx cash received abc)  
        elif "cash received" in entry:
            cashreceived=entry
            crvar=int(cashreceived[4])
            received.append(crvar)
            
            
print(spending)
print('Money spent in month',cmonth,' = ',sum(spending)) 

print(received)
print('Money received in month',cmonth,' = ',sum(received)) 


            

