def appearance(intervals):
    for x in range(0, len(intervals['pupil']), 2): #выбор значений из списка
        for y in range(0, len(intervals['pupil']), 2): #проход по значениям из списка
            xs, xe = (intervals['pupil'][x]), (intervals['pupil'][x+1]) #проверка пересечения интервалов внутри списка по началу
            ys, ye = (intervals['pupil'][y]), (intervals['pupil'][y+1]) #проверка пересечения интервалов внутри списка по концу
            if (ys < xs < ye):
                intervals['pupil'][x] = ye #обрезка интервала по концу сравниваемого
            elif (ys < xe < ye):
                intervals['pupil'][x+1] = ys #обрезка интервала по началу сравниваемого
            else: continue
    sum = 0
    ls, le = (intervals['lesson'][0]), (intervals['lesson'][1]) #время начала и конца урока
    for x in range(0, len(intervals['pupil']), 2):
        ps, pe = (intervals['pupil'][x]), (intervals['pupil'][x+1]) #проход по списку и запись переменных начала и конца присутствия ученика
        for y in range(0, len(intervals['tutor']), 2):
            ts, te = (intervals['tutor'][y]), (intervals['tutor'][y+1]) #проход по списку и запись переменных начала и конца присутствия учителя
            bs = max(ps, ts) #из двух точек старта интервалов присутствия выбирается более поздняя / старт общего присутствия
            be = min(pe, te) #из двух точек конца интервалов присутствия выбирается более ранняя / конец общего присутствия
            if (be - bs > 0):
                bs = max(bs, ls)#отсекаем присутствие до начала урока
                be = min(be, le)#отсекаем присутствие после окончания урока
            else: continue
            if (be - bs) > 0: #проверяем, что интервалы пересекаются, если не пересекаются, то значение будет меньше 0  
                sum += be - bs
            else: continue
    return sum