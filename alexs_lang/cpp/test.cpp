#include "src/base.h"

class f0:public AlFunction
{
public:
  virtual AlObj * operator () (ARG_TYPE args, KWARG_TYPE kwargs)
  {
    AlObj *n = args.back ();
      args.pop_back ();
      return (*(n)) + (AlObj *) (new AlInt (1));
  }
};

AlObj *f = new f0 ();
int
main ()
{
  ARG_TYPE t0;
  ARG_TYPE t1;
  t1.push_back ((AlObj *) (new AlInt (2)));
  t0.push_back ((*f) (t1, KWARG_TYPE ()));
  (*print) (t0, KWARG_TYPE ());
  AlObj *x = (AlObj *) (new AlInt (2));;
  ARG_TYPE t2;
  t2.push_back (x);
  (*print) (t2, KWARG_TYPE ());
  ARG_TYPE t3;
  t3.push_back ((*(x)) == (AlObj *) (new AlInt (3)));
  (*print) (t3, KWARG_TYPE ());
  if (bool ((*(x)) == (AlObj *) (new AlInt (3))))
    {
      ARG_TYPE t4;;
      t4.push_back (x);;
      (*print) (t4, KWARG_TYPE ());;
    }
}
