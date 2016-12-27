class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.numRows = len(self.matrix)
        if not self.matrix:
            self.numCols = 0
        else:
            self.numCols = len(self.matrix[0])
            
        self.sumTotal = self.sumAll()
        print "total sum {0}".format(self.sumTotal)
   
    
    def sumAll(self):
        accum = 0
        # for r in range(numRows):
        #     for c in range(numCols):
        #         if self.inRange(upperLeft, bottomRight, r, c):
        #             accum += self.matrix[r][c]
        for r in range(self.numRows):
            for c in range(self.numCols):
                accum += self.matrix[r][c]
        return accum
        
    

    def sumRegion(self, row1, col1, row2, col2):
        print "Running sumRegion({0},{1},{2},{3})".format(row1,col1,row2,col2)
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # pack up tuples
        upperLeft = (row1,col1)
        bottomRight = (row2, col2)
        
        # check if we should subtract
        if abs(row1-row2)*abs(col1-col2) >= self.numRows*self.numCols/2:
            print "subtractin"
            accum = self.sumTotal
            rows = range(0,row1)+range(row2+1,self.numRows)
            
            # print "rows: {0}".format(rows)
            # print "cols: {0}".format(cols)

            # for rows that don't have grid contained in them
            for r in rows:
                for c in range(self.numCols):
                    accum -= self.matrix[r][c]
            
            # for rows that have grid contained in them
            cols = range(0,col1)+range(col2+1,self.numCols)
            for r in range(row1,row2+1):
                for c in cols:
                    accum -= self.matrix[r][c]

            return accum
        else:
            print "adding"
            accum = 0
            # for r in range(numRows):
            #     for c in range(numCols):
            #         if self.inRange(upperLeft, bottomRight, r, c):
            #             accum += self.matrix[r][c]
            for r in range(row1, row2+1):
                for c in range(col1, col2+1):
                    accum += self.matrix[r][c]
                    print accum

            return accum
        
    def inRange(self, upperLeft,bottomRight,r,c):
        return r >= upperLeft[0] and r <= bottomRight[0] and c >=upperLeft[1] and c <= bottomRight[1]
        

def main():
    matrix  =[[-5208,1041,-93779,-64152,17850,29055,-63731,-23568,41170,58457,-39616,55683,-51662,-75015,21726],[4535,-72412,86878,-60825,67088,48794,-23471,-22403,58200,-31153,-94668,-27274,-11003,33894,-66125],[-9538,-33861,54822,42636,48430,-56030,-33348,-30617,5219,56501,-95879,-73537,-18157,-72815,-40977],[15602,40115,-32475,99011,47251,84035,83793,-74389,-99042,65460,11671,-95294,68311,47893,71866],[69607,57288,55022,36610,-75113,31344,34319,-13381,-74800,-71904,-15625,-5398,-29689,-68805,-41994],[-32276,95017,-96452,-47311,13238,46324,95358,13247,-30930,5815,-36748,-25712,-83982,29391,-73922],[-29140,-70403,-3168,12219,-4473,-10013,-85502,87222,-44858,66506,-99821,-16992,-80758,59210,87145],[-9557,67725,-27359,-28647,46781,-67948,-28154,-3498,91489,-3887,-96422,6568,42380,73264,-55406],[40555,70153,-51490,-14237,9684,-54000,-8443,-32063,-96157,-70083,-7050,56221,93013,-1157,-45593],[-28686,-54296,628,11189,18227,-64455,-10528,-69244,94796,-39806,69194,45024,-14417,-51291,6387],[-28485,36898,97259,-83875,83650,-36715,80692,-55055,40025,-69379,-1548,-13045,23318,79349,-42774],[82645,17721,84052,-35036,-751,90269,-77187,51972,-90217,-5956,-34552,95560,40436,51650,72778],[-970,77788,10423,-1406,-90844,6732,-60197,59393,-82111,33737,-4731,-52679,-12011,69741,-91931]]
    numMatrix = NumMatrix(matrix)
    print numMatrix.sumRegion(1,1,10,13)

if __name__ == "__main__":
    main()







# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)