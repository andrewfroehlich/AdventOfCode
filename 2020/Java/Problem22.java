import java.io.*;
import java.util.*;
import java.time.*;

class Problem22 {
    static HashMap<String,Boolean> previousDecks;
    public static void main(String args[]){
        try{
            File file = new File("/home/ec2-user/environment/AOC2020/Resources/problem22.txt");
            Instant i0 = Instant.now();
            //System.out.println("Part 1: "+war(file, false));
            Instant i1 = Instant.now();
            System.out.println("Part 2: "+war(file, true));
            Instant i2 = Instant.now();
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static long war(File file, boolean recursive) throws Exception{
        // Build player decks in LinkedLists
        BufferedReader br = new BufferedReader(new FileReader(file));
        LinkedList<Integer> player1  = new LinkedList<Integer>();
        LinkedList<Integer> player2  = new LinkedList<Integer>();
        String current; 
        boolean player1done = false;
        previousDecks = new HashMap<String,Boolean>();
        StringBuilder player1string = new StringBuilder();
        StringBuilder player2string = new StringBuilder();
        while ((current = (br.readLine())) != null) {
            if(current.startsWith("Player 2")){
                player1done = true;
            } else if(!current.equals("") && !current.startsWith("Player")){
                Integer c = Integer.parseInt(current);
                if(player1done){
                    player2.addLast(c);
                    player2string.append(c).append(",");
                } else {
                    player1.addLast(c);
                    player1string.append(c).append(",");
                }
            }
        } 
        player1string.deleteCharAt(player1string.length()-1);
        player2string.deleteCharAt(player2string.length()-1);
        
        //printLists();
        //System.out.println(player1string.toString());
        //System.out.println(player2string.toString());
        
        // Play War
        int rounds = 0;
        while(!player1.isEmpty() && !player2.isEmpty()){
            //printLists(player1,player2);
            //System.out.println(String.format("P1: %s | P2: %s",player1string.toString(),player2string.toString()));
            if(previousDecks.containsKey(String.format("%s|%s",player1string.toString(),player2string.toString()))){
                System.out.println("Previous decks has seen this before! Player 1 wins!");
                break;
            }
            previousDecks.put(String.format("%s|%s",player1string.toString(),player2string.toString()), true);
            //System.out.println(String.format("%s|%s",player1string.toString(),player2string.toString()));
            Integer card1 = player1.removeFirst();
            player1string.delete(0, player1string.indexOf(",")+1);
            Integer card2 = player2.removeFirst();
            player2string.delete(0, player2string.indexOf(",")+1);
            boolean player1wins = false;
            if(recursive && player1.size() >= card1 && player2.size() >= card2){
                LinkedList<Integer> subP1 = new LinkedList<Integer>();
                StringBuilder p1sb = new StringBuilder();
                Iterator i1 = player1.iterator();
                for(int i=1; i <= card1; i++){
                    Integer n = (Integer)i1.next();
                    subP1.addLast(n);
                    p1sb.append(n).append(",");
                }
                LinkedList<Integer> subP2 = new LinkedList<Integer>();
                StringBuilder p2sb = new StringBuilder();
                Iterator i2 = player2.iterator();
                for(int i=1; i <= card2; i++){
                    Integer n = (Integer)i2.next();
                    subP2.addLast(n);
                    p2sb.append(n).append(",");
                }
                p1sb.deleteCharAt(p1sb.length()-1);
                p2sb.deleteCharAt(p2sb.length()-1);
                player1wins = subwar(subP1, subP2, p1sb, p2sb);
            } else {
                player1wins = card1 > card2;
            }
            
            if(player1wins){
                player1.addLast(card1);
                player1.addLast(card2);
                player1string.append(",").append(card1).append(",").append(card2);
            } else {
                player2.addLast(card2);
                player2.addLast(card1);
                player2string.append(",").append(card2).append(",").append(card1);
            }
            
            rounds++;
        }
        System.out.println("Rounds: "+rounds);
        
        printLists(player1, player2);
        
        LinkedList<Integer> winner = player1.isEmpty() ? player2 : player1;
        long returnVal = 0;
        int multiplier = winner.size();
        for(Integer item:winner){
            returnVal += item*multiplier;
            multiplier--;
        }
        return returnVal;
    }
    
    //returns true if Player 1 wins, false is Player 2 wins
    public static boolean subwar(LinkedList<Integer> player1, LinkedList<Integer> player2, StringBuilder p1sb, StringBuilder p2sb) throws Exception{
        boolean player1wins = false;
        //ArrayList<String> configsToAdd = new ArrayList<String>();
        while(!player1.isEmpty() && !player2.isEmpty()){
            /*if(previousDecks.containsKey(String.format("%s|%s",p1sb.toString(),p2sb.toString()))){
                //System.out.println(String.format("(subloop) Seen %s|%s before!", p1sb.toString(),p2sb.toString()));
                return previousDecks.get(String.format("%s|%s",p1sb.toString(),p2sb.toString()));
            }*/
            //configsToAdd.add(String.format("%s|%s",p1sb.toString(),p2sb.toString()));
            //System.out.println(String.format("Sub: %s|%s",p1sb.toString(),p2sb.toString()));
            Integer card1 = player1.removeFirst();
            Integer card2 = player2.removeFirst();
            //p1sb.delete(0, p1sb.indexOf(",")+1);
            //p2sb.delete(0, p2sb.indexOf(",")+1);
            if(player1.size() >= card1 && player2.size() >= card2){
                LinkedList<Integer> subP1 = new LinkedList<Integer>();
                Iterator i1 = player1.iterator();
                StringBuilder subp1sb = new StringBuilder();
                for(int i=1; i <= card1; i++){
                    Integer n = (Integer)i1.next();
                    subP1.addLast(n);
                    //subp1sb.append(n).append(",");
                }
                LinkedList<Integer> subP2 = new LinkedList<Integer>();
                Iterator i2 = player2.iterator();
                StringBuilder subp2sb = new StringBuilder();
                for(int i=1; i <= card2; i++){
                    Integer n = (Integer)i2.next();
                    subP2.addLast(n);
                    //subp2sb.append(n).append(",");
                }
                //subp1sb.deleteCharAt(subp1sb.length()-1);
                //subp2sb.deleteCharAt(subp2sb.length()-1);
                player1wins = subwar(subP1, subP2, subp1sb, subp2sb);
            } else {
                player1wins = (card1 > card2);
            }
            
            if(player1wins){
                player1.addLast(card1);
                player1.addLast(card2);
                //p1sb.append(",").append(card1).append(",").append(card2);
            } else {
                player2.addLast(card2);
                player2.addLast(card1);
                //p2sb.append(",").append(card1).append(",").append(card2);
            }
        }
        /*
        for(String c:configsToAdd){
            previousDecks.put(c, !player1.isEmpty());
        }*/
        return !player1.isEmpty();
    }
    
    public static void printLists(LinkedList<Integer> player1, LinkedList<Integer> player2){
        System.out.print("Player 1: ");
        for(Integer i:player1){
            System.out.print(i+" ");
        }
        System.out.print("\nPlayer 2: ");
        for(Integer i:player2){
            System.out.print(i+" ");
        }
        System.out.println("");
    }
}
