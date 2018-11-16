def coverPoints(self, A, B):
        prev_x, prev_y, total = A[0], B[0], 0
        for curr_x, curr_y in zip(A, B):
            dx, dy = abs(curr_x - prev_x), abs(curr_y - prev_y)
            if dx < dy:
                total += dy
            else:
                total += dx
            prev_x, prev_y = curr_x, curr_y
        return total
