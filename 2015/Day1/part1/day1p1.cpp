#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("input.txt");
    char paren;
    int floor = 0;
    while(file.get(paren)) {
        if(paren == '(')
            floor++;
        else if (paren == ')')
            floor--;
    }
    std::cout << floor << '\n';
}
