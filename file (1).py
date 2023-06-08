filename0='005'

filename=filename0+'.txt'

f=open(filename,"r", encoding="utf-8", errors="ignore")

lines=f.readlines()

f.close()

length=len(lines)

blank=[]

for i in range(0,length):
        if len(lines[i])==1:
                blank.append(i)

parts=[]

startpoint=0

standard=50
if length>standard:
        wait=0
        i=standard
        while i<length:
                if len(lines[i])==1:
                        parts.append(lines[i-standard+1:i])
                        start_point=i
                        i=i+standard
                        if  i>length:
                                start_point=i
                                print("343556y5")
                else:
                        for j in range(0,len(blank)-1):
                                if blank[j]<=i and i<=blank[j+1]:
                                        if blank[j+1]-i>=i-blank[j] and i-blank[j]<100:
                                                parts.append(lines[i-standard+1:blank[j]])
                                                startpoint=blank[j]+1
                                                i=blank[j]+standard
                                        else:
                                                parts.append(lines[i-standard+1:blank[j+1]])
                                                startpoint=blank[j+1]+1
                                                i=blank[j+1]+standard
                                        break
                                
                print('part'+str(wait)+'\n')    
                wait+=1         

parts.append(lines[startpoint:length-1])
                        
print(len(parts))

index=1

for part in parts:
        fn=filename0+str(index)+'.txt'
        f=open(fn,"a")
        for line in part:
                f.write(line)
                "f.write('\n')"
        f.close()
        index+=1
        
for i in range(1,index):
        print("<a href='"+filename0+str(i)+".txt'>"+'Part'+str(i)+'</a><br/>')
