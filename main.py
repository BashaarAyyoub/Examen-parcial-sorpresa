from Supperclass_punto import Punto
from Rectangulo import Rectangulo


#PUNTOS 

A=Punto(0, 0)
B=Punto(5, 5)
C=Punto(-3, -1)
D=Punto(0, 0)

#puntos
print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

#cuadrante
print("\nCuadrantes:")
print(f"A: {A.cuadrante()}")
print(f"C: {C.cuadrante()}")
print(f"D: {D.cuadrante()}")

#vectores
print("\nVectores:")
print(f"Vector de A a B: {A.vector(B)}")
print(f"Vector de B a A: {B.vector(A)}")


#distancia
print("\nDistancias:")
print(f"Distancia de A a B: {A.distancia(B)}")
print(f"Distancia de A a C: {A.distancia(C)}")
print(f"Distancia de A a D: {A.distancia(D)}")

#puntos lejanos 
distanciass_ = {
    "A": A.distancia(Punto(0, 0)),
    "B": B.distancia(Punto(0, 0)),
    "C": C.distancia(Punto(0, 0))
}

punto_lejano = max(distanciass_, key=distanciass_.get)
print(f"\nEl punto más lejano del origen es {punto_lejano} con una distancia de {distanciass_[punto_lejano]}")

#Rectángulo
print("\nRectángulo:")
rectangulo = Rectangulo(A, B)
print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Área: {rectangulo.area()}")



