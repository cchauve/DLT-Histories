import numpy as np
import scipy
import scipy.optimize as opt

ALL_RHS = {}

def f_0(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[0] = [0,0,0,0,0]

def f_1(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[1] = [0,0,0,0]

def f_2(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[2] = [0,0,0,0]

def f_3(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[3] = [0,0,0,0,0]

def f_4(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[4] = [0,0,0,0]

def f_5(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[5] = [0,0,0,0]

def f_6(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[6] = [0,0,0,0,0]

def f_7(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[7] = [0,0,0,0]

def f_8(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[8] = [0,0,0,0,0]

def f_9(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[9] = [0,0,0,0]

def f_10(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[10] = [0,0,0,0,0]

def f_11(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[11] = [0,0,0,0]

def f_12(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[12] = [0,0,0,0,0]

def f_13(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[13] = [0,0,0,0,0]

def f_14(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[14] = [0,0,0,0,0]

def f_15(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[15] = [0,0,0,0]

def f_16(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[16] = [0,0,0,0]

def f_17(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[17] = [0,0,0,0]

def f_18(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[18] = [0,0,0,0]

def f_19(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[19] = [0,0,0,0,0]

def f_20(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[20] = [0,0,0,0,0]

def f_21(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[21] = [0,0,0,0]

def f_22(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[22] = [0,0,0,0]

def f_23(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[23] = [0,0,0,0,0]

def f_24(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[24] = [0,0,0,0,0]

def f_25(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[25] = [0,0,0,0,0]

def f_26(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[26] = [0,0,0,0,0]

def f_27(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[27] = [0,0,0,0,0]

def f_28(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[28] = [0,0,0,0,0]

def f_29(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[29] = [0,0,0,0,0]

def f_30(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[30] = [0,0,0,0]

def f_31(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[31] = [0,0,0,0]

def f_32(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[32] = [0,0,0,0,0]

def f_33(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[33] = [0,0,0,0,0]

def f_34(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[34] = [0,0,0,0,0]

def f_35(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[35] = [0,0,0,0]

def f_36(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[36] = [0,0,0,0,0]

def f_37(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[37] = [0,0,0,0,0]

def f_38(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[38] = [0,0,0,0,0]

def f_39(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[39] = [0,0,0,0]

def f_40(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[40] = [0,0,0,0,0]

def f_41(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[41] = [0,0,0,0]

def f_42(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[42] = [0,0,0,0]

def f_43(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[43] = [0,0,0,0,0]

def f_44(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[44] = [0,0,0,0]

def f_45(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[45] = [0,0,0,0,0]

def f_46(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[46] = [0,0,0,0]

def f_47(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[47] = [0,0,0,0,0]

def f_48(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[48] = [0,0,0,0]

def f_49(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[49] = [0,0,0,0]

def f_50(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[50] = [0,0,0,0]

def f_51(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[51] = [0,0,0,0]

def f_52(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[52] = [0,0,0,0]

def f_53(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[53] = [0,0,0,0]

def f_54(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[54] = [0,0,0,0,0]

def f_55(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[55] = [0,0,0,0,0]

def f_56(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[56] = [0,0,0,0]

def f_57(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[57] = [0,0,0,0,0]

def f_58(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[58] = [0,0,0,0]

def f_59(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[59] = [0,0,0,0,0]

def f_60(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[60] = [0,0,0,0]

def f_61(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[61] = [0,0,0,0,0]

def f_62(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[62] = [0,0,0,0,0]

def f_63(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[63] = [0,0,0,0]

def f_64(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[64] = [0,0,0,0]

def f_65(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[65] = [0,0,0,0,0]

def f_66(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[66] = [0,0,0,0]

def f_67(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[67] = [0,0,0,0]

def f_68(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[68] = [0,0,0,0]

def f_69(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[69] = [0,0,0,0,0]

def f_70(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[70] = [0,0,0,0]

def f_71(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[71] = [0,0,0,0,0]

def f_72(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[72] = [0,0,0,0,0]

def f_73(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[73] = [0,0,0,0,0]

def f_74(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[74] = [0,0,0,0,0]

def f_75(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[75] = [0,0,0,0,0]

def f_76(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[76] = [0,0,0,0]

def f_77(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[77] = [0,0,0,0]

def f_78(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[78] = [0,0,0,0]

def f_79(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[79] = [0,0,0,0,0]

def f_80(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[80] = [0,0,0,0]

def f_81(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[81] = [0,0,0,0]

def f_82(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[82] = [0,0,0,0,0]

def f_83(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[83] = [0,0,0,0]

def f_84(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[84] = [0,0,0,0,0]

def f_85(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[85] = [0,0,0,0]

def f_86(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[86] = [0,0,0,0]

def f_87(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[87] = [0,0,0,0,0]

def f_88(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[88] = [0,0,0,0]

def f_89(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[89] = [0,0,0,0]

def f_90(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[90] = [0,0,0,0]

def f_91(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[91] = [0,0,0,0,0]

def f_92(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[92] = [0,0,0,0]

def f_93(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[93] = [0,0,0,0,0]

def f_94(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[94] = [0,0,0,0,0]

def f_95(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[95] = [0,0,0,0]

def f_96(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[96] = [0,0,0,0,0]

def f_97(X):
	(z,r0,r1,r2) = X
	f = [-(2*r0-1)*(2*r1-1)*(2*r2-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r1**2-r2**2-2*r1+r2]
	return(f)

ALL_RHS[97] = [0,0,0,0]

def f_98(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[98] = [0,0,0,0,0]

def f_99(X):
	(z,r0,r1,r2,r3) = X
	f = [-(-2*r0+1)*(2*r1-1)*(2*r2-1)*(2*r3-1), -r0**2-z+r0, -r0**2-r1**2-2*r0+r1, -r0*r1-r2**2-r0-r1+r2, -r0*r2-r3**2-r0-r2+r3]
	return(f)

ALL_RHS[99] = [0,0,0,0,0]

def solve_nk(f,t):
	return(opt.newton_krylov(f,ALL_RHS[t],f_tol=1e-14))

if __name__ == '__main__':
	print('#size	tree index	growth factor')
	sol_nk_0 = solve_nk(f_0,0)
	print('4\t0\t'+str(1.0/sol_nk_0[0]))
	sol_nk_1 = solve_nk(f_1,1)
	print('4\t1\t'+str(1.0/sol_nk_1[0]))
	sol_nk_2 = solve_nk(f_2,2)
	print('4\t2\t'+str(1.0/sol_nk_2[0]))
	sol_nk_3 = solve_nk(f_3,3)
	print('4\t3\t'+str(1.0/sol_nk_3[0]))
	sol_nk_4 = solve_nk(f_4,4)
	print('4\t4\t'+str(1.0/sol_nk_4[0]))
	sol_nk_5 = solve_nk(f_5,5)
	print('4\t5\t'+str(1.0/sol_nk_5[0]))
	sol_nk_6 = solve_nk(f_6,6)
	print('4\t6\t'+str(1.0/sol_nk_6[0]))
	sol_nk_7 = solve_nk(f_7,7)
	print('4\t7\t'+str(1.0/sol_nk_7[0]))
	sol_nk_8 = solve_nk(f_8,8)
	print('4\t8\t'+str(1.0/sol_nk_8[0]))
	sol_nk_9 = solve_nk(f_9,9)
	print('4\t9\t'+str(1.0/sol_nk_9[0]))
	sol_nk_10 = solve_nk(f_10,10)
	print('4\t10\t'+str(1.0/sol_nk_10[0]))
	sol_nk_11 = solve_nk(f_11,11)
	print('4\t11\t'+str(1.0/sol_nk_11[0]))
	sol_nk_12 = solve_nk(f_12,12)
	print('4\t12\t'+str(1.0/sol_nk_12[0]))
	sol_nk_13 = solve_nk(f_13,13)
	print('4\t13\t'+str(1.0/sol_nk_13[0]))
	sol_nk_14 = solve_nk(f_14,14)
	print('4\t14\t'+str(1.0/sol_nk_14[0]))
	sol_nk_15 = solve_nk(f_15,15)
	print('4\t15\t'+str(1.0/sol_nk_15[0]))
	sol_nk_16 = solve_nk(f_16,16)
	print('4\t16\t'+str(1.0/sol_nk_16[0]))
	sol_nk_17 = solve_nk(f_17,17)
	print('4\t17\t'+str(1.0/sol_nk_17[0]))
	sol_nk_18 = solve_nk(f_18,18)
	print('4\t18\t'+str(1.0/sol_nk_18[0]))
	sol_nk_19 = solve_nk(f_19,19)
	print('4\t19\t'+str(1.0/sol_nk_19[0]))
	sol_nk_20 = solve_nk(f_20,20)
	print('4\t20\t'+str(1.0/sol_nk_20[0]))
	sol_nk_21 = solve_nk(f_21,21)
	print('4\t21\t'+str(1.0/sol_nk_21[0]))
	sol_nk_22 = solve_nk(f_22,22)
	print('4\t22\t'+str(1.0/sol_nk_22[0]))
	sol_nk_23 = solve_nk(f_23,23)
	print('4\t23\t'+str(1.0/sol_nk_23[0]))
	sol_nk_24 = solve_nk(f_24,24)
	print('4\t24\t'+str(1.0/sol_nk_24[0]))
	sol_nk_25 = solve_nk(f_25,25)
	print('4\t25\t'+str(1.0/sol_nk_25[0]))
	sol_nk_26 = solve_nk(f_26,26)
	print('4\t26\t'+str(1.0/sol_nk_26[0]))
	sol_nk_27 = solve_nk(f_27,27)
	print('4\t27\t'+str(1.0/sol_nk_27[0]))
	sol_nk_28 = solve_nk(f_28,28)
	print('4\t28\t'+str(1.0/sol_nk_28[0]))
	sol_nk_29 = solve_nk(f_29,29)
	print('4\t29\t'+str(1.0/sol_nk_29[0]))
	sol_nk_30 = solve_nk(f_30,30)
	print('4\t30\t'+str(1.0/sol_nk_30[0]))
	sol_nk_31 = solve_nk(f_31,31)
	print('4\t31\t'+str(1.0/sol_nk_31[0]))
	sol_nk_32 = solve_nk(f_32,32)
	print('4\t32\t'+str(1.0/sol_nk_32[0]))
	sol_nk_33 = solve_nk(f_33,33)
	print('4\t33\t'+str(1.0/sol_nk_33[0]))
	sol_nk_34 = solve_nk(f_34,34)
	print('4\t34\t'+str(1.0/sol_nk_34[0]))
	sol_nk_35 = solve_nk(f_35,35)
	print('4\t35\t'+str(1.0/sol_nk_35[0]))
	sol_nk_36 = solve_nk(f_36,36)
	print('4\t36\t'+str(1.0/sol_nk_36[0]))
	sol_nk_37 = solve_nk(f_37,37)
	print('4\t37\t'+str(1.0/sol_nk_37[0]))
	sol_nk_38 = solve_nk(f_38,38)
	print('4\t38\t'+str(1.0/sol_nk_38[0]))
	sol_nk_39 = solve_nk(f_39,39)
	print('4\t39\t'+str(1.0/sol_nk_39[0]))
	sol_nk_40 = solve_nk(f_40,40)
	print('4\t40\t'+str(1.0/sol_nk_40[0]))
	sol_nk_41 = solve_nk(f_41,41)
	print('4\t41\t'+str(1.0/sol_nk_41[0]))
	sol_nk_42 = solve_nk(f_42,42)
	print('4\t42\t'+str(1.0/sol_nk_42[0]))
	sol_nk_43 = solve_nk(f_43,43)
	print('4\t43\t'+str(1.0/sol_nk_43[0]))
	sol_nk_44 = solve_nk(f_44,44)
	print('4\t44\t'+str(1.0/sol_nk_44[0]))
	sol_nk_45 = solve_nk(f_45,45)
	print('4\t45\t'+str(1.0/sol_nk_45[0]))
	sol_nk_46 = solve_nk(f_46,46)
	print('4\t46\t'+str(1.0/sol_nk_46[0]))
	sol_nk_47 = solve_nk(f_47,47)
	print('4\t47\t'+str(1.0/sol_nk_47[0]))
	sol_nk_48 = solve_nk(f_48,48)
	print('4\t48\t'+str(1.0/sol_nk_48[0]))
	sol_nk_49 = solve_nk(f_49,49)
	print('4\t49\t'+str(1.0/sol_nk_49[0]))
	sol_nk_50 = solve_nk(f_50,50)
	print('4\t50\t'+str(1.0/sol_nk_50[0]))
	sol_nk_51 = solve_nk(f_51,51)
	print('4\t51\t'+str(1.0/sol_nk_51[0]))
	sol_nk_52 = solve_nk(f_52,52)
	print('4\t52\t'+str(1.0/sol_nk_52[0]))
	sol_nk_53 = solve_nk(f_53,53)
	print('4\t53\t'+str(1.0/sol_nk_53[0]))
	sol_nk_54 = solve_nk(f_54,54)
	print('4\t54\t'+str(1.0/sol_nk_54[0]))
	sol_nk_55 = solve_nk(f_55,55)
	print('4\t55\t'+str(1.0/sol_nk_55[0]))
	sol_nk_56 = solve_nk(f_56,56)
	print('4\t56\t'+str(1.0/sol_nk_56[0]))
	sol_nk_57 = solve_nk(f_57,57)
	print('4\t57\t'+str(1.0/sol_nk_57[0]))
	sol_nk_58 = solve_nk(f_58,58)
	print('4\t58\t'+str(1.0/sol_nk_58[0]))
	sol_nk_59 = solve_nk(f_59,59)
	print('4\t59\t'+str(1.0/sol_nk_59[0]))
	sol_nk_60 = solve_nk(f_60,60)
	print('4\t60\t'+str(1.0/sol_nk_60[0]))
	sol_nk_61 = solve_nk(f_61,61)
	print('4\t61\t'+str(1.0/sol_nk_61[0]))
	sol_nk_62 = solve_nk(f_62,62)
	print('4\t62\t'+str(1.0/sol_nk_62[0]))
	sol_nk_63 = solve_nk(f_63,63)
	print('4\t63\t'+str(1.0/sol_nk_63[0]))
	sol_nk_64 = solve_nk(f_64,64)
	print('4\t64\t'+str(1.0/sol_nk_64[0]))
	sol_nk_65 = solve_nk(f_65,65)
	print('4\t65\t'+str(1.0/sol_nk_65[0]))
	sol_nk_66 = solve_nk(f_66,66)
	print('4\t66\t'+str(1.0/sol_nk_66[0]))
	sol_nk_67 = solve_nk(f_67,67)
	print('4\t67\t'+str(1.0/sol_nk_67[0]))
	sol_nk_68 = solve_nk(f_68,68)
	print('4\t68\t'+str(1.0/sol_nk_68[0]))
	sol_nk_69 = solve_nk(f_69,69)
	print('4\t69\t'+str(1.0/sol_nk_69[0]))
	sol_nk_70 = solve_nk(f_70,70)
	print('4\t70\t'+str(1.0/sol_nk_70[0]))
	sol_nk_71 = solve_nk(f_71,71)
	print('4\t71\t'+str(1.0/sol_nk_71[0]))
	sol_nk_72 = solve_nk(f_72,72)
	print('4\t72\t'+str(1.0/sol_nk_72[0]))
	sol_nk_73 = solve_nk(f_73,73)
	print('4\t73\t'+str(1.0/sol_nk_73[0]))
	sol_nk_74 = solve_nk(f_74,74)
	print('4\t74\t'+str(1.0/sol_nk_74[0]))
	sol_nk_75 = solve_nk(f_75,75)
	print('4\t75\t'+str(1.0/sol_nk_75[0]))
	sol_nk_76 = solve_nk(f_76,76)
	print('4\t76\t'+str(1.0/sol_nk_76[0]))
	sol_nk_77 = solve_nk(f_77,77)
	print('4\t77\t'+str(1.0/sol_nk_77[0]))
	sol_nk_78 = solve_nk(f_78,78)
	print('4\t78\t'+str(1.0/sol_nk_78[0]))
	sol_nk_79 = solve_nk(f_79,79)
	print('4\t79\t'+str(1.0/sol_nk_79[0]))
	sol_nk_80 = solve_nk(f_80,80)
	print('4\t80\t'+str(1.0/sol_nk_80[0]))
	sol_nk_81 = solve_nk(f_81,81)
	print('4\t81\t'+str(1.0/sol_nk_81[0]))
	sol_nk_82 = solve_nk(f_82,82)
	print('4\t82\t'+str(1.0/sol_nk_82[0]))
	sol_nk_83 = solve_nk(f_83,83)
	print('4\t83\t'+str(1.0/sol_nk_83[0]))
	sol_nk_84 = solve_nk(f_84,84)
	print('4\t84\t'+str(1.0/sol_nk_84[0]))
	sol_nk_85 = solve_nk(f_85,85)
	print('4\t85\t'+str(1.0/sol_nk_85[0]))
	sol_nk_86 = solve_nk(f_86,86)
	print('4\t86\t'+str(1.0/sol_nk_86[0]))
	sol_nk_87 = solve_nk(f_87,87)
	print('4\t87\t'+str(1.0/sol_nk_87[0]))
	sol_nk_88 = solve_nk(f_88,88)
	print('4\t88\t'+str(1.0/sol_nk_88[0]))
	sol_nk_89 = solve_nk(f_89,89)
	print('4\t89\t'+str(1.0/sol_nk_89[0]))
	sol_nk_90 = solve_nk(f_90,90)
	print('4\t90\t'+str(1.0/sol_nk_90[0]))
	sol_nk_91 = solve_nk(f_91,91)
	print('4\t91\t'+str(1.0/sol_nk_91[0]))
	sol_nk_92 = solve_nk(f_92,92)
	print('4\t92\t'+str(1.0/sol_nk_92[0]))
	sol_nk_93 = solve_nk(f_93,93)
	print('4\t93\t'+str(1.0/sol_nk_93[0]))
	sol_nk_94 = solve_nk(f_94,94)
	print('4\t94\t'+str(1.0/sol_nk_94[0]))
	sol_nk_95 = solve_nk(f_95,95)
	print('4\t95\t'+str(1.0/sol_nk_95[0]))
	sol_nk_96 = solve_nk(f_96,96)
	print('4\t96\t'+str(1.0/sol_nk_96[0]))
	sol_nk_97 = solve_nk(f_97,97)
	print('4\t97\t'+str(1.0/sol_nk_97[0]))
	sol_nk_98 = solve_nk(f_98,98)
	print('4\t98\t'+str(1.0/sol_nk_98[0]))
	sol_nk_99 = solve_nk(f_99,99)
	print('4\t99\t'+str(1.0/sol_nk_99[0]))
