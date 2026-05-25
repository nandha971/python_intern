import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 50)
y_sine = np.sin(x)
y_noise = y_sine + np.random.normal(0, 0.2, 50)  


categories = ["Product A", "Product B", "Product C", "Product D"]
sales = [35, 50, 20, 45]



fig, axes = plt.subplots(1, 3, figsize=(15, 5))



axes[0].plot(x, y_sine, color="blue", linewidth=2.5, label="Sine Wave")
axes[0].set_title("Line Plot", fontsize=14, fontweight="bold")
axes[0].set_xlabel("X Axis")
axes[0].set_ylabel("Y Axis")
axes[0].grid(True, linestyle="--", alpha=0.6)  
axes[0].legend()



axes[1].bar(categories, sales, color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"])
axes[1].set_title("Bar Chart", fontsize=14, fontweight="bold")
axes[1].set_xlabel("Categories")
axes[1].set_ylabel("Sales (Units)")
axes[1].set_xticklabels(categories, rotation=15)  



axes[2].scatter(x, y_noise, color="red", marker="o", edgecolors="black", label="Data Points")
axes[2].plot(x, y_sine, color="black", linestyle=":", label="Trendline") # Overlay line
axes[2].set_title("Scatter Plot", fontsize=14, fontweight="bold")
axes[2].set_xlabel("X Axis")
axes[2].set_ylabel("Y Axis")
axes[2].legend()




plt.suptitle("Mastering Matplotlib: Core Plot Types", fontsize=18, fontweight="bold", y=1.02)


plt.tight_layout()


plt.show()