'''
import PROGRAM.Modules
print(PROGRAM.Modules.add(2,3))

from PROGRAM import Modules
print(Modules.add(4,5))
'''
from PROGRAM.Modules import add
print(add(5,6))
