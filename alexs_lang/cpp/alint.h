#ifndef ALINT_H
#define ALINT_H

#include "alobj.h"

class AlInt : public AlObj {
    public:
        AlInt();
        AlInt(int val);
        
        void setup();
        int value;
};

#endif
