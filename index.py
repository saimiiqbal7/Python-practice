
def checkingIfIn(key:str,
                 direction:bool=True,
                 d:dict | None=None) -> bool:
    
    if d is None:
        d = {
            'apple': 2,
            'pear': 1,
            'fruit': 19,
            'orange': 5,
            'banana': 3,
            'grapes': 2,
            'watermelon': 7
        }
    
    if direction:
        return key in d
    else:
        return key not in d
