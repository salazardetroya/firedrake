from firedrake.adjoint.function import *               # noqa: F401
from firedrake.adjoint.assembly import *               # noqa: F401
from pyadjoint.tape import Tape, set_working_tape

set_working_tape(Tape())

