#-- Fruits into basket 
blocks = [(k, len(list(v)))
              for k, v in itertools.groupby(tree)]
print(blocks)
ans = i = 0
while i < len(blocks):
    # We'll start our scan at block[i].
    # types : the different values of tree[i] seen
    # weight : the total number of trees represented
    #          by blocks under consideration
    types, weight = set(), 0

    # For each block from i and going forward,
    for j in range(i, len(blocks)):
        print('j is: '+str(j))
        # Add each block to consideration
        types.add(blocks[j][0])
        weight += blocks[j][1]
        print('--------')
        print(blocks[j][1])
        print(types)
        print(weight)

        # If we have 3 types, this is not a legal subarray
        if len(types) >= 3:
            i = j-1
            print('i is :' + str(i))
            break

        ans = max(ans, weight)

    # If we go to the last block, then stop
    else:
        break

print(ans)