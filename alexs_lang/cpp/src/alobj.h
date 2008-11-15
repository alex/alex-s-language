#ifndef ALOBJ_H
#define ALOBJ_H

#include <gc/gc_allocator.h>
#include <gc/gc_cpp.h>

#include <iostream>
#include <map>
#include <string>
#include <vector>


class AlObj;

typedef std::map<std::string, AlObj*, std::less<std::string>, gc_allocator<std::pair<const std::string, AlObj*> > > KWARG_TYPE;
typedef std::vector<AlObj*, gc_allocator<AlObj*> > ARG_TYPE;

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
