import re

validEyeColors = ["amb","blu","brn","gry","grn","hzl","oth"]

def problem4(validateInputs):
    f = open("/home/ec2-user/environment/AOC/Resources/problem4.txt")
    valid = 0
    passport = ""
    for current in f.readlines():
        if current == "\n":
            if checkPassport(passport, validateInputs):
                valid += 1
            #clear passport for next run
            passport = ""
        else:
            passport += current
    
    # the input won't end with a "\n" line, so we need to check one last time
    if checkPassport(passport, validateInputs):
        valid += 1
    
    return valid

def checkPassport(passport, validateInputs):
    if passport != "":
        passportWithoutCid = [s for s in passport.split() if "cid:" not in s]
        if len(passportWithoutCid) == 7:
            if not validateInputs:
                return True
            else:
                try:
                    return validate(passportWithoutCid)
                except Exception:
                    print("Exception for "+passportWithoutCid)
                    return False
                    
    return False

def validate(splitPassport):
    for x in splitPassport:
        y = x.split(":")
        key = y[0]
        val = y[1]
        if key == "byr":
            if not (1920 <= int(val) <= 2002):
                return False
        elif key == "iyr":
            if not (2010 <= int(val) <= 2020):
                return False
        elif key == "eyr":
            if not (2020 <= int(val) <= 2030):
                return False
        elif key == "hgt":
            if "cm" in val:
                if not (150 <= int(val.replace("cm","")) <= 193):
                    return False
            elif "in" in val:
                if not (59 <= int(val.replace("in","")) <= 76):
                    return False
            else:
                return False
        elif key == "hcl":
            if not (len(val) == 7 and re.search("#[0-9a-f]{6}",val) is not None):
                return False
        elif key == "ecl":
            if val not in validEyeColors:
                return False
        elif key == "pid":
            if not (len(val) == 9 and re.search("[0-9]{9}",val) is not None):
                return False
        else:
            print("Unexpected key found: "+key)
            return False
    return True



print(problem4(False))
print(problem4(True))