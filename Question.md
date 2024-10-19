# 1545. Find Kth Bit in Nth Binary String

__Type__: Medium <br>
__Topics:__ String, Recursion, Simulation <br>
__Companies:__ Amazon, Microsoft <br>
__Leetcode Link:__ [Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/) <br>
__Reference Video:__ [Find Kth Bit in Nth Binary String - Leetcode 1545 - Python](https://www.youtube.com/watch?v=h9DOEqeb_ZA)
<hr>

Given two positive integers `n` and `k`, the binary string <code>S<sub>n</sub></code> is formed as follows:
- `S1 = "0"`
- <code>S<sub>i</sub> = S<sub>i - 1</sub> + "1" + reverse(invert(S<sub>i - 1</sub>))</code> for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:
- `S1 = "0"`
- `S2 = "011"`
- `S3 = "0111001"`
- `S4 = "011100110110001"`

Return _the_ <code>k<sup>th</sup></code> _bit in_ <code>S<sub>n</sub></code>. It is guaranteed that `k` is valid for the given `n`.
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ n = 3, k = 1 <br>
__Output:__ "0" <br>
__Explanation:__ S<sub>3</sub> is "<u><b>0</b></u>111001". <br> 
The 1st bit is "0".

- __Example 2:__ <br>
__Input:__ n = 4, k = 11 <br>
__Output:__ "1" <br>
__Explanation:__ S<sub>4</sub> is "0111001101<u><b>1</b></u>0001". <br>
The 11th bit is "1".
<hr>

### Constraints:
- `1 <= n <= 20`
- <code>1 <= k <= 2<sup>n</sup> - 1</code>
<hr>

### Hint
- Since n is small, we can simply simulate the process of constructing S<sub>1</sub> to S<sub>n</sub>.