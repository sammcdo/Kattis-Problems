#include 
#include 

using namespace std;

int main() {
    vector nums;
    int count = 0;
    
    for (int i = 0; i < 10; i++) {
        int tmp;
        cin >> tmp;
        nums.push_back(tmp % 42);
    }
    
    for (int i = 0; i < 10; i++) {
        bool found = false;
        for (int j = 0; j < i; j++) {
            if (nums[i] == nums[j]) {
                found = true;
            }
        }
        if (found == false) {
            count++;
        }
    }

    cout << count << endl;
}