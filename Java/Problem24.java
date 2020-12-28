import java.io.*;
import java.util.*;
import java.time.*;

class Problem24 {
    public static void main(String args[]){
        try{
            File file = new File("/home/ec2-user/environment/AOC2020/Resources/problem24.txt");
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+part1(file));
            Instant i1 = Instant.now();
            //TODO
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static int part1(File file) throws Exception{
        HashSet<String> blackTiles = new HashSet<String>();
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        while ((current = (br.readLine())) != null) {
            int row = 0;
            int col = 0;
            for(int i = 0; i < current.length(); i++){
                String direction = ""+current.charAt(i);
                if(direction.equals("n") || direction.equals("s")){
                    direction = direction + current.charAt(++i);
                }
                
                switch(direction){
                    case "w":
                        col--;
                        break;
                    case "e":
                        col++;
                        break;
                    case "nw":
                        if(row % 2 == 0){
                            row++;
                        } else {
                            row++;
                            col--;
                        }
                        break;
                    case "sw":
                        if(row % 2 == 0){
                            row--;
                        } else {
                            row--;
                            col--;
                        }
                        break;
                    case "ne":
                        if(row % 2 == 0){
                            row++;
                            col++;
                        } else {
                            row++;
                        }
                        break;
                    case "se":
                        if(row % 2 == 0){
                            row--;
                            col++;
                        } else {
                            row--;
                        }
                        break;
                    default:
                        System.out.println("Something went wrong");
                        break;
                }
            }
            
            String coord = String.format("%s,%s",row,col);
            if(blackTiles.contains(coord)){
                blackTiles.remove(coord);
            } else {
                blackTiles.add(coord);
            }
        } 
        
        return blackTiles.size();
    }
}
