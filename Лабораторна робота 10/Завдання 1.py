import matplotlib.pyplot as plt
import numpy as np
# Створюємо діапазон значень x
x = np.linspace(0.01, 4, 400)
# Обчислюємо значення функції
y = np.sin(10 * x) * np.sin(3 * x) / (x ** 2)
# Будуємо графіка
plt.plot(x, y, label='Y(x) = sin(10x)*sin(3x)/x^2', color='red', linewidth=3, linestyle='-')
# Параметри оформлення
plt.title('Графік функції Y(x) = sin(10x)*sin(3x)/x^2', fontsize=14)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
