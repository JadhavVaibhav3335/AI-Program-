1 tmport math

2 def minimax (

curDepth, nodeIndex, maxTurn, scores,

3

targetDepth):

4 5

if (curDepth == targetDepth):

6

return scores [nodeIndex]

7

tf (maxTurn):

return max(minimax (curDepth + 1, nodeIndex * 2,

8

9

False, scores, targetDepth),

10

minimax(curDepth + 1, nodeIndex 2+1,

False, scores, targetDepth))

11 12

else:

return min(minimax (curDepth 1, nodeIndex * 2,

13 14

15

True, scores, targetDepth),

minimax(curDepth 1, nodeIndex 2+1,

16

True, scores, targetDepth))

17 scores [3, 5, 2, 9, 12, 5, 23, 23]

18 treeDepth = math.log(len(scores), 2)

A

19 print("The optimal value is : ", end = "") 20 print(minimax(0, 0, True, scores, treeDepth))

21