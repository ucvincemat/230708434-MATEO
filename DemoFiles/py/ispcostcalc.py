# MATEO, Vince N.

#'''''' VARIABLE INIT ......#

companyLogo = """ .--------------------------.  
 | _ ___ _     |         ___|  
 |/   | |_) |  |   /\  |  | |  
 |\_  | | \ |_ |  /--\ |_ | |  
 .--------------------------.  
 | _  _             _  _ ___|  
 |/  / \ |\ | |\ | |_ /   | |  
 |\_ \_/ | \| | \| |_ \_  | |  
 '--------------------------'  
       CTRL your world.        
     ALT your experience.      
    CONNECT uninterrupted.     
    ..........|...........     
"""

# In this scenario, 1 GB = 1024 MB

internetPlan = {
    "STANDARD" : {
        "subscriptionCost" : 1000.00,
        "bandwidthLimitMB" : 30 * 1024.00,
        "penaltyPerMBOverLimit" :  0.05
    },
    "PRO" : {
        "subscriptionCost" : 2000.00,
        "bandwidthLimitMB" : 60 * 1024.00,
        "penaltyPerMBOverLimit" :  0.15
    },
    "BUSINESS" : {
        "subscriptionCost" : 3500.00,
        "bandwidthLimitMB" : 120 * 1024.00,
        "penaltyPerMBOverLimit" :  0.50
    }
}

#'''''' FUNCTION DEFS ......#

def isValidAmount(f):
    n = str(f).replace('.', '')
    if n.isnumeric():
        return True
    else:
        return False

def stringify(list):
    string = ""
    for char in list:
        string += char
    return string

def billCalculator(userPlan, userConsumption):
    plan = internetPlan.get(userPlan.upper())
    
    cost = plan.get("subscriptionCost")
    limit = plan.get("bandwidthLimitMB")
    penalty = plan.get("penaltyPerMBOverLimit")
    extracharge = 0.0
    overshotMB = 0.0

    if userConsumption > limit:
        overshotMB = userConsumption - limit
        extracharge = overshotMB * penalty

    return {"subscription" : cost, "limit" : limit, "overlimit" : overshotMB, "overlimitFee" : extracharge}

def analyzePhoneNum(numb):
    # Only accepts numbers that follows the Philippine standards for phone numbers
    # Not including services such as #MyNumber as those aren't usually used by consumers
    dial = list(numb)
    
    for i in dial:
        if i not in ('0','1','2','3','4','5','6','7','8','9'):
            if i in (' ', '-', '+', '.', ',', '#', '*', '(', ')'):
                dial.remove(i)
            else:
                return "Invalid"

    if not dial:
        return "Invalid"

    def formatNum(num, type="default"):
        phonenum = []
        
        if type == "invalid":
            return None
        elif type == "ncrLine":
            length = 9
        elif type == "landlineX":
            length = 8
        else:
            length = 10

        while length > 0:
            phonenum.append(num.pop())
            length -= 1

        phonenum.reverse()

        if type == "ncrLine":
            phonenum.insert(0, '0')

        # format with dashes/spaces
        if type in ("ncrLine", "landline"):
            phonenum.insert(0, '0')
            phonenum.insert(3, '-')
            phonenum.insert(8, '-')
            if type == "ncrLine":  # remove extra zero so its 02 instead of 002
                phonenum.pop(0)
        elif type == "landlineX":
            phonenum.insert(4, '-')
        elif type == "mobile":
            phonenum.insert(0, '+63-')
            phonenum.insert(4, '-')
            phonenum.insert(8, '-')
        
        return stringify(phonenum)
    
    # remove 0
    if dial[0] == '0':
        dial.pop(0)

    if dial[0] == '2' and len(dial) == 9:
        # METRO MANILA (2 .... ....)
        numType = "ncrLine"
    elif (dial[0] in ('9', '8') and len(dial) == 10) or (dial[0] == '6' and dial[1] == '3' and len(dial) == 12):
        # MOBILE NUMBER (X.. ... ....)
        numType = "mobile"
    elif len(dial) == 10:
        # LANDLINE (XX .... ....)
        numType = "landline"
    elif len(dial) == 8:
        # LANDLINE WITHOUT AREA CODE (.... ....)
        numType = "landlineX"
    else:
        numType = "invalid"
    
    phoneNum = formatNum(dial, numType)

    if not phoneNum:
        return "Invalid"
    else:
        return phoneNum

def validateInput(userInput, type):
    if userInput == None:
        return False
    elif type == "name":
        if userInput.isalpha():
            return True
        else:
            return False
    elif type == "id":
        if userInput.replace('-', '').isnumeric():
            return True
        else:
            return False
    elif type == "phone":
        if userInput != "Invalid":
            return True
        else:
            return False
    elif type == "email":
        if "@" in userInput and "." in userInput:
            if userInput.find("@") < userInput.find("."):
                return True
            else:
                return False
        else:
            return False
    elif type == "plan":
        if userInput == 'STANDARD' or userInput == 'PRO' or userInput == 'BUSINESS':
            return True
        else:
            return False

#'''''' STARTUP ......#

print(companyLogo)
print("Welcome to the Ctrl Alt Connect Ltd. Bill Calculator™!")

#'''''' USER INPUT ......#

while True:
    consumerName = input("Name: ")
    if not validateInput(consumerName, "name"):
        print("<!> Oops. Please use only letters (A-Z) when entering your name.")
        continue
    while True:
        consumerAccountID = input("Account Number: ")
        if not validateInput(consumerAccountID, "id"):
            print("<!> Oops. Please use only numbers when entering your account number.")
            continue
        while True:
            consumerPhoneNum = input("Phone Number: ")
            standardizedPhoneNum = analyzePhoneNum(consumerPhoneNum)
            if not validateInput(standardizedPhoneNum, "phone"):
                print("<!> Oops. Please enter a valid phone number.")
                continue
            while True:
                consumerEmail = input("Email Address: ")
                if not validateInput(consumerEmail, "email"):
                    print("<!> Oops. Please enter a valid email address.")
                    continue
                while True:
                    print("| State your current subscription plan: STANDARD, PRO, or BUSINESS")
                    consumerPlan = input("Current Internet Plan: ")
                    if not validateInput(consumerPlan.upper(), "plan"):
                        print("<!> Oops. This is not one of our plans offered. Please select one of the plans below.")
                        continue
                    while True:
                        consumerBandwidth = input("Bandwith usage this month (MB): ")
                        if not isValidAmount(consumerBandwidth):
                            print("<!> Oops. Please try entering a valid amount.")
                            continue
                        break
                    break
                break
            break
        break
    break

#'''''' PROCESSING ......#

consumerBandwidth = float(consumerBandwidth)
billInfo = billCalculator(consumerPlan, consumerBandwidth)

subscriptionCost = billInfo.get("subscription")
subscriptionLimit = billInfo.get("limit")

consumerOverlimit = billInfo.get("overlimit")
consumerOverFee = billInfo.get("overlimitFee")

#'''''' PRESENT RESULTS ......#

print("\n\n\n")
print(
        "DETAILS OF CURRENT CHARGES\n",
        "| Customer Information\n",
        "Name:				", consumerName, '\n',
        "Account Number:			", consumerAccountID, '\n',
        "Phone Number: 			", standardizedPhoneNum, '\n',
        "Email Address:			", consumerEmail, '\n',
        '============================================================\n',
        "| Plan Details\n",
        "Plan:				", consumerPlan.upper(), '\n',
        '\n',
        "Bandwidth usage this month:	", consumerBandwidth, "MB (", round(consumerBandwidth / 1024, 2), " GB)\n",
        "Monthly Limit: 		        ", subscriptionLimit, "MB (", round(subscriptionLimit / 1024, 2), " GB)\n",
        '.............................................................\n',
        "Over limit usage:		", consumerOverlimit, "MB (", round(consumerOverlimit / 1024, 2), " GB)\n",
        '=============================================================\n',
        "| ISP Bill\n",
        "Subscription Cost:		PHP ", subscriptionCost, '\n',
        "Overlimit Fee:			PHP ", round(consumerOverFee, 2), '\n',
        '.............................................................\n',
        "Total Charges			PHP ", round(subscriptionCost + consumerOverFee, 2), '\n',
    sep='')