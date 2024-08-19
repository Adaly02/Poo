class Empleado:
    def __init__(self, sueldo_base, valor_ventas, bonificacion=250):
        self.sueldo_base = sueldo_base
        self.valor_ventas = valor_ventas
        self.bonificacion = bonificacion
    
    def calcular_comision(self):
        return self.valor_ventas * 0.10
    
    def calcular_igss(self):
        return self.sueldo_base * 0.0483
    
    def calcular_ahorro(self, total_ganado):
        return total_ganado * 0.07
    
    def calcular_total_ganado(self):
        return self.sueldo_base + self.calcular_comision() + self.bonificacion
    
    def calcular_total_descuentos(self, total_ganado):
        return self.calcular_ahorro(total_ganado) + self.calcular_igss()
    
    def calcular_sueldo_liquido(self):
        total_ganado = self.calcular_total_ganado()
        total_descuentos = self.calcular_total_descuentos(total_ganado)
        return total_ganado - total_descuentos
    
    def mostrar_resultados(self):
        print(f"Sueldo Base: Q{self.sueldo_base}")
        print(f"Comisión por Ventas: Q{self.calcular_comision()}")
        print(f"IGSS: Q{self.calcular_igss()}")
        total_ganado = self.calcular_total_ganado()
        print(f"Total Ganado: Q{total_ganado}")
        total_descuentos = self.calcular_total_descuentos(total_ganado)
        print(f"Total Descuentos: Q{total_descuentos}")
        print(f"Sueldo Líquido: Q{self.calcular_sueldo_liquido()}")

# corrida
sueldo_base = float(input("Ingrese el sueldo base: Q"))
valor_ventas = float(input("Ingrese el valor de ventas realizadas: Q"))

empleado = Empleado(sueldo_base, valor_ventas)
empleado.mostrar_resultados()
