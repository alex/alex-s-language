#include <map>
#include <vector>

#include "alobj.h"
#include "alfunction.h"
#include "alstring.h"

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
    ARG_TYPE args;
    args.push_back(this);
    args.push_back(other);
    return (*method)(args, KWARG_TYPE());
}

AlObj* AlObj::operator-(AlObj* other)   {
    AlFunction* method = (AlFunction*)this->getattr("__sub__");
    if (method == NULL) {
        throw "Can't add these 2 objects together";
    }
    ARG_TYPE args;
    args.push_back(this);
    args.push_back(other);
    return (*method)(args, KWARG_TYPE());
}

AlObj* AlObj::operator*(AlObj* other)   {
    AlFunction* method = (AlFunction*)this->getattr("__mul__");
    if (method == NULL) {
        throw "Can't add these 2 objects together";
    }
    ARG_TYPE args;
    args.push_back(this);
    args.push_back(other);
    return (*method)(args, KWARG_TYPE());
}

AlObj* AlObj::operator/(AlObj* other)   {
    AlFunction* method = (AlFunction*)this->getattr("__div__");
    if (method == NULL) {
        throw "Can't add these 2 objects together";
    }
    ARG_TYPE args;
    args.push_back(this);
    args.push_back(other);
    return (*method)(args, KWARG_TYPE());
}

std::ostream& operator<<(std::ostream &ostr, AlObj* obj) {
    AlFunction* method = (AlFunction*)obj->getattr("__str__");
    if (method == NULL) {
        throw "Can't print this object";
    }
    ARG_TYPE args;
    args.push_back(obj);
    AlString* str = (AlString*)(*method)(args, KWARG_TYPE());
    ostr << str;
    return ostr;
}


