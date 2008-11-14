#ifndef ALFUNCTION_H
#define ALFUNCTION_H

#include <map>
#include <vector>

#include "alobj.h"

class AlFunction : public AlObj {
    public:
        virtual AlObj* operator()(ARG_TYPE args, KWARG_TYPE kwargs) {
            return NULL;
        }
};

#endif
