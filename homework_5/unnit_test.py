
def is_year_leap(z):
    if (z % 4 == 0 and z % 100 != 0) or z % 400 == 0:
        return True
    else:
        return False


