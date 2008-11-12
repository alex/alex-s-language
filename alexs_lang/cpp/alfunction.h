#ifndef ALFUNCTION_H
#define ALFUNCTION_H

#include <map>
#include <vector>

#include "alobj.h"

class AlFunction : public AlObj {
    public:
        virtual AlObj* operator()(std::vector<AlObj*> args, std::map<std::string, AlObj*> kwargs) {
            return NULL;
        }
};

#endif
