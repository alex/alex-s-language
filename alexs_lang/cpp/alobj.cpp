#include <map>
#include <vector>

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
    std::vector<AlObj*> args;
    args.push_back(this);
    args.push_back(other);
    return (*method)(args, std::map<std::string, AlObj*>());
}

std::ostream& operator<<(std::ostream &ostr, AlObj* obj) {
    return ostr;
}

