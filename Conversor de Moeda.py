reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolares = reais / taxa_dolar
euros = reais / taxa_euro

print("Valor em reais: R$", reais)
print("Em dólares: $", round(dolares, 2))
print("Em euros: €", round(euros, 2))