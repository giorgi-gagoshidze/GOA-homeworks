def get_size(W,H,D):
    AREA = 2 * (W * H + H * D + W * D)
    VOLUME = W * H * D
    return[AREA, VOLUME]