# RL Trading Proyecto: Semillero de Aprendizaje por Refuerzo (Cripto + Sentimiento)

Este repositorio contiene el desarrollo de un agente de **Aprendizaje por Refuerzo (RL)** diseñado para operar en el mercado de **criptodivisas**, específicamente a través de la plataforma **Binance**. El proyecto incorpora un enfoque de **Finanzas Conductuales**, integrando datos tradicionales de mercado con un **Índice de Miedo y Codicia** colectivo.

## 👥 Integrantes
*   **Julian Duarte**
*   **Julian Jimenez**

## 👨‍🏫 Tutores de Semillero
*   Julián Sánchez López
*   Juan Carlos Urueña
*   Camilo Castillo

## 🎯 Objetivo Estratégico
Desarrollar un agente de RL capaz de ejecutar estrategias de compra, venta o mantenimiento en el mercado spot de criptoactivos (**BNB/USDT**), maximizando el **capital final acumulado $(\sum \gamma^t R_t)$** mediante una gestión inteligente del riesgo y el sentimiento del mercado.

## 🛠️ Metodología (MDP Extendido y Resolución)

### 1. El Estado ($S_t$)
El agente observa un vector compuesto por cuatro dimensiones críticas:
- **Régimen de Mercado ($M_t$):** Dirección del precio (Alcista / Bajista).
- **Sentimiento ($Sent_t$):** Nivel emocional del mercado (0-100) vía *Crypto Fear & Greed Index*.
- **Indicador Técnico (RSI):** Medida de sobrecompra o sobreventa del activo.
- **Inventario ($I_t$):** Posición actual (0: Efectivo, 1: Activo).

### 2. Función de Recompensa ($R_{t+1}$)
La recompensa incentiva las ganancias mientras penaliza los costos y el riesgo:
$$R_{t+1} = I_{t+1}r_{t+1} - c|I_{t+1} - I_t| - \lambda \sigma_t$$
*Donde $c$ son comisiones y $\lambda \sigma_t$ es una penalización por volatilidad excesiva.*

### 3. Algoritmo de Resolución
Utilizamos **Q-Learning Tabular**, un método que permite al agente aprender una "Tabla de Sabiduría" (Q-Table) basada en la experiencia histórica, optimizando sus decisiones a lo largo del tiempo.

## 📅 Datos y Periodo de Análisis
- **Activo:** BNB/USDT (Binance).
- **Temporalidad:** 1 hora (1h).
- **Periodo:** Enero 2023 - Diciembre 2024 (Elegido por su relevancia estratégica y variedad de ciclos).
- **Fuentes:** API de Binance y alternative.me.

## 📈 Estructura del Repositorio
- `trading_rl_project/`
  - `docs/`: Reporte LaTeX detallado y **Plan de Póster**.
  - `src/`: Lógica del Agente y Entorno de Simulación.
  - `data/`: Históricos de OHLCV y Sentimiento.

---
*Este proyecto se presentará en el evento de Semilleros de la Universidad Externado de Colombia.*
