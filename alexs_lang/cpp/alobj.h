#ifndef ALOBJ_H
#define ALOBJ_H

#include <map>
#include <string>

class AlObj {
    public:
        AlObj* getattr(std::string key);
        AlObj* operator+(AlObj* other);


        std::map<std::string, AlObj*> attrs;
};

#endif
