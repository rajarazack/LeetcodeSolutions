/*
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
*/

public class Solution {
    public int reverse(int x) {
        String a = new StringBuilder(Integer.toString(x)).reverse().toString();
        long r = Long.parseLong(a.contains("-") ? "-"+a.replace("-","") : a);
        return ( r > Integer.MAX_VALUE || r < Integer.MIN_VALUE ) ? 0 : (int) r; 
    }
}
