def optionalFieldIsGood(mine, theirs):
        """check if optional field theirs matches with mine"""
        if (theirs is None or
                theirs == "" or
                theirs == mine):
            return True
        else:
            return False

def requiredFieldIsGood(mine, theirs):
    """check if required field theirs matches with mine"""
    if (theirs is not None and
            mine == theirs):
        return True
    else:
        return False