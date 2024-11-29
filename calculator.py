def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def main():
    print("Bem-vindo à Calculadora Básica!")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    while True:
        try:
            operation = input("\nEscolha a operação (1/2/3/4 ou 'sair' para encerrar): ").strip().lower()
            if operation == 'sair':
                print("Encerrando a calculadora. Até mais!")
                break

            if operation not in ['1', '2', '3', '4']:
                print("Operação inválida! Tente novamente.")
                continue
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operation == '1':
                print(f"Resultado: {add(num1, num2)}")
            elif operation == '2':
                print(f"Resultado: {subtract(num1, num2)}")
            elif operation == '3':
                print(f"Resultado: {multiply(num1, num2)}")
            elif operation == '4':
                print(f"Resultado: {divide(num1, num2)}")
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números.")
            
if __name__ == "__main__":
    main()
