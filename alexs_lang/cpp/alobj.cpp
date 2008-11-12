#include "alobj.h"
#include "alfunction.h"

AlObj* AlObj::getattr(std::string key)  {
    if (this->attrs.count(key) > 0) {
        return this->attrs[key];
    }
    return NULL;
//    return this->attrs[std::string("__class__")]->getattr(key);
}

AlObj* AlObj::operator+(AlObj* other)   {
    AlFunction* method = (AlFunction*)this->getattr("__add__");
    if (method == NULL) {
        throw "Can't add these 2 objects together";
    }
    return (*method)(this, other);
}
