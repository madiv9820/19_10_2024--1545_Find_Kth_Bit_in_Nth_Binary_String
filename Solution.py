class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Calculate the length of the n-th binary string
        length = 2**n - 1
        invert = False  # Flag to track if we need to invert the bit

        # Iteratively determine the k-th bit
        while length > 1:
            half = length // 2  # Find the position of the middle bit

            if k <= half:
                length = half  # Move to the left half
            elif k > half + 1:
                k = 1 + length - k  # Reflect k for the right half
                length = half
                invert = not invert  # Toggle the invert flag
            else:
                return '1' if not invert else '0'  # Return the middle bit

        return '0' if not invert else '1'  # Return the final result based on invert flag

# Time Complexity: O(log k)
# The while loop reduces the problem size by half in each iteration, leading to logarithmic complexity.

# Space Complexity: O(1)
# The space used is constant, as no additional data structures are employed beyond a few variables.