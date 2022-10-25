
# Flow Directions from the multiple flow direction codes
# Created by Daria Rapoport, 2016/04,
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 
"""
The script gives the directions from the input array of MFD codes
"""
codes=[]
flowdir=['East','South-East','South','South-West','West','North-West','North', 'North-East']
#Input part - just enter flow direction codes into array
MFDcodes=[195,252,207,60,195,255,255]
for el in MFDcodes:
    codes.append(int(el))
for code in codes:
    count=1
    print 'Flow direction code '+str(code)+' equals to:'
    for i in range(8):
                 try:
                    if bin(code)[-i-1]=='1':
                        print str(count)+')'+flowdir[i]+'\n'
                        count+=1
                 except:
                    pass 
