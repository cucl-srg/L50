from useful import local_cmd, ssh_cmd, ssh_connect

def getdeltas(exp,num):
    local_cmd('tshark -r /root/L50Lab3/'+exp+'.erf -V | grep "previous captured" > '
              '/root/L50Lab3/'+exp+'_d.txt')
    deltas = []
    with open('/root/L50Lab3/'+exp+'_d.txt') as f:
        f.next()
        for i in range(2,num+1):
            delta = f.next()[46:57]
            deltas.append(float(delta)*1000000)
    return deltas
