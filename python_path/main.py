# import calc
# import calc as cc
# from calc import add, sub
# from calc.basic_calc import add, sub
# from calc import advanced_calc

# calc.power(2,3)

# advanced_calc.sqrt(10)



#다른 폴더에서 import 하려면?
import sys
sys.path.append("../modules/calc/basic_calc")
#`from calc import add
from modules.calc.basic_calc import add

print(f"{add(1,3)}")