class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # student_queue = deque(students)
        # sandwich_stack = []

        # for sandwich in reversed(sandwiches):
        #     sandwich_stack.append(sandwich)
        
        # rem_servings = 0

        # while rem_servings < len(student_queue):
        #     # either take the sandwich
        #     if sandwich_stack[-1] == student_queue[0]:
        #         sandwich_stack.pop()
        #         student_queue.popleft()
        #         rem_servings = 0
        #     # doesn't take the sandwich
        #     else:
        #         student_queue.append(student_queue[0])
        #         student_queue.popleft()
        #         rem_servings += 1
            
        
        # return len(student_queue)


        # Sol 2: O(N) O(1)
        # count the number of sandwiches left to serve as num students == num sandwiches given
        circle_sandwich = square_sandwich = 0

        for student_pref in students:
            if student_pref == 1:
                square_sandwich += 1
            else:
                circle_sandwich += 1
            print(circle_sandwich, square_sandwich)
        
        for sandwich in sandwiches:
            if sandwich == 1:
                if square_sandwich > 0:
                    square_sandwich -= 1
                else:
                    break
            
            else: 
                if circle_sandwich > 0:
                    circle_sandwich -= 1
                else:
                    break

            print(circle_sandwich, square_sandwich)
        
        return square_sandwich + circle_sandwich
                



        