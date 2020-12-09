import java.io.*;
import java.util.*;

class Problem9 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem9.txt");
        
        try{
            XMAS x = new XMAS(25);
            Long invalidNumber = part1(file,x);
            System.out.println("Part 1: "+invalidNumber);
            
            System.out.println("Part 2: "+part2(file, invalidNumber));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static long part1(File file, XMAS x) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        Long val;
        while ((current = (br.readLine())) != null) {
            val = Long.parseLong(current);
            if(x.isValid(val)){
                x.addValue(val);
            } else {
                return val;
            }
        }
        return -1;
    }
    
    public static long part2(File file, Long invalidNumber) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        Long val;
        
        // Add everything up to the invalid number to a List
        ArrayList<Long> l = new ArrayList<Long>();
        while ((current = (br.readLine())) != null) {
            val = Long.parseLong(current);
            if(val.equals(invalidNumber)){
                break;
            }
            l.add(val);
        }
                    
        int index1 = 0;
        int index2 = 1;
        Long currentTotal = l.get(index1) + l.get(index2);
        while(!currentTotal.equals(invalidNumber)){
            if (currentTotal.compareTo(invalidNumber) < 0){
                index2 ++;
                currentTotal += l.get(index2);
            } else {
                currentTotal -= l.get(index1);
                index1 ++;
            }
        }
        
        Long min = Long.MAX_VALUE;
        Long max = new Long(0); 
        for(int i = index1; i <= index2; i++){
            min = Math.min(min, l.get(i));
            max = Math.max(max, l.get(i));
        }
        return min+max;
    }
    
}

class XMAS {
    HashSet<Long> buffer;
    LinkedList<Long> queue;
    int CAPACITY;
    
    public XMAS(int preambleSize){
        CAPACITY = preambleSize;
        buffer = new HashSet<Long>(CAPACITY);
        queue = new LinkedList<Long>();
    }
    
    public boolean isValid(Long val){
        if(buffer.size() < CAPACITY){
            return true;
        }
        Iterator iter = queue.iterator();
        Long current;
        while(iter.hasNext()){
            current = (Long)iter.next();
            if(!val.equals(current) && buffer.contains(val - current)){
                return true;
            }
        }
        return false;
    }
    
    // Assumes validity was already checked
    public void addValue(Long val){
        if(buffer.size() == CAPACITY){
            buffer.remove(queue.peekLast());
            queue.removeLast();
        }
        queue.addFirst(val);
        buffer.add(val);
    }
}