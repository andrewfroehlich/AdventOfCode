import java.io.*;
import java.util.*;
import java.time.*;

class Problem16 {
    public static void main(String args[]){
        try{
            Instant i0 = Instant.now();
            File file = new File("/home/ec2-user/environment/AOC/Resources/problem16.txt");
            System.out.println("Part 2: "+solve(file));
            Instant i1 = Instant.now();
            System.out.println(String.format("Problem 16: %s ms",Duration.between(i0, i1).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static long solve(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        ArrayList<Range> ranges = new ArrayList<Range>();
        ArrayList<Field> fields = new ArrayList<Field>();
        String current;
        int fieldId = 0;
        // Create the fields with ranges
        while ((current = (br.readLine())) != null) {
            if(current.trim().equals("\n") || current.trim().equals("")){
                break;
            }
            String[] rangeSplits = current.split(": ")[1].split(" or ");
            for(String r : rangeSplits){
                String[] lowHigh = r.split("-");
                ranges.add(new Range(Integer.parseInt(lowHigh[0]), Integer.parseInt(lowHigh[1])));
            }
            fields.add(new Field(fieldId++, current.split(": ")[0], ranges.get(ranges.size()-2), ranges.get(ranges.size()-1)));
        }
        //Get my ticket and iterate the buffer to nearby tickets
        Ticket myTicket = null;
        while ((current = (br.readLine())) != null) {
            if(current.contains("your ticket:")){
                break;
            }
        }
        if ((current = (br.readLine())) != null) {
            myTicket = new Ticket(current);
        }
        while ((current = (br.readLine())) != null) {
            if(current.contains("nearby tickets:")){
                break;
            }
        }
        //Solve Part 1, while also generating a list of all valid tickets per part 1
        int scanningError = 0;
        ArrayList<Ticket> validTickets = new ArrayList<Ticket>();
        while ((current = (br.readLine())) != null) {
            Ticket tick = new Ticket(current);
            boolean ticketIsValid = true;
            for(int i : tick.values){
                boolean fieldIsValid = false;
                int index = 0;
                while(!fieldIsValid && index < fields.size()){
                    fieldIsValid = (fields.get(index)).validForNumber(i);
                    index++;
                }
                if(!fieldIsValid) {
                    ticketIsValid = false;
                    scanningError += i;
                }
            }
            if(ticketIsValid){
                validTickets.add(tick);
            } 
        }
        System.out.println("Part 1: "+scanningError);
        //Create a HashSet per index with all fieldIds to start so we can remove as fieldIds become invalid
        ArrayList<HashSet<Integer>> possibleFieldsPerIndex = new ArrayList<HashSet<Integer>>(fields.size());
        for(int i = 0; i < fields.size(); i++){
            HashSet<Integer> validFields = new HashSet<Integer>();
            for(int j = 0; j < fields.size(); j++){
                validFields.add(j);
            }
            possibleFieldsPerIndex.add(validFields);
        }
        //For all tickets, remove the fieldId from the index's HashSet if that ticket would not be valid for the given fieldId
        for(Ticket t:validTickets){
            for(int i=0; i<t.values.length; i++){
                for(int j=0; j<fields.size(); j++){
                    if(possibleFieldsPerIndex.get(i).contains(j) && !fields.get(j).validForNumber(t.values[i])){
                        possibleFieldsPerIndex.get(i).remove(j);
                    }
                }
            }
        }
        //Iterate through the fields finding where the possible field hashset is one item and choosing that item, updating the fields and other hashes
        int indexFound = 0;
        while(indexFound > -1){
            indexFound = -1;
            for(int i=0; i<possibleFieldsPerIndex.size(); i++){
                if(possibleFieldsPerIndex.get(i).size() == 1){
                    indexFound = i;
                    break;
                }
            }
            
            if(indexFound > -1){
                // get the single item in that HashSet, which has to be the FieldId of the index
                Integer fieldIdToUpdate = (possibleFieldsPerIndex.get(indexFound)).toArray(new Integer[1])[0];
                fields.get(fieldIdToUpdate).index = indexFound;
                for(HashSet<Integer> hs : possibleFieldsPerIndex){
                    hs.remove(fieldIdToUpdate);
                }
            }
        }
        //Iterate through all fields to create the part 2 return value using the field indices and myTicket
        long returnValue = 1L;
        for(Field f:fields){
            if(f.name.contains("departure")){
                returnValue *= myTicket.values[f.index];
            }
        }
        return returnValue;
    }
}

class Range{
    int low;
    int high;
    public Range(int l, int h){
        this.low = l;
        this.high = h;
    }
    public boolean inRange(int num){
        return low <= num && num <= high;
    }
    @Override
    public String toString() { 
        return String.format(low + "-" + high); 
    } 
}
class Field{
    int fieldId;
    String name;
    Range range1;
    Range range2;
    int index;
    public Field(int id, String n, Range r1, Range r2){
        fieldId = id;
        name = n;
        range1 = r1;
        range2 = r2;
        index = -1;
    }
    public boolean validForNumber(int num){
        return range1.inRange(num) || range2.inRange(num);
    }
}
class Ticket{
    int[] values;
    public Ticket(String text){
        String[] ticket = text.split(",");
        values = new int[ticket.length];
        int index = 0;
        for(String s : ticket){
            values[index++] = Integer.parseInt(s);
        }
    }
}