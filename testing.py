# test all the shit
A = Matrix([[1,2,3],[6,5,2],[9,0,2]])
A_col = Matrix([[1,2,3],[6,5,2],[9,0,2]], 'col')
B = Matrix([[1,2,3],[6,5,2],[9,0,2],[6,2,3]])
B_col = Matrix([[1,2,3],[6,5,2],[9,0,2],[6,2,3]], 'col')
C = Matrix([[4,7,2],[0,7,4],[1,7,8]])
C_col = Matrix([[4,7,2],[0,7,4],[1,7,8]], 'col')
v1 = Vector([3,6,1])
v1_row = Vector([3,6,1], 'row')
v2 = Vector([2,8,2])
v2_row = Vector([2,8,2], 'row')

'''begin Vector tests'''
def vecSlicing():
    probs = []
    if v1[0] != 3:
        probs.append('col vector slicing')
    if v1_row[0] != 3:
        probs.append('row vector slicing')
    return probs

def vecLength():
    probs = []
    if len(v1) != 3:
        probs.append('col vector slicing')
    if len(v1_row) != 3:
        probs.append('row vector slicing')
    return probs

def vecIterate():
    probs = []
    for x,y in enumerate(v1):
        if y != v1[x]:
            probs.append('col vector iteration')
    for x,y in enumerate(v1_row):
        if y != v1_row[x]:
            probs.append('row vector iteration')
    return probs

def vecEquivalence():
    probs = []
    if v1 != v1_row:
        probs.append('cross orientation vector equivalence')
    return probs

def vecAddition():
    probs = []
    if (v1 + v1) != Vector([6,12,2]):
        probs.append('row vector addition values')
    if (v1_row + v1_row) != Vector([6,12,2]):
        probs.append('col vector addition values')
    if (v1 + v1).orientation != 'col':
        probs.append('col vector addition orientation not retained')
    if (v1_row + v1_row).orientation != 'row':
        probs.append('row vector addition orientation not retained')
    if (v1_row + v1).orientation != 'row':
        probs.append('cross orientation vector addition orientation not row')
    return probs

def vecSubtraction():
    probs = []
    if (v1 - v2) != Vector([1,-2,-1]):
        probs.append('row vector subtraction values')
    if (v1_row - v2_row) != Vector([1,-2,-1]):
        probs.append('col vector subtraction values')
    if (v1 - v2).orientation != 'col':
        probs.append('col vector subtraction orientation not retained')
    if (v1_row - v2_row).orientation != 'row':
        probs.append('row vector subtraction orientation not retained')
    if (v1_row - v2).orientation != 'row':
        probs.append('cross orientation vector subtraction orientation not row')
    return probs

def vecDot():
    probs = []
    if (v1 * v1) != v1.magnitude:
        probs.append('col vector dot product values')
    if (v1 * v1_row) != v1.magnitude:
        probs.append('cross orientation vector dot product values')
    if (v1_row * v1_row) != v1.magnitude:
        probs.append('row vector dot product values')
    return probs

def vecCross():
    probs = []
    if v1.cross(v2) != Vector([4,-4,12]):
        probs.append('col vector cross product values')
    if v1.cross(v2_row) != Vector([4,-4,12]):
        probs.append('cross orientation vector cross product values')
    if v1_row.cross(v2_row) != Vector([4,-4,12]):
        probs.append('row vector cross product values')
    if v2.cross(v1) != v1.cross(v2) * -1:
        probs.append('cross product order inversion not changing sign')
    if v1.cross(v2) * v1 != 0 or v1.cross(v2) * v2 != 0:
        probs.append('cross product not perpendicular to multiplied vectors')
    return probs

def vecUnit():
    probs = []
    if v1.isUnit():
        probs.append('col vector isUnit')
    if v1_row.isUnit():
        probs.append('row vector isUnit')
    if not Vector([.5,.5,.5,.5]).isUnit():
        probs.append('R4 col unit not isUnit')
    if not Vector([.5,.5,.5,.5], 'col').isUnit():
        probs.append('R4 row unit not isUnit')
    return probs

def vecNormalize():
    probs = []
    if v1.normalize() != Vector([3/46,6/46,1/46]):
        probs.append('normalize col vector')
    if v1_row.normalize() != Vector([3/46,6/46,1/46]):
        probs.append('normalize row vector')
    return probs

def vecExtend():
    probs = []
    if v1.extend([5]) != Vector([3,6,1,5]):
        probs.append('col vector extend')
    if v1_row.extend([5]) != Vector([3,6,1,5]):
        probs.append('row vector extend')
    return probs

'''begin Matrix tests'''
def matSlicing():
    probs = []
    if A[0] != Vector([1,2,3], 'row'):
        probs.append('row matrix slicing')
    if A_col[0] != Vector([1,2,3]):
        probs.append('col matrix slicing')
    return probs

def matDimensions():
    probs = []
    if B.dimensions != (4,3):
        probs.append('row matrix dimensions')
    if B_col.dimensions != (3,4):
        probs.append('col matrix dimensions')
    return probs

def matLength():
    probs = []
    if len(B) != 4:
        probs.append('row matrix length')
    if len(B_col) != 3:
        probs.append('col matrix length')
    return probs

def matIterate():
    probs = []
    for x,y in enumerate(A):
        if y != A[x]:
            probs.append('row matrix iteration')
    for x,y in enumerate(A_col):
        if y != A_col[x]:
            probs.append('col matrix iteration')
    return probs

def matEquivalence():
    probs = []
    if A.transpose() != A_col:
        probs.append('not equating row version with col version')
    return probs

def matAddition():
    probs = []
    if A+B != 'cannot add, matrices not same size':
        probs.append('matrix addition size error not thrown')
    if (A+A).orientation != 'row':
        probs.append('row matrix addition orientation not preserved')
    if (A_col+A_col).orientation != 'col':
        probs.append('col matrix addition orientation not preserved')
    if (A+A_col).orientation != 'row':
        probs.append('cross orientation matrix addition orientation not row')
    if A+A != Matrix([[2,4,6],[12,10,4],[18,0,4]]):
        probs.append('row matrix addition values')
    if A_col+A_col != Matrix([[2,4,6],[12,10,4],[18,0,4]], 'col'):
        probs.append('col matrix addition values')
    if A+C_col != Matrix([[5,2,4],[13,12,9],[11,4,10]]):
        probs.append('cross orientation matrix addition values')
    return probs

def matSubtraction():
    probs = []
    if A-B != 'cannot subtract, matrices not same size':
        probs.append('addition size error not thrown')
    if C-A != Matrix([[3,5,-1],[-6,2,2],[-8,7,6]]):
        probs.append('row matrix subtraction values')
    if C_col-A_col != Matrix([[3,-6,-8],[5,2,7],[-1,2,6]]):
        probs.append('col matrix subtraction values')
    if A-C_col != Matrix([[-3,2,2],[-1,-2,-5],[7,-4,-6]]):
        probs.append('cross orientation matrix subtraction values')
    return probs

def matMultiplication():
    probs = []
    if (A * 5).orientation != A.orientation:
        probs.append('row matrix scalar multiplication orientation not preserved')
    if (A_col * 5).orientation != A_col.orientation:
        probs.append('col matrix scalar multiplication orientation not preserved')
    if (A * A).orientation != 'row':
        probs.append('row matrix multiplication orientation not row')
    if (A_col * A_col).orientation != 'col':
        probs.append('col matrix multiplication orientation not col')
    if (A * A_col). orientation != 'row':
        probs.append('cross orientation matrix multiplication orientation not row')
    if (A*5) != Matrix([[5,10,15],[30,25,10],[45,0,10]]):
        probs.append('row matrix scalar multiplication values')
    if (A_col*5) != Matrix([[5,30,45],[10,25,0],[15,10,10]]):
        probs.append('col matrix scalar multiplication values')
    if (A*A) != Matrix([[40,12,13],[54,37,32],[27,18,31]]):
        probs.append('row matrix multiplication values')
    if (A_col*A_col) != Matrix([[40,12,13],[54,37,32],[27,18,31]], 'col'):
        probs.append('col matrix multiplication values')
    if (A*C_col) != Matrix([[24,26,39],[63,43,57],[40,8,25]]):
        probs.append('cross orientation matrix multiplication values')
    if (A*v1) != Vector([18,50,29]):
        probs.append('row matrix * col vector values')
    if (A*v1_row) != Vector([18,50,29]):
        probs.append('row matrix * row vector values')
    if (A_col*v1) != Vector([48,36,23]):
        probs.append('col matrix * col vector values')
    if (A_col*v1_row) != Vector([48,36,23]):
        probs.append('col matrix * row vector values')
    return probs

tests = [
vecSlicing(),
vecLength(),
vecIterate(),
vecEquivalence(),
vecAddition(),
vecSubtraction(),
vecDot(),
vecCross(),
vecUnit(),
vecNormalize(),
vecExtend(),
matSlicing(),
matDimensions(),
matLength(),
matIterate(),
matEquivalence(),
matAddition(),
matSubtraction(),
matMultiplication(),
]

if __name__ == '__main__':
    print ("Problems:")
    for test in tests:
        if test != []:
            for x in test:
                print (x)
