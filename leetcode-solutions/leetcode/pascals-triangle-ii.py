class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate_row(row_index):
            if row_index == 0:
                return [1]
            
            prev_row = generate_row(row_index - 1)
            row = [1]
            
            for i in range(1, row_index):
                row.append(prev_row[i-1] + prev_row[i])
            
            row.append(1)
            return row
        
        return generate_row(rowIndex)

        