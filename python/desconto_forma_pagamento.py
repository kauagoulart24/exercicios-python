n1=float(input('Quanto foi o valor da sua compra?'))
desct_ou_prcld=input('Se a sua compra for a vista vai ganhar um desconto de 10%, se for parcelado não terá desconto. Por isso digite v se for a vista ou p se for parcelado.')
desconto=(n1-(n1*0.1))
if desct_ou_prcld == 'V':
    print(f'Você terá um desconto de 10%. O valor da sua compra foi {n1} e agora será {desconto:.2f}. Volte sempre.')
else:
    print('Você não tera o desconto. Escolha quantas parcelas quer parcelar.')