import java.io.*;
import java.util.*;
import java.time.*;
import java.util.stream.*;

class Problem13 {
    public static void main(String args[]) throws Exception{
        try{
            File file = new File("/home/ec2-user/environment/AOC/Resources/problem13.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));
            String current;
            int targetTimestamp = 0;
            ArrayList<Integer> buses = new ArrayList<Integer>();
            
            if ((current = br.readLine()) != null) {
                targetTimestamp = Integer.parseInt(current);
            }   
            if ((current = br.readLine()) != null) {
                String[] busArray = current.split(",");
                for(String s:busArray){
                    if(!s.equals("x")){
                        buses.add(Integer.parseInt(s));
                    }
                }
            } 
            
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+part1(targetTimestamp, buses));
            Instant i1 = Instant.now();
            
            ArrayList<Bus> buses2 = new ArrayList<Bus>();
            String[] busArray = current.split(",");
            for(int offset = 0; offset < busArray.length; offset++){
                if(!"x".equals(busArray[offset])){
                    buses2.add(new Bus(Integer.parseInt(busArray[offset]), offset));
                }
            }
            System.out.println("Part 2: "+part2(buses2, 100000000000000L));
            Instant i2 = Instant.now();
            
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static int part1(int target, List<Integer> buses) throws Exception{
        int currentTarget = target;
        while(true){
            for(Integer i:buses){
                if(currentTarget % i == 0){
                    return i * (currentTarget - target);
                }
            }
            currentTarget++;
        }
    }
    
    public static long part2(List<Bus> buses, long startingNumber) throws Exception{
        // Assume the hint is true /shrug
        long currentTarget = startingNumber;
        
        //find the largest bus to increment with
        int largestBus = 0;
        int largestBusOffset = 0;
        for(Bus b:buses){
            if(b.bus > largestBus){
                largestBus = b.bus;
                largestBusOffset = b.offset;
            }
        }
        
        //remove the largest bus
        for(int i = 0; i < buses.size(); i++){
            if(buses.get(i).bus == largestBus){
                buses.remove(i);
                break;
            }
        }
        
        //start with something divisible by the largest bus (minus offset)
        while(currentTarget % largestBus > 0){
            currentTarget++;
        }
        currentTarget -= largestBusOffset;
        
        long incrementer = largestBus;
        while(true){
            Bus b;
            for(int i=0; i<buses.size(); i++){
                b = buses.get(i);
                if((currentTarget + b.offset) % b.bus == 0){
                    // if this value works, multiply the incrementer by the bus and remove the bus
                    incrementer *= b.bus;
                    buses.remove(i);
                    // if all the buses are gone, you're on the answer
                    if(buses.size() == 0){
                        return currentTarget;
                    }
                    i = -1;
                } else {
                    break;
                }
            }
            currentTarget += incrementer;
        }
    }
}

class Bus{
    int bus;
    int offset;
    public Bus(int b, int o){
        this.bus = b;
        this.offset = o;
    }
}