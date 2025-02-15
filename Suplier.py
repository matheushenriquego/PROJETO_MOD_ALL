class Suplier:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    
    def __repr__(self):
        return(f"Nome: {self.name}" f" | Código: {self.code}\n")
