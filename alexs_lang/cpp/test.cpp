#include <iostream>

#include "alobj.h"
#include "alint.h"

int main() {
    AlObj* a = new AlInt(3);
    AlObj* b = new AlInt(4);
    std::cout << *a+b << std::endl;
}
