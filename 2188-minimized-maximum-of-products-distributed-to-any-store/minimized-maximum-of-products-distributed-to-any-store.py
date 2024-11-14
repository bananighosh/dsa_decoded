class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def can_distribute(x: int, quantities: List[int], n: int) -> bool:
            # Pointer to the first not fully distributed product type
            j = 0
            # Remaining quantity of the jth product type
            remaining = quantities[j]

            # Loop through each store
            for i in range(n):
                # Check if the remaining quantity of the jth product type
                # can be fully distributed to the ith store
                if remaining <= x:
                    # If yes, move the pointer to the next product type
                    j += 1
                    # Check if all products have been distributed
                    if j == len(quantities):
                        return True
                    else:
                        remaining = quantities[j]
                else:
                    # Distribute the maximum possible quantity (x) to the ith store
                    remaining -= x

            return False


        left = 0
        right = max(quantities)

        # Perform binary search until the boundaries converge
        while left < right:
            middle = (left + right) // 2
            if can_distribute(middle, quantities, n):
                right = middle
            else:
                left = middle + 1

        return left
        