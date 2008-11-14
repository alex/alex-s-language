#ifndef ALSTRING_H
#define ALSTRING_H

#include <iostream>
#include <string>

#include "alobj.h"

class AlString : public AlObj {
    public:
        AlString(std::string val);
        
        std::string value;
};

std::ostream& operator<<(std::ostream &ostr, AlString* obj);

#endif
