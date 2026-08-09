from classesraces import RACE_CLASS_LIMITS

def classRestriction(charrace, charclass):
    if RACE_CLASS_LIMITS[charrace][charclass] == 0:
        raise ValueError
    return charclass
