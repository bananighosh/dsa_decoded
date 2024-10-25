class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # apply topological sort
        # for every item in the array, recursion needed

        folder.sort()

        result_set = [folder[0]]

        for i in range(1, len(folder)):
            prev_folder = result_set[-1] + '/'

            print(prev_folder, folder[i])
            if not folder[i].startswith(prev_folder):
                result_set.append(folder[i])
        
        return result_set


        