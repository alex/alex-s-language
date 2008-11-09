#include "alobj.h"

AlObj* AlObj::getattr(std::string key)  {
    if (this->attrs.count(key) > 0) {
        return this->attrs[key];
    }
    return NULL;
//    return this->attrs[std::string("__class__")]->getattr(key);
}
