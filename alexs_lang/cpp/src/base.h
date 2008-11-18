#ifndef BASE_H
#define BASE_H

#include <iostream>

#include "alobj.h"
#include "alint.h"
#include "alfunction.h"

class AlPrint : public AlFunction {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            std::cout << args[0] << std::endl;
            return NULL;
        }

};

extern AlObj* print;

#endif
