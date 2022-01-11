import java.io.*;
import java.util.*;
import java.time.*;

class Problem14 {
    public static void main(String args[]){
        try{
            Instant i0 = Instant.now();
            File file = new File("/home/ec2-user/environment/AOC/Resources/problem14.txt");
            
            System.out.println("Part 1: "+part1(file));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+part2(file));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static long part1(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        Mask m = new Mask("");
        String current;
        HashMap<Integer,Long> memory = new HashMap<Integer,Long>();
        while ((current = (br.readLine())) != null) {
            String[] split = current.split(" = ");
            if(split[0].equals("mask")){
                m = new Mask(split[1]);
            } else {
                Integer locInt = Integer.parseInt(split[0].substring(4, split[0].indexOf("]")));
                memory.put(locInt, m.apply(Integer.parseInt(split[1])));
            }
        }
        
        long returnVal = 0L;
        for(Long val : memory.values()){
            returnVal += val;
        }
        return returnVal;
    }
    
    public static long part2(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        AddressMask m = new AddressMask("");
        String current;
        HashMap<Long,Long> memory = new HashMap<Long,Long>();
        ArrayList<Long> memoryLocs;
        while ((current = (br.readLine())) != null) {
            String[] split = current.split(" = ");
            if(split[0].equals("mask")){
                m = new AddressMask(split[1]);
            } else {
                Long loc = Long.parseLong(split[0].substring(4, split[0].indexOf("]")));
                Long value = Long.parseLong(split[1]);
                memoryLocs = m.apply(loc);
                for(Long l : memoryLocs){
                    memory.put(l, value);
                }
            }
        }
        
        long returnVal = 0L;
        for(Long val : memory.values()){
            returnVal += val;
        }
        return returnVal;
    }
}

class Mask{
    long orMask;
    long andMaskInverse;
    public Mask(String s){
        orMask = 0;
        andMaskInverse = 0;
        
        long twos = 1L;
        for(int i = s.length()-1; i >= 0; i--){
            if(s.charAt(i) == '0'){
                andMaskInverse += twos;
            } else if(s.charAt(i) == '1'){
                orMask += twos;
            }
            twos *= 2;
        }
    }
    
    public long apply(int num){
        return (num & ~andMaskInverse) | orMask;
    }
}

class AddressMask{
    long orMask;
    ArrayList<Long> floatingTwos;
    public AddressMask(String s){
        orMask = 0;
        floatingTwos = new ArrayList<Long>();
        
        long twos = 1L;
        for(int i = s.length()-1; i >= 0; i--){
            if(s.charAt(i) == '1'){
                orMask += twos;
            } else if(s.charAt(i) == 'X'){
                floatingTwos.add(twos);
            }
            twos *= 2;
        }
    }
    
    //returns list of all valid locations
    public ArrayList<Long> apply(long num){
        num = num | orMask;
        ArrayList<Long> toReturn = new ArrayList<Long>();
        toReturn.add(num);
        ArrayList<Long> temp = new ArrayList<Long>();
        
        for(Long two : floatingTwos){
            for(Long n : toReturn){
                temp.add(n | two);
                temp.add(n & ~(two));
            }
            toReturn.clear();
            for(Long x : temp){
                toReturn.add(x);
            }
            temp.clear();
        }
        
        return toReturn;
    }
}