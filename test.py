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
    servers.append({"efficiency": round(float(s), 4), "isavailable": True, "customersserved": 0, "lastidletime": 0.0000,
                    "totalservedtime": 0.0000, "idletimespent": 0.0000, "timetobereleaved": 0.0000, "servedcustomerrank": []})

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
        customers.append({"arrivaltime": d[0], "timespend": d[1], "averagetimespentinqueue": 0.0000,
                          "served": False, "rank": counter})
        counter += 1
        # print customers

queue = {"customers": customers, "currentqueue": 0,
         "lastcustomertimeout": 0.0000}

# print queue

print len(queue["customers"])
nextarrivaltime = round(float(queue["customers"][0]["arrivaltime"]), 4)
currenttime = round(float(queue["customers"][0]["arrivaltime"]), 4)
# crawl time in terms of seconds
isqueue = True
count = 0
epsilon = 0.0000

dataqueue = []
# abs(a - b)<epsilon
while len(queue["customers"]) > 0:
    # start server serving
    # currenttime = currenttime + 0.0001
    # print "currenttime : " + str(round(currenttime,4))
    # and if customer processed pop that customers
    if len(queue["customers"]) == 0:
        # isqueue = False
        break
    # print currenttime
    isinqueue = True
    for ser in servers:
        if len(queue["customers"]) > 0:
            print "diff : " + str(abs(round(currenttime, 4) - round(ser["timetobereleaved"], 4)))
            if abs(round(currenttime, 4) - round(ser["timetobereleaved"], 4)) > epsilon:
                # if True:
                if ser["isavailable"] is True:
                    # serve the customers and calculate
                    # print ser["isavailable"] + "" +

                    # if ser["lastidletime"] <=
                    # round(float(queue["customers"][0]["arrivaltime"]),4):
                    if queue["customers"][0]["arrivaltime"] >= ser["lastidletime"]:
                        requiredtimeforcustomers = ser["efficiency"] * \
                            float(queue["customers"][0]["timespend"])
                        # print requiredtimeforcustomers
                        # print "Time tobe releaved: " +
                        # str(round(float(queue["customers"][0]["arrivaltime"]) +
                        # requiredtimeforcustomers,4))
                        ser["timetobereleaved"] = round(
                            float(ser["lastidletime"]), 4) + round(requiredtimeforcustomers, 4)
                        ser["totalservedtime"] += round(
                            requiredtimeforcustomers, 4)
                        # ser["servedcustomerrank"].append(queue["customers"][0]["rank"])
                        # print (ser["timetobereleaved"])
                        dataqueue.append({"servedtime": ser["lastidletime"], "rank": queue["customers"][0]["rank"],
                                          "waitingtime": float(ser["lastidletime"]) - float(queue["customers"][0]["arrivaltime"])})
                        isinqueue = False
                        ser["isavailable"] = False
                        ser["customersserved"] += 1
                        # queue["customers"].pop(0)
                        break
                        # print ser
    if isinqueue:
            # reset server here by crawling time.
        print "in queue"
        for ser in servers:
            # if ser["isavailable"] is False:
            if abs(round(currenttime, 4) - round(ser["timetobereleaved"], 4)) > epsilon:
                ser["isavailable"] = True
                # ser["idle"] = True
                ser["lastidletime"] = ser["timetobereleaved"]
                # print "available"
                # print ser
                # print currenttime
                # pass
    else:
            # if len(queue["customers"]) > 0:
        print "in else"
        queue["customers"].pop(0)
        # print "popped"
        if len(queue["customers"]) > 0:
            currenttime = round(
                float(queue["customers"][0]["arrivaltime"]), 4)
        else:
            break

            # currenttime
            # break

            # print queue["customers"]
        print currenttime
for s in servers:
    print s
server = open("server.data", 'w')
server.write(str(servers))
cust = open("cust.data", 'w')
finaldata = []
for d in dataqueue:
    if d["waitingtime"] > 0.00000:
        finaldata.append(d)
        print d
print len(finaldata)
cust.write(str(finaldata))
