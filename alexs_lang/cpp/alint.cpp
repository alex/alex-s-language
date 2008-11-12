#include "alint.h"
#include "alfunction.h"

class AddInts : public AlFunction  {
    public:
        virtual AlObj* operator()(std::vector<AlObj*> args, std::map<std::string, AlObj*> kwargs) {
            AlInt* self = (AlInt*)args[0];
            AlInt* other = (AlInt*)args[1];
            return new AlInt(self->value+other->value);
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

std::ostream& operator<<(std::ostream &ostr, AlInt* obj) {
    ostr << obj->value;
    return ostr;
}

