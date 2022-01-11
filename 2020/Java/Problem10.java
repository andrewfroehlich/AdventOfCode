import java.io.*;
import java.util.*;
import java.time.*;

class Problem10 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem10.txt");
        
        try{
            Instant i0 = Instant.now();
            ArrayList<Integer> vals = buildSortedList(file);
            System.out.println("Part 1: "+part1(vals));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+part2(vals));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static ArrayList<Integer> buildSortedList(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        ArrayList<Integer> vals = new ArrayList<Integer>();
        String current;
        while ((current = (br.readLine())) != null) {
            vals.add(Integer.parseInt(current));
        }
        Collections.sort(vals);
        return vals;
    }
    
    public static int part1(ArrayList<Integer> vals) throws Exception{
        int previousValue = 0;
        int oneJumps = 0;
        //the last value is 3 more than max, so add one to threeJumps (start at 1)
        int threeJumps = 1;
        for(int i : vals){
            if(i - 3 == previousValue){
                threeJumps++;
            } else if(i - 1 == previousValue){
                oneJumps++;
            }
            previousValue = i;
        }
        
        return oneJumps * threeJumps;
    }
    
    public static long part2(ArrayList<Integer> vals) throws Exception{
        //add 0 as the first item in the list
        vals.add(0, 0);
        
        HashMap<Integer,Long> indexToPathCount = new HashMap<Integer,Long>();
        // Max value is valid
        indexToPathCount.put(vals.size() - 1, new Long(1));
        for(int i = vals.size() - 2; i >= 0; i--){
            long pathsFromCurrentIndex = 0;
            
            //check the next three indices to add paths
            int currentVal = vals.get(i);
            for(int j = i+1; j <= i+3; j++){
                if(j < vals.size() && currentVal+3 >= vals.get(j)){
                    pathsFromCurrentIndex += indexToPathCount.get(j);
                }
            }
            indexToPathCount.put(i, pathsFromCurrentIndex);
        }
        
        return indexToPathCount.get(0);
    }
}
