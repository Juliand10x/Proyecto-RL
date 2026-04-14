import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ─────────────────────────────────────────────
# PALETA UNIFICADA — Colores del poster Externado
# ─────────────────────────────────────────────
C_BG        = '#FFFFFF'   # Fondo blanco (match poster blocks)
C_GREEN     = '#005C35'   # Verde Externado oscuro (header)
C_GREEN_L   = '#00A86B'   # Verde claro
C_GOLD      = '#B8860B'   # Dorado
C_RED       = '#C0392B'   # Rojo riesgo
C_ORANGE    = '#E67E22'   # Naranja advertencia
C_TEXT      = '#1A1A2E'   # Texto oscuro
C_GRAY      = '#6C757D'   # Gris secundario
C_LIGHT     = '#F0F4F0'   # Fondo suave para paneles

output_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(output_dir, exist_ok=True)


# ─────────────────────────────────────────────
# 1. MONTANA RUSA (Precio vs. Sentimiento)
# ─────────────────────────────────────────────
def generate_rollercoaster_chart():
    np.random.seed(42)
    time = np.arange(120)
    price = 100 + np.cumsum(np.random.normal(0, 1.8, 120)) + 20 * np.sin(time / 12)
    sentiment = 50 + 25 * np.sin((time - 6) / 12) + np.random.normal(0, 4, 120)
    sentiment = np.clip(sentiment, 0, 100)

    fig, ax1 = plt.subplots(figsize=(11, 5.5), dpi=180)
    fig.patch.set_facecolor(C_BG)
    ax1.set_facecolor(C_LIGHT)
    ax1.tick_params(colors=C_TEXT)
    for spine in ax1.spines.values():
        spine.set_edgecolor(C_GRAY)
        spine.set_linewidth(0.5)

    # Precio
    ax1.plot(time, price, color=C_GREEN, linewidth=2.8, label='Precio BNB/USDT', zorder=3)
    ax1.fill_between(time, price.min() - 5, price, color=C_GREEN, alpha=0.07)
    ax1.set_ylabel('Precio BNB (USD)', color=C_GREEN, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=C_GREEN)
    ax1.set_xlabel('Tiempo (horas de entrenamiento)', color=C_TEXT, fontsize=10)
    ax1.set_title('Precio vs. Sentimiento del Mercado',
                  fontsize=15, fontweight='bold', color=C_GREEN, pad=14)

    # Sentimiento
    ax2 = ax1.twinx()
    ax2.fill_between(time, sentiment, 50,
                     where=(sentiment >= 50), color=C_GOLD, alpha=0.30, label='Codicia')
    ax2.fill_between(time, sentiment, 50,
                     where=(sentiment < 50), color=C_RED, alpha=0.25, label='Miedo')
    ax2.plot(time, sentiment, color=C_GOLD, linewidth=1.2, alpha=0.7, linestyle='--')
    ax2.set_ylabel('Indice Fear & Greed', color=C_GOLD, fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=C_GOLD)
    ax2.set_ylim(0, 100)

    # Anotaciones
    idx_panic = np.argmin(price[:70])
    idx_euphoria = np.argmax(price[70:]) + 70
    ax1.annotate('Panico = Oportunidad',
                 xy=(time[idx_panic], price[idx_panic]),
                 xytext=(time[idx_panic] + 12, price[idx_panic] + 16),
                 color=C_RED, fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=C_RED, lw=1.5))
    ax1.annotate('Euforia = Riesgo',
                 xy=(time[idx_euphoria], price[idx_euphoria]),
                 xytext=(time[idx_euphoria] - 24, price[idx_euphoria] + 12),
                 color=C_GOLD, fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=C_GOLD, lw=1.5))

    ax2.axhline(y=75, color=C_GOLD, linewidth=0.7, linestyle=':', alpha=0.6)
    ax2.axhline(y=25, color=C_RED,  linewidth=0.7, linestyle=':', alpha=0.6)

    leg1 = mpatches.Patch(color=C_GREEN, label='Precio BNB')
    leg2 = mpatches.Patch(color=C_GOLD,  alpha=0.6, label='Codicia (F&G)')
    leg3 = mpatches.Patch(color=C_RED,   alpha=0.5, label='Miedo (F&G)')
    ax1.legend(handles=[leg1, leg2, leg3], loc='upper left',
               facecolor=C_BG, edgecolor=C_GRAY, labelcolor=C_TEXT, fontsize=9)
    ax1.grid(axis='y', color=C_GRAY, alpha=0.15, linewidth=0.5)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/grafica_montana_rusa.png', bbox_inches='tight', facecolor=C_BG)
    plt.close()
    print("  OK grafica_montana_rusa.png")


# ─────────────────────────────────────────────
# 2. COMPARATIVA IA vs. HUMANO
# ─────────────────────────────────────────────
def generate_risk_comparison():
    categories = ['Rentabilidad\nTotal (%)', 'Max. Drawdown\n(Riesgo %)', 'Sharpe\nRatio']
    human_vals = [15.1, 38.5, 0.62]
    agent_vals = [28.4, 12.2, 1.87]

    x = np.arange(len(categories))
    width = 0.32

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=180)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_LIGHT)
    for spine in ax.spines.values():
        spine.set_edgecolor(C_GRAY)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=C_TEXT)

    bars1 = ax.bar(x - width/2, human_vals, width, label='Trader Humano',
                   color=C_RED, alpha=0.80, zorder=3, edgecolor=C_BG, linewidth=0.5)
    bars2 = ax.bar(x + width/2, agent_vals, width, label='Agente IA (RL)',
                   color=C_GREEN, alpha=0.85, zorder=3, edgecolor=C_BG, linewidth=0.5)

    ax.set_ylabel('Valor', color=C_TEXT, fontsize=11)
    ax.set_title('Rendimiento Esperado: Agente IA vs. Trader Humano',
                 fontsize=13, fontweight='bold', color=C_GREEN, pad=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10, color=C_TEXT, fontweight='bold')
    ax.tick_params(axis='y', labelcolor=C_TEXT)
    ax.grid(axis='y', color=C_GRAY, alpha=0.15, linewidth=0.5)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., h + 0.4,
                    f'{h:.1f}', ha='center', va='bottom',
                    color=C_TEXT, fontsize=10, fontweight='bold')

    ax.text(x[1], -3.0, '<-- menor es mejor', ha='center',
            color=C_GRAY, fontsize=8, style='italic')
    ax.legend(facecolor=C_BG, edgecolor=C_GRAY, labelcolor=C_TEXT, fontsize=10)
    ax.set_ylim(-4, max(agent_vals + human_vals) * 1.20)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/grafica_comparativa_riesgo.png', bbox_inches='tight', facecolor=C_BG)
    plt.close()
    print("  OK grafica_comparativa_riesgo.png")


# ─────────────────────────────────────────────
# 3. CICLO PSICOLOGICO — Curva intuitiva
#    Estilo "Wall Street Cheat Sheet": una curva
#    de precio con emociones en cada punto.
# ─────────────────────────────────────────────
def generate_market_psychology_cycle():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=180)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_LIGHT)

    # Curva de precio sintetica que sube, llega a un pico, cae y se recupera
    t = np.linspace(0, 4 * np.pi, 500)
    # Forma asimetrica: subida lenta, caida rapida, recuperacion
    price = (
        3.0 * np.sin(t - np.pi/2)               # onda base
        + 1.5 * np.sin(0.5 * t - np.pi/4)       # tendencia larga
        + 0.3 * np.sin(3 * t)                    # ruido de mercado
        + 0.08 * t                               # drift ascendente
    )
    # Normalizar para que se vea bien
    price = (price - price.min()) / (price.max() - price.min()) * 100

    # Dibujar la curva principal
    ax.plot(t, price, color=C_GREEN, linewidth=3.0, zorder=3)
    ax.fill_between(t, 0, price, color=C_GREEN, alpha=0.06)

    # Etapas emocionales en puntos clave de la curva
    # Encontrar picos y valles
    peak1_idx = np.argmax(price[:250])
    valley_idx = np.argmin(price[200:350]) + 200
    peak2_start = 350
    
    emotions = [
        # (indice_t, label, color, va_offset, ha)
        (40,         'Esperanza',           C_GREEN_L, 6,  'center'),
        (100,        'Optimismo',           C_GREEN,   6,  'center'),
        (peak1_idx - 20, 'Euforia',        C_GOLD,    8,  'center'),
        (peak1_idx,  'CODICIA\nMAXIMA',     C_ORANGE,  10, 'center'),
        (peak1_idx + 40, 'Ansiedad',       C_ORANGE,  -12, 'center'),
        (peak1_idx + 70, 'Negacion',       C_RED,     -12, 'center'),
        (valley_idx - 20, 'Panico',        C_RED,     -14, 'center'),
        (valley_idx, 'MIEDO\nEXTREMO',     C_RED,     -16, 'center'),
        (valley_idx + 30, 'Capitulacion',  C_RED,     -12, 'center'),
        (valley_idx + 60, 'Depresion',     C_GRAY,    -12, 'center'),
        (valley_idx + 90, 'Esperanza',     C_GREEN_L, 6,   'center'),
        (440,        'Optimismo',           C_GREEN,   6,  'center'),
    ]

    for idx, label, color, offset, ha in emotions:
        if idx < len(t):
            # Punto en la curva
            ax.plot(t[idx], price[idx], 'o', color=color, markersize=8,
                    zorder=5, markeredgecolor=C_BG, markeredgewidth=1.2)
            # Etiqueta
            y_pos = price[idx] + offset
            ax.text(t[idx], y_pos, label, ha=ha, va='center',
                    fontsize=9, color=color, fontweight='bold')

    # Zonas de color
    ax.axhspan(70, 105, color=C_GOLD, alpha=0.06)
    ax.axhspan(-5, 30, color=C_RED, alpha=0.06)

    # Etiquetas de zona
    ax.text(t[-1] + 0.15, 85, 'ZONA DE\nCODICIA', fontsize=8, color=C_GOLD,
            fontweight='bold', va='center', alpha=0.7)
    ax.text(t[-1] + 0.15, 15, 'ZONA DE\nMIEDO', fontsize=8, color=C_RED,
            fontweight='bold', va='center', alpha=0.7)

    # Flechas indicando "Donde compran los sabios" y "Donde venden los sabios"
    ax.annotate('La IA compra aqui\n(miedo = oportunidad)',
                xy=(t[valley_idx], price[valley_idx]),
                xytext=(t[valley_idx] + 1.5, price[valley_idx] + 25),
                fontsize=9, color=C_GREEN, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2.0),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=C_GREEN, alpha=0.1))

    ax.annotate('La IA vende aqui\n(euforia = peligro)',
                xy=(t[peak1_idx], price[peak1_idx]),
                xytext=(t[peak1_idx] + 1.8, price[peak1_idx] - 20),
                fontsize=9, color=C_RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_RED, lw=2.0),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=C_RED, alpha=0.1))

    # Ejes y titulo
    ax.set_title('Ciclo Psicologico del Mercado: Donde actua nuestra IA',
                 fontsize=14, fontweight='bold', color=C_GREEN, pad=14)
    ax.set_xlabel('Tiempo', color=C_GRAY, fontsize=10)
    ax.set_ylabel('Precio del activo', color=C_GRAY, fontsize=10)
    ax.set_xlim(t[0] - 0.2, t[-1] + 1.8)
    ax.set_ylim(-5, 110)

    # Limpiar ejes numericos (no necesitamos valores exactos)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_edgecolor(C_GRAY)
        ax.spines[spine].set_linewidth(0.5)

    ax.grid(axis='y', color=C_GRAY, alpha=0.10, linewidth=0.5)

    # Cita Buffett
    ax.text(t[len(t)//2], -3,
            '"Se temeroso cuando los demas son codiciosos, codiciosos cuando los demas son temerosos." - W. Buffett',
            ha='center', va='top', color=C_GRAY, fontsize=8, style='italic')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/ciclo_psicologico_mercado.png',
                bbox_inches='tight', facecolor=C_BG)
    plt.close()
    print("  OK ciclo_psicologico_mercado.png")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Generando graficas con paleta unificada (fondo claro)...")
    generate_rollercoaster_chart()
    generate_risk_comparison()
    generate_market_psychology_cycle()
    print("Todas las graficas generadas exitosamente.")
