# Efficient Retrieval of the K-th Bit in the N-th Binary String

- ## Exponential String Construction (Brute Force) 

    - ### Intuition
        - The problem revolves around generating a specific binary string based on a recursive pattern. Each string at position n is formed by taking the string from the previous position n-1, appending '1', and then appending the inverted (flipped) and reversed version of the previous string. Understanding this recursive nature helps in realizing that the string grows exponentially in size with each increase in n.

    - ### Approach
        1. **Initialization**: Start with the base string for n=1, which is '0'.
        2. **Iterative Construction**: For each subsequent n from 1 to the target n:
            - Invert the current string by flipping '0's to '1's and vice versa, and reverse it.
            - Construct the new string by concatenating the current string, '1', and the inverted string.
        3. **Retrieve Result**: After constructing the string for the required n, return the k-th character (1-indexed).

        The approach efficiently constructs the desired string through a series of string manipulations based on the defined rules.

    - ### Time and Space Complexity

        - __Time Complexity:__ ___O(2<sup>n</sup>)___
            - The length of the string grows exponentially, leading to an iterative process that involves string manipulations proportional to the length of the current string.

        - __Space Complexity:__ ___O(2<sup>n</sup>)___
            - The space required to store the strings increases exponentially, as each new string is a combination of the previous string and its inverted version.

    - ### Code
        ```python
        class Solution:
            def findKthBit(self, n: int, k: int) -> str:
                # Start with the initial string for n=1
                current_String = '0'
                
                # Generate the string for each n from 1 to n
                for _ in range(n):
                    # Create the inverted version of the current string, reversed and toggled
                    inverted_String = ''.join('1' if ch == '0' else '0' for ch in current_String[::-1])
                    # Form the new string by concatenating current, '1', and inverted
                    new_String = current_String + '1' + inverted_String
                    # Update current_String for the next iteration
                    current_String = new_String

                # Return the k-th character (1-indexed) from the final string
                return current_String[k - 1]
        ```

- ## Direct Bit Retrieval (Optimization using Cache (Arrays / Hashmaps))
    
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

- ## Recursive Search

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