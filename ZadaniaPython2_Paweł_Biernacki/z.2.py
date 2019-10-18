
data_text = "Ala Ma Kota"


def funkcja_info(data_text):
    a = len(data_text)
    b = list(data_text)
    c = data_text.upper()
    d = data_text.lower()
    dict = {'length': a , 'letters': b , 'big_letters': c , 'small_letters': d}
    return dict

print(funkcja_info(data_text))