"""
Had trouble parsing output from chunkinator ,
it was a list with almost 190 unsorted members
I needed to build a "snapshot" on an output of a healthy system
slightly modify it and use it as my expected result when everything was fixed.
I brainstormed this concept in local small python script
"""
import re

chunkinatorOutput = ["aslkdj", " c>", "asd", "asd ", "asd", "213423",
                     "MGMT_COMP_STATE_FAILED",
                     "16",
                     "Loading 800 sym_journal_md JR_TYPE_SYM_REPO(17) chunk descriptors starting at index 0",
                     "Loading 5 sym_journal_md JR_TYPE_SYM_REPO_SCSI_REG(19) chunk descriptors", "3245", "df", "dfg",
                     "Node 8",
                     "Xenv 10 is in transition (MODULE_TYPE_CONTROL(2)+MODULE_TYPE_DATA(3)+xenv+node<sym_repo>+node<sym_md.mapping_adjcent>+node<sym_journal_md> HEALTHY, Dmdl+A2H+CIO chunks NOT MOVED, MODULE_TYPE_ROUTER(1) FAILED)",
                     "Xenv 11 is healthy",
                     "Journal is in transition (is_synced_to_disk==FALSE, journal+node<sym_repo>+node<sym_md.mapping_adjcent>+node<sym_journal_md> HEALTHY, enough amount of chun",
                     "Node 9",
                     "Xenv 12 is healthy",
                     "Xenv 13 is healthy",
                     "Journal is in transition (is_synced_to_disk==FALSE, journal+node<sym_repo>+node<sym_md.mapping>+node<sym_journal_md> HEALTHY, enough amount of chunks)",
                     "Node 14",
                     "Xenv 16 is healthy", "Xenv 17 is healthy",
                     "Journal is in transition (is_synced_to_disk==FALSE, journal+node<sym_repo>+node<sym_md.mapping_adjcent>+node<sym_journal_md> HEALTHY, enough amount of chunks)"
                     "Node 15",
                     "Xenv 18 is healthy",
                     "Xenv 19 is healthy",
                     "Journal is in transition (is_synced_to_disk==FALSE, journal+node<sym_repo>+node<sym_md.mapping>+node<sym_journal_md> HEALTHY, enough amount of chunks)",
                     "ERROR36: Too much nodes in transition for this script"]

nodeDict = {}  # { Node name : Xenv Number and status
nodeKeysList = []
xenvValues = []
curNodeKey = None
xenvName = None
isThisLineXenvValue = False

for line in chunkinatorOutput:
    if isThisLineXenvValue == True and curNodeKey != None:
        matchXenv = re.search(r'Xenv [0-9]+', line)  # get Xenv number
        if matchXenv:
            xenvName = matchXenv.group()
            xenvValues.append(xenvName)
            #print "XenvName {}".format(xenvName)

            nodeDict[curNodeKey].append(line)
            continue
        else:
            isThisLineXenvValue == False
    match = re.search(r'Node [0-9]+', line)
    if match:  # Node found
        isThisLineXenvValue = True
        curNodeKey = match.group()  # Getting Node name as key
        #print type(curNodeKey)
        nodeKeysList.append(curNodeKey)  # Appending key to list for usage in nodeDict
        #print ("found node key !", curNodeKey)
        nodeDict[curNodeKey] = []
        continue

areOtherXenvsHealthy = False
isKeyfound=False


# def checkXenvStatus
#will return False or True based on that will proceed or fail


for key, value in nodeDict.items():
    if not(not isKeyfound or areOtherXenvsHealthy and value[1].find("healthy") and value[0].find("healthy")):
        areOtherXenvsHealthy = False
        break

    if key == "Node 8" and value[0].find("FAILED"):
        print (value[0])
        print "Validated Xenv 10 is Fucked up !".upper()
        print value[1]
        areOtherXenvsHealthy = True
        isKeyfound=True
    else:
        print key,value


print areOtherXenvsHealthy









# if "FAILED" in z and ("FAILED" not in node9Diagnostic and "FAILED" not in node8Diagnostic[1]):
# print ('found "FAILED" on {}'.format(z[0:8]))

# cluster.sym_repo.SymPersObjMdl[0].state=16
