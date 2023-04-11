DeviceName = input("Device Name is ")
Pins_Cnt =input("Digital Pins count is ")
Path = DeviceName + '_WalkingZ_'+ Pins_Cnt + '.atp'
f = open(Path,'w')
print('import tset tset_WalkZ;')
f.write('import tset tset_WalkZ;\n')
print('vm_vector    ( $tset , AllDigPins)')
f.write('vm_vector    ( $tset , AllDigPins)\n')
print('{')
f.write('{\n')
PinsStr_0 =''
countA =0
for number in range(0,int(Pins_Cnt)):
    PinsStr_0 = PinsStr_0 + "0"
print('                    > tset_WalkZ     '+ PinsStr_0 + ';//Vector ='+str(countA))
f.write('                    > tset_WalkZ     '+ PinsStr_0 + ';//Vector ='+str(countA)+'\n');countA=countA+1
for number in range(0,int(Pins_Cnt)):
    PinsStrlist = list(PinsStr_0)
    PinsStrlist_M =list(PinsStr_0)
    PinsStrlist[number] = "X"
    PinsStrlist_M[number] = "M"
    PinsStr_0_new =''
    PinsStr_M_new =''
    for number1 in range(0,int(Pins_Cnt)):
        PinsStr_0_new = PinsStr_0_new + str(PinsStrlist[number1])
        PinsStr_M_new = PinsStr_M_new + str(PinsStrlist_M[number1])
    print('repeat 20           > tset_WalkZ     ' + PinsStr_0_new + ';//Vector ='+str(countA))
    f.write('repeat 20           > tset_WalkZ     ' + PinsStr_0_new + ';//Vector ='+str(countA)+'\n');countA=countA+1
    print('                    > tset_WalkZ     ' + PinsStr_M_new + ';//Vector ='+str(countA))
    f.write('                    > tset_WalkZ     ' + PinsStr_M_new + ';//Vector ='+str(countA)+'\n');countA=countA+1
print('halt                > tset_WalkZ     ' + PinsStr_0 + ';//Vector ='+str(countA))
f.write('halt                > tset_WalkZ     ' + PinsStr_0 + ';//Vector ='+str(countA)+'\n');countA=countA+1
if int(countA) < 64 :
    for number in range(int(countA) ,64):
        print('                    > tset_WalkZ     ' + PinsStr_0 + ';//Dummy Vector ='+str(countA))
        f.write('                    > tset_WalkZ     ' + PinsStr_0 + ';//Dummy Vector ='+str(countA)+'\n');countA=countA+1
    
print('}')
f.write('}\n')
f.close()
