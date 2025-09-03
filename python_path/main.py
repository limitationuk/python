# import calc
# import calc as cc
# from calc import add, sub
# from calc.basic_calc import add, sub
# from calc import advanced_calc

# calc.power(2,3)

# advanced_calc.sqrt(10)



#아예 다른 폴더에서 import하게 하려면?
import sys
sys.path.append("../6.Modules")
from calc import add
