import java.io.*;
import java.util.*;

class Problem8 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem8.txt");
        
        try{
            ArrayList<Line> lines = buildInstructions(file);
            System.out.println("Part 1: "+part1(lines));
            lines = resetInstructions(lines);
            System.out.println("Part 2: "+part2(lines));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static ArrayList<Line> buildInstructions(File file) throws Exception{
        ArrayList<Line> lines = new ArrayList<Line>();
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        while ((current = (br.readLine())) != null) {
            Line t = new Line(current);
            lines.add(t);
        } 
        return lines;
    }
    
    public static ArrayList<Line> resetInstructions(ArrayList<Line> list){
        for(Line l:list){
            l.reset();
        }
        return list;
    }
    
    public static int part1(ArrayList<Line> lines){
        int acc = 0;
        int index = 0;
        Line current = lines.get(index);
        while(current != null && !current.visited){
            current.visited = true;
            if(current.instruction.equals("jmp")){
                index += current.number;
            } else if(current.instruction.equals("acc")){
                acc += current.number;
                index++;
            } else {
                index++;
            }
            current = lines.get(index);
        }
        return acc;
    }
    
    public static int part2(ArrayList<Line> lines) throws Exception{
        // hold onto all the elements that make up the loop, but not the elements before it
        HashSet<Integer> loopIndexes = new HashSet<Integer>();
        int acc = 0;
        int index = 0;
        Line current = lines.get(index);
        while(current != null && !loopIndexes.contains(index)){
            if(current.visited){
                loopIndexes.add(index);
            }
            current.visited = true;
            if(current.instruction.equals("jmp")){
                index += current.number;
            } else if(current.instruction.equals("acc")){
                acc += current.number;
                index++;
            } else {
                index++;
            }
            current = lines.get(index);
        }
        lines = resetInstructions(lines);
        
        //iterate over the loop indices swapping nops and jmps to find the issue
        Iterator<Integer> iter = loopIndexes.iterator();
        int swapIndex;
        while(iter.hasNext()){
            swapIndex = iter.next();
            if("acc".equals(lines.get(swapIndex).instruction)){
                continue;
            }
            
            acc = 0;
            index = 0;
            current = lines.get(index);
            while(current != null && !current.visited){
                current.visited = true;
                if(current.instruction.equals("jmp")){
                    if(index == swapIndex){
                        index++;
                    } else {
                        index += current.number;
                    }
                } else if(current.instruction.equals("acc")){
                    acc += current.number;
                    index++;
                } else {
                    if(index == swapIndex){
                        index += current.number;
                    } else {
                        index++;
                    }
                }
                
                // if we are out of the bounds of indices, we terminate
                if(index == lines.size()){
                    return acc;
                }
                current = lines.get(index);
            }
            
            lines = resetInstructions(lines);
        }
        
        return -1;
    }
}


class Line {
    String instruction;
    int number;
    boolean visited;
    
    public Line(String i, int n){
        this.instruction = i;
        this.number = n;
        this.visited = false;
    }
    
    public Line(String fullLine){
        String[] temp = fullLine.split(" +");
        this.instruction = temp[0];
        this.number = Integer.parseInt(temp[1]);
        this.visited = false;
    }
    
    public void reset(){
        this.visited = false;
    }
}