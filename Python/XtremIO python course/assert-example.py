def test(x=None):
    if x < 20:
        return True
    return False


assert test(input("enter int:> \n")), "False assert message !"
# assert is intended to kick you out of code execution !
# use exceptions if you need to wrap them and continue execution 

print ("lets proceed with CODE execution")
