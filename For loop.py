STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

for key , value in STATE_NAMES.items():
    print("{:<5} is {:>5}".format(key, value))
    