#ifndef ALINT_H
#define ALINT_H

#include <map>
#include <string>
#include <vector>

#include <gmp.h>
#include <gmpxx.h>

#include "alobj.h"

typedef mpz_class INT_TYPE;

class AlInt : public AlObj {
    public:
        AlInt();
        AlInt(INT_TYPE val);
        
        void setup();
        INT_TYPE value;
};

#endif
