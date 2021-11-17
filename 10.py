def subsets( A ):
    sets = []
    len_A = len( A )
    for i in range( 1 << len_A ):
        subset = [ A[ bit ] for bit in range( len_A ) if i & ( 1 << bit ) ]
        sets.append( subset )
    return sets
    
A = [ 1, 2, 3, 4 ] 
for m in subsets( A ):
    print( m )