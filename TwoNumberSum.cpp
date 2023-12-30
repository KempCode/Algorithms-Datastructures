
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


