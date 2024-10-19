- ## Brute Force 

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