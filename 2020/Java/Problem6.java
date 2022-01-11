import java.io.*;
import java.util.*;

class Problem6 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem6.txt");
        
        try{
            System.out.println("Part 1: "+part1(file));
            
            System.out.println("Part 2: "+part2(file));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static int part1(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        HashSet<Character> s = new HashSet<Character>();
        int answer = 0;
        while ((current = (br.readLine())) != null) {
            if(current == null || "".equals(current)){
                s.clear();
            } else {
                for(int i=0; i<current.length(); i++){
                    Character c = current.charAt(i);
                    if(!s.contains(c)){
                        s.add(c);
                        answer++;
                    }
                }
            }
        } 
        
        return answer;
    }
    
    public static int part2(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        HashSet<Character> s = new HashSet<Character>();
        HashSet<Character> t = new HashSet<Character>();
        boolean newGroup = true;
        int answer = 0;
        while ((current = (br.readLine())) != null) {
            if(current == null || "".equals(current)){
                answer += s.size();
                s.clear();
                newGroup = true;
            } else {
                if(newGroup){
                    newGroup = false;
                    for(int i=0; i<current.length(); i++){
                        s.add(current.charAt(i));
                    }
                } else {
                    for(int i=0; i<current.length(); i++){
                        t.add(current.charAt(i));
                    }
                    s.retainAll(t);
                    t.clear();
                }
            }
        } 
        answer += s.size(); 
        
        return answer;
    }
}
