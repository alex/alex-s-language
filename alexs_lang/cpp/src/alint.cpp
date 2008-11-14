#include <cmath>
#include <sstream>

#include "alobj.h"
#include "alint.h"
#include "alfunction.h"
#include "alstring.h"

class AddInts : public AlFunction  {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(self->value+other->value);
        }
};

class SubtractInts : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(self->value-other->value);
        }

};

class MultiplyInts : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(self->value*other->value);
        }

};

class DivideInts : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(self->value/other->value);
        }

};

class PowerInts : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(std::pow(self->value, other->value));
        }

};


class PrintInt : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlInt* self = (AlInt*)args[0];
            std::ostringstream stream;
            stream << self->value;
            return new AlString(stream.str());
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
    this->attrs["__sub__"] = new SubtractInts();
    this->attrs["__mul__"] = new MultiplyInts();
    this->attrs["__div__"] = new DivideInts();
    this->attrs["__pow__"] = new PowerInts();
    this->attrs["__str__"] = new PrintInt();
}
