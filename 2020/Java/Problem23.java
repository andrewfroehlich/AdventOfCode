import java.io.*;
import java.util.*;
import java.time.*;

class Problem23 {
    public static void main(String args[]){
        try{
            String input = "364297581";
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+solve(input, 100, false));
            Instant i1 = Instant.now();
            //System.out.println("Part 2: "+solve(input, 10000000, true));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static String solve(String input, int moves, boolean partTwo) throws Exception{
        ArrayList<Integer> list = new ArrayList<Integer>();
        int size = partTwo ? 1000000 : input.length();
        int currentIndex = 0;
        for(int i=0; i<input.length(); i++){
            list.add(Character.getNumericValue(input.charAt(i)));
        }
        // if part 2, keep adding up to 1,000,000
        if(partTwo){
            for(int i=input.length()+1; i <= 1000000; i++){
                list.add(i);
            }
        }
        
        int movesCompleted = 0;
        while(movesCompleted < moves){
            //if(movesCompleted % 50000 == 0) System.out.println(String.format("Move #%s",movesCompleted));
            
            // remove the next three cups
            int target = (list.get(currentIndex))-1;
            boolean decCurrentIndex = false;
            if((currentIndex + 1)%list.size() < currentIndex) decCurrentIndex = true;
            int removedOne = list.remove((currentIndex + 1)%list.size());
            if(decCurrentIndex){
                currentIndex--;
                decCurrentIndex = false;
            }
            
            if((currentIndex + 1)%list.size() < currentIndex) decCurrentIndex = true;
            int removedTwo = list.remove((currentIndex + 1)%list.size());
            if(decCurrentIndex){
                currentIndex--;
                decCurrentIndex = false;
            }
            
            if((currentIndex + 1)%list.size() < currentIndex) decCurrentIndex = true;
            int removedThree = list.remove((currentIndex + 1)%list.size());
            if(decCurrentIndex) currentIndex--;
            
            // determine the target value
            while(target < 1 || target == removedOne || target == removedTwo || target == removedThree){
                if(target < 1){
                    target += size;
                } else {
                    target--;
                }
            }
            // find where the target value is and add the removed ones in order
            int targetIndex = list.indexOf(target);
            list.add(targetIndex+1, removedOne);
            list.add(targetIndex+2, removedTwo);
            list.add(targetIndex+3, removedThree);
            if(targetIndex < currentIndex){
                currentIndex += 3;
            }
            // increment current and moves count
            currentIndex = (currentIndex + 1) % size;
            movesCompleted++;
        }
        
        int oneIndex = list.indexOf(1);
        oneIndex = (oneIndex + 1) % size;
        StringBuilder sb = new StringBuilder();
        while(list.get(oneIndex) != 1){
            sb.append(list.get(oneIndex));
            oneIndex = (oneIndex + 1) % size;
        }
        
        return sb.toString();
    }
}
