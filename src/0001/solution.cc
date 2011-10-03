#include <iostream>

//SOLVED

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

void method2() {
    int i = 3, j = 5, k = 15, sum3 = 0, sum5 = 0, sum15 = 0;
    for (i = 3;  i < 1000; i += 3)  { sum3  += i; }
    for (i = 5;  i < 1000; i += 5)  { sum5  += i; }
    for (i = 15; i < 1000; i += 15) { sum15 += i; }
    cout << "Method 2: " << sum3 + sum5 - sum15 << endl;
}

int main(int argc, char **argv) {
    method1();
    method2();
    return 0;
}
