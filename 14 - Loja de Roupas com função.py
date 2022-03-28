print('')
print('=============================================')

cliente = str(input('Cliente: '))
print('')

valor_total = 0
roupa = []
qntd = []
valor_unitario = []
venda_acumulada = []
pagamento = 0
troco = 0
i = 0


def adicionarDados(roupa, qntd, valor_unitario, venda_acumulada):
      roupa.append(str(input('Roupa: ')))
      qntd.append(int(input('Quantidade: ')))
      valor_unitario.append(float(input('Valor Unitário: R$ ')))
      venda_acumulada.append(qntd[i] * valor_unitario[i])
    
def mostrarDados(j, roupa, qntd, valor_unitario):
   print('Roupa: {}'.format(roupa[j]))
   print('Quantidade: {}'.format(qntd[j]))
   print('Valor Unitário: R$ {:.2f}'.format(valor_unitario[j]))
   print('=' * 30) 

def definirPagamento(valor_total, pagamento, troco):
    print('Valor total: R$ {:.2f}'.format(valor_total))
    pagamento = float(input('Pagamento do cliente: R$ '))
    troco = pagamento - valor_total

    if troco < 0:
      print('Devendo R$ {:.2f}'.format(troco))
    else:
      print('Troco: R$ {:.2f}'.format(troco))

#-------------------------------Módulo de Venda---------------------------------
while True:
  adicionarDados(roupa, qntd, valor_unitario, venda_acumulada)
  print('Valor total do produto: R$ {:.2f}'.format(venda_acumulada[i]))
  print('=============================================')
  print('')
  opcao = str(input(('Vender outra roupa? (S/N): ')))
  opcao = opcao.upper()
  valor_total += venda_acumulada[i]
  print('')
  i += 1
  if opcao == 'N':
    break
#----------------------------------------------------------------------------------

#-------------------------------Módulo de Pagamento--------------------------------

print('=========================Histórico==========================')

for j in range(0, i):
   mostrarDados(j, roupa, qntd, valor_unitario)    

print('')

definirPagamento(valor_total, pagamento, troco)

#----------------------------------------------------------------------------------

print('')
print('Obrigado, volte sempre {}!'.format(cliente))
print('') 
