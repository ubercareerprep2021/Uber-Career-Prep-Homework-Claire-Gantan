import java.util.*;

public class Part2 {
   public static void main(String[] args) {
   // test cases
   System.out.println(isStringPermutation("asdf","fsda"));//should be true
   System.out.println(isStringPermutation("asdf","fsa"));//should be false
   System.out.println(isStringPermutation("asdf","fsax"));//should be false
   System.out.println(isStringPermutation("as/f","fsa/"));//should be true
   System.out.println(isStringPermutation("asda","dsa"));//should be false

   List<Integer> input = new ArrayList<Integer>();
   System.out.println(pairsThatEqualSum(input, 1));// == []
   input.add(4);
   input.add(-3);
   input.add(1);
   input.add(2);
   input.add(5);
   System.out.println(pairsThatEqualSum(input, 7));// == [(2, 5), (3, 4)]
   System.out.println(pairsThatEqualSum(input, 5));// == [(1, 4), (2, 3)]
   System.out.println(pairsThatEqualSum(input, 1));// == []
   input.remove(1);
   input.add(2);
   System.out.println(pairsThatEqualSum(input, 4));// == [(2,2)]
   }

  /*Examples
  isStringPermutation(s1: "asdf", s2: "fsda") == true
  isStringPermutation(s1: "asdf", s2: "fsa") == false
  isStringPermutation(s1: "asdf", s2: "fsax") == false*/
  //Outline:
  //count the number of times each letter shows up in the first String and check if the second String works as well
  public static boolean isStringPermutation(String s1, String s2) {
    // first attempt
    // int[] counter = new int[26]; // wont work for all Strings (want to try Hash Map?) -- change length to 128
    // for (int i=0; i<s1.length(); i++){
    //   char c = s1.charAt(i);
    //   counter[c-'a']++;
    // }
    // for (int i=0; i<s2.length(); i++){
    //   char c2 = s2.charAt(i);
    //   if (counter[c2-'a'] > 0){
    //     counter[c2-'a']--;
    //   } else {
    //     return false;
    //   }
    // }
    // return true;
    HashMap counter = new HashMap();
    for (int i = 0; i<s1.length(); i++){
      char c = s1.charAt(i);
      if (counter.containsKey(c)){
        counter.put(c,(int)counter.get(c) + 1);
      } else {
        counter.put(c,1);
      }
    }
    for (int i=0; i<s2.length(); i++){
      char c2 = s2.charAt(i);
      if (counter.containsKey(c2) && (int)(counter.get(c2)) > 0){
        counter.put(c2,(int)counter.get(c2)-1);
        counter.remove(c2,0);//removes if equal to zero
      } else {
        return false;
      }
    }
    if (counter.size() ==0){
      return true;
    }
    return false;
  }

  /*Examples
  pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
  pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
  pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]
  */
  //Outline: go through HALF of list and add tuple if rest of the list contains   targetSum -i for a list value i
  //ASSUMED doubles (i.e. counting (2,2) as a valid tuple for targetSum 4 if there is only one value of 2) are valid
  public static List<List<Integer>> pairsThatEqualSum(List<Integer> inputArray, Integer targetSum) {
    List<List<Integer>> result = new ArrayList<List<Integer>>();//HashMap values instead
    for (int i=0; i<inputArray.size(); i++){
      int num = inputArray.get(i);
      if (inputArray.indexOf(targetSum-num) >= i){
        List<Integer> temp = new ArrayList<Integer>();
        temp.add(num);
        temp.add(targetSum-num);
        result.add(temp);
      }
    }
    return result;
  }

}

//TIMING
//initial code writing/understanding problems 6:45-7:10
//edits after running code 7:10-7:33
//total time = 48 min

//reflection: took me longer than I expected and I think I used more complex code than needed for isStringPermutation
