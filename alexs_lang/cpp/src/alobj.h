#ifndef ALOBJ_H
#define ALOBJ_H

#include <gc/gc_allocator.h>
#include <gc/gc_cpp.h>

#include <iostream>
#include <map>
#include <string>
#include <vector>


class AlObj;

typedef std::basic_string<char, std::char_traits<char>, gc_allocator<char> > KEY_TYPE;
typedef std::map<KEY_TYPE, AlObj*, std::less<KEY_TYPE>, gc_allocator<std::pair<KEY_TYPE, AlObj*> > > KWARG_TYPE;
typedef std::vector<AlObj*, gc_allocator<AlObj*> > ARG_TYPE;

class AlObj : public gc {
    public:
        AlObj* getattr(KEY_TYPE key);
        void setattr(KEY_TYPE key, AlObj* value);
        
        virtual operator bool();
        
        AlObj* operator==(AlObj* other);
        
        AlObj* operator||(AlObj* other);
        
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
