# Variáveis da pizzaria
FRETE = 2 # Constante Fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão], [caçabresa], [mussarela], [banana com chocolate]: ")
pizza_tamanho = input("Informe o tamnho da pizza - [pequena], [média], [grande]: ")
dia_semana = input("Informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]: ")

print(f" o sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")
# Promoções -> Estruturas condicionais

# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito
if dia_semana == "sabado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O refri hoje é por conta da casa!.")
elif dia_semana == "domingo":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje é por conta da casa!.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!.")


# Comprando uma pizza de calabresa tamanho médio, em qualquer dis, o frete é gratuito.

# Compreando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.