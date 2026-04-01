def converter_celsius_para_fahrenheit():
    print("--- Conversor de Celsius para Fahrenheit ---")
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"\nResultado: {celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
    except ValueError:
        print("\nErro: Por favor, digite um número válido (ex: 25 ou 25.5).")

if __name__ == "__main__":
    converter_celsius_para_fahrenheit()
