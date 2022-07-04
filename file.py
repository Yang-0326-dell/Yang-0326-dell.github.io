filename0=input("file name:")
bookname=input("book name:")

filename=filename0+'.txt'

f=open(filename,"r")

lines=f.readlines()

f.close()

length=len(lines)

blank=[]

for i in range(0,length):
	if len(lines[i])==1:
		blank.append(i)

parts=[]

startpoint=0

standard=500

standard=int(input("lines in each part:"))
if length>standard:
	wait=0
	i=standard
	while i<length:
		if len(lines[i])==1:
			parts.append(lines[i-standard:i])
			startpoint=i
			i=i+standard
		else:
			for j in range(0,len(blank)-2):
				if blank[j]<=i and i<=blank[j+1]:
					if blank[j+1]-i>=i-blank[j] and i-blank[j]<standard/4:
						parts.append(lines[i-standard+1:blank[j]])
						startpoint=blank[j]+1
						i=blank[j]+standard
					else:
						parts.append(lines[i-standard+1:blank[j+1]])
						startpoint=blank[j+1]+1
						i=blank[j+1]+standard
					break
				
		print('part'+str(wait)+"  "+str(startpoint)+"  "+str(i)+'\n')	
		wait+=1		

parts.append(lines[startpoint:length-1])
			
print(len(parts))

index=1

for part in parts:
	fn=filename0+str(index)+'.txt'
	f=open(fn,"w")
	for line in part:
		f.write(line)
	f.close()
	index+=1
	
filename=filename0+".html"
f=open(filename,"w")
f.write("<head><a target='_blank' href='index.html'><input type='button' value='Back to home' alt='Click to go back to homepage;'></a></head>")
f.write("<p>\""+bookname+"\"<p>")
for i in range(1,index):
	print("<a href='"+filename0+str(i)+".txt'>"+'Part'+str(i)+'</a><br/>')
	f.write("<a href='"+filename0+str(i)+".txt'>"+'Part'+str(i)+'</a><br/>')

f.close()