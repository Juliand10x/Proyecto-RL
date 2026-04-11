# Proyecto: Trading con Aprendizaje por Refuerzo (RL) e IA de Sentimiento

Este repositorio contiene el desarrollo de un agente de **Aprendizaje por Refuerzo (Reinforcement Learning)** diseñado para operar en el mercado de criptomonedas (BNB/USDT) integrando análisis técnico y un indicador de sentimiento emocional.

## 🚀 Estado Actual del Proyecto: Fase Teórica Finalizada
Hemos completado el marco conceptual y la formulación matemática del agente, asegurando que el proyecto sea académicamente riguroso y pedagógicamente claro.

### Decisiones Técnicas Clave:
- **Algoritmo:** Q-Learning Tabular (Basado en la Ecuación de Bellman).
- **Objetivo de Optimización:** Maximización del Retorno Acumulado ($G_t$).
- **Control de Riesgo:** Función de recompensa penalizada por volatilidad ($-\lambda \sigma_t$) y comisiones de transacción.
- **Estado ($S_t$):** Vector compuesto por Régimen de Mercado, RSI, Sentimiento Emocional e Inventario (Discretizados).
- **Fuente de Sentimiento:** Crypto Fear & Greed Index de **Alternative.me** (Frecuencia: 1 hora).
- **Datos:** API de Binance, periodo enero 2023 - diciembre 2024.

## 📁 Estructura del Repositorio
- `docs/`: Contiene el reporte técnico detallado en LaTeX (`trading_rl_report_v2.tex`).
- `src/`: (En desarrollo) Scripts de Python para la simulación y entrenamiento del agente.
- `README.md`: Este archivo, con el resumen y estado del proyecto.

## 📑 Documentación Destacada
El reporte **`trading_rl_report_v2.tex`** incluye:
- Glosario técnico interactivo (37 términos).
- Desglose pedagógico de la Ecuación de Bellman.
- Justificación basada en Finanzas Conductuales.
- Criterios de evaluación (Ratio de Sharpe, Drawdown).

---
**Universidad Externado de Colombia**  
*Ciencia de Datos - Departamento de Matemáticas*  
*Semillero de Aprendizaje por Refuerzo*
