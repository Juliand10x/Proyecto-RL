# RL Trading Proyecto: Semillero de Aprendizaje por Refuerzo (Cripto + Sentimiento)

Este repositorio contiene el desarrollo de un agente de **Aprendizaje por Refuerzo (RL)** diseñado para operar en el mercado de **criptodivisas**, específicamente a través de la plataforma **Binance**. El proyecto incorpora un enfoque de **Finanzas Conductuales**, integrando datos tradicionales de mercado con un **Índice de Miedo y Codicia** derivado del sentimiento en redes sociales.

## 👥 Integrantes
*   **Julian Duarte**
*   **Julian Jimenez**

## 👨‍🏫 Tutores de Semillero
*   Julián Sánchez López
*   Juan Carlos Urueña
*   Camilo Castillo

## 🎯 Objetivo
Desarrollar un agente de RL capaz de ejecutar estrategias de compra, venta o mantenimiento en el mercado spot de criptoactivos (foco en el par **BNB/USDT**), validando si la inclusión de métricas de sentimiento colectivo mejora la rentabilidad y la gestión de riesgo frente a modelos puramente técnicos.

## 💡 Justificación: Por qué Cripto y Binance
1.  **Influencia de la Emoción Colectiva:** Los mercados de criptomonedas son altamente sensibles al sentimiento en redes sociales (FOMO, FUD), lo que los convierte en el escenario ideal para probar el impacto de variables psicológicas en la toma de decisiones.
2.  **Volatilidad y Liquidez:** La alta volatilidad de activos como BNB ofrece mayores oportunidades de aprendizaje para el agente, mientras que la liquidez de Binance permite simulaciones de ejecución realistas.
3.  **Operación 24/7:** A diferencia de los mercados tradicionales, el flujo continuo de datos de criptomonedas permite un entrenamiento y validación sin pausas por cierres de mercado.

## 🛠️ Metodología (MDP Extendido)
El proyecto escala el modelo tradicional integrando una tercera dimensión al estado:
- **Estados ($S$):** $S_t = (M_t, I_t, Sent_t)$
    - $M_t$: Régimen de mercado (Basado en retornos logarítmicos).
    - $I_t$: Posición de inventario (Plano o Largo).
    - $Sent_t$: Nivel de sentimiento (Fear & Greed Index / Sentimiento en X/Reddit).
- **Acciones ($A$):** Buy, Sell, Hold (admisibles según inventario).
- **Entorno:** Implementación personalizada en Python integrada con la API de Binance.

## 📅 Próximos Pasos (Evento del 17 de Abril)
- [ ] Conexión a la API de Binance para recolección de datos históricos (Klines/Candelas).
- [ ] Integración de un pipeline de sentimiento (ej: Crypto Fear & Greed API).
- [ ] Entrenamiento de agentes con algoritmos de Tabular RL y/o Deep RL (DQN).
- [ ] Comparativa de P&L acumulado frente a la estrategia *Buy & Hold*.

## 📈 Estructura del Repositorio
- `trading_rl_project/`
  - `docs/`: Reporte LaTeX y póster para el encuentro.
  - `src/`: Entorno Gymnasium y lógica del agente.
  - `data/`: Datos de Binance y series de tiempo de sentimiento.
