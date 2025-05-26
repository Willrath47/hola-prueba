# Generar la secuencia de Fibonacci hasta n términos

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Ejemplo de uso:
n = 10  # Cambia este valor para más términos
print(fibonacci(n))