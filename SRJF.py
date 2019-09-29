class Process:
    def __init__(self, pid, at, bt):
        self.pid=pid
        self.arrival=at
        self.burst=bt
chart = []
#waiting queue      fila de espera
#not preemptive     não preemptivo
def SJF(plist, n, preemp):
    global chart
    queue=[]     #Fila de processos
    time=0      #Time
    ap=0        #arrived process
    rp=0        #ready process
    done=0      #done process

    if not preemp:
        while(done<n):
            for i in range (ap,n):
                if time>=plist[i].arrival:
                    queue.append(plist[i])
                    ap+=1
                    rp+=1
            if rp<1:
                time+=1
                chart.append(0)
                continue
            queue.sort(key=lambda x: (x.burst, x.arrival))
            if queue [0].burst>0:
                for q in range (queue[0].burst):
                    chart.append(queue[0].pid)
                time+=queue[0].burst
                queue[0].burst=9999999999
                done+=1
                rp-=1
    else :
        while(done<n):
            for i in range (ap,n):
                if time>=plist[i].arrival:
                    queue.append(plist[i])
                    ap+=1
                    rp+=1
            if rp<1:
                time+=1
                chart.append(0)
                continue
            queue.sort(key=lambda x: (x.burst, x.arrival))
            if queue [0].burst>0:
                chart.append(queue[0].pid)
                time+=1
                queue[0].burst-=1
                if queue[0].burst<1:
                    queue[0].burst=9999999999
                    done+=1
                    rp-=1
plist=[]
plist.append(Process([1],0,7))
plist.append(Process([2],2,4))
plist.append(Process([3],4,1))
plist.append(Process([4],5,4))

SJF(plist,len(plist),1)
print(chart)