class Solution {
    public int solution(String number) {
        int answer = 0;
        int total = 0;
        for(char s : number.toCharArray()){
            int num = s - '0';
            total += num;
        }
        answer = total % 9;
            
        
        return answer;
    }
}