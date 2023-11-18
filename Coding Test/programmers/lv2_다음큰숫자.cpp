#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;
    int n_copy = n;
    int num_one = 1;
    
    while (true) {
        if (n_copy==1) {
            break;
        }
        if (n_copy%2==1){
            num_one++;
        }
        n_copy /= 2;
    }
    n_copy = n;
    
    while (true) {
        n_copy++;
        int tmp = n_copy;
        int num_one_copy = 1;    
        while (true) {
            if (tmp==1) {
                break;
            }
            if (tmp%2==1){
                num_one_copy++;
            }
            tmp /= 2;
        }
        if (num_one_copy == num_one) {
            answer = n_copy;
            break;
        }
    }
    
    return answer;
}