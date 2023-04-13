import matplotlib.pyplot as plt
import cmath
import math


class Trace(file_name, self):
    def __init__(self, file_name, description):
        self.file_name = file_name
        self.description = description
        





common = []
differential = []
frequency = []
traces = []

with open("C:/Users/muhaa/Documents/AWR Projects/data/void testing/voidw_9.txt", 'r') as f:
    lines = f.readlines()
    measurement = lines

    while(len(measurement)):
        trace_names = measurement.pop(0)
        attributes = measurement.pop(0)
        trace_name = trace_names.split(":")
        i = 0 
        frequency = []
        trace = []
        for line in measurement:
            #print(line)
            i += 1
            if(line.isspace()): 
                break
            line.split(" ")
            entries = line.split("\t")
            frequency.append(float(entries[0].strip()))
            real = float(entries[1].strip())
            imag = float(entries[2].strip())
            trace.append(complex(real, imag))
         
        traces.append(trace)
        measurement = measurement[i: -1]

common = []
differential = []
for i in range(len(traces[0])):
    add = traces[0][i] + traces[1][i]
    sub = traces[0][i] - traces[1][i]
    common.append(math.sqrt(add.real**2 + add.imag**2)/math.sqrt(2))
    differential.append(math.sqrt(sub.real**2 + sub.imag**2)/math.sqrt(2))
common_nom = common
diff_nom = differential
plt.plot(frequency, common, "y--", label = "common mode 10um trace")
plt.plot(frequency, differential, 'b', label = "differential mode 10um trace")



frequency = []
traces = []

with open("C:/Users/muhaa/Documents/AWR Projects/data/void testing/voidw_0.txt", 'r') as f:
    lines = f.readlines()
    measurement = lines

    while(len(measurement)):
        trace_names = measurement.pop(0)
        attributes = measurement.pop(0)
        trace_name = trace_names.split(":")
        i = 0 
        frequency = []
        trace = []
        for line in measurement:
            #print(line)
            i += 1
            if(line.isspace()): 
                break
            line.split(" ")
            entries = line.split("\t")
            frequency.append(float(entries[0].strip()))
            real = float(entries[1].strip())
            imag = float(entries[2].strip())
            trace.append(complex(real, imag))
         
        traces.append(trace)
        measurement = measurement[i: -1]

common = []
differential = []
for i in range(len(traces[0])):
    add = traces[0][i] + traces[1][i]
    sub = traces[0][i] - traces[1][i]
    common.append(math.sqrt(add.real**2 + add.imag**2)/math.sqrt(2))
    differential.append(math.sqrt(sub.real**2 + sub.imag**2)/math.sqrt(2))
common_9 = common
diff_9 = differential
plt.plot(frequency, common, "y--", label = "common mode nominal resistance")
plt.plot(frequency, differential, 'b', label = "differential mode nominal resistance")

#plt.xlim(min(frequency), max(frequency))\
plt.title("Scattering Parameters |Sds| and |Scs|")
plt.legend()
plt.xlabel("frequency (GHz)")
plt.ylabel("|Sds|, |Scs|")
plt.show()

##Calculate and show ratios##

def graph_tracew():

    ratio_9 = []
    ratio_8 = []
    ratio_nom = []
    for i in range(len(common)):
        ratio_nom.append(common_nom[i]/diff_nom[i])
        ratio_9.append(common_9[i]/diff_9[i])
        ratio_8.append(common_8[i]/diff_8[i])


    plt.plot(frequency, ratio_9, 'r', label = "9um trace")
    plt.plot(frequency, ratio_8, 'b', label = "7um trace")
    plt.plot(frequency, ratio_nom, 'g', label = "10um trace")
    plt.legend()
    plt.xlabel("frequency")
    plt.ylabel("|Scs|/|Sds|")
    plt.title("ratio of common to differential mode scattering parameters")

    #plt.xlim(min(frequency), max(frequency))
    plt.show()



def graph_voidw():

    ratio_nom = []
    ratio_9 = []
    print(len(frequency))
    for i in range(len(common_nom)):
        ratio_nom.append(common_nom[i]/diff_nom[i])
        ratio_9.append(common_9[i]/diff_9[i])
    
    print(ratio_nom[0])
    print(ratio_9[0])
    plt.plot(frequency, ratio_9, 'r', label = "2 um void")
    plt.plot(frequency, ratio_nom, 'g', label = "1um void")
    plt.legend()
    plt.xlabel("frequency")
    plt.ylabel("|Scs|/|Sds|")
    plt.title("ratio of common to differential mode scattering parameters")

    #plt.xlim(min(frequency), max(frequency))
    print("here")
    plt.show()

    



graph_voidw()
        


