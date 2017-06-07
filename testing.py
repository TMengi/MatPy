import matpy as M
import copy

# test all the shit
v1 = M.Vector([3,6,1])
v1_row = M.Vector([3,6,1], 'row')
v2 = M.Vector([2,8,2])
v2_row = M.Vector([2,8,2], 'row')
v3 = M.Vector([4,0,1])
v3_row = M.Vector([4,0,1], 'row')

s1 = M.Set([v1, v2, v3])
s1_row = M.Set([v1_row, v2_row, v3_row])
s1_m = M.Set([v1, v2_row, v3])

A = M.Matrix([[1,2,3],[6,5,2],[9,0,2]])
A_col = M.Matrix([[1,2,3],[6,5,2],[9,0,2]], 'col')
A_alt = M.Matrix([[1,6,9],[2,5,0],[3,2,2]], 'col')
B = M.Matrix([[1,2,3],[6,5,2],[9,0,2],[6,2,3]])
B_col = M.Matrix([[1,2,3],[6,5,2],[9,0,2],[6,2,3]], 'col')
C = M.Matrix([[4,7,2],[0,7,4],[1,7,8]])
C_col = M.Matrix([[4,7,2],[0,7,4],[1,7,8]], 'col')

probs = []

'''begin Vector tests'''
def vecSlicing():
    if v1[0] != 3:
        probs.append('col vector slicing')
    if v1_row[0] != 3:
        probs.append('row vector slicing')

def vecLength():
    if len(v1) != 3:
        probs.append('col vector slicing')
    if len(v1_row) != 3:
        probs.append('row vector slicing')

def vecIterate():
    for x,y in enumerate(v1):
        if y != v1[x]:
            probs.append('col vector iteration')
    for x,y in enumerate(v1_row):
        if y != v1_row[x]:
            probs.append('row vector iteration')

def vecEquivalence():
    if v1 != v1_row:
        probs.append('cross orientation vector equivalence')

def vecAddition():
    if (v1 + v1) != M.Vector([6,12,2]):
        probs.append('row vector addition values')
    if (v1_row + v1_row) != M.Vector([6,12,2]):
        probs.append('col vector addition values')
    if (v1 + v1).orientation != 'col':
        probs.append('col vector addition orientation not retained')
    if (v1_row + v1_row).orientation != 'row':
        probs.append('row vector addition orientation not retained')
    if (v1_row + v1).orientation != v1_row.orientation:
        probs.append('cross orientation vector addition orientation not retained')

def vecSubtraction():
    if (v1 - v2) != M.Vector([1,-2,-1]):
        probs.append('row vector subtraction values')
    if (v1_row - v2_row) != M.Vector([1,-2,-1]):
        probs.append('col vector subtraction values')
    if (v1 - v2).orientation != 'col':
        probs.append('col vector subtraction orientation not retained')
    if (v1_row - v2_row).orientation != 'row':
        probs.append('row vector subtraction orientation not retained')
    if (v1_row - v2).orientation != v1_row.orientation:
        probs.append('cross orientation vector subtraction orientation not retained')

def vecScalarMul():
    if v1 * 5 != M.Vector([15,30,5]):
        probs.append("col vector scalar multiplication values")
    if (v1 * 5).orientation != v1.orientation:
        probs.append("col vector scalar multiplication orientation not preserved")
    if v1_row * 5 != M.Vector([15,30,5]):
        probs.append("row vector scalar multiplication values")
    if (v1_row * 5).orientation != v1_row.orientation:
        probs.append("row vector scalar multiplication orientation not preserved")

def vecDot():
    if (v1 * v1) != v1.magnitude**2:
        probs.append('col vector dot product values')
    if (v1 * v1_row) != v1.magnitude**2:
        probs.append('cross orientation vector dot product values')
    if (v1_row * v1_row) != v1.magnitude**2:
        probs.append('row vector dot product values')

def vecCross():
    if v1.cross(v2) != M.Vector([4,-4,12]):
        probs.append('col vector cross product values')
    if v1.cross(v2_row) != M.Vector([4,-4,12]):
        probs.append('cross orientation vector cross product values')
    if v1_row.cross(v2_row) != M.Vector([4,-4,12]):
        probs.append('row vector cross product values')
    if v2.cross(v1) != v1.cross(v2) * -1:
        probs.append('cross product order inversion not changing sign')
    if v1.cross(v2) * v1 != 0 or v1.cross(v2) * v2 != 0:
        probs.append('cross product not perpendicular to multiplied vectors')

def vecUnit():
    if v1.isUnit():
        probs.append('col vector isUnit')
    if v1_row.isUnit():
        probs.append('row vector isUnit')
    if not M.Vector([.5,.5,.5,.5]).isUnit():
        probs.append('R4 col unit not isUnit')
    if not M.Vector([.5,.5,.5,.5], 'col').isUnit():
        probs.append('R4 row unit not isUnit')

def vecNormalize():
    if v1.normalize() != M.Vector([3/(46)**.5,6/(46)**.5,1/(46)**.5]):
        probs.append('normalize col vector')
    if v1_row.normalize() != M.Vector([3/(46)**.5,6/(46)**.5,1/(46)**.5]):
        probs.append('normalize row vector')

def vecExtend():
    if v1.extend([5]) != M.Vector([3,6,1,5]):
        probs.append('col vector extend')
    if v1_row.extend([5]) != M.Vector([3,6,1,5]):
        probs.append('row vector extend')

def vecGet():
    if v1[0] != 3 or v1[1] != 6 or v1[2] != 1:
        probs.append('col vector getitem')
    if v1_row[0] != 3 or v1_row[1] != 6 or v1_row[2] != 1:
        probs.append('row vector getitem')

def vecSet():
    v1_cop = copy.deepcopy(v1)
    v1_row_cop = copy.deepcopy(v1_row)
    v1_cop[2] = 5
    v1_row_cop[2] = 5
    if v1_cop[2] != 5:
        probs.append('col vector setitem')
    if v1_row_cop[2] != 5:
        probs.append('row vector setitem')

def vecDel():
    v1_cop = copy.deepcopy(v1)
    v1_row_cop = copy.deepcopy(v1_row)

    del v1_cop[0]
    if v1_cop[0] != 6:
        probs.append('col vector delitem')
    del v1_cop[0]
    if v1_cop[0] != 1:
        probs.append('col vector delitem')

    del v1_row_cop[0]
    if v1_row_cop[0] != 6:
        probs.append('row vector delitem')
    del v1_row_cop[0]
    if v1_row_cop[0] != 1:
        probs.append('row vector delitem')

'''begin Set tests'''
def setLength(): # empty
    if len(s1) != 3:
        probs.append('len of col set')
    if len(s1_row) != 3:
        probs.append('len of row set')
    if len(s1_m) != 3:
        probs.append('len of mixed set')

def setIterate(): # empty
    pass

def setEquivalence(): # empty
    pass

def setGet(): # empty
    pass

def setSet(): # empty
    pass

def setDel(): # empty
    pass

def setIsIndependent(): # empty
    pass

def setMakeIndpendent(): # empty
    pass

'''begin Matrix tests'''
def matSlicing():
    if A[0] != M.Vector([1,2,3], 'row'):
        probs.append('row matrix slicing')
    if A_col[0] != M.Vector([1,2,3]):
        probs.append('col matrix slicing')

def matDimensions():
    if B.dimensions != (4,3):
        probs.append('row matrix dimensions')
    if B_col.dimensions != (3,4):
        probs.append('col matrix dimensions')

def matLength():
    if len(B) != 4:
        probs.append('row matrix length')
    if len(B_col) != 4:
        probs.append('col matrix length')

def matIterate():
    for x,y in enumerate(A):
        if y != A[x]:
            probs.append('row matrix iteration')
    for x,y in enumerate(A_col):
        if y != A_col[x]:
            probs.append('col matrix iteration')

def matEquivalence():
    if A != A_alt:
        probs.append("cross orientation matrix equivalence")

def matAddition():
    if A+B != 'cannot add, matrices not same size':
        probs.append('matrix addition size error not thrown')
    if (A+A).orientation != 'row':
        probs.append('row matrix addition orientation not preserved')
    if (A_col+A_col).orientation != 'col':
        probs.append('col matrix addition orientation not preserved')
    if (A+A_col).orientation != 'row':
        probs.append('cross orientation (r+c) matrix addition orientation not preserved')
    if (A_col+A).orientation != 'col':
        probs.append('cross orientation (c+r) matrix addition orientation not preserved')
    if A+A != M.Matrix([[2,4,6],[12,10,4],[18,0,4]]):
        probs.append('row matrix addition values')
    if A_col+A_col != M.Matrix([[2,4,6],[12,10,4],[18,0,4]], 'col'):
        probs.append('col matrix addition values')
    if A+C_col != M.Matrix([[5,2,4],[13,12,9],[11,4,10]]):
        probs.append('cross orientation matrix addition values')

def matSubtraction():
    if A-B != 'cannot subtract, matrices not same size':
        probs.append('addition size error not thrown')
    if C-A != M.Matrix([[3,5,-1],[-6,2,2],[-8,7,6]]):
        probs.append('row matrix subtraction values')
    if C_col-A_col != M.Matrix([[3,-6,-8],[5,2,7],[-1,2,6]]):
        probs.append('col matrix subtraction values')
    if A-C_col != M.Matrix([[-3,2,2],[-1,-2,-5],[7,-4,-6]]):
        probs.append('cross orientation matrix subtraction values')

def matMultiplication():
    # orientation tests
    if (A * 5).orientation != A.orientation:
        probs.append('row matrix scalar multiplication orientation not preserved')
    if (A_col * 5).orientation != A_col.orientation:
        probs.append('col matrix scalar multiplication orientation not preserved')
    if (A * A).orientation != 'row':
        probs.append('row matrix multiplication orientation not preserved')
    if (A_col * A_col).orientation != 'col':
        probs.append('col matrix multiplication orientation not preserved')
    if (A * A_col).orientation != 'row':
        probs.append('cross orientation (r*c) matrix multiplication orientation not preserved')
    if (A_col * A).orientation != 'col':
        probs.append('cross orientation (c*r) matrix multiplication orientation not preserved')
    if (A * v1).orientation != 'col':
        probs.append('matrix vector (r*c) orientation incorrect')
    if (A * v1_row).orientation != 'row':
        probs.append('matrix vector (r*r) orientation incorrect')
    if (A_col * v1).orientation != 'col':
        probs.append('matrix vector (c*c) orientation incorrect')
    if (A_col * v1_row).orientation != 'row':
        probs.append('matrix vector (c*r) orientation incorrect')
    # value tests
    if (A*5) != M.Matrix([[5,10,15],[30,25,10],[45,0,10]]):
        probs.append('row matrix scalar multiplication values')
    if (A_col*5) != M.Matrix([[5,30,45],[10,25,0],[15,10,10]]):
        probs.append('col matrix scalar multiplication values')
    if (A*A) != M.Matrix([[40,12,13],[54,37,32],[27,18,31]]):
        probs.append('row matrix multiplication values')
    if (A_col*A_col) != M.Matrix([[40,12,13],[54,37,32],[27,18,31]], 'col'):
        probs.append('col matrix multiplication values')
    if (A*C_col) != M.Matrix([[24,26,39],[63,43,57],[40,8,25]]):
        probs.append('cross orientation (r*c) matrix multiplication values')
    if (C_col*A) != M.Matrix([[13,8,14],[112,49,49],[98,24,30]]):
        probs.append('cross orientation (c*r) matrix multiplication values')
    if (A*v1) != M.Vector([18,50,29]):
        probs.append('row matrix * col vector values')
    if (A*v1_row) != M.Vector([18,50,29]):
        probs.append('row matrix * row vector values')
    if (A_col*v1) != M.Vector([48,36,23]):
        probs.append('col matrix * col vector values')
    if (A_col*v1_row) != M.Vector([48,36,23]):
        probs.append('col matrix * row vector values')

def matGet():
    if A[0] != M.Vector([1,2,3]) or A[1] != M.Vector([6,5,2]) or A[2] != M.Vector([9,0,2]):
        probs.append('row matrix getitem')
    if A_col[0] != M.Vector([1,2,3]) or A_col[1] != M.Vector([6,5,2]) or A_col[2] != M.Vector([9,0,2]):
        probs.append('col matrix getitem')

def matSet():
    A_cop = copy.deepcopy(A)
    A_col_cop = copy.deepcopy(A_col)
    A_cop[2] = M.Vector([0,-1,8])
    A_col_cop[2] = M.Vector([0,-1,8])
    if A_cop[2] != M.Vector([0,-1,8]):
        probs.append('row matrix setitem')
    if A_col_cop[2] != M.Vector([0,-1,8]):
        probs.append('col matrix setitem')

def matDel():
    A_cop = copy.deepcopy(A)
    A_col_cop = copy.deepcopy(A_col)
    del A_cop[0]
    if A_cop[0] != M.Vector([6,5,2]):
        probs.append('row matrix delitem')
    del A_cop[0]
    if A_cop[0] != M.Vector([9,0,2]):
        probs.append('row matrix delitem')

    del A_col_cop[0]
    if A_col_cop[0] != M.Vector([6,5,2]):
        probs.append('col matrix delitem')
    del A_col_cop[0]
    if A_col_cop[0] != M.Vector([9,0,2]):
        probs.append('col matrix delitem')

def matIsSquare():
    pass

def matCheckLead():
    pass

def matSwapRows(): # empty
    pass

def matIsRREF(): # empty
    pass

def matRREF(): # empty
    pass

def matElimNegs(): # empty
    pass

def matCheckPivots(): # empty
    pass

def matCountSolutions(): # empty
    pass

def matTranspose(): # empty
    pass

def matIsOrthogonal(): # empty
    pass

def matIsSymmetric(): # empty
    pass

def matisInvertible(): # empty
    pass

def matInverse(): # empty
    pass

def matExtend(): # empty
    pass

def matPop(): # empty
    pass

def matImage(): # empty
    pass



tests = [
vecSlicing(),
vecLength(),
vecIterate(),
vecEquivalence(),
vecAddition(),
vecSubtraction(),
vecScalarMul(),
vecDot(),
vecCross(),
vecUnit(),
vecNormalize(),
vecExtend(),
vecGet(),
vecSet(),
vecDel(),
# all vector tests have been completed and included
setLength(),
setIterate(),
setEquivalence(),
setGet(),
setSet(),
setDel(),
setIsIndependent(),
setMakeIndpendent(),
# all Set tests have been included
matSlicing(),
matDimensions(),
matLength(),
matIterate(),
matEquivalence(),
matAddition(),
matSubtraction(),
matMultiplication(),
matGet(),
matSet(),
matDel(),
matSwapRows(),
matIsRREF(),
matRREF(),
matElimNegs(),
matCheckPivots(),
matCountSolutions(),
matTranspose(),
matIsOrthogonal(),
matIsSymmetric(),
matisInvertible(),
matInverse(),
matExtend(),
matPop(),
matImage(),
# all Matrix tests have been included
]

if __name__ == '__main__':
    print ("Problems:")
    for test in tests:
        test
    for prob in probs:
        print (prob)
