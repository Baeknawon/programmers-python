class Solution {
    public int solution(String binomial) {
        int answer = 0;
        
        //이항식을 공백으로 분리
        String [] parts = binomial.split("\\s+");
        
        int a = Integer.parseInt(parts[0]);
        int b = Integer.parseInt(parts[2]);
        String op = parts[1];
        if(op.equals("+")){
            answer = a + b;
        }else if(op.equals("-")){
            answer = a - b;
        }else{
            answer = a * b;
        }
        return answer;
    }
}