C = 2.998 * 10**8
IR_f = input("Please input IR frequency in cm-1:\n")
IR_f = int(IR_f) * C * 10**2
vis_f = C/ (532* 10**-9)
SFG_f = IR_f + vis_f
#IR_wave = C/IR_f
SFG_wave = (C / SFG_f)*10**9 
print (f'The corresponding SFG wavelength is {SFG_wave} nm')

# new comment
