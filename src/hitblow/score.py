def calculate_score(tries):
    if tries == 1:
        return 100
    elif tries <= 3:
        return 80
    elif tries <= 5:
        return 60
    elif tries <= 10:
        return 40
    else:
        return 20