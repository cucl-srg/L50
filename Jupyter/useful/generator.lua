local device = require "device"
local moongen = require "moongen"
local memory = require "memory"

function master(ports,rate,iter,size)
	txDev0 = device.config{
		port = 0,
		rxQueues = 1,
		txQueues = 1,
	}
    if (ports == 2) then
        txDev1 = device.config{
		    port = 1,
		    rxQueues = 1,
		    txQueues = 1,
	    }
    end
	device.waitForLinks()
    if (ports == 1) then
        moongen.startTask("send",txDev0:getTxQueue(0),rate,iter,size)
    end
    if (ports == 2) then
        moongen.startTask("send",txDev0:getTxQueue(0),rate,iter,size)
        moongen.startTask("send",txDev1:getTxQueue(0),rate,iter,size)
    end
    moongen.waitForTasks()
end

function send(queue,rate,iter,size)
	queue:setRate(rate) --Mbits/sec
	moongen.sleepMillis(1000)
	local mem = memory.createMemPool(function(buf)
		buf:getEthernetPacket():fill{
		ethSrc = txDev,
		ethDst = "00:01:02:03:04:05",
		ethType = 0x1234,
		}
	end)
	local bufs = mem:bufArray(100) --packets per iteration
	local iters = 0
	while iters < iter and moongen.running() do -- iterations
		bufs:alloc(size) --packet size
		bufs:offloadUdpChecksums()
		queue:send(bufs)
        iters = iters + 1
	end
end
