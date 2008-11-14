#include <iostream>

#include "alobj.h"
#include "alint.h"
#include "alfunction.h"

class AlPrint : AlFunction {
    public:
        virtual AlObj* operator()(std::vector<AlObj*> args, std::map<std::string, AlObj*> kwargs) {
            std::cout << args[0] << std::endl;
            return NULL;
        }

};
