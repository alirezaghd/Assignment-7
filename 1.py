def mul(x,y):
    result = {'s' : None , "m" : None}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']

    return result

def sum(x,y):
    result = {'s' : None , 'm': None}
    result['s'] = x['s'] * y['m'] + x['m'] * y['s']
    result['m'] = x['m'] * y['m']

    return result

def sub(x,y):
    result = {'s' : None , 'm' : None}
    result['s'] = x['s'] *y['m'] - x['m'] * y['s']
    result['m'] = x['m'] * y['m']

    return result

def div(x,y):
    result = {'s' : None , 'm': None}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']

    return result


a= {'s':5 , 'm':8} 
b= {'s':2 , 'm' :4}

c = mul(a,b)
print("Multiplication")
print(c['s'] , '/' , c['m'])
print("sum")

c  = sum(a,b)
print(c['s'] , '/' , c['m'])

print("Submission")
c = sub(a,b)
print(c['s'] , '/' , c['m'])


print("Division")
c = div(a,b)
print(c['s'] , '/' , c['m'])

