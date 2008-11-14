#ifndef ALINT_H
#define ALINT_H

#include <map>
#include <string>
#include <vector>

#include "alobj.h"

typedef std::map<std::string, AlObj*> KWARG_TYPE;

class AlInt : public AlObj {
    public:
        AlInt();
        AlInt(int val);
        
        void setup();
        int value;
};

#endif
