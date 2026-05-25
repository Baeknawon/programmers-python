
class Solution {
    public String solution(String n_str) {
        
        for(char s : n_str.toCharArray()){
            if(s != '0'){
                return n_str;
            }
            else{
                n_str = n_str.substring(1);
            }
        }
        return n_str;
    }
}