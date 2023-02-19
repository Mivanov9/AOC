#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("input.txt");
    char paren;
    int floor = 0;
    int position = 0;
    while(file.get(paren)) {
        if(paren == '(')
            floor++;
        else if (paren == ')')
            floor--;
        else
            continue;
        position++;
        if(floor < 0)
            break;
    }
    std::cout << position << '\n';
}
