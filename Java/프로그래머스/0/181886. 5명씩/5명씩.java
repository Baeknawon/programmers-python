class Solution {
    public String[] solution(String[] names) {
        String[] answer = new String[(names.length + 4) / 5];
        int n = 0;
        for(int i = 0; i < names.length; i+=5){
            answer[n++] = names[i];
            
        }
        return answer;
    }
}