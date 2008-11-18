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
AlObj *f = new f0 ();

int
main ()
{
  ARG_TYPE t0;
  ARG_TYPE t1;
  t1.push_back (new AlInt (2));
  t0.push_back ((*f) (t1, KWARG_TYPE ()));
  (*print) (t0, KWARG_TYPE ())AlObj *x = new AlInt (2)
    if (*(x) == new AlInt (3))
    {
      ARG_TYPE t2;;
      t2.push_back (x);;
      (*print) (t2, KWARG_TYPE ());
    }
  else
    {
      ARG_TYPE t3;;
      t3.push_back (new AlInt (4));;
      (*print) (t3, KWARG_TYPE ());
    }
}
