#include <string>

#include "albool.h"
#include "alfunction.h"
#include "alstring.h"

class BoolPrint : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlBool* self = (AlBool*)args[0];
            std::string str;
            if (self->value) {
                str = "True";
            }
            else {
                str = "False";
            }
            return new AlString(str);
        }
};

class BoolOr : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            AlBool* self = (AlBool*)args[0];
            AlObj* other = args[1];
            return new AlBool(bool(*self) || bool(*other));
        }
};

AlBool::AlBool(bool val) {
    this->value = val;
    this->setup();
}

AlBool::AlBool() {
    this->value = false;
    this->setup();
}

AlBool::operator bool() {
    return this->value;
}

void AlBool::setup() {
    this->setattr("__str__", new BoolPrint());
    this->setattr("__or__", new BoolOr());
}
