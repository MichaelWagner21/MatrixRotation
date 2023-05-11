import math
def rotateMultiple(matrix,r):
    rowTotal = len(matrix)
    colTotal = len(matrix[0])
    returnMatrix = []
    
    for _ in range(rowTotal):
        returnMatrix.append(colTotal*[0])


    for rowNum in range(rowTotal):
        for colNum in range(colTotal):
            currentNewValRow = rowNum
            currentNewValCol = colNum
            transDone = 0
            ringNum = min(rowNum,colNum,(rowTotal-rowNum-1),colTotal-1-colNum)
            circumference = (2*(rowTotal-(2*ringNum))+2*(colTotal-(2*ringNum)))-4

            topBound = ringNum
            bottomBound = rowTotal-ringNum-1
            leftBound = ringNum
            rightBound = colTotal-ringNum-1
            
            transNeeded = r
            if transNeeded>=circumference:
                transNeeded = transNeeded % circumference
            
            while transDone<transNeeded:
                transLeft = transNeeded-transDone
                isTop = False
                isRight = False
                isBottom = False
                isLeft = False

                if currentNewValRow == topBound:
                    isTop = True
                elif currentNewValRow == bottomBound:
                    isBottom = True
                if currentNewValCol == leftBound:
                    isLeft = True
                elif currentNewValCol == rightBound:
                    isRight = True

                cycleBroken = False
                while (not cycleBroken) and transDone<transNeeded:


                    if isTop and not isRight:
                        if transLeft >= rightBound-currentNewValCol:
                            transDone+= rightBound-currentNewValCol
                            transLeft = transNeeded-transDone
                            currentNewValCol = rightBound
                            isRight = True
                            isLeft = False
                        elif transDone<transNeeded:
                            currentNewValCol+=transLeft
                            transDone+=transLeft
                            transLeft = transNeeded-transDone
                            cycleBroken = True
                    if isRight and not isBottom:
                        if transLeft >= bottomBound-currentNewValRow:
                            transDone+=bottomBound-currentNewValRow
                            transLeft = transNeeded-transDone
                            currentNewValRow = bottomBound
                            isBottom = True
                            isTop = False
                        elif transDone<transNeeded:
                            currentNewValRow+=transLeft
                            transDone+=transLeft
                            transLeft = transNeeded-transDone
                            cycleBroken = True
                    if isBottom and not isLeft:
                        if transLeft >= currentNewValCol-leftBound:
                            transDone += currentNewValCol-leftBound
                            transLeft = transNeeded-transDone
                            currentNewValCol = leftBound
                            isLeft = True
                            isRight = False
                        elif transDone<transNeeded:
                            currentNewValCol-=transLeft
                            transDone+=transLeft
                            transLeft = transNeeded-transDone
                            cycleBroken = True
                    if isLeft and not isTop:
                        if transLeft >= currentNewValRow-topBound:
                            transDone+=currentNewValRow-topBound
                            transLeft = transNeeded-transDone
                            currentNewValRow = topBound
                            isTop = True
                            isBottom = False
                        elif transDone<transNeeded:
                            currentNewValRow-=transLeft
                            transDone+=transLeft
                            transLeft = transNeeded-transDone
                            cycleBroken = True
            print(matrix[currentNewValRow][currentNewValCol], end=" ")
        print()

def matrixRotation(matrix, r):
    finalMatrix = matrix
    ringQuantity = int(min(len(matrix),len(matrix[0]))/2)
    ringElementQuantityList = []
    minRotNum = r
    for i in range(ringQuantity):
        ringElementQuantityList.append(  (2*(len(matrix)-(2*i)))+(2*(len(matrix)-(2*i)))-4  )
    repeatRotNum = 1
    for i in ringElementQuantityList:
        repeatRotNum=(repeatRotNum*i)//math.gcd(repeatRotNum,i)
    if minRotNum > repeatRotNum:
        minRotNum = minRotNum%repeatRotNum
    
    rotateMultiple(finalMatrix, minRotNum)

testMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrixRotation(testMatrix,42971434)