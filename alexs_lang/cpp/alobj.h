#include <map>
#include <string>

class AlObj {
    public:
        AlObj* getattr(std::string key);
        AlObj* operator+(AlObj*);
        
    private:
        std::map<std::string, AlObj*> attrs;
}
