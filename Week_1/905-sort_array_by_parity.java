/*
    # This solution runs in O(n) time complexity. I think (for now) the only solution is O(n) because the
    program has to run through each element in the array. The numerical order does not matter. Therefore I
    created two bins called "even" and "odd" to keep elements of each category, then concatenate both.
    Space efficiency is O(n) because space only grows as much as # of input elements.
    
Questions:
1. How to reduce memory use (non-copy)?
2. How to improve time?
3. How to improve the elegance of my code?
*/

class Solution {
    public int[] sortArrayByParity(int[] A) {
        ArrayList<Integer> even = new ArrayList<Integer>();
        ArrayList<Integer> odd = new ArrayList<Integer>();
        
        for(int i = 0; i < A.length; i++) {
            if(A[i] % 2 == 0) { //even
                even.add(A[i]);
            }
            else { //odd
                odd.add(A[i]);
            }
        }
        
        even.addAll(odd);
        
        int[] res = new int[even.size()];
        
        for(int i = 0; i < even.size(); i++) {
            res[i] = even.get(i);
        }
        
        return res;
    }
}
