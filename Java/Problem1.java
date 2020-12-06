import java.io.*;
import java.util.*;

class Problem1 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem1.txt");
        
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
        HashSet<Integer> s = new HashSet<Integer>();
        while ((current = (br.readLine())) != null) {
            Integer i = Integer.parseInt(current);
            if(s.contains(2020-i)){
                return i * (2020-i);
            } else {
                s.add(i);
            }
        } 
        
        return -1;
    }
    
    public static int part2(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        HashSet<Integer> s = new HashSet<Integer>();
        List<Integer> l = new ArrayList<Integer>();
        while ((current = (br.readLine())) != null) {
            Integer a = Integer.parseInt(current);
            s.add(a);
            l.add(a);
        } 
        
        Integer x,y;
        for(int i=0; i<l.size(); i++){
            for(int j=i+1; j<l.size(); j++){
                x = l.get(i);
                y = l.get(j);
                if(s.contains(2020 - x - y)){
                    return x * y * (2020 - x - y);
                }
            }
        }
        return -1;
    }
}
