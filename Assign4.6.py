try:
    inp =raw_input("Please enter Hours: ")
    hours=float(inp)
    inp=raw_input("Please Enter Rate: ")
    rate=float(inp)
except:
        print "Please enter a number as input"
        quit()
def computepay(h,r):
    if (h>40):
        pay =(40*r)+(h-40)*1.5*r
    else:
        pay =(h*r)
    return pay
print computepay(hours,rate)    
        
    