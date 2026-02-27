"""list of list"""
l1=[1,2,3]
l2=[10,11,12]
l3=[20,22,24]
# other languages me 2d array inplement krte hai yaha use list se kr skte hai

l4=[[32,22,4],[54,55,62],[7,12,43,21]] #list of list
print(l4)
print(l4[1])
print(l4[1][1])

# using range +list can slove 2d array type problems
l4=[[32,22,4],[54,55,62],[7,12,43]]
for i in range(0,3,1):
    for j in range(0,3,1):
        print(l4[i][j],end=' ')
    print()