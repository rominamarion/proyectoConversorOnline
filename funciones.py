def second(minutos, segundos):             #minutos y segundos ---> minutos y segundos MODIFICADO ---> le agregue minutos a los parámetros
    minutes = minutos
    min = segundos //60 + minutes
    seg = segundos % 60
    return min,seg

def hour(segundos):            # segundos ---> hora, min y seg  NO SE USA
    hs = segundos // 3600
    sec = segundos % 3600
    min = sec // 60
    seg = sec % 60
    return hs, min, seg

def sec(minutos, segundos):           # min y seg ---> seg
    seg = minutos*60 + segundos
    return seg

def hora(min, seg): 
    min = seg // 60 + min                # min y seg ---> hora, min y se
    hora = min // 60 
    minuto = min % 60
    segundos = seg % 60
    return hora, minuto, segundos
