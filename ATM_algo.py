import time


def counter(needed):
    sp = [5000, 2000, 1000, 500, 200, 100]
    answer = []
    for i in sp:
        x = needed.count(i)
        if x:
            answer.append(f'{i}:{x}')
    return ';'.join(answer)


def mini_ATM(dano, input_sum):
    start = time.time()
    if input_sum % 100 != 0:
        end = time.time() - start
        return False, ''
    else:
        needed = {0: []}
        for banknote in dano:
            temp = {}
            for summ in needed:
                prom_summ = summ + banknote
                if prom_summ == input_sum:
                    print(needed[summ] + [banknote])
                    end = time.time() - start
                    return True, counter(needed[summ] + [banknote]), end
                if prom_summ < input_sum and prom_summ not in needed:
                    temp[prom_summ] = needed[summ] + [banknote]
            needed = {**needed, **temp}
        end = time.time() - start
        return False, '', end
