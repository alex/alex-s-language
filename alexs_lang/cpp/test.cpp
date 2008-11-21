#include "src/base.h"

AlObj *fact;
class f0:public AlFunction
{
public:
  virtual AlObj * operator () (ARG_TYPE args, KWARG_TYPE kwargs)
  {
    AlObj *n = args.back ();
      args.pop_back ();
    if (*
	((*((*(n)) == (AlObj *) (new AlInt (1))))
	 || (*(n)) == (AlObj *) (new AlInt (0))))
      {
	return (AlObj *) (new AlInt (1));;
      }
    ARG_TYPE t0;
    t0.push_back ((*(n)) - (AlObj *) (new AlInt (1)));
    return (*(n)) * (*fact) (t0, KWARG_TYPE ());
  }
};

int
main ()
{
  fact = new f0 ();
  ARG_TYPE t1;
  ARG_TYPE t2;
  t2.push_back ((AlObj *) (new AlInt (1)));
  t1.push_back ((*fact) (t2, KWARG_TYPE ()));
  (*print) (t1, KWARG_TYPE ());
  ARG_TYPE t3;
  ARG_TYPE t4;
  t4.push_back ((AlObj *) (new AlInt (25)));
  t3.push_back ((*fact) (t4, KWARG_TYPE ()));
  (*print) (t3, KWARG_TYPE ());
}
