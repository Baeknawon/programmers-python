import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer = "";
        
        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i); //a에서 i번째 인덱스에 있는 문자를 찾아서 c에 넣기
            if(Character.isUpperCase(c)){
                answer += Character.toLowerCase(c);
            }
            else if(Character.isLowerCase(c)){
                answer += Character.toUpperCase(c);
            }
            
        }
        System.out.println(answer);
    }
}