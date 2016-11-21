reasonable_choice = False
assert reasonable_choice, "You have made a False choice and will never see me !"

"""
@xioDecorators.TCSetup('QC-20817')
def test_QC20817_ChunkinatorOnActiveCluster():
    # region test Variables
    #  Variables required for TC ############################
    nodeDict = {}  # Node name (key) ,  (xenv output)value )
    nodeKeysList = []  # Node names list
    xenvValues = []  # xenv output
    curNodeKey = None  # node name e.g Node 8 , Node 9
    xenvName = None  # xenv name e.g Xenv 10 , Xenv 15
    isThisLineXenvValue = False  # internal for parsing  chunkiknator output
    areOtherXenvsHealthy = False  # result of XenvsStatusFailed - based on this we decide if result is as expected
    isKeyfound = False  # internal for iterating over Xenvs
    node_state_command = "cluster.sym_repo.SymPersObjMdl[0].state"
    invalid_xenv10_state = "16"
    valid_xenv10_state = "4"

    # chunkinatorOutput = [] #
    #  Variables required for TC ############################
    # endregion


    def createChunkinatorOutPutDictionary(chunkinatorOutput, nodeDict=nodeDict,
                                          isThisLineXenvValue=isThisLineXenvValue):
        for line in chunkinatorOutput:
            if isThisLineXenvValue is True and curNodeKey is not None:
                matchXenv = re.search(r"Xenv [0-9]+", line)  # get Xenv number regEx
                if matchXenv:
                    xenvName = matchXenv.group()
                    xenvValues.append(xenvName)
                    # print "XenvName {}".format(xenvName)

                    nodeDict[curNodeKey].append(line)
                    continue
                else:
                    isThisLineXenvValue == False
            match = re.search(r'Node [0-9]+', line)
            if match:  # Node found
                isThisLineXenvValue = True
                curNodeKey = match.group()  # Getting Node name as key
                # print type(curNodeKey)
                nodeKeysList.append(curNodeKey)  # Appending key to list for usage in nodeDict
                # print ("found node key !", curNodeKey)
                nodeDict[curNodeKey] = []
                continue

    def XenvsStatusFailed(nodeDict=nodeDict, areOtherXenvsHealthy=areOtherXenvsHealthy,
                          isKeyfound=isKeyfound):
        for key, value in nodeDict.items():
            if not (not isKeyfound or areOtherXenvsHealthy and value[1].find("healthy") and value[0].find("healthy")):
                areOtherXenvsHealthy = False
                break
            if key == "Node 8" and value[0].find("FAILED") != -1:
                # Printing dictionary generated from chunkinator output
                print (value[0])
                print value[1]
                areOtherXenvsHealthy = True
                isKeyfound = True
            else:
                print key, value
        return areOtherXenvsHealthy

    chuck_norris.reportObj.Info('Starting test QC-20817\n\n', color='bright blue')
    chuck_norris.TSF_DeployChuckNorris('<cluster>.xms',
                                       '<options>.CNVersion',
                                       cnInstallocation='/var/tmp/',
                                       latestVersion=False)
    chuck_norris.TSF_ConnectToChuckNorris('<cluster>.xms',
                                          '<options>.CNVersion',
                                          '<options>.CNRelease',
                                          stopSys='n',
                                          stopPMs='n')
    # cluster is NOT stopped as required by TC
    # changing Xenv 10 status to FAILED and in transition
    chuck_norris.reportObj.Info('Changing Node 8 Xenv 10 state to FAILED ....\n', color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('\n')
    chuck_norris.TSF_GetValFromChuckNorris(node_state_command + " = " + invalid_xenv10_state)
    chuck_norris.TSF_GetValFromChuckNorris('\n')
    message = "Changed Node 8 Xenv 10 state to FAILED, dumping...symrepo... "
    chuck_norris.reportObj.Info(message, color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('dump symrepo')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.parallel_jr_dump()')
    chuck_norris.TSF_GetValFromChuckNorris('\n')
    chuck_norris.TSF_GetValFromChuckNorris('exit()')
    # reconnecting to CN - here we have a framework performance issue
    chuck_norris.TSF_ConnectToChuckNorris('<cluster>.xms',
                                          '<options>.CNVersion',
                                          '<options>.CNRelease',
                                          stopSys='n',
                                          stopPMs='n')
    chuck_norris.reportObj.Info('validating with Chunkinator changed value \n', color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris("execfile('/var/tmp/chucknorris/scripts/chunkinator/import_and_run.py')",
                                           "chunkinatorOutPut")

    chunkinatorOutput = testInit.GetVar("chunkinatorOutPut")

    # test logic
    createChunkinatorOutPutDictionary(chunkinatorOutput)
    assert XenvsStatusFailed(), "Expecting FAILED status on Xenv 10 , Aborting test ! "

    if XenvsStatusFailed():
        chuck_norris.reportObj.Info('PASSED - status IS FAILED as expected !\n', color='bright blue')
    else:
        print "STATUS NOT FAILED! SHOULD STOP EXECUTION!"
        return # replace with assert in final commit framework does not fail TC if return is used

    chuck_norris.reportObj.Info('Changing node state to back to HEALTHY ....\n', color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('\n')
    # reverting Xenv 10 state to "healthy"
    chuck_norris.TSF_GetValFromChuckNorris(node_state_command + " = " + valid_xenv10_state)
    chuck_norris.TSF_GetValFromChuckNorris('\n')
    message = "Changed node 8 state to Healthy"
    chuck_norris.reportObj.Info(message, color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('dump symrepo')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.parallel_jr_dump()')
    chuck_norris.TSF_GetValFromChuckNorris('exit()')
    # Connecting to CN for the third time - here we have a HUGE performance drop, need to talk to Tehila when she is back
    chuck_norris.TSF_ConnectToChuckNorris('<cluster>.xms',
                                          '<options>.CNVersion',
                                          '<options>.CNRelease',
                                          stopSys='n',
                                          stopPMs='n')

    chuck_norris.reportObj.Info('validating with Chunkinator changed value  - EXPECTING HEALTHY!\n',
                                color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris("\n")
    chuck_norris.TSF_GetValFromChuckNorris("execfile('/var/tmp/chucknorris/scripts/chunkinator/import_and_run.py')",
                                           "chunkinatorOutPut")
    chunkinatorOutput = testInit.GetVar("chunkinatorOutPut")

    createChunkinatorOutPutDictionary(chunkinatorOutput)


    if not XenvsStatusFailed():
        chuck_norris.reportObj.Info('PASSED HEALTHY !\n', color='bright blue')
    else:
        print "FAILED! SHOULD STOP EXECUTION!"
        return # replace with assert in final commit framework does not fail TC if return is used

    assert not XenvsStatusFailed(), "Expecting HEALTHY status on all XENV , Aborting test ! "
    chuck_norris.reportObj.Info('Xenv10 is healthy failure reverted, finishing test!\n', color='bright blue')

    chuck_norris.TSF_GetValFromChuckNorris('exit()')
    chuck_norris.reportObj.Info('Finished test_QC20817_ChunkinatorOnActiveCluster', color='green')


if __name__ == '__main__':
    # testSetId param should be mandatory, line below verifies that.
    assert [True for param in sys.argv if 'testsetid' in param.lower()], 'Please add --testSetId param'
"""