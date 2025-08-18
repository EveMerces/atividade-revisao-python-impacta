"""O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado."""

total_geral = 0

print("Cardápio:")
print("100 - Cachorro Quente - R$ 1,20")
print("101 - Bauru Simples - R$ 1,30") 
print("102 - Bauru com ovo - R$ 1,50")
print("103 - Hambúrguer - R$ 1,20")
print("104 - Cheeseburguer - R$ 1,30")
print("105 - Refrigerante - R$ 1,00")

while True:
    codigo = int(input("Digite o código do item (0 para finalizar): "))
    
    if codigo == 0:
        print("Finalizando pedido...")
        break
        
    qtd = int(input("Digite a quantidade: "))
    
    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00
    else:
        print("Código inválido")
        preco = 0
        
    if preco > 0:
        valor_item = preco * qtd
        total_geral = total_geral + valor_item
        print(f"Valor do item: R$ {valor_item:.2f}")
    
print(f"Total do pedido: R$ {total_geral:.2f}")