print('')
print('=============================================')

cliente = str(input('Cliente: '))
print('')

valor_total = 0

#-------------------------------Módulo de Venda---------------------------------
while True:
    roupa = str(input('Roupa: '))
    qntd = int(input('Quantidade: '))
    valor_unitario = float(input('Valor Unitário: R$ '))
    venda_acumulada = qntd * valor_unitario
    print('Valor total do produto: R$ {:.2f}'.format(venda_acumulada))
    print('=============================================')
    print('')
    opcao = str(input(('Vender outra roupa? (S/N): ')))
    opcao = opcao.upper()
    valor_total += venda_acumulada
    print('')
    if opcao == 'N':
      break
#----------------------------------------------------------------------------------

#-------------------------------Módulo de Pagamento--------------------------------
print('Valor total: R$ {:.2f}'.format(valor_total))
pagamento = float(input('Pagamento do cliente: R$ '))
troco = pagamento - valor_total

if troco < 0:
    print('Devendo R$ {:.2f}'.format(troco))
else:
    print('Troco: R$ {:.2f}'.format(troco))    
#----------------------------------------------------------------------------------

print('Obrigado, volte sempre {}!'.format(cliente))
print('') 
