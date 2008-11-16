#include <iostream>

#include "src/base.cpp"

int main() {
    AlObj* print = new AlPrint();
    
    for (int i = 0; ; i++) {
        AlObj* a = new AlInt(3);
        if (i % 100000 == 0) {
            std::cout << GC_get_heap_size() << std::endl;
        }
        
//        AlObj* b = new AlInt(4);
//        ARG_TYPE args;
//        args.push_back(*a+b);
//        (*print)(args, KWARG_TYPE());
    }
}
