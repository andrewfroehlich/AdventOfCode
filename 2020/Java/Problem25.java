import java.io.*;
import java.util.*;
import java.time.*;

class Problem25 {
    public static void main(String args[]){
        Instant i0 = Instant.now();
        int publicKey1 = 15733400;
        int publicKey2 = 6408062;
        int loops = -1;
        
        int loopNumber = 0;
        long current = 1;
        while(true){
            if(current == publicKey1){
                loops = loopNumber;
                break;
            }
            current = (current * 7) % 20201227;
            loopNumber++;
        }
        
        current = 1;
        loopNumber = 0;
        while(loopNumber < loops){
            current = (current * publicKey2) % 20201227;
            loopNumber++;
        }
        
        System.out.println(String.format("Part 1: %s", current));
        Instant i1 = Instant.now();
        //TODO
        Instant i2 = Instant.now();
        System.out.println(String.format("Part 1: %s, Part 2: %s", 
            Duration.between(i0, i1).toMillis(),
            Duration.between(i1, i2).toMillis()));
    }
}