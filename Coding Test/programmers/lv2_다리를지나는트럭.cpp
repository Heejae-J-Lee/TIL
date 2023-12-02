#include <string>
#include <vector>
#include <queue>
//#include <iostream>
using namespace std;
typedef pair<int,int> truck_state;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    
    queue<truck_state> q;
    int quantity_trucks = truck_weights.size();
    int cur_weight = 0;
    int next_truck = 0;
    while (true) {
        answer++;
        //cout << "second : " << answer << '\n';
        
        if (!q.empty()) {
            truck_state front_truck = q.front();
            //cout << "first truck is " << front_truck.first << " in " << front_truck.second << '\n';
            if ((front_truck.second + bridge_length) == answer) {
                cur_weight -= truck_weights[front_truck.first];
                q.pop();
            }
        }
        
        if (next_truck < quantity_trucks) {
            if (((cur_weight + truck_weights[next_truck]) <= weight) && q.size() < bridge_length) {
                q.push({next_truck, answer});
                cur_weight += truck_weights[next_truck];
                next_truck++;
            }
        }
        

        //cout << "cur weight : " << cur_weight << " next truck is " << next_truck << '\n';
        if ((next_truck == quantity_trucks) && q.empty())    break;
    }
    return answer;
}