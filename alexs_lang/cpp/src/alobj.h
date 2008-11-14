#ifndef ALOBJ_H
#define ALOBJ_H

#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "gc_cpp.h"

class AlObj;

typedef std::map<std::string, AlObj*> KWARG_TYPE;
typedef std::vector<AlObj*> ARG_TYPE;

class AlObj : public gc {
    public:
        AlObj* getattr(std::string key);
        AlObj* operator+(AlObj* other);
        AlObj* operator-(AlObj* other);
        AlObj* operator*(AlObj* other);
        AlObj* operator/(AlObj* other);
        
        
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            throw "Don't call an ABC";
        }

        KWARG_TYPE attrs;
};

std::ostream& operator<<(std::ostream &ostr, AlObj* obj);

#endif
