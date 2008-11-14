#include <string>

#include "alstring.h"

AlString::AlString(std::string val) {
    this->value = val;
}

std::ostream& operator<<(std::ostream &ostr, AlString* obj) {
    ostr << obj->value;
    return ostr;
}
