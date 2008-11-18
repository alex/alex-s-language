#include "src/base.h"

class f0:public AlFunction
{
public:
  virtual AlObj * operator () (ARG_TYPE args, KWARG_TYPE kwargs)
  {
    AlObj *n = args.back ();
      args.pop_back ();
      return *(n) + new AlInt (1);
  }
};

int
main ()
{
  AlObj *f = new f0 ();
  ARG_TYPE t0;
  ARG_TYPE t1;
  t1.push_back (new AlInt (2));
  t0.push_back ((*f) (t1, KWARG_TYPE ()));
  (*print) (t0, KWARG_TYPE ());
}
