#ifndef ALBOOL_H
#define ALBOOL_H

#include "alobj.h"

class AlBool : public AlObj {
    public:
        AlBool(bool val);
        AlBool();
        
        virtual operator bool();
        
        void setup();
        
        bool value;
};

#endif
