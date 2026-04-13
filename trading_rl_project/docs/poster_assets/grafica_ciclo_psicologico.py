import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración de estilo y colores
plt.style.use('seaborn-v0_8-whitegrid')
color_curve = '#1A237E'  # Azul oscuro profundo
color_dots_high = '#E65100'  # Naranja para zonas de riesgo
color_dots_low = '#1A237E'   # Azul para zonas de inicio
color_bg = '#F5F5F5'

# Directorio de salida
output_dir = '/home/julianxd/.gemini/antigravity/brain/cdadb1c8-8db1-47ab-adc1-bd29d0e09709'
os.makedirs(output_dir, exist_ok=True)

def generate_psycho_cycle():
    # Crear la curva (una mezcla de senos para darle la forma de ciclo de mercado)
    x = np.linspace(0, 10, 500)
    y = np.sin(x) + 0.5 * np.sin(x * 0.5)
    
    # Puntos específicos de las emociones
    # (x, y, etiqueta, posición_texto)
    emotions = [
        (0.8, 0.9, "Optimismo", "left"),
        (1.5, 1.3, "Entusiasmo", "left"),
        (2.2, 1.45, "Emoción", "left"),
        (3.1, 1.5, "EUFORIA", "top"),
        (4.0, 1.3, "Ansiedad", "right"),
        (4.8, 0.8, "Negación", "right"),
        (5.5, 0.2, "Miedo", "right"),
        (6.2, -0.6, "Desesperación", "right"),
        (6.8, -1.1, "PÁNICO", "right"),
        (7.5, -1.4, "Capitulación", "right"),
        (8.2, -1.5, "Desánimo", "bottom"),
        (8.8, -1.3, "Depresión", "right"),
        (9.4, -0.8, "Esperanza", "right"),
        (9.9, -0.2, "Alivio", "right")
    ]

    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    fig.patch.set_facecolor(color_bg)
    ax.set_facecolor(color_bg)

    # Dibujar la curva principal
    ax.plot(x, y, color=color_curve, linewidth=3, zorder=1)

    # Añadir los puntos y las etiquetas
    for ex, ey, label, pos in emotions:
        dot_color = color_dots_high if ey > 1.0 or ey < -1.2 else color_dots_low
        ax.scatter(ex, ey, color=dot_color, s=80, zorder=2)
        
        # Ajuste de posición del texto
        ha = 'right' if pos == 'left' else 'left'
        va = 'center'
        offset = 0.2
        
        if pos == 'top': 
            va = 'bottom'
            offset = 0.1
        elif pos == 'bottom': 
            va = 'top'
            offset = 0.1
            
        ax.text(ex + (0.1 if ha=='left' else -0.1), ey + (offset if va=='bottom' else -offset if va=='top' else 0), 
                label, fontsize=10, fontweight='bold', ha=ha, va=va, color='#37474F')

    # Añadir títulos de zonas críticas (Arriba y Abajo)
    # Zona de Máximo Riesgo (Arriba)
    ax.text(3.1, 1.9, "CODICIA / COMPRA", fontsize=22, fontweight='black', color=color_curve, ha='center')
    ax.text(3.1, 1.7, "Máximo punto de riesgo financiero", fontsize=12, color=color_dots_high, ha='center', fontweight='bold')
    ax.arrow(3.1, 1.65, 0, -0.1, head_width=0.1, head_length=0.05, fc=color_dots_high, ec=color_dots_high)

    # Zona de Mejor Oportunidad (Abajo)
    ax.text(8.2, -2.1, "MIEDO / VENTA", fontsize=22, fontweight='black', color=color_curve, ha='center')
    ax.text(8.2, -1.9, "Mejor momento para invertir", fontsize=12, color=color_dots_high, ha='center', fontweight='bold')
    ax.arrow(8.2, -1.85, 0, 0.1, head_width=0.1, head_length=0.05, fc=color_dots_high, ec=color_dots_high)

    # Mensaje irónico lateral
    ax.text(9.5, 0.5, "Repetir hasta\nquedar en la quiebra...", fontsize=14, fontweight='black', color=color_curve, ha='left')

    # Limpieza visual
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/ciclo_psicologico_mercado.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_psycho_cycle()
    print("Gráfica del ciclo psicológico generada exitosamente.")
