import java.io.*;
import java.util.*;
import java.time.*;

class Problem17 {
    public static void main(String args[]){
        try{
            Instant i0 = Instant.now();
            File file = new File("/home/ec2-user/environment/AOC/Resources/problem17.txt");
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
        Grid g = new Grid(file, false);
        while(g.cycles < 6){
            g.runCycle();
        }
        return g.activeCount();
    }
    
    public static int part2(File file) throws Exception{
        Grid g = new Grid(file, true);
        while(g.cycles < 6){
            g.runCycle();
        }
        return g.activeCount();
    }
}

class Grid{
    HashMap<Coordinate,Cube> grid;
    int x_low, x_high, y_low, y_high, z_low, z_high, w_low, w_high, cycles;
    boolean part2;
    
    public Grid(File file, boolean isPart2) throws Exception{
        grid = new HashMap<Coordinate,Cube>();
        
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        int x = 0;
        while ((current = (br.readLine())) != null) {
            for(int y=0; y < current.length(); y++){
                grid.put(new Coordinate(x, y, 0, 0), current.charAt(y) == '#' ? Cube.ACTIVE : Cube.INACTIVE);
            }
            x++;
            y_high = current.length() - 1;
        } 
        
        x_low = 0;
        x_high = x;
        y_low = 0;
        z_low = 0;
        z_high = 0;
        w_low = 0;
        w_high = 0;
        cycles = 0;
        part2 = isPart2;
    }
    
    public void runCycle(){
        cycles++;
        
        x_low--;
        y_low--;
        z_low--;
        x_high++;
        y_high++;
        z_high++;
        if(part2){
            w_low--;
            w_high++;
        }
        
        // update all to intermediate states
        for(int x=x_low; x<=x_high; x++){
            for(int y=y_low; y<=y_high; y++){
                for(int z=z_low; z<=z_high; z++){
                    for(int w=w_low; w<=w_high; w++){
                        Coordinate c = new Coordinate(x,y,z,w);
                        if(isActive(c) && checkActiveToInactive(c)){
                            grid.put(c, Cube.ACTIVE_TO_INACTIVE);
                        } else if(!isActive(c) && checkInactiveToActive(c)){
                            grid.put(c, Cube.INACTIVE_TO_ACTIVE);
                        }
                    }
                }
            }
        }
        
        // finalize intermediate states
        for(int x=x_low; x<=x_high; x++){
            for(int y=y_low; y<=y_high; y++){
                for(int z=z_low; z<=z_high; z++){
                    for(int w=w_low; w<=w_high; w++){
                        Coordinate c = new Coordinate(x,y,z,w);
                        if(grid.containsKey(c)){
                            if(grid.get(c) == Cube.INACTIVE_TO_ACTIVE){
                                grid.put(c, Cube.ACTIVE);
                            } else if(grid.get(c) == Cube.ACTIVE_TO_INACTIVE){
                                grid.put(c, Cube.INACTIVE);
                            }
                        }
                    }
                }
            }
        }
    }
    public Cube getCube(Coordinate c){
        return grid.containsKey(c) ? grid.get(c) : Cube.INACTIVE;
    }
    public boolean isActive(Coordinate c){
        return isActive(getCube(c));
    }
    public boolean isActive(Cube value){
        return value == Cube.ACTIVE || value == Cube.ACTIVE_TO_INACTIVE;
    }
    public boolean checkActiveToInactive(Coordinate c){
        int adjacentActive = 0;
        int w_low = c.w;
        int w_high = c.w;
        if(part2){
            w_low--;
            w_high++;
        }
        for(int x=c.x-1; x<=c.x+1; x++){
            for(int y=c.y-1; y<=c.y+1; y++){
                for(int z=c.z-1; z<=c.z+1; z++){
                    for(int w=w_low; w<=w_high; w++){
                        if(!(x == c.x && y == c.y && z == c.z && w == c.w) && isActive(new Coordinate(x,y,z,w))){
                            adjacentActive++;
                            if(adjacentActive > 3){
                                return true;
                            }
                        }
                    }
                }
            }
        }
        
        return !(adjacentActive == 2 || adjacentActive == 3);
    }
    public boolean checkInactiveToActive(Coordinate c){
        int adjacentActive = 0;
        int w_low = c.w;
        int w_high = c.w;
        if(part2){
            w_low--;
            w_high++;
        }
        for(int x=c.x-1; x<=c.x+1; x++){
            for(int y=c.y-1; y<=c.y+1; y++){
                for(int z=c.z-1; z<=c.z+1; z++){
                    for(int w=w_low; w<=w_high; w++){
                        if(!(x == c.x && y == c.y && z == c.z && w == c.w) && isActive(new Coordinate(x,y,z,w))){
                            adjacentActive++;
                            if(adjacentActive > 3){
                                return false;
                            }
                        }
                    }
                }
            }
        }
        
        return (adjacentActive == 3);
    }
    public int activeCount(){
        int active = 0;
        for(int x=x_low; x<=x_high; x++){
            for(int y=y_low; y<=y_high; y++){
                for(int z=z_low; z<=z_high; z++){
                    for(int w=w_low; w<=w_high; w++){
                        if(isActive(new Coordinate(x,y,z,w))){
                            active++;
                        }
                    }
                }
            }
        }
        return active;
    }
}
class Coordinate{
    int x;
    int y;
    int z;
    int w;
    public Coordinate(int xval, int yval, int zval, int wval){
        x = xval;
        y = yval;
        z = zval;
        w = wval;
    }
    @Override
    public int hashCode() {
        return ((Integer)(x + 4*y + 9*z + 13*w)).hashCode();
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        Coordinate c = (Coordinate)obj;
        return this.x == c.x && this.y == c.y && this.z == c.z && this.w == c.w;
    }
}
enum Cube{
    ACTIVE,
    INACTIVE,
    ACTIVE_TO_INACTIVE,
    INACTIVE_TO_ACTIVE
}