def subsets( X ):
    sets = []
    len_X = len( X )
    for i in range( 1 << len_X ):
        subset = [ X[ bit ] for bit in range( len_X ) if i & ( 1 << bit ) ]
        sets.append( subset )
    return sets
    
X = [ 'A', 'B', 'C', 'D' ] 
for m in subsets( X ):
    print( m )