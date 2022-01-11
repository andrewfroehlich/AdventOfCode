import java.io.*;
import java.util.*;
import java.time.*;

class Problem19 {
    static ArrayList<String> messages;
    static HashMap<Integer, String> h;
    public static void main(String args[]){
        try{
            File file = new File("/home/ec2-user/environment/AOC2020/Resources/problem19.txt");
            Instant i0 = Instant.now();
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
    
    public static int part1(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        h = new HashMap<Integer, String>();
        messages = new ArrayList<String>();
        String current; 
        while ((current = (br.readLine())) != null) {
            if(current.trim().equals("\n") || current.trim().equals("")){
                break;
            }
            String[] split = current.split(": ");
            int i = Integer.parseInt(split[0]);
            // remove the quotes around a and b if they're there
            h.put(i, split[1].replace("\"", ""));
        }
        
        String re = "^" + makeRegex(0) + "$";
        int matches = 0;
        while ((current = (br.readLine())) != null) {
        	//add to messages for part 2
            messages.add(current);
            if(!current.equals("") && current.matches(re)){
                matches++;
            }
        }
        
        return matches;
    }
    
    public static int part2(File file) throws Exception{
        String rule42 = makeRegex(42);
        String rule31 = makeRegex(31);

        //build disgusting possible regex assuming max of 5 loops
        String masterRegex = "(" + rule42 + "+)(";
        for (int i = 1; i < 5; i++) {
            masterRegex += "(";
            for (int j = 1; j <= i; j++) {
                masterRegex += rule42;
            }
            for (int j = 1; j <= i; j++) {
                masterRegex += rule31;
            }
            masterRegex += ")";
            if (i < 4) {
                masterRegex += "|";
            }
        }
        masterRegex = "^(" + masterRegex + "))$";

        int count = 0;
        for (String m : messages) {
            if (m.matches(masterRegex)) {
                count++;
            }
        }

        return count;
    }
    
    private static String makeRegex(int i) {
        // keep going while there's still a number
        while ((h.get(i)).matches(".*\\d.*")) {
            String[] parts = (h.get(i)).split(" ");
            String current = ""; 
            for (String part : parts) {
                if (part.matches("\\d+")) {
                    // if simply numerical, add the rule from that index, otherwise prepare to be split next round
                    String nestedRule = h.get(Integer.parseInt(part));
                    if (nestedRule.matches("[ab]")) {
                        current += nestedRule;
                    } else {
                        current += "( " + nestedRule + " )";
                    }
                } else {
                    // just a/b, add it
                    current += part;
                }
            }
            h.put(i, current);
        }
        return "(" + h.get(i) + ")";
    }
}