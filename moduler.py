import operator
# File_name = raw_input("File Name: ")
File_name = "test.txt"
linelist = open(File_name).readlines()

# print linelist

with open(File_name) as fp:
    linelist = fp.read().split("\n")

linelist = [i.strip() for i in linelist]
noofserver = int(linelist[0])

print noofserver
# s_nextavail = [0 for i in range(0, noofserver)]
# read all server's efficiency
serverefficiency = linelist[1:noofserver + 1]
# sort all server's efficiency
serverefficiency.sort(key=float)
# create a dict for calculating required all valid data
servers = []
counter = 0
for s in serverefficiency:
    servers.append({"efficiency": float(s), "isavailable": True, "customersserved": 0,
                    "lastidletime": 0.0000, "totalservedtime": 0.0000, "idletimespent": 0.0000,
                    "timetobereleaved": 0.0000, "rank": counter})
    counter += 1

# print servers
for i in servers:
    # print i
    pass
# start reading queue from first person
customers = []
counter = 0
for cust in linelist[noofserver + 1:]:
    d = cust.split()
    if len(d) is 2:
        customers.append({"arrivaltime": float(d[0]), "timespend": float(d[1]),
                          "averagetimespentinqueue": 0.0000, "isprocessed": False,
                          "rank": counter})
        # print customers
        counter += 1

queue = {"customers": customers, "greatestqueuelength": 0,
         "currentqueue": 0, "lastcustomertimeout": 0.0000, "averagequeuelength": [], "servedcustomer": []}

# print queue


def servercustomer(customer):
    served = False
    # print "serving"
    servers.sort(lambda x,y : cmp(x["timetobereleaved"], y["rank"]))
    for s in servers:
        if s["isavailable"] == True:
            s["customersserved"] += 1
            s["lastidletime"] = round(customer["arrivaltime"],4) 
            s["timetobereleaved"] = round(s["lastidletime"] + \
                (customer["timespend"] * s["efficiency"]),4)
            s["isavailable"] = False
            s["totalservedtime"] += round(customer["timespend"] * s["efficiency"],4)
            s["idletimespent"] = round(s["timetobereleaved"] - customer["arrivaltime"],4) 
            served = True
            break
    return served

# print len(queue["customers"])
def resetallserver(time):
    servergetempty = False
    co = 0
    for s in servers:
        # print str(s["timetobereleaved"]) + "  "+str(time)
        if not s["isavailable"]:
            if round(s["timetobereleaved"], 4) * 10000 > round(time, 4)*10000:
                s["isavailable"] = True
                servergetempty = True
                co += 1
                # break
        else:
            s["lastidletime"] = time
    return servergetempty

iscalled = True
def nextservertobereleaved():
    global iscalled
    servers.sort(lambda x,y : cmp(x["rank"], y["timetobereleaved"]))
    return servers[0]['timetobereleaved']
    if iscalled:
        print "final"
        print servers[0]['timetobereleaved']
        print servers[1]['timetobereleaved']
        print "servers"
        for s in servers:
            print s
        iscalled = False


queuelength = 0
isqueueavailable = False
nexttime = 0.0000
waitingqueue = []
try:
    while len(queue["customers"]) > 0:
        # if anyserveravialable():
        # if isqueueavailable:
        #     isserved = servercustomer(waitingqueue[0])
        # else:
        isserved = servercustomer(queue["customers"][0])
        if isserved:
            # pop that customer
            print "popped : " + str(queue["customers"][0]["rank"])
            queue["customers"].pop(0)
            print queue["customers"][0]["arrivaltime"]
            for s in servers:
                print s["timetobereleaved"]
        # else:
        if resetallserver(queue["customers"][0]["arrivaltime"]):
            # we got at least 1 server free
            # for next cycle 
            pass
            nexttime = 0.0000
        else:
            pass
                # maintain queue
                # isqueueavailable = True
                # waitingqueue.append(queue["customers"].pop(0))
                # nexttime = nextservertobereleaved()

except :
    # print e
    totalserved = 0
    totalservedtime = 0.0000
    for s in servers:
        # print s
        print "Server " + str(s["rank"])+":"
        print "Served Customer : " + str(s["customersserved"])
        print "Last customer served time : " +str(s["timetobereleaved"])
        print "Total Served time : " + str(s["totalservedtime"])
        print "Last Idle Time : " + str(s["lastidletime"])
        totalserved += s["customersserved"]
        totalservedtime += round(s["totalservedtime"],4)
        print "----------------------------------"
    print "Total Served Customer : " + str(totalserved)
    print "Total Served Time : " + str(totalservedtime)
server = open("server.data", 'w')
# customers =
