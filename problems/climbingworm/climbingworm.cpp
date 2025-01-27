#include 

using namespace std;

int main() {
    int a, b, c;
    int position;
    int count = 0;
    
    cin >> a >> b >> c;
    
    position = 0;
    
    
    while (position <= c) {
        position += a;
        count++;
        
        if (position >= c) {
            break;
        }
        
        position -= b;
        
    }
    
    cout << count << endl;
    
    return 0;
}