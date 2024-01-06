def is_black_or_white(image_in):
    img = image_in

    h = img.shape[0]
    w = img.shape[1]
    black_counter = 0
    other_counter = 0

    for i in range(h):
        for j in range(w):
            if (img[i, j] == 0).all():
                black_counter += 1
            elif (img[i, j] > 0).all():
                other_counter += 1

    if black_counter > other_counter:
        return "black"
    elif other_counter > black_counter:
        return "white"
    else:
        # extreme edge case where white pixels = black pixels
        return "other"
