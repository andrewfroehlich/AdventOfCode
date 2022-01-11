import java.io.*;
import java.util.*;
import java.time.*;

class Problem20 {
    public static void main(String args[]){
        try{
            File file = new File("/home/ec2-user/environment/AOC2020/Resources/problem20.txt");
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
    
    public static long part1(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        HashMap<String,HashSet<Integer>> h = new HashMap<String,HashSet<Integer>>();
        while ((current = (br.readLine())) != null) {
            // grab a full tile
            int tileId = -1;
            ArrayList<String> temp = new ArrayList<String>();
            while(current != null && !current.trim().equals("\n") && !current.trim().equals("")){
                if(current.contains("Tile")){
                    tileId = Integer.parseInt(current.substring(5,9));
                } else {
                    temp.add(current);
                }
                current = br.readLine();
            }
            // grab the edges of the tile
            ArrayList<String> edges = new ArrayList<String>(4);
            edges.add(temp.get(0));
            edges.add(temp.get(temp.size()-1));
            StringBuilder sb1 = new StringBuilder();
            StringBuilder sb2 = new StringBuilder();
            for(String s:temp){
                sb1.append(s.charAt(0));
                sb2.append(s.charAt(s.length()-1));
            }
            edges.add(sb1.toString());
            edges.add(sb2.toString());
            // for each edge, update the hashtable with edge -> tileId containing that edge. Same for reverse of the edge
            for(String edge:edges){
                if(h.containsKey(edge)){
                    HashSet<Integer> ids = h.get(edge);
                    ids.add(tileId);
                    h.put(edge, ids);
                    h.put((new StringBuffer(edge)).reverse().toString(), ids);
                } else {
                    HashSet<Integer> ids = new HashSet<Integer>();
                    ids.add(tileId);
                    h.put(edge, ids);
                    h.put((new StringBuffer(edge)).reverse().toString(), ids);
                }
            }
        } 
        
        // Count the matches per edge to find what tiles have 2 unmatched edges
        HashMap<Integer,Integer> edgesWithNoMatchPerId = new HashMap<Integer,Integer>();
        Iterator it = h.entrySet().iterator();
        long returnNumber = 1;
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            HashSet<Integer> hs = (HashSet<Integer>)pair.getValue();
            if( hs.size() == 1 ){
                int tId = hs.toArray(new Integer[1])[0];
                if(edgesWithNoMatchPerId.containsKey(tId)){
                    int count = edgesWithNoMatchPerId.get(tId);
                    count++;
                    // 4 rather than 2, as the reverses are also in the list
                    if(count == 4){
                        returnNumber *= tId;
                    }
                    edgesWithNoMatchPerId.put(tId, count);
                } else {
                    edgesWithNoMatchPerId.put(tId, 1);
                }
                
            }
            it.remove();
        }
        
        return returnNumber;
    }
    
    public static int part2(File file) throws Exception{
        //TODO
        return -1;
    }
}