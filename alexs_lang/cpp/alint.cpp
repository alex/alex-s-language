#include "alint.h"
#include "alfunction.h"

class AddInts : public AlFunction  {
    AlObj* operator()(AlInt* self, AlInt* other)  {
        return new AlInt(self->value + other->value);
    }
};

AlInt::AlInt()  {
    this->value = 0;
    this->setup();
}

AlInt::AlInt(int val)   {
    this->value = val;
    this->setup();
}

void AlInt::setup() {
    this->attrs["__add__"] = new AddInts();
}

