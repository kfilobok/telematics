import time


def counter(needed):
    sp = sorted(set(needed), key=lambda x: x[1])
    answer = []

    for i in sp:
        x = needed.count(i)
        if x:
            answer.append(f'Кассета№{i[1]}({i[0]}):{x}')
    return ';_'.join(answer)


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
                prom_summ = summ + banknote[0]
                if prom_summ == input_sum:
                    end = time.time() - start
                    return True, counter(needed[summ] + [banknote]), end
                if prom_summ < input_sum and prom_summ not in needed:
                    temp[prom_summ] = needed[summ] + [banknote]
            needed = {**needed, **temp}
        end = time.time() - start
        return False, '', end


# dano = [(200, 2), (500, 1), (200, 2), (200, 3)]
# dano.sort(reverse=True, key=lambda x: x[0])
# print(dano)
# print(mini_ATM(dano, 600))
