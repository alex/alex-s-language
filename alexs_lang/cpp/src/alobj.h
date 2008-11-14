#ifndef ALOBJ_H
#define ALOBJ_H

#include <iostream>
#include <map>
#include <string>
#include "gc_cpp.h"


class AlObj : public gc {
    public:
        AlObj* getattr(std::string key);
        AlObj* operator+(AlObj* other);
        AlObj* operator-(AlObj* other);
        AlObj* operator*(AlObj* other);
        AlObj* operator/(AlObj* other);


        std::map<std::string, AlObj*> attrs;
};

std::ostream& operator<<(std::ostream &ostr, AlObj* obj);

#endif
