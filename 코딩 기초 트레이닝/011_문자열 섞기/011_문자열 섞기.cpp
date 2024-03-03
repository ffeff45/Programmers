#include <string>
#include <vector>

using namespace std;

string solution(string str1, string str2) {
    string answer = "";
    int length1 = str1.length();
    int length2 = str2.length();
    
    if(1 <= length1 == length2 <= 10){
        for(int i =0; i < length1; i++){
            answer.push_back(str1[i]);
            answer.push_back(str2[i]);
        }
    }
    return answer;
}