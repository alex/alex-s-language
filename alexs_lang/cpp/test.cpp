
#include "src/base.cpp"



int main() {
    AlObj* print = new AlPrint();
    ARG_TYPE t0;
t0.push_back(*(new AlInt(3)) + new AlInt(4));
(*print)(t0, KWARG_TYPE());
}
