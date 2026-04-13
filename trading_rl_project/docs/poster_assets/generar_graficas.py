import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración de estilo
plt.style.use('seaborn-v0_8-whitegrid')
color_price = '#2563EB'  # Azul moderno
color_sent = '#10B981'   # Verde esmeralda
color_bg = '#FFFFFF'
color_text = '#1F2937'

# Asegurar que el directorio de salida existe
output_dir = '/home/julianxd/.gemini/antigravity/brain/cdadb1c8-8db1-47ab-adc1-bd29d0e09709'
os.makedirs(output_dir, exist_ok=True)

def generate_rollercoaster_chart():
    # Generar datos sintéticos realistas
    np.random.seed(42)
    time = np.arange(100)
    
    # Precio con tendencia y ruido (Montaña rusa)
    price = 100 + np.cumsum(np.random.normal(0, 2, 100)) + 15 * np.sin(time / 10)
    
    # Sentimiento (Correlacionado pero con desfase)
    sentiment = 50 + 20 * np.sin((time - 5) / 10) + np.random.normal(0, 5, 100)
    sentiment = np.clip(sentiment, 0, 100)

    fig, ax1 = plt.subplots(figsize=(10, 5), dpi=150)
    fig.patch.set_facecolor(color_bg)
    ax1.set_facecolor(color_bg)

    # Eje del Precio
    ax1.plot(time, price, color=color_price, linewidth=2.5, label='Precio BNB/USDT')
    ax1.set_ylabel('Precio (USD)', color=color_price, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_price)
    ax1.set_title('La Montaña Rusa: Precio vs. Sentimiento', fontsize=16, fontweight='bold', pad=20)

    # Eje del Sentimiento
    ax2 = ax1.twinx()
    ax2.fill_between(time, sentiment, 50, where=(sentiment >= 50), color=color_sent, alpha=0.3, label='Codicia')
    ax2.fill_between(time, sentiment, 50, where=(sentiment < 50), color='#EF4444', alpha=0.3, label='Miedo')
    ax2.set_ylabel('Índice Fear & Greed', color='#d4a017', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 100)

    ax1.set_xlabel('Tiempo (Horas de Entrenamiento)', fontsize=11)
    
    # Anotaciones
    ax1.annotate('Pánico (Oportunidad)', xy=(35, 95), xytext=(15, 80),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
    ax1.annotate('Euforia (Riesgo)', xy=(85, 115), xytext=(65, 125),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

    plt.tight_layout()
    plt.savefig(f'{output_dir}/grafica_montana_rusa.png', bbox_inches='tight')
    plt.close()

def generate_risk_comparison():
    # Datos de comparativa
    labels = ['Trader Humano\n(Emocional)', 'Agente IA\n(Estratégico)']
    drawdown = [38.5, 12.2]  # Máximo por ciento de pérdida
    profit = [15.1, 28.4]    # Rendimiento total

    x = np.array([0, 1])
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    fig.patch.set_facecolor(color_bg)
    ax.set_facecolor(color_bg)

    rects1 = ax.bar(x - width/2, profit, width, label='Rentabilidad (%)', color='#22C55E')
    rects2 = ax.bar(x + width/2, drawdown, width, label='Riesgo (Max. Drawdown %)', color='#EF4444')

    ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
    ax.set_title('El Escudo de Seguridad: IA vs. Humano', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12, fontweight='bold')
    ax.legend(frameon=True, shadow=True)

    # Etiquetas en las barras
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontweight='bold')

    autolabel(rects1)
    autolabel(rects2)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/grafica_comparativa_riesgo.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_rollercoaster_chart()
    generate_risk_comparison()
    print("Gráficas generadas exitosamente.")
