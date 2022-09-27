def validate_pin(pin):
    print(pin)
    try:
        if '.' in str(pin) or pin.isnumeric() is False :
            print('1')
            return False
        elif int(pin) < 0:
            print('2')
            return False
        #elif ord(pin)
        elif len(pin) == 4 or len(pin) == 6:

     #   elif pin.isnumeric and int(pin) > 0 and len(pin) == 4 or len(pin) == 6:
            print('3')
            return True
        else:
            return False
    except ValueError:
        return False