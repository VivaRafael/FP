#       Rafael Galhoz - ist190769

from parte1 import e_palavra
import itertools

#
#       TAD palavra_potencial
#


def cria_palavra_potencial(cad_caracters,tuple_letras):
    """
    Construtor do tipo palavra_potencial.
    Recebe como argumentos uma cadeia de caracteres e um conjunto de letras (potencialmente
    com	repeticoes) e devolve uma palavra_potencial.
    """

    if not isinstance(tuple_letras, tuple) or not isinstance(cad_caracters, str):
        raise ValueError('cria_palavra_potencial:argumentos invalidos.')

    letras = list(tuple_letras)

    for letra in cad_caracters:
        if not (ord('A') <= ord(letra) <= ord('Z')):
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')

        if letra in letras:
            letras.remove(letra)
        else:
            raise ValueError('cria_palavra_potencial:a palavra nao e valida.')

    for letra in tuple_letras:
        if not (ord('A') <= ord(letra) <= ord('Z')):
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')

    return [cad_caracters]+[tuple_letras]


def palavra_tamanho(palavra_potencial):
    """
    Selector do tipo palavra_potencial
    Recebe como argumento um elemento do tipo palavra_potencial e
    devolve o numero de letras da palavra.
    """

    return len(palavra_potencial[0])


def e_palavra_potencial(universal):
    """
    Reconhecedor do tipo palavra_potencial
    Recebe um argumento e devolve True caso esse argumento seja do tipo
    palavra_potencial, e False em caso contrario.
    """

    if not isinstance(universal, list) or not len(universal) == 2 or\
            not isinstance(universal[0], str) or not isinstance(universal[1], tuple):
        return False

    conj_letras = list(universal[1])

    for letra in universal[0]:
        if not (ord('A') <= ord(letra) <= ord('Z')):
            return False
        if letra in conj_letras:
            conj_letras.remove(letra)
        else:
            return False

    return True


def palavras_potenciais_iguais(palavra1,palavra2):
    """
    Teste do tipo palavra_potencial
    Recebe como argumentos dois elementos do tipo palavra_potencial e devolve True
    caso esses argumentos representem a mesma palavra, e False em caso contrario.
    """

    return palavra_potencial_para_cadeia(palavra1) == palavra_potencial_para_cadeia(palavra2)


def palavra_potencial_menor(palavra1,palavra2):
    """
    Teste do tipo palavra_potencial
    Recebe como argumentos dois elementos do tipo palavra_potencial e devolve True caso
    o primeiro argumento represente uma palavra alfabeticamente	anterior a palavra
    representada pelo segundo argumento, e False em caso contrario.
    """

    palavra1 = palavra_potencial_para_cadeia(palavra1)
    palavra2 = palavra_potencial_para_cadeia(palavra2)

    def auxiliar(palavra1,palavra2):
        """
        Funcao auxiliar recursiva para descobrir a menor palavra_potencial
        """

        if len(palavra1) == 0 and len(palavra2) == 0:
            return False

        if palavra1[:1] == palavra2[:1]:
            return auxiliar(palavra1[1:], palavra2[1:])
        return palavra1 < palavra2

    return auxiliar(palavra1, palavra2)


def palavra_potencial_para_cadeia(palavra_potencial):
    """
    Funcao do tipo palavra_potencial
    Recebe como argumento um elemento do tipo palavra_potencial e devolve uma cadeia
    de caracteres que a represente
    """

    return palavra_potencial[0]

#
#	TAD conjunto_palavras
#


def cria_conjunto_palavras():
    """
    Construtor do tipo conjunto_palavras
    Nao recebe argumentos e devolve um conjunto de palavras vazio.
    """

    return []


def numero_palavras(conjunto_palavras):
    """
    Seletor do tipo conjunto_palavras
    Recebe como argumento um elemento do tipo conjunto_palavras e devolve um inteiro
    correspondente ao numero de palavras guardadas.
    """

    return len(conjunto_palavras)


def subconjunto_por_tamanho(conjunto_palavras, inteiro):
    """
    Seletor do tipo conjunto_palavras
    Recebe como argumentos um elemento do tipo conjunto_palavras e um inteiro n, e
    devolve uma lista com as palavras_potenciais de tamanho n contidas no conjunto de palavras.
    """

    return [palavra for palavra in conjunto_palavras if palavra_tamanho(palavra) == inteiro]


def acrescenta_palavra(conj_palavras,palavra_potencial):
    """
    Modificador do tipo conjunto_palavras
    Recebe como argumentos um elemento do tipo conjunto_palavras e uma palavra_potencial, e
    junta a palavra ao conjunto de palavras, caso esta ainda nao pertença ao conjunto.
    Se a palavra já existir no conjunto, o conjunto fica inalterado.
    """
    if not e_palavra_potencial(palavra_potencial) or not e_conjunto_palavras(conj_palavras):

        raise ValueError('acrescenta_palavra:argumentos invalidos.')

    if palavra_potencial_para_cadeia(palavra_potencial) not in \
            [palavra_potencial_para_cadeia(x) for x in conj_palavras]:
        conj_palavras += [palavra_potencial]


def e_conjunto_palavras(universal):
    """
    Reconhecedor do tipo conjunto_palavras
    Recebe um unico argumento e devolve True caso esse argumento seja do tipo conjunto_palavras,
    e False em caso contrario
    """

    if isinstance(universal, list):
        for palavra in universal:
            if not e_palavra_potencial(palavra):
                return False

        return True
    return False


def conjuntos_palavras_iguais(conj_palavras1, conj_palavras2):
    """
    Teste do tipo conjunto_palavras
    Recebe como argumentos dois elementos do tipo conjunto_palavras e devolve True caso
    os dois argumentos contenham as mesmas palavras, e False caso contrario.
    """

    if numero_palavras(conj_palavras1) != numero_palavras(conj_palavras2):
        return False

    for palavra in conj_palavras1:
        if palavra_potencial_para_cadeia(palavra) not in \
                [palavra_potencial_para_cadeia(x) for x in conj_palavras2]:
            return False

    return True


def conjunto_palavras_para_cadeia(conj_palavras):
    """
    Funcao do tipo conjunto_palavras
    Recebe como argumento um elemento do tipo conjunto_palavras e devolve uma cadeia de
    caracteres que o represente. As palavras sao enumeradas por ordem crescente do seu tamanho,
    e para cada tamanho sao ordenadas alfabeticamente.
    """
    cadeia = ''
    inteiro = 0
    tamanho = 0
    qntd_palavras = numero_palavras(conj_palavras)

    while tamanho < qntd_palavras:

        subconjunto = subconjunto_por_tamanho(conj_palavras, inteiro)
        subconjunto = [palavra_potencial_para_cadeia(x) for x in subconjunto]
        subconjunto.sort()

        subconjunto = (', '.join(subconjunto))
        tamanho += numero_palavras(subconjunto_por_tamanho(conj_palavras, inteiro))

        if numero_palavras(subconjunto_por_tamanho(conj_palavras, inteiro)) != 0 or \
                ([] in conj_palavras and inteiro == 0):

            cadeia += str(inteiro)+'->'+'['+subconjunto+']'
            if tamanho != qntd_palavras:
                cadeia += ';'

        inteiro += 1

    return '[' + cadeia + ']'

#
#	TAD Jogador
#


def cria_jogador(cad_caracters):
    """
    Construtor do tipo jogador
    Recebe como argumento uma cadeia de caracteres correspondente ao nome do jogador,
    e devolve um jogador.
    """

    if not isinstance(cad_caracters, str):
        raise ValueError('cria_jogador:argumento invalido.')

    for car in cad_caracters:
        if not isinstance(car, str):
            raise ValueError('cria_jogador:argumento invalido.')

    return [cad_caracters]+[cria_conjunto_palavras()]+[cria_conjunto_palavras()]


def jogador_nome(jogador):
    """
    Seletor do tipo jogador
    Recebe como argumento um elemento do tipo jogador, e devolve o nome do jogador.
    """

    return jogador[0]


def jogador_pontuacao(jogador):
    """
    Funcao do tipo jogador
    Recebe como argumento um elemento do tipo jogador, e devolve a pontuacao obtida pelo
    jogador ate ao momento.
    """

    return sum([palavra_tamanho(palavra) for palavra in jogador_palavras_validas(jogador)]) - \
           sum([palavra_tamanho(palavra) for palavra in jogador_palavras_invalidas(jogador)])


def jogador_palavras_validas(jogador):
    """
    Seletor do tipo jogador
    Recebe como argumento um elemento do tipo jogador, e devolve o conjunto de palavras
    validas propostas pelo jogador ate ao momento.
    """
    return jogador[1]


def jogador_palavras_invalidas(jogador):
    """
    Seletor do tipo jogador
    Recebe como argumento um elemento do tipo jogador, e devolve o conjunto de palavras
    invalidas propostas pelo jogador ate ao momento.
    """
    return jogador[2]


def e_jogador(universal):
    """
    Reconhecedor do tipo jogador
    Recebe um único argumento e devolve True caso esse argumento seja do tipo jogador,
    e False em caso contrario.
    """

    return isinstance(universal, list) and len(universal) == 3 \
           and isinstance(jogador_nome(universal), str) \
           and e_conjunto_palavras(jogador_palavras_validas(universal)) \
           and e_conjunto_palavras(jogador_palavras_invalidas(universal))


def adiciona_palavra_valida(jogador,palavra_potencial):
    """
    Modificador do tipo jogador
    Este modificador recebe como argumentos um elemento do tipo jogador e uma
    palavra_potencial, e adiciona a palavra_potencial ao conjunto_de_palavras
    validas propostas pelo jogador.
    """

    if not e_jogador(jogador) or not e_palavra_potencial(palavra_potencial):
        raise ValueError('adiciona_palavra_valida:argumentos invalidos.')

    acrescenta_palavra(jogador[1], palavra_potencial)


def adiciona_palavra_invalida(jogador, palavra_potencial):
    """
    Modificador do tipo jogador
    Este modificador recebe como argumentos um elemento do tipo jogador e uma
    palavra_potencial, e adiciona a palavra_potencial ao conjunto_de_palavras
    invalidas propostas pelo jogador.
    """

    if not e_jogador(jogador) or not e_palavra_potencial(palavra_potencial):
        raise ValueError('adiciona_palavra_invalida:argumentos invalidos.')

    acrescenta_palavra(jogador[2], palavra_potencial)


def jogador_para_cadeia(jogador):
    """
    Funcao do tipo jogador
    Recebe como argumento um elemento do tipo jogador e devolve uma	cadeia de
    caracteres que o represente. Cada jogador e descrito pelo seu nome, seguido
    pela pontacao obtida e pelos conjuntos de palavras validas e invalidas.
    """

    return 'JOGADOR ' + jogador_nome(jogador) + ' PONTOS={0} VALIDAS={1} INVALIDAS={2}'\
        .format(jogador_pontuacao(jogador),
                conjunto_palavras_para_cadeia(jogador_palavras_validas(jogador)),
                conjunto_palavras_para_cadeia(jogador_palavras_invalidas(jogador)))

#
#       Funcoes adicionais
#


def gera_todas_palavras_validas(tuple_de_letras):
    """
    Funcao auxiliar
    Recebe um tuple_de_letras e forma a partir deste um conjunto de palavras_potencias
    validas pela gramatica do jogo, do tipo conjunto_palavras.
    """

    palavras_validas = cria_conjunto_palavras()

    for x in range(len(tuple_de_letras) + 1):
        for palavra in itertools.permutations(tuple_de_letras, x):

            if e_palavra(''.join(palavra)):
                acrescenta_palavra(palavras_validas,
                                   cria_palavra_potencial(''.join(palavra), tuple_de_letras))
    return palavras_validas


def guru_mj(tuple_de_letras):
    """
    Funcao principal
    Recebe um tuple_de_letras e inicia o jogo guru com base nesse tuple.
    """

    print('Descubra todas as palavras geradas a partir das letras:\n' + str(tuple_de_letras) +
          '\nIntroduza o nome dos jogadores (-1 para terminar)...')
    jogadores = []
    num_jogador = 0

    while True:

        num_jogador += 1
        nome = input('JOGADOR ' + str(num_jogador) + ' -> ')
        if nome == '-1':
            break

        jogadores.append(cria_jogador(nome))

    return main_jogo(tuple_de_letras, jogadores)


def main_jogo(tuple_de_letras, jogadores):
    """
    Funcao auxiliar
    Recebe um tuple_de_letras e uma lista com os jogadores criados e e responsavel
    pelo funcionamento prinicipal do jogo
    """

    conj_palavras = gera_todas_palavras_validas(tuple_de_letras)
    qntd_palavras = numero_palavras(conj_palavras)
    validas_usadas = cria_conjunto_palavras()
    invalidas_usadas = [cria_conjunto_palavras() for i in jogadores]
    jogadas = 1
    num_jogadores = len(jogadores)
    num_jogador = 1

    while True:
        while num_jogador <= num_jogadores:

            if qntd_palavras == 0:  # FIM DE JOGO
                return fim_jogo(jogadores)

            print('JOGADA {0} - Falta descobrir {1} palavras'.format(jogadas, qntd_palavras))
            palavra = input('JOGADOR ' + jogador_nome((jogadores[num_jogador - 1])) + ' -> ')

            palavra = cria_palavra_potencial(palavra, tuple_de_letras)

            if palavra in conj_palavras:  # Se a palavra pertencer ao conjunto de palavras validas
                print(str(palavra_potencial_para_cadeia(palavra)) + ' - palavra VALIDA')

                if palavra not in validas_usadas:
                    adiciona_palavra_valida(jogadores[num_jogador - 1], palavra)
                    acrescenta_palavra(validas_usadas, palavra)
                    qntd_palavras -= 1

            else:						 # Se a palavra nao pertencer ao conjunto de palavras validas
                print(str(palavra_potencial_para_cadeia(palavra)) + ' - palavra INVALIDA')
                if palavra not in invalidas_usadas[num_jogador - 1]:
                    adiciona_palavra_invalida(jogadores[num_jogador - 1], palavra)
                    acrescenta_palavra(invalidas_usadas[num_jogador - 1], palavra)

            num_jogador += 1
            jogadas += 1

        num_jogador = 1


def fim_jogo(jogadores):
    """
    Funcao auxiliar
    Recebe o conjunto dos jogadores e trata das impressoes do fim de jogo
    """

    pontuacoes = list(map(jogador_pontuacao, jogadores))
    pontuacoes_max = list(filter(lambda x: jogador_pontuacao(x) == max(pontuacoes), jogadores))

    if len(pontuacoes_max) == 1:
        print('FIM DE JOGO! O jogo terminou com a vitoria do jogador {0} com {1} pontos.'
              .format(jogador_nome(pontuacoes_max[0]), int(max(pontuacoes))))
    else:
        print('FIM DE JOGO! O jogo terminou em empate.')

    for jogador in jogadores:
        print(jogador_para_cadeia(jogador))
