class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sandwich_stack = []

        for sandwich in reversed(sandwiches):
            sandwich_stack.append(sandwich)
        
        rem_servings = 0

        while rem_servings < len(student_queue):
            # either take the sandwich
            if sandwich_stack[-1] == student_queue[0]:
                sandwich_stack.pop()
                student_queue.popleft()
                rem_servings = 0
            # doesn't take the sandwich
            else:
                student_queue.append(student_queue[0])
                student_queue.popleft()
                rem_servings += 1
            
        
        return len(student_queue)

        