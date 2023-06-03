altura = float(input('Digite sua altura em cm:  '))
peso = float(input('Digite seu peso em kg:  '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
  print(f'seu IMC é de {IMC}, tá muito maga mulé!, é classificado como magreza')
  
elif IMC >= 18.5 and IMC < 24.9:
  print(f'seu IMC é de {IMC}, tá gostosaaa!, é classificado como normal')
  
elif IMC >= 25 and IMC < 29.9:
  print(f'seu IMC é de {IMC}, vamos começar a fechar a boca, é classificado como Obesidade I!')
  
elif IMC >= 30 and IMC < 39.9:
  print(f'seu IMC é de {IMC}, procure uma academia e feche a boca logo!!! é classificado como Obesidade II!')
  
elif IMC > 40.0:
  print(f'seu IMC é de {IMC}, pode parar de comer que o negocio da feio pra o teu lado. Obesidade grave III')


#MENOR QUE 18,5	MAGREZA	0
#ENTRE 18,5 E 24,9	NORMAL	0
#ENTRE 25,0 E 29,9	SOBREPESO	I
#ENTRE 30,0 E 39,9	OBESIDADE	II
#MAIOR QUE 40,0	OBESIDADE GRAVE	III
