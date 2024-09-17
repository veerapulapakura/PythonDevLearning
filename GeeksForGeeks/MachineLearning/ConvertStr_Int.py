def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        #return 10000000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

print(value_to_float('2.90K'))
print(value_to_float('2.9M'))

#df['col'] = df['col'].apply(value_to_float)
# https://github.com/aneagoie/ML-Notes/blob/master/soccer.ipynb

