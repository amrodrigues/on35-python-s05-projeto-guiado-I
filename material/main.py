import print_reprograma as pr

compra_moc = [
    {'codigo':1,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 1','valor':10.00,'quantidade':1},
    {'codigo':2,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 2','valor':10.00,'quantidade':2},
    {'codigo':3,'nome':'Book - Web Programming Languages For Smart Students','valor':10.00,'quantidade':3}
]

#Preparando a função que vai imprimir o cabeçalho e mensagem de erro
def imprimir_cabecalho(erro_para_imprimir):
    #limpa a tela (igual dar um clear no terminal)
    pr.limpar()
    #mostra o texto inicial
    pr.retangulo('{reprograma}\nProjeto Guiado I\nTerminal de vendas',tamanho=120,cor_barra='magenta',cor_texto='azul')
    pr.separador(120,cor_texto='azul')
    #se eu tiver uma mensagem de erro para exibir eu mostro, se não eu não faço nada
    if(erro_para_imprimir != ''):
        #exibindo a mensagem de erro
        pr.imprimir(erro_para_imprimir,cor_texto='vermelho negrito',tamanho=120,alinhar='centro')
        pr.separador(120,cor_texto='azul')

#Preparando a função para imprimir o rodapé e pegar o comando que vai ser ser digitado
def imprimir_rodape():
    #imprimo o rodapé
    pr.imprimir('[S] Sair','[H] Ajuda',tamanho=110,alinhar='fim',caracter='─',end='┤')
    #pego o comando digitado mas sempre ele no formato minusculo (por isso a função lower)
    return input().lower()

#Preparando a função para imprimir a tela inicial
def imprimir_tela_inicial():
    #imprimindo o texto da tela inicial
    pr.pular_linha(quantidade=2)
    pr.imprimir('Tela inicial',tamanho=120,alinhar='centro')
    pr.pular_linha(quantidade=2)

#Preparando a função para imprimir a tela de ajuda
def imprimir_tela_ajuda():
    #imprimindo o texto de ajuda
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H] - Abre a tela de ajuda com todos os comandos', tamanho=120)
    pr.imprimir('[S] - Fecha o sistema inteiro',tamanho=120)
    pr.imprimir('[N] - Abre uma nova compra')
    pr.pular_linha(quantidade=2)

#Preparando a função para uma nova compra
def imprimir_nova_compra():
    pr.imprimir('Nova Compra')


#Declarando e inicializando as variaveis que vamos usar no controle das telas e dos comandos
opcao = ''
erro = ''
tela = ''
#definindo nosso laço de repetição, cada vez que esse laço executar é uma interação que o programa irá fazer
#isso é, a cada passo ele faz um novo comado
#while((opcao != 's') and (opcao != 'sair')):
while(True):
    #Chama a função declarada acima para imprimir o cabeçalho e o erro
    imprimir_cabecalho(erro)
    #sempre apaga o ultimo erro exibido
    erro = ''

    #Seleciono qual tela será exibida
    if(tela == ''):
        #Chama a função da tela inicial
        imprimir_tela_inicial()
    elif(tela == 'ajuda'):
        #Chama a função da tela de ajuda
        imprimir_tela_ajuda()
        #Sempre volta pra tela inicial depois de passar pela tela de ajuda
        tela=''
    elif(tela == 'nova'):
        #chama a função da tela de nova compra
        imprimir_nova_compra()

    #Chama a função que imprime o rodapé e lê o comando digitado pela usuária
    opcao = imprimir_rodape()

    #analisando o comando que foi digitado e tomando uma decisão
    if(opcao == 's'):
        #se for 's' para o looping e sai do sistema
        break
    elif(opcao == 'h'):
        #se for 'h' seta a variavel de tela para entrar na tela de ajuda
        tela = 'ajuda'
    elif(opcao == 'n'):
        #se for 'n' seta a variavel de tela para entrar na tela de nova compra
        tela = 'nova'
    else:
        #se não for nenhum comando válido dá uma mensagem de erro
        erro = 'A opção não existe!!!'
        