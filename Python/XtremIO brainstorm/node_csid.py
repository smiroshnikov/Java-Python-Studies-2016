def give_me_node_csid(xenv_csid):
    """
    :param xenv_csid: csid value for node's csid
    :type xenv_csid : integer
    :return: node csid value
    """
    assert 10 < xenv_csid <= 55, "Invalid csid value"
    node = xenv_csid - 1 - xenv_csid % 2 - (xenv_csid - 8) % 6 / 2
    return node


print give_me_node_csid(43)
