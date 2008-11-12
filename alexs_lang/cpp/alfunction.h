#ifndef ALFUNCTION_H
#define ALFUNCTION_H

#include "alobj.h"

class AlFunction : public AlObj {
    public:
        virtual AlObj* operator()();
};

#endif
