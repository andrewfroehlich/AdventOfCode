import java.io.*;
import java.util.*;
import java.time.*;

class Problem11 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem11.txt");
        
        try{
            Instant i0 = Instant.now();
            Airplane a = new Airplane(file);
            System.out.println("Part 1: "+part1(a));
            System.out.println("Iterations = "+a.iterationsRun);
            Instant i1 = Instant.now();
            a = new Airplane(file);
            System.out.println("Part 2: "+part2(a));
            System.out.println("Iterations = "+a.iterationsRun);
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static int part1(Airplane a) throws Exception{
        while(a.runIteration1()){
            // will break when nothing changed
        }
        return a.currentOccupied();
    }
    
    public static int part2(Airplane a) throws Exception{
        while(a.runIteration2()){
            // will break when nothing changed
        }
        return a.currentOccupied();
    }
}

class Airplane {
    SeatValue[][] seats;
    int iterationsRun;
    
    public Airplane(File file) throws Exception{
        iterationsRun = 0;
        
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current = br.readLine();
        seats = new SeatValue[94][current.length()];
        int line = 0;
        do {
            for(int i = 0; i < current.length(); i++){
                if(current.charAt(i) == '.'){
                    seats[line][i] = SeatValue.FLOOR;
                } else {
                    seats[line][i] = SeatValue.EMPTY;
                }
            }
            line++;
        } while ((current = (br.readLine())) != null);
    }
    
    public int getAdjacentOccupied1(int line, int col){
        int occupied = 0;
        for(int i = line-1 ; i <= line+1 ; i++) {
            if(i >= 0 && i < seats.length) {
                for(int j = col-1 ; j <= col+1 ; j++) {
                    if(j >= 0 && j < seats[line].length && !(i == line && j == col) && 
                        (seats[i][j] == SeatValue.OCCUPIED || seats[i][j] == SeatValue.OCCUPIED_TO_EMPTY)){
                        occupied++;
                    }
                }
            }
        }
        return occupied;
    }
    
    // returns if anything changed
    public boolean runIteration1(){
        iterationsRun++;
        
        SeatValue current;
        // Loop through to mark ones that are to change
        boolean seatChanged = false;
        for(int i=0; i<seats.length; i++){
            for(int j=0; j<seats[i].length; j++){
                current = seats[i][j];
                if(current == SeatValue.EMPTY && getAdjacentOccupied1(i,j) == 0){
                    seats[i][j] = SeatValue.EMPTY_TO_OCCUPIED;
                    seatChanged = true;
                } else if(current == SeatValue.OCCUPIED && getAdjacentOccupied1(i,j) >= 4){
                    seats[i][j] = SeatValue.OCCUPIED_TO_EMPTY;
                    seatChanged = true;
                }
            }
        }
        // Loop again to change the values
        if(seatChanged){
            for(int i=0; i<seats.length; i++){
                for(int j=0; j<seats[i].length; j++){
                    current = seats[i][j];
                    if(current == SeatValue.EMPTY_TO_OCCUPIED){
                        seats[i][j] = SeatValue.OCCUPIED;
                    } else if(current == SeatValue.OCCUPIED_TO_EMPTY){
                        seats[i][j] = SeatValue.EMPTY;
                    }
                }
            }
        }
        
        return seatChanged;
    }
    
    public int getInSightOccupied2(int line, int col){
        int occupied = 0;
        int currentLine = line;
        int currentCol = col;
        
        //up
        currentLine--;
        while(currentLine >= 0){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine--;
        }
        currentLine = line;
        
        //down
        currentLine++;
        while(currentLine < seats.length){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine++;
        }
        currentLine = line;
        
        //left
        currentCol--;
        while(currentCol >= 0){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentCol--;
        }
        currentCol = col;
        
        //right
        currentCol++;
        while(currentCol < seats[currentLine].length){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentCol++;
        }
        currentCol = col;
        
        //up-left
        currentLine--;
        currentCol--;
        while(currentLine >= 0 && currentCol >= 0){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine--;
            currentCol--;
        }
        currentLine = line;
        currentCol = col;
        
        //up-right
        currentLine--;
        currentCol++;
        while(currentLine >= 0 && currentCol < seats[currentLine].length){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine--;
            currentCol++;
        }
        currentLine = line;
        currentCol = col;
        
        //down-left
        currentLine++;
        currentCol--;
        while(currentLine < seats.length && currentCol >= 0){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine++;
            currentCol--;
        }
        currentLine = line;
        currentCol = col;
        
        //down-right
        currentLine++;
        currentCol++;
        while(currentLine < seats.length && currentCol < seats[currentLine].length ){
            if(seats[currentLine][currentCol] == SeatValue.OCCUPIED 
                || seats[currentLine][currentCol] == SeatValue.OCCUPIED_TO_EMPTY){
                occupied++;
                break;
            } else if(seats[currentLine][currentCol] == SeatValue.EMPTY 
                || seats[currentLine][currentCol] == SeatValue.EMPTY_TO_OCCUPIED){
                break;
            }
            currentLine++;
            currentCol++;
        }
        currentLine = line;
        currentCol = col;
        
        return occupied;
    }
    
    // returns if anything changed
    public boolean runIteration2(){
        iterationsRun++;
        
        SeatValue current;
        // Loop through to mark ones that are to change
        boolean seatChanged = false;
        for(int i=0; i<seats.length; i++){
            for(int j=0; j<seats[i].length; j++){
                current = seats[i][j];
                if(current == SeatValue.EMPTY && getInSightOccupied2(i,j) == 0){
                    seats[i][j] = SeatValue.EMPTY_TO_OCCUPIED;
                    seatChanged = true;
                } else if(current == SeatValue.OCCUPIED && getInSightOccupied2(i,j) >= 5){
                    seats[i][j] = SeatValue.OCCUPIED_TO_EMPTY;
                    seatChanged = true;
                }
            }
        }
        // Loop again to change the values
        if(seatChanged){
            for(int i=0; i<seats.length; i++){
                for(int j=0; j<seats[i].length; j++){
                    current = seats[i][j];
                    if(current == SeatValue.EMPTY_TO_OCCUPIED){
                        seats[i][j] = SeatValue.OCCUPIED;
                    } else if(current == SeatValue.OCCUPIED_TO_EMPTY){
                        seats[i][j] = SeatValue.EMPTY;
                    }
                }
            }
        }
        
        return seatChanged;
    }
    
    public int currentOccupied(){
        int occupied = 0;
        for(int i=0; i<seats.length; i++){
            for(int j=0; j<seats[i].length; j++){
                if(seats[i][j] == SeatValue.OCCUPIED){
                    occupied++;
                } 
            }
        }
        return occupied;
    }
}

enum SeatValue {
    FLOOR,
    EMPTY,
    OCCUPIED,
    OCCUPIED_TO_EMPTY,
    EMPTY_TO_OCCUPIED
}
