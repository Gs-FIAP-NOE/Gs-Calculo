import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ===================================================
# CONFIGURAÇÃO INICIAL
# ===================================================
plt.style.use('seaborn-v0_8')
np.set_printoptions(precision=2)

# ===================================================
# 1. DADOS DO RIO ITAJAÍ-AÇU (BLUMENAU/SC)
# ===================================================
dias = np.arange(1, 11)
nivel_rio = np.array([0.8, 1.2, 1.6, 2.1, 2.5, 2.8, 2.6, 2.3, 1.9, 1.5])
nivel_alerta = 2  # Nível para risco de enchente

# ===================================================
# 2. MODELAGEM MATEMÁTICA
# ===================================================
# Ajuste polinomial (grau 3)
coeficientes = np.polyfit(dias, nivel_rio, 3)
polinomio = np.poly1d(coeficientes)

# Função para previsão
def prever_nivel(dia):
    return polinomio(dia)

# ===================================================
# 3. ANÁLISE DOS DADOS
# ===================================================
# Pontos críticos
derivada = np.polyder(polinomio)
raizes = np.roots(derivada)
pontos_criticos = raizes[(raizes >= dias.min()) & (raizes <= dias.max())]

# Dias de risco
dias_risco = dias[nivel_rio > nivel_alerta]
max_nivel = nivel_rio.max()
dia_max = dias[nivel_rio.argmax()]

# ===================================================
# 4. VISUALIZAÇÃO GRÁFICA
# ===================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [1.5, 1]})

# Gráfico principal
x_continuo = np.linspace(dias.min(), dias.max(), 100)
ax1.plot(dias, nivel_rio, 'bo-', label='Dados reais', markersize=8, linewidth=2)
ax1.plot(x_continuo, polinomio(x_continuo), 'r--', label=f'Modelo: {polinomio}', linewidth=2)

# Áreas de risco
ax1.axhline(y=nivel_alerta, color='orange', linestyle=':', linewidth=3, label='Nível de alerta')
ax1.fill_between(x_continuo, nivel_alerta, 3, color='orange', alpha=0.1)

# Destaques
ax1.plot(dia_max, max_nivel, 'ro', markersize=10, label='Pico máximo')
for dia in dias_risco:
    ax1.plot(dia, nivel_rio[dia-1], 'yo', markersize=8)

# Configurações do gráfico
ax1.set_title('NOÉ\nMonitoramento do Nível do Rio Itajaí-Açu', 
              fontsize=10,)
ax1.set_xlabel('Dias de monitoramento', fontsize=10)
ax1.set_ylabel('Nível do rio (metros)', fontsize=10)
ax1.grid(True, linestyle='--', alpha=1)
ax1.legend(loc='upper right', fontsize=10)
ax1.set_ylim(0, 3.5)

# Tabela de dados
col_labels = ['Dia', 'Nível (m)', 'Status']
cell_text = []
for dia, nivel in zip(dias, nivel_rio):
    if nivel > 2.5:
        status = 'EMERGÊNCIA'
    elif nivel > nivel_alerta:
        status = 'Alerta'
    else:
        status = 'Normal'
    cell_text.append([f'Dia {dia}', f'{nivel:.1f}m', status])

ax2.axis('off')
table = ax2.table(cellText=cell_text,
                  colLabels=col_labels,
                  loc='center',
                  cellLoc='center',
                  colWidths=[0.3, 0.3, 0.4])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)

# Destaque para células críticas
for i in range(1, len(cell_text)+1):
    if cell_text[i-1][2] == 'EMERGÊNCIA':
        table[(i, 2)].set_facecolor('red')
        table[(i, 2)].set_text_props(color='white')
    elif cell_text[i-1][2] == 'Alerta':
        table[(i, 2)].set_facecolor('orange')
        table[(i, 2)].set_text_props(color='black')


plt.tight_layout()
plt.show()

# ===================================================
# 5. RELATÓRIO DE ANÁLISE
# ===================================================
print("\n" + "="*60)
print("RELATÓRIO TÉCNICO - NOÉ".center(60))
print("="*60)

print(f"\n{'1. MODELO MATEMÁTICO':-^60}")
print(f"Função polinomial ajustada:\n{polinomio}")
print(f"\nDomínio: Dias {dias.min()} a {dias.max()}")
print(f"Imagem: Nível de {nivel_rio.min():.1f}m a {nivel_rio.max():.1f}m")

print(f"\n{'2. PONTOS CRÍTICOS':-^60}")
print(f"Nível máximo: {max_nivel:.1f}m no Dia {dia_max}")
print(f"Dias com risco de enchente (> {nivel_alerta}m): {', '.join(map(str, dias_risco))}")

print(f"\n{'3. RECOMENDAÇÕES':-^60}")
if len(dias_risco) > 3:
    print("⚠️ Situação CRÍTICA: Acionar plano de evacuação!")
elif len(dias_risco) > 0:
    print("⚠️ Atenção: Monitorar áreas ribeirinhas")
else:
    print("✅ Situação dentro da normalidade")
print("="*60 + "\n")