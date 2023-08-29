# https://leetcode.com/problems/excel-sheet-column-title/



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = deque()
        while columnNumber > 0:
            columnNumber, output = divmod(columnNumber-1, 26)
            column.appendleft(output)

        return "".join([chr(i+ord("A"))for i in column])
