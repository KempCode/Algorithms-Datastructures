
// sample input
//array = [3, 5, -4, 8, 11, 1, -1, 6] 
//targetSum = 10
//sample output
//[-1, 11]

// O(N^2) time and space is O(1) as outputArray has 
//at most 2 items in it. size of array doesnt effect size complexity
#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
  vector<int> outputArray;
  for(auto &it : array){
      for(auto &ij : array){
        if ((it + ij == targetSum) && (outputArray.size() <= 1) && (it != ij)){
          outputArray.push_back(it);
          outputArray.push_back(ij);
          break;
        }
      }
  }
  return outputArray;
}


//O(N) Time and O(N) Space
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  unordered_set<int> myDict;
  //currentNum + y = targetSum
  // SO y = targetSum - currentNum
  // y = potentialMatch
  for(int i = 0; i < array.size(); i++){
    int currentNum = array[i];
    int potentialMatch = targetSum - currentNum;
    myDict.insert(currentNum);

    if(myDict.find(potentialMatch) != myDict.end()){
      // If id does exist in dictionary.
      if(currentNum + potentialMatch == targetSum && currentNum != potentialMatch){
        return vector<int>{currentNum, potentialMatch};
      }
    }
  }
  return{};
}





//O(nlogn) time and O(1) space
// O(n) is better - my solution 2 is best.

// obviously sort array first,
// left pointer to the 1st number, right pointer to the end number
//is L + R == answer ??
    // if we want smaller sum move right left,
    //if we want larger sum move left right.
#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  //sort vector...
  sort(array.begin(), array.end());
  // Write your code here
  // initialise initial positions outside of the loop...
  int leftPos = 0;
  int rightPos = array.size()-1;
 

  for(int i = 0; i < array.size(); i++){
    //start of loop always update left and right with their positions.
    int left = array[leftPos];
    int right = array[rightPos];
    
    if (left + right == targetSum){
      return vector<int>{left, right};
    }
    else if(left + right > targetSum){
      // if we want smaller sum move right left,
      // update the position
      rightPos -= 1;

    }else{
      // We want a larger sum. move left right.
      leftPos += 1;

    }
    
  }
  // If no such pair is found, return an empty vector
  return vector<int>{};
}
