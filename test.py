# File_name = raw_input("File Name: ")
File_name = "test.txt"
linelist = open(File_name).readlines()

print linelist

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
    servers.append({"efficiency": s, "isavailable": True, "customersserved": 0,
                    "totalservedtime": 0.0, "idletimespent": 0.00,"timetobereleaved" : 0.00, "lastidletime" : 0.00})

# print servers
for i in servers:
    print i
# start reading queue from first person
customers = []
for cust in linelist[noofserver + 1:]:
    d = cust.split()
    if len(d) is 2:
        customers.append({"arrivaltime": d[0], "timespend": d[1], "averagetimespentinqueue": 0.00,
                          "isprocessed": False})
        # print customers

queue = {"customers": customers, "greatestqueuelength": 0,
        "currentqueue": 0, "lastcustomertimeout": 0.00, "averagequeuelength": []}

# print queue
def processqueue(_q):
    pass
print  len(queue["customers"])

currenttime = 0.00
# crawl time in terms of seconds
isqueue = True

while isqueue:
    # start server serving
    currenttime = currenttime + 0.0001
    # print currenttime
    # and if customer processed pop that customers 
    isinqueue = True
    for ser in servers:
        if ser["isavailable"]:
            # serve the customers and calculate
            if len(queue["customers"]) > 0: 
                requiredtimeforcustomers = float(ser["efficiency"]) * float(queue["customers"][0]["timespend"])
                print requiredtimeforcustomers
                ser["timetobereleaved"] += requiredtimeforcustomers
            isinqueue = False
            ser["isavailable"] = False
            # print ser
            # exit
    if isinqueue:
        # don't delete it, save it until server got time next cycle
        # reset server here by crawling time.
        for ser in servers:
            if ser["timetobereleaved"] >= currenttime:
                ser["isavailable"] = True
        pass
    else: 
        if len(queue["customers"]) > 0:
            queue["customers"].pop(0)
            pass
    if len(queue["customers"]) == 0:
        isqueue = False

print queue["customers"]