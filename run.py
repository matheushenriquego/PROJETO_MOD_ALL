from Suplier import Suplier
from Product import Product
from Purchase import Purchase

INVENTORY = dict()
REGISTRATION = list()
SUPLIER = dict()
    
def list_products_quantities():
    for code,product in INVENTORY.items():
        print(product)

def buy_product():
    code = input("Código do produto para compra: ")
    quantity=int(input("diga a quantidade:"))
    product = INVENTORY.get(code)
    if not product:
        print("Código não existente, adicione um produto primeiro.")
        return
    if product.quantity < quantity:
        print("Quantidade invalida.")
        return
    print(product)
    product.quantity -= quantity
    INVENTORY[code]=product
    REGISTRATION.append(build_purchase(product,quantity))
    verify_product_quantity(product)
    
def build_purchase(product,quantity):
    purchase = Purchase(
        code = product.code,
        unit_cost = product.unit_cost,
        quantity = quantity,
        cost = product.unit_cost*quantity
    )
    return purchase

def build_custom_product():
    product = Product(
        name=input("Nome do produto: "),
        code=input("Código do produto: "),
        quantity=int(input("Quantidade: ")),
        category=input("Categoria: "),
        unit_cost=float(input("Valor unitário: "))
    )
    return product

def verify_product_quantity(product):
    if product.quantity < 3:
        print(f"Produto de código {product.code} com estoque baixo ({product.quantity} unidade(s))")

def add_product():
    product = build_custom_product()
    INVENTORY[product.code] = product
    verify_product_quantity(product)

def update_product():
    code = input("Código do produto: ")
    product = INVENTORY.pop(code, None)
    if not product:
        print("Código não existente, adicione um produto primeiro.")
        return
    print(product)
    new_product = build_custom_product()

    verify_product_quantity(product=new_product)

    INVENTORY[new_product.code] = new_product

def list_products_quantities():
    for code, product in INVENTORY.items():
        print(f"Código: {code} Nome: {product.name} Quantidade: {product.quantity}")

def get_inventory_value():
    total = 0
    for code, product in INVENTORY.items():
        total += product.unit_cost * product.quantity
    print(f"Inventario atual avaliando em :R${total}\n")   

def get_supliers():
    choice=input("1.adicionar\n2.remover\n")
    if choice == "1":
        name = input("Diga o nome do carregador\n")
        code = input("Diga o codigo do carregador\n")
        suplier = Suplier(name,code)
        SUPLIER[code] = suplier 
    elif choice == "2":
        code = input("Diga o codigo do carregador\n")
        try:
            del SUPLIER[code]
        except ValueError:
            print(f"O codigo não é de um funcionario.") 
    else:
        print("INVALIDO")

should_run = True

message = """
1 - Adicionar produto
2 - Atualizar produto
3 - Verificar quantidade de produtos em estoque
4 - Verificar valor do estoque atual
5 - Realizar uma compra
6 - historico de compras
7 - adicionar/remover funcionario
8 - mostrar os funcioanrios atuais
0 - Fechar programa
"""


while should_run:
    print(message)
    result = input("Próxima ação: ")
    if result == "1":
        add_product()
    elif result == "2":
        update_product()
    elif result == "3":
        list_products_quantities()
    elif result == "4":
        get_inventory_value()
    elif result == "5":
        buy_product()
    elif result == "6":
        print(REGISTRATION)
    elif result == "7":
        get_supliers()
    elif result == "8":
        for code,employer in SUPLIER.items():
            print(employer)
    elif result == "0":
        should_run = False
    else:
        print("Errado")