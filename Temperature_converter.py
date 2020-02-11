#  ---------------- Temperature converter ---------------------------
def temperature_converter(args: str):
    # --------------    Input temperature format checking  -------------

    while True:

        if args == '':
            print('Empty input.')

        elif " " not in args:
            print('Error sample: Please use a space between value and unit:')

        elif (args[-1]).upper() not in ('C', 'F', 'K'):
            print('Unsupported temperature format. '
                  'Please use one of the followings:')

        elif not isinstance((args[:(len(args) - 1)]).strip(), float):
            try:
                converting_value = float((args[:(len(args) - 1)]).strip())

            except ValueError:
                print('ValueError : Please use one of the followings:')

            except NameError:
                print('NameError: Please use one of the followings:')

            else:
                break
        args = input(' sample 36.6 C | 97.88 F | 309.75 K: ')

    measurement_unit = (args[-1]).upper()
    converting_value = float((args[:(len(args) - 1)]).strip())

    # ----------------- Output Temperature format checking-------------
    output_unit = (input('Convert to (C(elsius) | K(elvin) | '
                         'F(ahrenheit)): ')).upper()
    while True:
        if output_unit not in ('C', 'F', 'K'):
            print('Unsupported temperature format. Please '
                  'use one of the followings:')
            output_unit = (input('Convert to (C(elsius) | K(elvin) | '
                                 'F(ahrenheit)): ')).upper()
        else:
            break

        #        ---------------- Converting --------------

    # ---------------   Celsius to Fahrenheit ---------------------
    if measurement_unit == 'C' and output_unit == 'F':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f'{str(round((converting_value * 9 / 5 + 32), 2))} F')

    # ---------------  Celsius to Kelvin  --------------------------
    elif measurement_unit == 'C' and output_unit == 'K':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f' {str(converting_value + 273.15)} K')

    #  ---------------   Fahrenheit to Celsius ------------------------
    elif measurement_unit == 'F' and output_unit == 'C':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f' {str(round(((converting_value - 32) * 5 / 9), 2))} C')

    #  ---------------  Kelvin to Celsius   -------------------------
    elif measurement_unit == 'K' and output_unit == 'C':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f'{str(round((converting_value - 273.15), 2))} C')

    #  --------------   Fahrenheit to Kelvin    -------------------------
    elif measurement_unit == 'F' and output_unit == 'K':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f'{str(round(((converting_value - 32) / 1.8 + 273.15), 2))} K')

    #  --------------   Kelvin to Fahrenheit    -------------------------
    elif measurement_unit == 'K' and output_unit == 'F':
        print(f'Conversion result: {converting_value} {measurement_unit} = '
              f'{str(round(((converting_value - 273.15) * 1.8 + 32), 2))} F')

    #  ------------------- The same input/output ----------------
    else:
        print(f'Conversion result: {converting_value} {measurement_unit}  = '
              f'{converting_value} {measurement_unit} ')


temperature_converter(input("Temperature to convert"))
