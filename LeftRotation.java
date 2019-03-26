//Left Rotation
//Input: two integers- n (number of integers) and d (number of left rotations)
//Constraints: 1<=n<=10^5 1<=d<=n 1<=a sub i<=10^6
//Output: single line of n space-seperated integers denoting final state of array after d left rotations

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class LeftRotation {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int d = scan.nextInt();
        int[] array = new int[n];
        for(int i=0; i<n;i++){
            array[(i+n-d)%n] = scan.nextInt();}
        for(int i=0; i<n;i++){
            System.out.print(array[i] + " ");}      
    }
}