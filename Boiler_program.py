THERMO_LOW = 10
THERMO_HIGH = 35
is_boiler_on = False
room_temp = 20
program_shutdown = False

def get_input (input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            print(f"Thanks for giving a {input_type}")
            break

        except ValueError:
            print(f"Please input a {input_type}")

    return user_input

thermo_setting = get_input("please input a temprature between 9 and 36", int)

while(True):
    if thermo_setting < THERMO_LOW:
        print("Too Low")
    elif thermo_setting > THERMO_HIGH:
        print("Too High")
    else:
        break

while not program_shutdown:
    if room_temp >= thermo_setting and is_boiler_on == True:
        is_boiler_on = False
        print("Boiler is turned off")
    elif room_temp<= thermo_setting and is_boiler_on == False:
        is_boiler_on = True
        print("Boiler is turned on")
    
