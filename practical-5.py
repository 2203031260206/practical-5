fh=open("output5.txt",'w')
year = int(input("enter the year:"))
if(year%100!=0)&(year%4==0):
 fh.write("this is a leap year")
else:
 fh.write("this is not leap year") 