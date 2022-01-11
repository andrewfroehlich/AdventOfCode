import java.io.*;
import java.util.*;
import java.time.*;

class Problem15 {
    public static void main(String args[]){
        try{
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+solve("12,1,16,3,11,0",2020));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+solve("12,1,16,3,11,0",30000000));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static int solve(String input, int turnCount) throws Exception{
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
        int turn = 1;
        int lastValue = 0;
        int turnsSince = 0;
        String[] inpSplit = input.split(",");
        for(String n : inpSplit){
            Integer val = Integer.parseInt(n);
            turnsSince = hm.containsKey(val) ? turn - hm.get(val) : 0;
            hm.put(val, turn++);
            lastValue = val;
        }
        
        while(true){
            int val = turnsSince;
            if(turn == turnCount){
                return val;
            }
            turnsSince = hm.containsKey(val) ? turn - hm.get(val) : 0;
            hm.put(val, turn++);
            lastValue = val;
        }
    }
}
