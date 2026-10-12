class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int n = pat.length();
        for(int i = 0; i< myString.length() - n + 1; i++){
            if(pat.equals(myString.substring(i,i+n))){
                answer++;
            }
        }
        return answer;
    }
}