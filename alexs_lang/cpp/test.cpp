#include "src/base.cpp"


int
main ()
{
  AlObj *print = new AlPrint ();
  AlObj *a = new AlInt (3);
  ARG_TYPE t0;
  t0.push_back (*(a) + new AlInt (4));
  (*print) (t0, KWARG_TYPE ());
}
