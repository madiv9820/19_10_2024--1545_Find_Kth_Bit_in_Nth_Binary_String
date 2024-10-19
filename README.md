- ## Recursion

    - ### Intuition
        - The problem leverages the recursive structure of binary strings generated through a specific pattern. Each string at level n consists of the previous string at level n-1, a middle bit ('1'), and an inverted (flipped) and reversed version of the previous string. This recursive structure allows us to determine the k-th bit without constructing the entire string, simply by navigating through its properties.

    - ### Approach
        1. **Calculate Length**: First, compute the length of the n-th binary string, which is (2<sup>n</sup> - 1).
        2. **Recursive Function**: Use a helper function (`recursive_find`) that:
            - **Base Case**: Returns '0' if the length is 1.
            - **Determine Segment**:
                - If the requested position k is in the left half, recursively search in that half.
                - If k is in the right half, find the corresponding bit in the left half and invert it.
                - If k corresponds to the middle bit, return '1'.
        3. **Call Function**: Invoke the recursive function with the calculated total length and the desired position k.

    - ### Time and Space Complexity
        
        - __Time Complexity:__ ___O(log k)___
            - Each recursive call reduces the problem size by half, leading to logarithmic complexity relative to k.

        - __Space Complexity:__ ___O(log k)___
            - The recursion stack can go as deep as log k in the worst case, leading to logarithmic space complexity.

    - ### Code
        ```python
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
        ```