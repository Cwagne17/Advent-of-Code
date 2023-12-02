import numpy

forest = []
with open('input.txt') as fin:
    for ln in [ln.replace('\n', '') for ln in fin.readlines()]:
        forest.append([char for char in ln])
    
    visible_total = (len(forest) + (len(forest[0]) - 2)) * 2 # (left edge + top edge - corners) * 2
    scenic_values = []

    for i in range(1, len(forest) - 1): # second row till second to last row
        row = forest[i]
        
        ## Part 1: Check if the trees are visible
        for j in range(1, len(row) - 1): # second column till second to last column
            current = int(forest[i][j])
                        
            # check from top
            # iter from top row edge in column j until row above current tree
            if all(int(current) > int(forest[k][j]) for k in range(0, i)):
                visible_total += 1
                continue
                
            # check from right
            # iter from right column edge in row i until column right of current tree
            if all(int(current) > int(forest[i][k]) for k in range(j+1, len(row))):
                visible_total += 1
                continue
                
            # check from bottom
            # iter from bottom row edge in column j until row below current tree
            if all(int(current) > int(forest[k][j]) for k in range(i+1, len(forest))):
                visible_total += 1
                continue
                
            # check from left
            # iter from left column edge in row j until column left of current tree
            if all(int(current) > int(forest[i][k]) for k in range(0, j)):
                visible_total += 1
                continue

        ## Part 2: Calculate Scenic score
        for j in range(1, len(row) - 1): # second column till second to last column
            current = int(forest[i][j])
            
            viewing_distance = []
            
            # check from top
            # iter from row above current tree in column j until top row edge
            for k in range(i-1, -1, -1):
                if int(current) <= int(forest[k][j]) or k == 0:
                    viewing_distance.append(i-k) # current row index - furthest row index
                    break
                
            # check from right
            # iter from column right of current tree in row i until right column edge 
            for k in range(j+1, len(row)):
                if int(current) <= int(forest[i][k]) or k == len(row) - 1:
                    viewing_distance.append(k-j) # furthest column index - current column index
                    break
            
            # check from bottom
            # iter from row below current tree in column j until bottom row edge 
            for k in range(i+1, len(forest)):
                if int(current) <= int(forest[k][j]) or k == len(forest) - 1:
                    viewing_distance.append(k-i) # furthest row index - current row index
                    break
                
            # check from left
            # iter from column left of current tree in row j until left column edge
            for k in range(j-1, -1, -1):
                if int(current) <= int(forest[i][k]) or k == 0:
                    viewing_distance.append(j-k) # current column index - furthest column index
                    break
            
            scenic_value = numpy.prod(viewing_distance)
            scenic_values.append(scenic_value)
    
    print(visible_total)
    print(max(scenic_values))
    