from useful import np,plt,findall,ceil,floor
import os


def ind_of(value,arr):
    for j in range(len(arr)):
            if (arr[j] == value or j == len(arr)-1):
                return j
            elif (arr[j] > value):
                return j-0.5

def smallest_index(value, arrarr):
    smalls = []
    for i in range(10):
        smalls.append(ind_of(value,arrarr[i]))
    return min(smalls)

def largest_index(value, arrarr):
    larges = []
    for i in range(10):
        larges.append(ind_of(value,arrarr[i]))
    return max(larges)
    
def getrtts(exp,crsid,num):
    rtts= [[] for i in range(10)]
    for i in range(10):
        with open('/root/'+crsid+'/L50Lab1/'+exp+'_'+str(i)) as f:
            for j in range(num):
                rt = f.next()
                rt = findall(r'time=(.*?) ms',rt)[0]
                rtts[i].append(float(rt)*1000)
        rtts[i] = sorted(rtts[i])
    return rtts

# you will use functions under this line

def getrtt(ffile,crsid,num):
    rtt= []
    with open('/root/'+crsid+'/L50Lab1/'+ffile) as f:
            for j in range(num):
                rt = f.next()
                rt = findall(r'time=(.*?) ms',rt)[0]
                rtt.append(float(rt)*1000)
    rtt = sorted(rtt)
    return rtt

def graph1(exp,crsid,div,num):
    rtts= getrtts('1/'+exp,crsid,num)
    avgs = []
    for i in range(num):
        avg = np.median([rtts[j][i] for j in range(10)])
        avgs.append(avg)
    values, base = np.histogram(avgs, bins=1000)
    cumulative = np.cumsum(values/float(num))
    plt.plot(base[:-1], cumulative)
    plt.ylabel("Cumulative probability")
    plt.xlabel("RTT (us)")

    minn = int(ceil(avgs[0]/ div)*div)
    maxx = int(floor(avgs[num-1] / div)*div)
    errxs = np.arange(minn,maxx+1,div)
    minsmaxs = [[],[]]
    errys = []
    for i in errxs:
        ind = ind_of(i,avgs)
        errys.append((ind+1)/float(num))
        sml = smallest_index(i, rtts)
        minsmaxs[0].append(abs(ind-sml)/float(num))
        lrg = largest_index(i, rtts)
        minsmaxs[1].append(abs(ind-lrg)/float(num))
    plt.errorbar(errxs, errys, yerr=minsmaxs,linestyle="none")
    plt.show()

def graph5_000001(exp,crsid,usecs,num):
    maxs_000001 = [[] for u in usecs]
    mins_000001 = [[] for u in usecs]
    meds_000001 = [[] for u in usecs]
    for u in range(len(usecs)):
        for i in range(10):
            rtt = getrtt('5/'+exp+'_0.000001_'+str(usecs[u])+'_'+str(i), crsid,num)
            maxs_000001[u].append(max(rtt))
            mins_000001[u].append(min(rtt))
            meds_000001[u].append(np.median(rtt))

    maxs_000001_meds = []
    maxs_000001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(maxs_000001[u])
        maxs_000001_meds.append(med)
        maxs_000001_minsmaxs[0].append(abs(min(maxs_000001[u])- med))
        maxs_000001_minsmaxs[1].append(abs(max(maxs_000001[u])- med))
    plt.errorbar(usecs, maxs_000001_meds, yerr=maxs_000001_minsmaxs,label="maximum")

    meds_000001_meds = []
    meds_000001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(meds_000001[u])
        meds_000001_meds.append(med)
        meds_000001_minsmaxs[0].append(abs(min(meds_000001[u])- med))
        meds_000001_minsmaxs[1].append(abs(max(meds_000001[u])- med))
    plt.errorbar(usecs, meds_000001_meds, yerr=meds_000001_minsmaxs,label="median")

    mins_000001_meds = []
    mins_000001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(mins_000001[u])
        mins_000001_meds.append(med)
        mins_000001_minsmaxs[0].append(abs(min(mins_000001[u])- med))
        mins_000001_minsmaxs[1].append(abs(max(mins_000001[u])- med))
    plt.errorbar(usecs, mins_000001_meds, yerr=mins_000001_minsmaxs,label="minimum")

    plt.ylabel("RTT (us)")
    plt.xlabel("rx-usecs")
    plt.title("Ping interval = 0.000001 s")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def graph5_001(exp,crsid,usecs,num):
    maxs_001 = [[] for u in usecs]
    mins_001 = [[] for u in usecs]
    meds_001 = [[] for u in usecs]
    for u in range(len(usecs)):
        for i in range(10):
            rtt = getrtt('5/'+exp+'_0.001_'+str(usecs[u])+'_'+str(i), crsid,num)
            maxs_001[u].append(max(rtt))
            mins_001[u].append(min(rtt))
            meds_001[u].append(np.median(rtt))

    maxs_001_meds = []
    maxs_001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(maxs_001[u])
        maxs_001_meds.append(med)
        maxs_001_minsmaxs[0].append(abs(min(maxs_001[u])- med))
        maxs_001_minsmaxs[1].append(abs(max(maxs_001[u])- med))
    plt.errorbar(usecs, maxs_001_meds, yerr=maxs_001_minsmaxs,label="maximum")

    meds_001_meds = []
    meds_001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(meds_001[u])
        meds_001_meds.append(med)
        meds_001_minsmaxs[0].append(abs(min(meds_001[u])- med))
        meds_001_minsmaxs[1].append(abs(max(meds_001[u])- med))
    plt.errorbar(usecs, meds_001_meds, yerr=meds_001_minsmaxs,label="median")

    mins_001_meds = []
    mins_001_minsmaxs = [[],[]]
    for u in range(len(usecs)):
        med = np.median(mins_001[u])
        mins_001_meds.append(med)
        mins_001_minsmaxs[0].append(abs(min(mins_001[u])- med))
        mins_001_minsmaxs[1].append(abs(max(mins_001[u])- med))
    plt.errorbar(usecs, mins_001_meds, yerr=mins_001_minsmaxs,label="minimum")

    plt.ylabel("RTT (us)")
    plt.xlabel("rx-usecs")
    plt.title("Ping interval = 0.001 s")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def data_iperf(fexp,crsid):
    bws = [[] for i in range(10)]
    for j in range(5):
        with open('/root/'+crsid+'/L50Lab1/'+fexp+'_' + str(j)) as f:
            for i in range(10):
                bw = f.next()
                bww = findall(r'Bytes(.*?)Gbits/sec', bw)[0]
                bws[i].append(float(bww))
    return bws


def data10(crsid):
    sbw = [[] for i in range(10)]
    cbw = [[] for i in range(10)]
    for j in range(5):
        with open('/root/'+crsid+'/L50Lab1/10/exp10_' + str(j)) as f:
            f.next()
            f.next()
            for i in range(10):
                sb = f.next()
                sbww = findall(r'GBytes(.*?)Gbits/sec', sb)[0]
                sbw[i].append(float(sbww))
                cb = f.next()
                cbww = findall(r'GBytes(.*?)Gbits/sec', cb)[0]
                cbw[i].append(float(cbww))
    return sbw, cbw

def data11(windows,crsid):
    winds = []
    bws = [[] for w in windows]
    for b in range(len(windows)):
        for i in range(5):
            with open('/root/'+crsid+'/L50Lab1/11/exp11_'+str(windows[b])+'_'+str(i)) as f:
                wind = f.next()
                if (i==0):
                    w = findall(r'size:(.*?)KByte', wind)[0]
                    winds.append(float(wind[17:21]))
                bw = f.next()
                bww =findall(r'KBytes(.*?)Kbits/sec',bw)[0]
                bws[b].append(float(bww)/1000000)
    return winds, bws


def data_band(fexp,crsid,bands):
    pcs = [[] for b in bands]
    bans = [[] for b in bands]
    for b in range(len(bands)):
        for i in range(5):
            with open('/root/'+crsid+'/L50Lab1/'+fexp+'_'+str(bands[b])+'_'+str(i)) as f:
                out = f.read()
                ba = float(findall(r'Bytes(.*?)Mbits/sec',out)[0])
                bans[b].append(ba)
                pc = float(findall(r' \((.*?)%\)',out)[0])
                pcs[b].append(pc)
    bans = map(np.average,bans)
    return bans,pcs

def data13b(windows,crsid):
    bws = [[] for w in windows]
    for b in range(len(windows)):
        for i in range(5):
            with open('/root/'+crsid+'/L50Lab1/13/exp13b_'+str(windows[b])+'_'+str(i)) as f:
                for i in range(3):
                    f.next()
                bb = f.next()
                bb= findall(r'Bytes(.*?)Mbits/sec',bb)[0]
                bws[b].append(float(bb)/1000)
    return bws

def graph_error(data):
    meds = map(np.median,data)
    mins = map(min,data)
    maxs = map(max,data)
    minsmaxs = [[],[]]
    for i in range(len(data)):
        minsmaxs[0].append(abs(mins[i] - meds[i]))
        minsmaxs[1].append(abs(maxs[i] - meds[i]))
    return meds,minsmaxs
