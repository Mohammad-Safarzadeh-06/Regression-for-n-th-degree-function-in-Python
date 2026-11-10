def zigma(lis , st):
    sum = 0
    for i in range(len(lis)):
        xi , yi = lis[i][0] , lis[i][1]
        sum += eval(st)
    return sum

class regnsun:
    detA = 0
    matris_zarib = []
    matris_malom = []
    def determinan(matris):
        i = len(matris)
        if i == 2:
            return ((matris[0][0] * matris[1][1]) - (matris[0][1] * matris[1][0]))
        elif i == 1:
            return matris[0][0]
        det = 0
        for delit in range(i):
            mat = []
            for satr in range(i):
                if satr != delit:
                    mat += [matris[satr][1 :]]
            det += (matris[delit][0] * ((-1) ** delit) * regnsun.determinan(mat))
        return det

    def find_majhol(majhol):
        lis = []
        for i in range(len(regnsun.matris_zarib)):
            satr = []
            for j in range(len(regnsun.matris_zarib[i])):
                if j == majhol - 1:
                    satr += [regnsun.matris_malom[i]]
                else:
                    satr += [regnsun.matris_zarib[i][j]]
            lis += [satr]
        return (regnsun.determinan(lis) / regnsun.detA)

    def main(list_xi , list_xiyi , n):
        for satr in range(n + 1):
            regnsun.matris_malom += [list_xiyi[satr]]
            sat = []
            for soton in range(n + 1):
                sat += [list_xi[satr + soton]]
            regnsun.matris_zarib += [sat]
        regnsun.detA = regnsun.determinan(regnsun.matris_zarib)
        if regnsun.detA == 0:
            return 'javab nadard'
        else:
            lis = []
            for l in range(n + 1):
                lis += [regnsun.find_majhol(l + 1)]
            return lis

class runer:
    n = -1
    e = -1
    list_data = []
    list_zigma_xinyi = {}
    list_zigma_xin = {}
    zarayeb = []
    list_zarayeb = []
    function = ''

    def funcion_maker():
        runer.function += f'{runer.list_zarayeb[0]}'
        for i in range(1 , runer.n + 1):
            runer.function += f' + {runer.list_zarayeb[i]} * (x ** {i})'

    def mohasebe_E():
        st_function = f'({runer.list_zarayeb[0]}'
        for i in range(1 , runer.n + 1):
            st_function += f' + {runer.list_zarayeb[i]} * (xi ** {i})'
        st_function += f' - yi) ** 2'
        runer.e = zigma(runer.list_data , st_function)

    def hesab_zigma():
        runer.list_zigma_xin[0] , runer.list_zigma_xinyi[0] = len(runer.list_data) , zigma(runer.list_data , 'yi')
        for pow in range(1 , runer.n + 1):
            runer.list_zigma_xin[pow] = zigma(runer.list_data , f'xi ** {pow}')
            runer.list_zigma_xinyi[pow] = zigma(runer.list_data , f'xi ** {pow} * yi')
        for pow in range(runer.n + 1 , 2 * runer.n + 1):
            runer.list_zigma_xin[pow] = zigma(runer.list_data , f'xi ** {pow}')
    
    def digitstring_to_toplefloat(string : str):
        st = string.split(':')
        return (float(st[0]) , float(st[1]))

    def main():
        runer.n = int(input('Enter number of data: ')) - 1
        for i in range(1 , runer.n + 2):
            runer.list_data.append(runer.digitstring_to_toplefloat(input(f'data {i} -->   ')))
        runer.n = int(input('enter n(daraje tabe): '))
        runer.hesab_zigma()
        runer.list_zarayeb = regnsun.main(runer.list_zigma_xin , runer.list_zigma_xinyi , runer.n)
        runer.mohasebe_E()
        runer.funcion_maker()
        print(f'\n{runer.function}\nE = {runer.e}\n'.replace(' + ' , ' +\n'))
        while True:
            x = float(input('x = '))
            print('y =' , str(eval(runer.function)) , end = '\n\n')

runer.main()