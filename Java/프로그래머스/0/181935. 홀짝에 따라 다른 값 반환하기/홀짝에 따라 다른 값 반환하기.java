class Solution {
    public int solution(int n) {
        int sum = 0;
        if(n % 2 == 0){
            for(int i = n; i > 0; i-= 2){
                sum += i* i;
            }
        }
        else{
            for(int i = n; i > 0; i -= 2){
                sum += i;
            }
        }
        return sum;
    }
}