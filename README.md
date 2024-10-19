- ## Optimization using Cache (Arrays / Hashmaps)
    
    - ### Intuition
        - The solution builds the k-th bit of the n-th binary string directly without constructing the entire string. The binary string is built recursively, where each level introduces a middle bit ('1') and reflects the previous bits while inverting them. This allows us to use an array to store only the bits we care about, significantly improving efficiency.

    - ### Approach
        1. Initialization: Create an array `bit_At_Index` to hold the bits, with the first bit set to '0'.
        2. Iterative Construction: For each level up to n:
            - If the k-th bit has already been determined, exit the loop.
            - Set the middle bit (current index + 1) to '1'.
            - Use a while loop to fill in the inverted bits from the current index to the next index.
        3. Retrieve Result: Return the k-th bit (1-indexed) from the array.

    - ### Time and Space Complexity
        
        - __Time Complexity:__ ___O(k)___
            - The algorithm runs in linear time relative to k, as it processes up to k bits in the array.

        - __Space Complexity:__ ___O(k)___
            - The space complexity is also O(k) due to the storage of the bits in the `bit_At_Index` array.

    - ### Code
        ```python3 []
        class Solution:
            def findKthBit(self, n: int, k: int) -> str:
                # Initialize a list to store bits, with the first bit being '0'
                bit_At_Index = [None] * k
                bit_At_Index[0] = '0'

                current_Index = 0
                
                # Generate the string iteratively for n levels
                for _ in range(n):
                    # Stop if we've already determined the k-th bit
                    if bit_At_Index[k - 1]: 
                        break
                    
                    # Set the middle bit to '1'
                    bit_At_Index[current_Index + 1] = '1'
                    
                    next_Index = current_Index + 2
                    
                    # Invert and fill the bits from the current index to the next index
                    while current_Index >= 0 and next_Index < k:
                        # Invert the current bit and assign it to the next position
                        bit_At_Index[next_Index] = '1' if bit_At_Index[current_Index] == '0' else '0'
                        next_Index += 1
                        current_Index -= 1

                    # Move to the next index for the next iteration
                    current_Index = next_Index - 1

                # Return the k-th bit (1-indexed)
                return bit_At_Index[k - 1]

        # Time Complexity: O(k)
        # The algorithm processes up to k bits in the array.

        # Space Complexity: O(k)
        # The space complexity is O(k) due to the storage of the bits in the bit_At_Index array.
        ```