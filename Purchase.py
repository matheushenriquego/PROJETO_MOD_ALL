class Purchase:
    def __init__(self, unit_cost, quantity, code ,cost):
        self.unit_cost = unit_cost
        self.cost = cost
        self.quantity = quantity
        self.code = code
        
    
    def __repr__(self):
        return (
            f"Código: {self.code}\n"
            f"Valor unitário: {self.unit_cost}\n"
            f"Quantidade comprada: {self.quantity}\n"
            f"Custo total: {self.cost}\n"
        ) 