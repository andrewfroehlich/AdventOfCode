import java.io.*;
import java.util.*;

class Problem7 {
    public static void main(String args[]){
        File file = new File("/home/ec2-user/environment/AOC/Resources/problem7.txt");
        
        try{
            DAG d = buildDAG(file);
            System.out.println("Part 1: "+part1(d));
            System.out.println("Part 2: "+part2(d));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static DAG buildDAG(File file) throws Exception{
        BufferedReader br = new BufferedReader(new FileReader(file));
        String current; 
        DAG d = new DAG();
        while ((current = (br.readLine())) != null) {
            //example: muted lime bags contain 1 wavy lime bag, 1 vibrant green bag, 3 light yellow bags.
            String[] split1 = current.split(" bags contain ");
            String containingColor = split1[0];
            Node containingNode = d.add(containingColor);
            
            String[] split2 = split1[1].split(", ");
            int count;
            String countString;
            String containsColor;
            for(String c : split2){
                countString = c.substring(0, c.indexOf(" "));
                //"no" means no other bag, so containing edges will be empty
                if(!"no".equals(countString)){
                    count = Integer.parseInt(countString);
                    containsColor = c.substring(c.indexOf(" ")+1, c.lastIndexOf(" "));
                    Node containsNode = d.add(containsColor);
                    d.addEdge(containingNode, containsNode, count);
                }
            }
            
        } 
        
        return d;
    }
    
    public static int part1(DAG d){
        Node shinyGold = d.get("shiny gold");
        HashSet<String> possibleColors = new HashSet<String>();
        List<Edge> toTraverse = shinyGold.containedEdges;
        Edge currentEdge;
        while(toTraverse.size() > 0){
            currentEdge = toTraverse.get(0);
            toTraverse.remove(0);
            
            Node containingNode = currentEdge.big;
            if(!possibleColors.contains(containingNode.value)){
                possibleColors.add(containingNode.value);
                toTraverse.addAll(containingNode.containedEdges);
            }
        }
        
        return possibleColors.size();
    }
    
    public static int part2(DAG d) throws Exception{
        Node shinyGold = d.get("shiny gold");
        //Subtract 1 to not count the shiny gold bag itself
        return addCount(shinyGold.containsEdges) - 1;
    }
    
    public static int addCount(List<Edge> edges){
        if(edges == null || edges.size() == 0){
            return 1;
        } else {
            int returnVal = 1;
            for(Edge e : edges){
                returnVal += e.containsCount * addCount(e.small.containsEdges);
            }
            return returnVal;
        }
    }
}

// DAG does not enforce no cycles, but it does enforce creating only one Node per value
class DAG {
    HashMap<String, Node> refs;
    
    public DAG(){
        refs = new HashMap<String, Node>();
    }
    
    public Node add(String val){
        if(refs.containsKey(val)){
            return refs.get(val);
        } else {
            Node n = new Node(val);
            refs.put(val, n);
            return n;
        }
    }
    
    public Node get(String val){
        return refs.get(val);
    }
    
    public void addEdge(Node big, Node small, int count){
        Edge e = new Edge(big, small, count);
        big.containsEdges.add(e);
        small.containedEdges.add(e);
    }
}

class Node {
    List<Edge> containsEdges;
    List<Edge> containedEdges;
    String value;
    
    public Node(String val){
        this.value = val;
        this.containsEdges = new ArrayList<Edge>();
        this.containedEdges = new ArrayList<Edge>();
    }
}

class Edge {
    Node big;
    Node small;
    int containsCount;
    
    public Edge(Node big, Node small, int count){
        this.big = big;
        this.small = small;
        this.containsCount = count;
    }
}