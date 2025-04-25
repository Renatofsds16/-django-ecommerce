def carts_to(carrinho):
    return sum(
        [
            item.get('price_unit_promotional')
            if item.get('price_unit_promotional')
            else item.get('price_unit')
            for item in carrinho.values()
        ]
    )