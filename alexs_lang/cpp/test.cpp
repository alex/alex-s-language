#include <iostream>

#include "src/base.cpp"

int main() {
    AlObj* print = new AlPrint();
    
    
    while (true) {
        AlObj* a = new AlInt(3);
        AlObj* b = new AlInt(4);
        ARG_TYPE args;
        args.push_back(*a+b);
//        (*print)(args, KWARG_TYPE());
    }
}
