class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];
        int i = 0;
        for(int num : arr){
            if(num % 2 ==0 && num >= 50){
                answer[i++] = num / 2;
            }
            else if(num % 2 != 0 && num < 50){
                answer[i++] = num * 2;
            }
            else{
                answer[i++] = num;
            }
            
        }
        return answer;
    }
}