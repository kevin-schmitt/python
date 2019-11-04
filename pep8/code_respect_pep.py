"""
    Module code_respect_pep
    Author kevin schmitt
"""
def good_function(val, val2=5):
    """
        Example function for pep8

        val  integer  : ...
        val2 integer  : ...

        return integer : ...
    """
    if val < 0:
        return - 1
    return val2


if __name__ == '__main__':
    print(good_function(3))