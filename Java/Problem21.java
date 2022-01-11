import java.io.*;
import java.util.*;
import java.time.*;
import java.util.regex.Pattern;

class Problem21 {
    static ArrayList<Recipe> recipes;
    public static void main(String args[]){
        try{
            Instant i0 = Instant.now();
            //read everything in to build a list of "Recipes"
            File file = new File("/home/ec2-user/environment/AOC2020/Resources/problem21.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));
            String current; 
            recipes = new ArrayList<Recipe>();
            HashSet<String> unmatchedAllergens = new HashSet<String>();
            ArrayList<String> allergenList = new ArrayList<String>();
            while ((current = (br.readLine())) != null) {
                Recipe r = new Recipe(current);
                recipes.add(r);
                unmatchedAllergens.addAll(r.allergens);
            } 
            allergenList.addAll(unmatchedAllergens);
            
            //For each allergen that hasn't been identified yet, intersect the sets that have it to find the unique ingredient.
            //Then remove the unmatched ingredient and keep iterating until all are matched. Also add to dangerous list for part 2.
            ArrayList<Ingredient> dangerousIngredients = new ArrayList<Ingredient>();
            int index = 0;
            while(allergenList.size() > 0){
                if(index >= allergenList.size()){
                    index = 0;
                }
                String currentAllergen = allergenList.get(index);
                HashSet<String> matchingIngredients = null;
                for(Recipe r : recipes){
                    if(r.allergens.contains(currentAllergen)){
                        if(matchingIngredients == null){
                            matchingIngredients = new HashSet<String>(r.ingredients);
                        } else {
                            matchingIngredients.retainAll(r.ingredients);
                        }
                    }
                }
                //If there is only one matching ingredient, process it by removing it from the lists, and save it in a list for Part 2
                if(matchingIngredients.size() == 1){
                    String ing = matchingIngredients.toArray(new String[1])[0];
                    for(Recipe rec:recipes){
                        rec.allergens.remove(currentAllergen);
                        rec.ingredients.remove(ing);
                    }
                    allergenList.remove(index);
                    dangerousIngredients.add(new Ingredient(ing, currentAllergen));
                } else {
                    //Only increment the index if it wasn't processed, as removing the item from the list shifts indices anyway
                    index++;
                }
            }
            
            //All matched ingredients/allergens have been removed, simply count the ingredients left
            int returnVal = 0;
            for(Recipe r:recipes){
                returnVal += r.ingredients.size();
            }
            System.out.println("Part 1: "+returnVal);
            
            //Sort the dangerous ingredients by allergen (Ingredient is a Comparable) and output the ingredients
            Instant i1 = Instant.now();
            Collections.sort(dangerousIngredients);
            StringBuilder sb = new StringBuilder("Part 2: ");
            for(Ingredient in : dangerousIngredients){
                sb.append(in.ingredientName+",");
            }
            String ret = sb.toString();
            System.out.println(ret.substring(0, ret.length()-1));
            Instant i2 = Instant.now();
            
            System.out.println(String.format("Part 1: %s, Part 2: %s", 
                Duration.between(i0, i1).toMillis(),
                Duration.between(i1, i2).toMillis()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class Recipe {
    HashSet<String> ingredients;
    HashSet<String> allergens;
    public Recipe(String line){
        ingredients = new HashSet<String>();
        String[] split = line.split(Pattern.quote(" (contains "));
        String[] ing = split[0].split(" ");
        for(String i:ing){
            ingredients.add(i);
        }
        allergens = new HashSet<String>();
        if(split.length > 1){
            String allerg = split[1].replace(")","");
            String[] allSplit = allerg.split(", ");
            for(String a:allSplit){
                allergens.add(a);
            }
        }
    }
}
class Ingredient implements Comparable<Ingredient>{
    String ingredientName;
    String allergenName;
    public Ingredient(String i, String a){
        ingredientName = i;
        allergenName = a;
    }
    @Override
    public int compareTo(Ingredient i2) {
      return this.allergenName.compareTo(i2.allergenName);
    }
}