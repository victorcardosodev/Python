altura = int(input('Digite sua altura em CM: '))
peso = float(input('Digite seu peso em KG: '))
imc = peso / (altura/100 * altura/100)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso ideal!')

elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está com peso ideal!')

elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso!')

elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade!')

elif imc >= 40:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida!')

else:
    print('Valor invalido, por favor verifique o valor digitado!')