# Assumption
# there can be no Order
# min inventory can be 0

def reward(oq,endinv,mcost,ocost,hcost,dummy,inv,rewardlast):
    rewar=[]
    for i in range(1,len(oq)+1):
        ocostt=ocost if (oq[i-1])>0 else 0
        if dummy==2 or dummy==3:
            e=oq[i-1]*mcost+ocostt+endinv[i-1]*hcost+rewardlast[inv.index(endinv[i-1])]
        if dummy==1:
            e=oq[i-1]*mcost+ocostt+endinv*hcost
        rewar+=[e]
    if dummy!=1:
        return(oq[rewar.index(min(rewar))],min(rewar))
    else:
        print(rewar)
        return(rewar)

print("Deterministic Programming")
maxinv=4
# maxinv=int(input("Enter Max inventory: "))
maxoquan=5
# maxoquan=int(input("Enter Max Order Quantity: "))
period=4
# period=int(input("Enter No.of period: "))
mcost=2
# mcost=int(input("Enter Material cost per unit: "))
ocost=4
# ocost=int(input("Enter Ordering Cost: "))
hcost=0.5
# hcost=float(input("Enter Holding Cost: "))
# demand=[]
demand=[3,4,2,4]
# for i in range(period):
#     d=int(input("Enter demand for period %i: "%(i+1)))
#     demand+=[d]
inv=[]
for i in range(maxinv+1):
    inv+=[i]
oquan=[]
for i in range(maxoquan+1):
    oquan+=[i]
for w in range(len(demand),0,-1):
    d=demand[w-1]
    print("demand = %i"%d)
    if w==len(demand):
        endinv=0
        oqsi=[]
        beginv=inv
        for i in inv:
            oqsi+=[d-i]
        rewardlast=reward(oqsi,endinv,mcost,ocost,hcost,1,5,5)
        final=[rewardlast]
        finalbeginv=[beginv]
        finaloquan=[oqsi]
    elif w==1:
        endinv=[]
        oqsi=[]
        beginv=0
        for j in oquan:
            if beginv+j>=d and (beginv+j-d)<=maxinv:
                oqsi+=[j]
                endinv+=[beginv+j-d]
        qstar,rewardi=reward(oqsi,endinv,mcost,ocost,hcost,3,inv,r)
        print(rewardi)
        final+=[rewardi]
        finalbeginv+=[beginv]
        finaloquan+=[qstar]
    else:
        rewardalli=[];qstars=[]
        for i in inv:
            oqsi=[];endinv=[];
            for j in oquan:
                if i+j>=d and (i+j-d)<=maxinv:
                    oqsi+=[j]
                    endinv+=[i+j-d]
            try:
                qstar,rewardi=reward(oqsi,endinv,mcost,ocost,hcost,2,inv,r)
            except:
                qstar,rewardi=reward(oqsi,endinv,mcost,ocost,hcost,2,inv,rewardlast)
            rewardalli+=[rewardi]
            qstars+=[qstar]
        r=rewardalli
        print(r)
        final+=[r]
        finalbeginv+=[beginv]
        finaloquan+=[qstars]
print()

for i in range(1,len(final)+1):
    if i==1:
        ew=(finaloquan[-i]+finalbeginv[-i]-demand[i-1])
        print("Qstar of the %i period ="%i,finaloquan[-1])
    else:
        print("Qstar of the %i period ="%i,finaloquan[-i][finalbeginv[-i].index(ew)])
        ew=(ew+finaloquan[-i][finalbeginv[-i].index(ew)])-demand[i-1]
print()
print("Total Minimun cost =",final[-1])



    
    
