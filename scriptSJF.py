class Process:
    def __init__(self, pid, wt, bt):
        self.pid=pid    #process
        self.arrival=wt #waiting time
        self.burst=bt   #waiting burst
chart = []
def SJF(plist, n, preemp):
#plist  lista de processo
#numero do processo
#preemptivo

    global chart
    fila=[]     #Fila de processos
    tempo=0     #tempo de chegada
    ap=0        #tempo do processo
    rp=0        #processo pronto
    done=0      #processo terminou

    if not preemp:
        while(done<n):
            for i in range (ap,n):
                if tempo>=plist[i].arrival:
                    fila.append(plist[i])
                    ap+=1
                    rp+=1
            if rp<1:
                tempo+=1
                chart.append(0)
                continue
            fila.sort(key=lambda x: (x.burst, x.arrival))
            if fila [0].burst>0:
                for q in range (fila[0].burst):
                    chart.append(fila[0].pid)
                tempo+=fila[0].burst
                fila[0].burst=9999999999
                done+=1
                rp-=1
plist=[]
plist.append(Process([1],0,3))
plist.append(Process([2],2,4))
plist.append(Process([3],4,2))
plist.append(Process([4],5,4))
SJF(plist,len(plist),0)
print(chart)
