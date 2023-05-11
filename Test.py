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
            

            
            while transDone<r:
                transLeft = r-transDone
                isTop = False
                isRight = False
                isBottom = False
                isLeft = False
                if currentNewValRow == ringNum:
                    isTop = True
                elif currentNewValRow == len(returnMatrix)-ringNum-1:
                    isBottom = True
                if currentNewValCol == ringNum:
                    isLeft = True
                elif currentNewValCol == len(returnMatrix[rowNum])-ringNum-1:
                    isRight = True


                if isTop and not isRight:
                    if transLeft > colTotal-2*ringNum:
                        transDone+= colTotal-ringNum-currentNewValCol-1
                        currentNewValCol = colTotal-ringNum-1
                    else:
                        currentNewValCol+=1
                        transDone+=1
                elif isRight and not isBottom:
                    if transLeft > rowTotal-2*ringNum:
                        transDone+=rowTotal-ringNum-currentNewValRow-1
                        currentNewValRow = rowTotal-ringNum-1
                    else:
                        currentNewValRow+=1
                        transDone+=1
                elif isBottom and not isLeft:
                    if transLeft > colTotal-2*ringNum:
                        transDone += currentNewValCol-ringNum
                        currentNewValCol = ringNum
                    else:
                        currentNewValCol-=1
                        transDone+=1
                elif isLeft and not isTop:
                    if transLeft > rowTotal-2*ringNum:
                        transDone+=currentNewValRow-ringNum
                        currentNewValRow = ringNum
                    else:
                        currentNewValRow-=1
                        transDone+=1
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

testMatrix = [[1,2],[3,4]]
matrixRotation(testMatrix,42971434)