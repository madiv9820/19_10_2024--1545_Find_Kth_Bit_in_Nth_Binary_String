class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Calculate the length of the n-th binary string
        total_length = 2 ** n - 1

        def recursive_find(length, position):
            # Base case: if the length is 1, return '0'
            if length == 1:
                return '0'
            
            # Find the position of the middle bit
            mid_index = length // 2
            
            # Recursively determine the k-th bit
            if position <= mid_index:
                return recursive_find(mid_index, position)  # Left side
            elif position > mid_index + 1:
                # Right side, find the inverted bit
                inverted_bit = recursive_find(mid_index, 1 + length - position)
                return '0' if inverted_bit == '1' else '1'  # Invert the bit
            else:
                return '1'  # Middle bit is always '1'
            
        # Call the recursive function to find the k-th bit
        return recursive_find(total_length, k)

# Title: Efficient K-th Bit Retrieval in N-th Binary String

# Time Complexity: O(log k)
# Each recursive call reduces the problem size by half, leading to logarithmic complexity relative to k.

# Space Complexity: O(log k)
# The recursion stack can go as deep as log k in the worst case, leading to logarithmic space complexity.