import java.io.*;
import java.util.*;
import java.time.*;

class Problem12 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem12.txt");
        DirectionHelper dh = new DirectionHelper();
        
        try{
            Instant i0 = Instant.now();
            System.out.println("Part 1: "+part1(file,dh));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+part2(file,dh));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    
    public static int part1(File file, DirectionHelper dh) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        int east = 0;
        int north = 0;
        char direction = 'E';
        
        String current;
        char lineDirection;
        int lineVal;
        while ((current = (br.readLine())) != null) {
            lineDirection = current.charAt(0);
            lineVal = Integer.parseInt(current.substring(1));
            
            if(lineDirection == 'F'){
                lineDirection = direction;
            }
            
            if(lineDirection == 'L' || lineDirection == 'R'){
                direction = dh.changeDirection(direction, lineDirection, lineVal);
            } else {
                int[] directionVector = dh.getDirectionVector(lineDirection);
                east += directionVector[0] * lineVal;
                north += directionVector[1] * lineVal;
            }
        }
        
        return Math.abs(east) + Math.abs(north);
    }
    
    public static int part2(File file, DirectionHelper dh) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        int east = 0;
        int north = 0;
        char direction = 'E';
        int waypointEast = 10;
        int waypointNorth = 1;
        
        String current;
        char lineDirection;
        int lineVal;
        while ((current = (br.readLine())) != null) {
            lineDirection = current.charAt(0);
            lineVal = Integer.parseInt(current.substring(1));
            
            if(lineDirection == 'F'){
                east += waypointEast * lineVal;
                north += waypointNorth * lineVal;
            } else if(lineDirection == 'L' || lineDirection == 'R'){
                Tuple t = dh.rotateWaypoint(waypointEast, waypointNorth, lineDirection, lineVal);
                waypointEast = t.left;
                waypointNorth = t.right;
            } else {
                int[] directionVector = dh.getDirectionVector(lineDirection);
                waypointEast += directionVector[0] * lineVal;
                waypointNorth += directionVector[1] * lineVal;
            }
        }
        
        return Math.abs(east) + Math.abs(north);
    }
}

class DirectionHelper{
    HashMap<Character, Tuple> map;
    char[] directionHelper;
    HashMap<Character, Integer> directionHelperMap;
    
    public DirectionHelper(){
        map = new HashMap<Character, Tuple>(4);
        map.put('N', new Tuple(0, 1));
        map.put('S', new Tuple(0, -1));
        map.put('E', new Tuple(1, 0));
        map.put('W', new Tuple(-1, 0));
        
        directionHelper = new char[] { 'N', 'E', 'S', 'W' };
        directionHelperMap = new HashMap<Character, Integer>(4);
        directionHelperMap.put('N', 0);
        directionHelperMap.put('E', 1);
        directionHelperMap.put('S', 2);
        directionHelperMap.put('W', 3);
    }
    
    public char changeDirection(char currentDirection, char turnDirection, int degrees){
        int unitMoves = (degrees % 360) / 90;
        if(turnDirection == 'L'){
            unitMoves *= -1;
        }
        int newIndex = (directionHelperMap.get(currentDirection) + unitMoves + 4) % 4;
        return directionHelper[newIndex];
    }
    
    public Tuple rotateWaypoint(int east, int north, char turnDirection, int degrees) throws Exception{
        if(turnDirection == 'L'){
            degrees *= -1;
        }
        degrees = (360 + degrees) % 360;
        if(degrees == 90){
            return new Tuple(north, -1 * east);
        } else if (degrees == 180){
            return new Tuple(-1 * east, -1 * north);
        } else if (degrees == 270){
            return new Tuple(-1 * north, east);
        } else if (degrees == 0){
            return new Tuple(-east, north);
        }
        
        throw new Exception(String.format("e = %s, n = %s, td = %s, deg = %s", 
            east, north, turnDirection, degrees));
    }
    
    public int[] getDirectionVector(char currentDirection){
        Tuple t = map.get(currentDirection);
        return new int[] { t.left , t.right };
    }
}

class Tuple{
    int left;
    int right;
    public Tuple(int l, int r){
        this.left = l;
        this.right = r;
    }
}