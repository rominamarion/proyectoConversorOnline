def second(segundos):             #segundos ---> minutos y segundos
    min = segundos //60
    seg = segundos % 60
    return min,seg

def hora(segundos):            # segundos ---> hora, min y seg 
    hs = segundos // 3600
    sec = segundos % 3600
    min = sec // 60
    seg = sec % 60
    return hs, min, seg

def sec(minutos, segundos):           # min y seg ---> seg
    seg = minutos*60 + segundos
    return seg

def hour(min, seg): 
    min = seg // 60 + min                # min y seg ---> hora, min y se
    hora = min // 60 
    minuto = min % 60
    segundos = seg % 60
    return hora, minuto, segundos