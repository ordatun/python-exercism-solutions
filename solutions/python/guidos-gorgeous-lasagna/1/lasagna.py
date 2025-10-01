EXPECTED_BAKE_TIME = 40
    

def bake_time_remaining(elapsed_bake_time):
    """Calculate the preparation time in minutes.

    :param elapsed_bake_time: int - the number of layers in the lasagna.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    if (elapsed_bake_time < EXPECTED_BAKE_TIME):
        remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
        return remaining
    else:
        return 0

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return (number_of_layers * 2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_time = (number_of_layers * 2) + elapsed_bake_time
    return (total_time)

elapsed_bake_time = 12
number_of_layers = 4

print(bake_time_remaining(elapsed_bake_time))
print(preparation_time_in_minutes(number_of_layers))
print(elapsed_time_in_minutes(number_of_layers, elapsed_bake_time))




