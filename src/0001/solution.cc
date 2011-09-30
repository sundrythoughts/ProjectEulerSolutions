#include <iostream>

using namespace std;

void method1() {
    int ans = 0;
    for (int i = 3; i < 1000; ++i) {
        if (i % 3 == 0 || i % 5 == 0) {
            ans += i;
        }
    }
    cout << "Method 1: " << ans << endl;
}

int main(int argc, char **argv) {
    method1();
    return 0;
}
