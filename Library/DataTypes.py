#===== Is Int =====
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#===== Is Float =====
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#===== Is String =====
def is_string(value):
    return isinstance(value, str)

#===== Is List =====
def is_list(value):
    return isinstance(value, list)

#===== Is Tuple =====
def is_tuple(value):
    return isinstance(value, tuple)

#===== Is Dictionary =====
def is_dict(value):
    return isinstance(value, dict)

#===== Is Boolean =====
def is_bool(value):
    return isinstance(value, bool)
