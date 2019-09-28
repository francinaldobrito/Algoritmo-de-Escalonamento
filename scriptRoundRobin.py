#Process objects
#Grantt Chart
#Shift CL
#RR
chart = []
class Process:
    def __init__(self, pid, AT, BT):
        self.pid = pid  # process
        self.arrival = AT  # waiting time
        self.burst = BT  # waiting burst


def shiftCL(alist):
    temp = alist[0]
    for i in range(len(alist) - 1):
        alist[i] = alist[i + 1]
    alist[len(alist) - 1] = temp
    return alist


def RR(tq, plist, n):
    global chart
    queue = []
    time = 0  # tempo de chegada
    ap = 0  # tempo do processo
    rp = 0
    done = 0  # processo terminou
    q = tq  # tempo de quantum
    start = 0
    while (done < n):

        for i in range(ap, n):
            if time >= plist[i].arrival:
                queue.append(plist[i])
                ap += 1
                rp += 1

        if rp < 1:
            chart.append(0)
            time += 1
            continue

        if start:
            queue = shiftCL(queue)

        if queue[0].burst > 0:
            if queue[0].burst > q:
                for q in range(time, time + q):
                    chart.append(queue[0].pid)
                time += q
                queue[0].burst -= q
            else:
                for q in (time, time + queue[0].burst):
                    chart.append(queue[0].pid)
                time += queue[0].burst
                queue[0].burst = 0
                done += 1
                rp -= 1
            start = 1


plist = []
plist.append(Process(1, 0, 5))
plist.append(Process(2, 1, 3))
plist.append(Process(3, 3, 6))
plist.append(Process(4, 5, 1))
plist.append(Process(5, 6, 4))
RR(3, plist, len(plist))
print(chart)

