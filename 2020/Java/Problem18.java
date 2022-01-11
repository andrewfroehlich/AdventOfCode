import java.io.*;
import java.util.*;
import java.time.*;

class Problem18 {
    public static void main(String args[]){
        try{
            File file = new File("/home/ec2-user/environment/AOC/Resources/problem18.txt");
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+solve(file, false));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+solve(file, true));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static long solve(File file, boolean part2) throws Exception{
        Expression e = new Expression();
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        long returnVal = 0;
        while ((current = (br.readLine())) != null) {
            returnVal += e.solve(current, part2);
        } 
        return returnVal;
    }
}

class Expression {
    Stack<Character> operations;
    Stack<Long> values;
    
    public Expression(){
        operations = new Stack<Character>();
        values = new Stack<Long>();
    }
    
    public long solve(String exp, boolean part2){
        char c;
        for(int i = 0; i < exp.length(); i++){
            c = exp.charAt(i);
            if(c == ' ') continue;
            else if(c == '+' || c == '*' || c == '(') operations.push(c);
            else if(c == ')'){
                runOperations();
                operations.pop();
                if(part2) runPlusOnly();
                else runOperations();
            }
            else {
                values.push((long)Character.getNumericValue(c));
                if(part2) runPlusOnly();
                else runOperations();
            }
        }
        
        runOperations();
        return values.pop();
    }
    
    public void runPlusOnly(){
        while(!operations.empty() && operations.peek() == '+'){
            operations.pop();
            values.push(values.pop() + values.pop());
        }
    }
    
    public void runOperations(){
        while(!operations.empty() && operations.peek() != '('){
            char op = operations.pop();
            long val = values.pop();
            if(op == '+') val = values.pop() + val;
            else if(op == '*') val = values.pop() * val;
            values.push(val);
        }
    }
}