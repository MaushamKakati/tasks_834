def getKey(x: dict):
    keys = list(x)
    if len(keys) != 1:
        raise Exception('either multiple keys or empty dict found')
    else:
        return keys[0]
        
def getValue(x: dict, key: str):
    #print(x, key)
    if (key in x.keys()):
        #print('x[key]=',x[key])
        if type(x[key] is dict):
            return getValue(x[key],getKey(x[key]))
        else:
            return x[getKey(x)]
    else:
        currentKey=getKey(x)
        #print('currentKey=',currentKey)
        return getValue(x[currentKey],key)
        
        
x = {'a': {'b': {'c': {'d': 'e'}}}}
output = getValue(x, 'c')
print (output)