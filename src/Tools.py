def convert_doll_to_int(string):
    return int(string[1:].replace(",",""))

def convert_number_to_month(number):
    look_up = {'1': 'Jan', '2': 'Feb',
               '3': 'Mar', '4': 'Apr',
               '5': 'May', '6': 'Jun',
               '7': 'Jul', '8': 'Aug',
               '9': 'Sep', '10': 'Oct',
               '11': 'Nov', '12': 'Dec'}
    return look_up[str(number)]