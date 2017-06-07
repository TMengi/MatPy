import copy

def buildVector():
    # ask for dimensions and orientation
    orientation = ''
    m = int(input("how many components? "))
    # ensure a valid orientation
    while not orientation == 'row' and not orientation == 'col':
        orientation = input('row or col vector? ')

    user_vector = []

    # ask for values until get a list of the correct length
    while len(user_vector) != m:
        user_vector = input("enter values separated by spaces: ").split(' ')

    return Vector([int(x) for x in user_vector], orientation)

def buildZeroVec(size):
    return Vector([0 for x in range(size)])

class Vector:
    def __init__(self, vector, orientation='col'):
        # checks for valid orientation
        if not orientation == 'row' and not orientation == 'col':
            raise Exception('orientation must be either "row" or "col"')

        if isinstance(vector, Vector):
            vector = list(vector)

        #checks that all values are numbers
        for n in vector:
            if not isinstance(n, int) and not isinstance(n, float):
                raise Exception('vector invalid, Args passed contains a non number')

        self.vector = vector
        self.dimension = len(vector)
        self.magnitude = sum(x**2 for x in self)**0.5
        self.orientation = orientation

    # adds vectors by adding corresponding values. returns another vector with same orientation as self
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ('cannot add number to vector')
        elif isinstance(other, Vector):
            if self.dimension == other.dimension:
                return Vector([self[index] + other.vector[index] for index, value in enumerate(self)], self.orientation)
            else:
                return ('cannot add, vectors not in same dimension')
        else:
            return ('cannot add, unexpected object')

    # subtracts vectors by subtracting corresponding values. returns another vector with same orientation as self
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ('cannot subtract number from vector')
        elif isinstance(other, Vector):
            if self.dimension == other.dimension:
                return Vector([self[index] - other.vector[index] for index, value in enumerate(self)], self.orientation)
            else:
                return ('cannot add, vectors not in same dimension')
        else:
            return None

    # normal multiplication for scalars (returns a vector). dot product for vectors (returns a number). got lazy for matrices and just reversed the order so it would redirect to Matrix.__mul__
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector([value * other for value in self], self.orientation)
        elif isinstance(other, Vector):
            return self.dot(other)
        elif isinstance(other, Matrix):
            return ('cannot multiply Vector by Matrix, only Matrix by Vector')
        else:
            return None

    # returns the dimension of the vector, not its length because __len__ must return an int
    def __len__(self):
        return self.dimension

    def __iter__(self):
        return (x for x in self.vector)

    # calls printVec
    def __str__(self):
        return str(self.printVec())

    def __repr__(self):
        return ("{} dimensional Vector object with values {}".format(len(self), self.vector))

    def __eq__(self, other):
        # reinitialize objects so that they have the same orientation for comparison
        return Vector(self).__dict__ == Vector(other).__dict__

    def __getitem__(self, index):
        return self.vector[index]

    def __delitem__(self, index):
        del self.vector[index]

    def __setitem__(self, index, value):
        if isinstance(value, int) or isinstance(value, float):
            self.vector[index] = value
        else:
            return None

    # dot product of self with other
    def dot(self, other):
        return sum(self_value * other.vector[index] for index, self_value in enumerate(self))

    # cross product of solf with other. requires three dimensional vectors
    def cross(self, other):
        if len(self) == 3 and len(other) == 3:
            return Vector([self[1]*other.vector[2]-self[2]*other.vector[1], self[2]*other.vector[0]-self[0]*other.vector[2], self[0]*other.vector[1]-self[1]*other.vector[0]])
        else:
            return ("cannot cross, vectors must be three dimensional")

    def printVec(self):
        if self.orientation == 'col':
            for comp_num, value in enumerate(self):
                print ('|', end='')
                if isinstance(value, int):
                    print ('%i|' % value)
                elif isinstance(value, float):
                    if value.is_integer():
                        print ('%i|' % int(value))
                    else:
                        print ('%.2f|' % value)
            return ('')
        if self.orientation == 'row':
            print ('|', end='')
            for value in self:
                if isinstance(value, int):
                    print ('%i ' % value, end='')
                elif isinstance(value, float):
                    if value.is_integer():
                        print ('%i ' % int(value), end='')
                    else:
                        print ('%.2f ' % value, end='')
            print ('\b|')
            return ('')

    # just looks at magnitude and decides if a unit vector or not
    def isUnit(self):
        if self.magnitude == 1.0:
            return True
        else:
            return False

    # divides a vector by its magnitude
    def normalize(self):
        return self * (1/self.magnitude)

    # extends a vector by tacking a numbers(s) onto the end
    def extend(self, other):
        new = copy.deepcopy(self.vector)
        if not isinstance(other, int) and not isinstance(other, list) and not isinstance(other, Vector):
            return ('invalid input, cannot extend vector')
        if isinstance(other, int):
            other = [other]
        if isinstance(other, Vector):
            other = other.vector
        new.extend(other)
        return Vector(new)

def leastSquaresSol(A, b):
    sol = (A.transpose() * A).extend(A.transpose() * b).rref().transpose().pop()
    sol.orientation = 'col'
    return sol

class Set:
    def __init__(self, set_vectors):
        if not isinstance(set_vectors, list):
            raise Exception('Set can only be created from a list')

        for vector in set_vectors:
            if len(vector) != len(set_vectors[0]):
                raise Exception('Set invalid, check vector dimensions')
            if isinstance(vector, list):
                vector = Vector(vector)
            if not isinstance(vector, Vector):
                raise Exception('set invalid, Args passed canont be turned into a Vector')
        else:
            self.set_vectors = set_vectors
            self.dimension = len(set_vectors[0])

    # length of set is the number of vectors in the set
    def __len__(self):
        return len(self.set_vectors)

    def __iter__(self):
        return (x for x in self.set_vectors)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # calls printSet
    def __str__(self):
        return self.printSet()

    def __repr__(self):
        return ("Set object containg {} vectors: {}".format(len(self), self.set_vectors))

    def __getitem__(self, index):
        return self.set_vectors[index]

    def __delitem__(self, index):
        del self.set_vectors[index]

    # always prints as columns just for readability
    def printSet(self):
        for comp_num, value in enumerate(self[0]):
            print ("{", end='')
            for vec_num, vector in enumerate(self):
                if isinstance(vector[comp_num], float):
                    if vector[comp_num].is_integer():
                        print ("|%i|" % int(vector[comp_num]), end = ' ')
                    else:
                        print ("|%.2f|" % vector[comp_num], end = ' ')
                if isinstance(vector[comp_num], int):
                    print ("|%i|" % vector[comp_num], end = ' ')
            print ("\b}")
        return ('')

    # creates a Matrix where each of the set vectors is a row and then computes rref. if every column is a pivot, the set is linearly independent
    def isIndependent(self):
        return Matrix([vector for vector in self], 'col').rref().checkPivots()['rank'] == len(self)

    # removes nontrivial dependence relations from a set by taking a subset of only those vectors which become pivot columns in rref
    def makeIndependent(self):
        if not self.isIndependent():
            return Set([self[index] for index in (column for column in Matrix([vector for vector in self], 'col').rref().checkPivots()['columns'])])
        else:
            return self

# lets the user create a matrix by specifying dimensions and an orientation then calling inputData
def buildMatrix():
    # ask for dimensions and orientation
    orientation = ''
    n = int(input("how many rows? "))
    m = int(input("how many columns? "))
    # ensure a valid orientation
    while not orientation == 'row' and not orientation == 'col':
        orientation = input('enter row or col vectors? ')

    # call inputData() and let the user enter rows in the preferred orientation
    if orientation == 'row':
        return Matrix(inputData(n, m), orientation)
    elif orientation == 'col':
        return Matrix(inputData(m, n), orientation)

# asks for input vectors in given orientation
def inputData(major, minor):
    # initialize an empty matrix to be filled by user input
    user_matrix = []
    while len(user_matrix) < major:
        vector_nums = [float(x) for x in input('enter vector values separated by spaces: ').split(' ')]
        # if row is valid, add it to the matrix
        if len(vector_nums) == minor:
            user_matrix.append(Vector(vector_nums))
        # if not, don't add it
        else:
            print ("incorrect vector length, should be %i numbers" % minor)

    return user_matrix

# builds the identity matrix for any given size. note the identity is a square matrix by definition
def buildIdentityMat(size):
    # initialize an empty matrix
    identity = []

    # for each row up to the correct size, add a new list in the matrix and iterate over the columns
    for i in range(size):
        identity.append([])
        # for each column, if the row number equals the column number, place a one. if not, place a zero
        for j in range(size):
            if i == j:
                identity[i].append(1.)
            else:
                identity[i].append(0.)

    return Matrix(identity)

# Matrix object can be passed vectors or lists as either rows or cols. default is rows
class Matrix:
    def __init__(self, matrix, orientation='row'):
        # checks for valid orientation
        if not orientation == 'row' and not orientation == 'col':
            raise Exception('orientation must be either "row" or "col"')

        if isinstance(matrix, Matrix):
            matrix = matrix.matrix

        # if an incoming piece of data is not a vector, turn it into one if possible
        for data_num, data in enumerate(matrix):
            if isinstance(data, list):
                matrix[data_num] = Vector(data)
            if isinstance(data, int) or isinstance(data, float):
                matrix[data_num] = Vector([data])
            if not isinstance(matrix[data_num], Vector):
                raise Exception("Matrix invalid, args passed can't be turned into vector")

        for vector in matrix:
            vector.orientation = orientation

        # checks that the incoming vectors are all the same length
        for vector in matrix:
            if len(vector) != len(matrix[0]):
                raise Exception('Matrix invalid, check lengths')

        self.matrix = matrix
        self.orientation = orientation
        if self.orientation == 'row':
            self.number_of_rows = len(self.matrix)
            self.number_of_cols = len(self.matrix[0])
        elif self.orientation == 'col':
            self.number_of_rows = len(self.matrix[0])
            self.number_of_cols = len(self.matrix)
        self.dimensions = (self.number_of_rows, self.number_of_cols)

    # returns the number of vectors in a matrix
    def __len__(self):
        if self.orientation == 'row':
            return self.number_of_rows
        else:
            return self.number_of_cols

    # returns consecutive vectors in the matrix
    def __iter__(self):
        return (x for x in self.matrix)

    def __repr__(self):
        return ("{}x{} Matrix object with {}s {}".format(self.number_of_rows, self.number_of_cols, self.orientation, self.matrix))

    # calls printMat
    def __str__(self):
        return str(self.printMat())

    def __eq__(self, other):
        # reinitialize objects so that they have the same orientation for comparison
        return self.makeOrientationRow().__dict__ == other.makeOrientationRow().__dict__

    # returns the vector at the specified index, meaning that it selects in orientaiton specified manner: row number for row matrix or col number for col matrix
    def __getitem__(self, index):
        return self.matrix[index]

    # checks for correct length then sets the value at the specified index
    def __setitem__(self, index, value):
        if not len(value) == len(self[0]):
            return ('invalid, check value dimension')
        if isinstance(value, Vector):
            value.orientation = self.orientation
            self.matrix[index] = value
        elif isinstance(value, list):
            self.matrix[index] = Vector(value, self.orientation)
        else:
            return ('invalid, value passed is not a list or Vector')

    # deletes the vector at the specified index and reassigns dimension values
    def __delitem__(self, index):
        del self.matrix[index]
        if self.orientation == 'row':
            self.number_of_rows = len(self.matrix)
            self.number_of_cols = len(self.matrix[0])
        elif self.orientation == 'col':
            self.number_of_rows = len(self.matrix[0])
            self.number_of_cols = len(self.matrix)
        self.dimensions = (self.number_of_rows, self.number_of_cols)

    # adds matrices by adding corresponding rows as vectors. returns a matrix with same orientation as self
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ('cannot add number to matrix')
        if isinstance(other, Vector):
            return ('cannot add Vector to matrix')
        elif isinstance(other, Matrix):
            if self.dimensions == other.dimensions:
                # need a specific case for cross orientation
                if self.orientation != other.orientation:
                    return Matrix([vec + other.makeOrientationRow()[vec_num] for vec_num, vec in enumerate(self.makeOrientationRow())], self.orientation)
                # both rows or cross orientation can both be handled by using the Matrix.makeOrientationRow method
                else:
                    return Matrix([vec + other[vec_num] for vec_num, vec in enumerate(self)], self.orientation)
            else:
                return ('cannot add, matrices not same size')
        else:
            return ('cannot add, unexpected type')

    # subtracts matrices by subtracting corresponding rows as vectors. returns a matrix with same orientation as self
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ('cannot add number to matrix')
        elif isinstance(other, Matrix):
            if self.dimensions == other.dimensions:
                # need a specific case for cross orientation
                if self.orientation != other.orientation:
                    return Matrix([vec - other.makeOrientationRow()[vec_num] for vec_num, vec in enumerate(self.makeOrientationRow())], self.orientation)
                # both rows or cross orientation can both be handled by using the Matrix.makeOrientationRow method
                else:
                    return Matrix([vec - other[vec_num] for vec_num, vec in enumerate(self)], self.orientation)
            else:
                return ('cannot subtract, matrices not same size')
        else:
            return None

    # normal multiplication for scalars (returns a matrix, preserves orientation), distributive dot product of transpose algorithm for matrices and vectors
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([row * other for row in self], self.orientation)

        # preserves orientation of self
        elif isinstance(other, Matrix):
            if self.number_of_cols != other.number_of_rows:
                return ('cannot multiply, size error')
            elif self.number_of_cols == other.number_of_rows:
                return Matrix([[row * other_row for other_row in other.transpose()] for row_num, row in enumerate(self)], self.orientation)

        # always outputs a col vector
        elif isinstance(other, Vector):
            if self.number_of_cols != len(other):
                return ('cannot multiply, size error')
            elif self.number_of_cols == len(other):
                return Vector([row * other for row in self])

        else:
            return None

    # takes a matrix and changes the orientation to rwos without changing the values
    def makeOrientationRow(self):
        if self.orientation == 'row':
            return self
        if self.orientation == 'col':
            return Matrix([Vector([col[row_num] for col in self]) for row_num, value in enumerate(self[0])])

    # checks if a matrix is square by checking if its dimensions are equivalent
    def isSquare(self):
        if self.dimensions[0] == self.dimensions[1]:
            return True
        else:
            return False

    # prints a matrix row by row
    def printMat(self):
        if self.orientation == 'row':
            for row_num, row in enumerate(self):
                print ("|", end='')
                for index, value in enumerate(row):
                    if isinstance(value, float):
                        if value.is_integer():
                            print (int(value), end=' ')
                        else:
                            print ('%.2f' % value, end=' ')
                    elif isinstance(value, int):
                        print (value, end=' ')
                print ("\b|")
            return ('')
        if self.orientation =='col':
            for row_num, row in enumerate(self[0]):
                print ("|", end='')
                for col in self:
                    if isinstance(col[row_num], int):
                        print (col[row_num], end=' ')
                    if isinstance(col[row_num], float):
                        if col[row_num].is_integer():
                            print (int(col[row_num]), end=' ')
                        else:
                            print ('%.2f' % col[row_num], end=' ')
                print ("\b|")
            return ('')

    # checks for the nonleading nonzero in a row. returns the number and which column it is in. returns no column for zero rows
    def checkLead(self, row):
        for col_num, digit in enumerate(row):
            if digit != 0:
                return {"column":col_num, "digit":digit}
        return {"column":len(row), "digit":0}

    # takes a matrix and pops out a second row and places before a first row. DOES change the actual matrix
    def swapRows(self, row1_loc, row2_loc):
        self.matrix.insert(row1_loc, self.matrix.pop(row2_loc))
        return self

    # run a series of checks to see if a matrix is in rref. carries a list of popped zero rows to be readded at the end
    def isRREF(self):
        # for each row use checkLead to find leading nonzero
        for row_num, row in enumerate(self):
            lead_info = self.checkLead(row)

            # if a zero row, pass over the leading one and zeroed column checks
            if lead_info['digit'] == 0:
                self.matrix.append(self.pop(row_num))

            # check that leading nonzero is a one
            elif lead_info['digit'] != 1:
                return {"solved":False, "problem":"leading nonzero in row", "location":row_num}

            elif True:
                # check that all other numbers in column are zero
                for other_row_num, other_row in enumerate(self):
                    if lead_info['column'] < len(row):
                        if other_row_num != row_num and other_row[lead_info['column']] != 0:
                            return {"solved":False, "problem":"nonzeroed column", "row":row_num, "location":other_row_num, "column":self.checkLead(row)['column']}

            # check that pivots are encountered in correct order
            elif row_num > 0 and self.checkLead(row)['digit'] != 0:
                if self.checkLead(row)['column'] < self.checkLead(self[row_num-1])['column']:
                    return {"solved":False, "problem":"pivots out of order", "location":row_num}

        # if all checks passed, matrix is solved
        return {"solved":True, "problem":None}

    # checks the current state of the matrix with isRREF
    def update(self):
        return self.isRREF()

    # puts a matrix into rref by continuously calling update and fixing the problem returned
    def rref(self):
        if self.orientation == 'col':
            self.orientation = 'row'
            was_cols = True

        RREF = copy.deepcopy(self)

        # scan for initial problem
        status = RREF.update()

        while status['solved'] == False:

            # if the leading nonzero is not a one, scale the row. update status
            if status['problem'] == 'leading nonzero in row':
                lead_info = RREF.checkLead(RREF[status['location']])
                RREF[status['location']] *= 1/lead_info['digit']
                status = RREF.update()

            # if the leading one has other nonzeroes in its column, scale and subtract from other rows to make zeroes. update status
            if status['problem'] == 'nonzeroed column':
                RREF[status['location']] -= RREF[status['row']] * RREF[status['location']][RREF.checkLead(RREF[status['row']])['column']]
                status = RREF.update()

            # if the rows are encountered out of order, swap them until order is correct. update status
            if status['problem'] == 'pivots out of order':
                RREF = RREF.swapRows(status['location']-1, status['location'])
                status = RREF.update()

        if status['solved'] == True:
            RREF = RREF.elimNegs()
            try:
                if was_cols == True:
                    RREF.orientation = 'col'
            except:
                pass
            return RREF

    # replaces -0.0 with just plain 0.0. necessary for comparing two matrices
    def elimNegs(self):
        for row_num, row in enumerate(self):
            for col_num, value in enumerate(row):
                if value == -0.0:
                    self[row_num][col_num] = 0.0
        return self

    # takes a matrix and finds pivot columns by converting to rref and checking for the location of leading ones (also finds rank by definition)
    def checkPivots(self):
        # convert the matrix to rref and check leads of all rows. if a one, store the column number of that pivot
        return {'columns':[self.checkLead(row)['column'] for row in self.rref() if self.checkLead(row)['digit'] != 0], 'rank':len([self.checkLead(row)['column'] for row in self.rref() if self.checkLead(row)['digit'] != 0])}

    # finds the number of solutions in a matrix by checking the rank against the number of rows
    def countSolutions(self):
        # if matrix is augmented and there is a pivot in the last column, no solution
        # if rank = n, one solution
        # if rank < n, infinite solutions
        pivs = self.checkPivots()
        augmented = ''
        while augmented != 'Y' and augmented != 'N':
            augmented = (input("is this an augmented matrix? (Y/N): ")).capitalize()

        # cases for augmented matrices
        if augmented == 'Y':
            # if there is a pivot in the last column, no solution
            if self.number_of_cols-1 in pivs['columns']:
                return ('no solutions')
            # if there is a pivot in every column before the equals bar and every row, one solution
            elif pivs['rank'] == self.number_of_cols-1 and pivs['rank'] == self.number_of_rows:
                return ('one solution')
            # if the rank is less than one less than the length, inifinite solutions
            elif pivs['rank'] < self.number_of_cols-1 or pivs['rank'] < self.number_of_rows:
                return ('inifinite solutions')

        # cases for not augmented matrices
        if augmented == 'N':
            # if there is a pivot in every column and every row, one solution
            if pivs['rank'] == self.number_of_cols and pivs['rank'] == self.number_of_rows:
                return ('one solution')
            # if there are fewer pivots than columns or rows, infinite solutions
            elif pivs['rank'] < self.number_of_cols or pivs['rank'] < self.number_of_rows:
                return ('infinite solutions')

    # transpose a matrix by turning all of the rows into columns
    def transpose(self):
        if self.orientation == 'row':
            return Matrix([row for row in self],'col')
        if self.orientation == 'col':
            return Matrix([col for col in self],'row')

    # a matrix is orthogonal if its columns are orthonormal. good thing there's a nice shortcut. a matrix is orthogonal is its inverse equals its transpose
    def isOrthogonal(self):
        return self.inverse() == self.transpose()
        #equivalently we could use self.transpose() * self = identity(len(self))

    # a matrix is symmetric if transposing it does nothing
    def isSymmetric(self):
        return self == self.transpose()

    # checks if a matrix is invertible by converting it to rref and checking if it matches the identity matrix
    def isInvertible(self):
        return self.rref() == buildIdentityMat(self.number_of_rows)

    # computes the inverse of a matrix by adding the identity matrix onto the end, computing rref, then removing the identity from the start
    def inverse(self):
        if not self.isInvertible():
            return ("matrix is not invertible")
        #  build the identity matrix for the same size as the self matrix
        #  take the top row of the matrix (a vector object) and append the top row of the identity matrix. create a new matrix
        #  rref
        #  delete the first half of each row of the matrix
        mat = self.extend(buildIdentityMat(self.number_of_rows))
        mat = mat.rref().transpose()
        for index in reversed(range(int(mat.number_of_rows/2))):
            del mat[index]
        return mat

    # just like extend method for list
    def extend(self, other):
        if isinstance(other, list):
            other = Vector(other)
        if not isinstance(other, Matrix) and not isinstance(other, Vector):
            return ('invalid input, cannot extend matrix')
        if not len(self) == len(other):
            return ('size error, cannot extend')
        if self.orientation == 'col':
            return Matrix([Matrix(self, 'row')[row_num].extend(other_row) for row_num, other_row in enumerate(Matrix(other, 'row'))], 'col')
        else:
            return Matrix([self[row_num].extend(other_row) for row_num, other_row in enumerate(Matrix(other, 'row'))], 'col')

    # just like pop method for list
    def pop(self, index=None):
        try:
            self[index]
        except TypeError:
            index = len(self)-1
        popped = copy.copy(self[index])
        del self[index]
        popped.orientation = 'row'
        return popped

    # computes rref and checks which columns are pivots, then takes those columns out of the original matrix and makes a set out of them
    def image(self):
        return Set([self.transpose()[column] for column in self.checkPivots()['columns']])
