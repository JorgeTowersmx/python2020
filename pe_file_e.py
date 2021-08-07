import pefile

pe = pefile.PE("C://windows/system32/calc.exe")

print(pe)