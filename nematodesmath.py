from math import comb

def histogram(N, factor=1): # N is total population; generates dictionary of value (total) : probability pairs
    n = N // 2 # factor is for multiplying probabilities, i.e. there's something "above" in the tree
    hist = {}
    
    for k in range(n+1): # generate histogram for total nematodes
        hist[k+N] = comb(n, k) / 2**n * factor                          
            #^+N is so that there are *total* values

    return hist # in value : probability format

tree = [
    {2 : 0.5, 3 : 0.5}
    # {value : probability, value : probability} for layer of tree 0
    # etc. for deeper layers 
]

days = 4
trimming_value = 0.00001
for i in range(days): 
    print(i)
    new_layer = {}
    for num, prob in tree[i].items():
        hist = histogram(num, prob)
        for key, value in hist.items(): # 'add' dictionaries together, but add values belonging to same key. {1 : 2, 3 : 4} + {1 : 5} = {1 : 7, 3 : 4}
            if hist[key] > trimming_value: # don't count tiny probabilities
                if key in new_layer.keys():
                    new_layer[key] += value
                else: new_layer[key] = value

    tree.append(new_layer)
#print(tree)
print(tree[-1])
print(sum(tree[-1].values()))
sum_ = 0
for key, value in tree[-1].items(): # now find expected probability
    sum_ += key * value

print(sum_)