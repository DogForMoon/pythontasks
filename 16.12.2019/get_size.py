def get_size(w, h, d):
    fig_params = []
    s = 2 * (int(w * h) + int(h * d) + int(w * d))
    v = w * h * d
    fig_params.append(s)
    fig_params.append(v)
    return(fig_params)
#https://www.codewars.com/kata/565f5825379664a26b00007c