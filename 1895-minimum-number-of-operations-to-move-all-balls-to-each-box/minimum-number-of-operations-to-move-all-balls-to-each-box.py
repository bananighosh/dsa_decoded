class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        for curr_box in range(len(boxes)):
            if boxes[curr_box] == "1":
                for new_pos in range(len(boxes)):
                    answer[new_pos] += abs(new_pos - curr_box)
        return answer
        