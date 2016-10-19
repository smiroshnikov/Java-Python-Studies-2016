@xioDecorators.TCSetup('QC-20842')
def test_QC20842_ModifySymMD():
    """
    Test purpose:
        Modify SYM meta data and check cluster's functionality.

    Steps:
        1) Stop cluster and all Pms using CN.
        2) Edit symmd.sys_guid array, dump symmd and compare between orig values and changed one.
        3) Restore orig values and dump symmd.
    """

    change_guid = 'symmd.sys_guid[:]={}'
    search = 'CN> symmd.sys_guid[:]'

    chuck_norris.reportObj.Info('Starting test QC-20842\n\n', color='blue')


    orig_guid_list = chuck_norris.GetGuidWithChuckNorris(search)
    modified_guid_list = orig_guid_list[:-3] + list(bytearray('hio'))  # 3 last indexes should be 104,105,111

    message = '\nChanging guid from:\n{0}\n to:\n{1}\n'.format(orig_guid_list, modified_guid_list)
    chuck_norris.reportObj.Info(message, color='blue')
    chuck_norris.TSF_GetValFromChuckNorris(change_guid.format(modified_guid_list))

    # Dump the new modified list, try to start up cluster - should fail and exit CN
    chuck_norris.reportObj.Info('Dump modified guid change and exit CN\n', color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('dump symmd')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.start_cluster_naturally()')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.start_cluster_via_gw()')

    try:
        cluster.TSF_WaitForClusterState("<cluster>", expectedState='down', period=240, deltaFactor=10)
    except TestFailure:
        cluster.TSF_WaitForClusterState("<cluster>", expectedState='unknown', period=240, deltaFactor=10)

    chuck_norris.TSF_GetValFromChuckNorris('exit()')
    chuck_norris.reportObj.Info('Out of CN after failed attempt to start the cluster \n', color='bright blue')

    chuck_norris.reportObj.Info('Connecting to CN\n', color='blue')
    chuck_norris.TSF_ConnectToChuckNorris('<cluster>.xms',
                                          '<options>.CNVersion',
                                          '<options>.CNRelease',
                                          stopSys='n',
                                          stopPMs='n')

    # Due to a failed attempt to start the cluster from above line
    # I found it easier and quicker to stop the cluster violently
    chuck_norris.TSF_GetValFromChuckNorris('cluster.stop_cluster_violently()')




    chuck_norris.reportObj.Info('Verifying edited value is stored in symmd.sys_guid and not the original', color='blue')
    after_change_list = chuck_norris.GetGuidWithChuckNorris(search)


    assert_msg = 'Expected list is: {}\nReceived list is: {}'
    # comparison when order and repetitions matter
    assert modified_guid_list == after_change_list, assert_msg.format(modified_guid_list, after_change_list)





    message = 'Restoring the original value of guid->\nFrom:\n{0} To:\n{1}\n'.format(modified_guid_list, orig_guid_list)
    chuck_norris.reportObj.Info(message, color='blue')
    chuck_norris.TSF_GetValFromChuckNorris(change_guid.format(orig_guid_list))

    # Dump the original list, start the cluster and exit CN
    chuck_norris.reportObj.Info('Dump orig guid change and starting up the cluster\n', color='bright blue')
    chuck_norris.TSF_GetValFromChuckNorris('dump symmd')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.start_cluster_naturally()')
    chuck_norris.TSF_GetValFromChuckNorris('cluster.start_cluster_via_gw()')
    cluster.TSF_WaitForClusterState("<cluster>", expectedState='active')
    chuck_norris.TSF_GetValFromChuckNorris('exit()')
    chuck_norris.reportObj.Info('Finished test_QC20842_ModifySymMD', color='blue')









