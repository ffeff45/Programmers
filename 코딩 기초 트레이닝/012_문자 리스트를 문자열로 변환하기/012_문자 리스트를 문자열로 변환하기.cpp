#include <string>
#include <vector>

using namespace std;

string solution(vector<string> arr) {
    string answer = "";
    int size = arr.size();
    
    if(1 <= size <= 200){
        for(int i = 0; i < size; i++){
            answer += arr[i];
        }
    }
    return answer;
}