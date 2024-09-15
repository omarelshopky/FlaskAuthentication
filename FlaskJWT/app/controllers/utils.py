def verify_missing_data(data, keys_to_verify):
    """verifies that a list of keys exist in the JSON data and :returns a list of missing keys"""
    missing_kays = []

    # verify JSON data
    for key in keys_to_verify:
        try:
            data[key]
        except KeyError:
            missing_kays.append(key)

    return missing_kays

def check_password_strength(password):
    """:returns False if the password doesn't follow the password policy, True otherwise."""
    # Policy:
    # Minimum length of 8 characters
    if len(list(password)) < 8:
        return False
    return True