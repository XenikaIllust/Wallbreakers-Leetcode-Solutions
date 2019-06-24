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
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> even;
        vector<int> odd;
        
        for(int i = 0; i < A.size(); i++) {
            if(A[i] % 2 == 0) { //even
                even.push_back(A[i]);
            }
            else {  //odd
                odd.push_back(A[i]);
            }
        }
        
        vector<int> total;
        total.insert(total.end(), even.begin(), even.end());
        total.insert(total.end(), odd.begin(), odd.end());
        
        return total; 
    }
};
