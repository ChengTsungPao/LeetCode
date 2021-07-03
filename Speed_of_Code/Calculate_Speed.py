from glob import glob
import platform

def get_speed(path, lower, upper):

    f = open(path + "/README.md", "r")

    if platform.system() == "Windows":
        result = path.split("..\\")[-1] + "\n"
    else:
        result = path.split("../")[-1] + "\n"

    count = 1
    speed = -1
    for line in f.readlines():
        if line.find("Runtime") != -1:
            speed = line.split("faster than ")[-1].split("%")[0]
            if lower <= float(speed) <= upper:
                result += "* Code{} faster than {}%\n".format(count, speed)
            count += 1

    f.close()
    
    if lower <= float(speed) <= upper:
        return result + "\n"
    else:
        return ""

if __name__ == "__main__":

    lower = 0
    upper = 50

    f = open("README.md".format(lower, upper), "w")

    f.write("## Faster Than {} ~ {} % Code\n\n".format(lower, upper))
    
    allPath = glob("../[0-9]*")
    for path in allPath:
        result = get_speed(path, lower, upper)
        if result.find("%") != -1:
            f.write(result)

    f.close()