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
for s in serverefficiency:
    servers.append({"efficiency": s, "isavailable": True, "customersserved": 0, "lastidletime": 0.0000,
                    "totalservedtime": 0.0000, "idletimespent": 0.0000, "timetobereleaved": 0.0000})

# print servers
for i in servers:
    # print i
    pass
# start reading queue from first person
customers = []
for cust in linelist[noofserver + 1:]:
    d = cust.split()
    if len(d) is 2:
        customers.append({"arrivaltime": d[0], "timespend": d[1], "averagetimespentinqueue": 0.0000,
                          "isprocessed": False})
        # print customers

queue = {"customers": customers, "greatestqueuelength": 0,
         "currentqueue": 0, "lastcustomertimeout": 0.0000, "averagequeuelength": []}

# print queue


def processqueue(_q):
    pass


print len(queue["customers"])

currenttime = round(float(queue["customers"][0]["arrivaltime"]),4)
# crawl time in terms of seconds
isqueue = True
count = 0 
epsilon = 0.0001
# abs(a - b)<epsilon
while isqueue:
    # start server serving
    # currenttime = currenttime + 0.0001
    # print "currenttime : " + str(round(currenttime,4))
    # and if customer processed pop that customers
    print currenttime
    isinqueue = True
    for ser in servers:
        if ser["isavailable"] is True:
            # serve the customers and calculate
            # print ser["isavailable"] + "" +
            if len(queue["customers"]) > 0:
                if abs(round(currenttime,4) - round(ser["timetobereleaved"],4)) > epsilon:
                # if ser["lastidletime"] <= round(float(queue["customers"][0]["arrivaltime"]),4):
                    requiredtimeforcustomers = float(
                        ser["efficiency"]) * float(queue["customers"][0]["timespend"])
                    # print requiredtimeforcustomers
                    ser["timetobereleaved"] = round(float(queue["customers"][0]["arrivaltime"]) + requiredtimeforcustomers,4)
                    ser["totalservedtime"] += round(requiredtimeforcustomers,4)
                    # print (ser["timetobereleaved"])
                    isinqueue = False
                    ser["isavailable"] = False
                    ser["customersserved"] += 1
                    # queue["customers"].pop(0)
                    break
            # print ser
    if not isinqueue:
        if len(queue["customers"]) > 0:
            queue["customers"].pop(0)
            # print "popped"
            if len(queue["customers"]) > 0:
                currenttime = round(float(queue["customers"][0]["arrivaltime"]),4)
            else:
                break
    else:
        # don't delete it, save it until server got time next cycle
        # reset server here by crawling time.
        for ser in servers:
            if ser["isavailable"] is False:                
                # if ser["timetobereleaved"] >= currenttime:
                    ser["isavailable"] = True
                    # ser["idle"] = True
                    ser["lastidletime"] = ser["timetobereleaved"]
                    print "available"
                    # print ser
                    # print currenttime
        pass
    if len(queue["customers"]) == 0:
        isqueue = False
    
    # currenttime
    # break

# print queue["customers"]
print currenttime
for s in servers:
    print s
