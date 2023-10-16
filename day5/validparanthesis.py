res=[]
def br(n,s,openc=0,closec=0):
    if openc==closec==n:
        res.append(s)
    if openc<n:
        br(n,s+'(',openc+1,closec)
    if closec<openc:
        br(n,s+")",openc,closec+1)
    return res
n=int(input())    
print(br(n,s=""))     
