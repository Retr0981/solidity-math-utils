from common.functions import getTaylorCoefs
from common.functions import getMaxExpArray
from common.functions import getMaxValArray
from common.constants import LOG_MAX_HI_TERM_VAL
from common.constants import EXP_MAX_HI_TERM_VAL
from common.constants import NUM_OF_TAYLOR_COEFS
from common.constants import MIN_PRECISION
from common.constants import MAX_PRECISION


coefficients = getTaylorCoefs(NUM_OF_TAYLOR_COEFS)
maxExpArray = getMaxExpArray(coefficients,MAX_PRECISION+1)
maxValArray = getMaxValArray(coefficients,maxExpArray)


print('module.exports.LOG_MAX_HI_TERM_VAL = {};'.format(LOG_MAX_HI_TERM_VAL))
print('module.exports.EXP_MAX_HI_TERM_VAL = {};'.format(EXP_MAX_HI_TERM_VAL))


print('module.exports.MIN_PRECISION = {};'.format(MIN_PRECISION))
print('module.exports.MAX_PRECISION = {};'.format(MAX_PRECISION))


print('module.exports.maxExpArray = [')
for precision in range(len(maxExpArray)):
    print('    /* {:3d} */    "0x{:x}",'.format(precision,maxExpArray[precision]))
print('];')


print('module.exports.maxValArray = [')
for precision in range(len(maxValArray)):
    print('    /* {:3d} */    "0x{:x}",'.format(precision,maxValArray[precision]))
print('];')
