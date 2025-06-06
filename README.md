<div align="center">

<img src="https://github.com/Gs-FIAP-NOE/Gs-FrontEnd-WebDev/raw/main/src/assets/img/logo-light.png" width="200px">

</div>

<div  align="center">

### Muito Antes Da Tempestade, Vem NOÉ!

# [noe.com.br](https://gs-fiap-noe.github.io/Gs-FrontEnd-WebDev/)
</div>


# 🌊 NOÉ - Plataforma de Prevenção de Enchentes

## 📃 Sobre o Projeto

O projeto **NOÉ** foi desenvolvido como parte da disciplina *Differentiated Problem Solving* do curso de Engenharia de Software da FIAP. A proposta tem como foco o **monitoramento de rios e comportas**, com alertas preventivos de **enchentes** no rio Itajaí-Açu.

Esta versão inclui:

- Modelo matemático de previsão
- Análise funcional
- Protótipo visual (gráfico)
- Identificação de dias de risco e emissão de alertas

## 🤓 Modelo Matemático

A função usada para estimar o nível do rio (em metros) ao longo de 10 dias é uma **função polinomial de 3º grau**:

```math
f(x) = −0.004662x³ + 0.004196x² + 0.5452x + 0.18
```

- **Domínio prático**: `x ∈ [1, 10]` (dias)
- **Imagem prática**: `f(x) ∈ [0.8, 2.8]` metros

### 🔍 Análise do Pico de Risco

O nível máximo do rio previsto pelo modelo ocorre no:

- **Dia 6**, com nível aproximado de **2,8 m**, coincidindo com os dados reais observados.
- Este valor **ultrapassa o limite de emergência**, exigindo atenção imediata das autoridades.

---

## 📊 Sistema de Alertas

Com base nos níveis diários observados, os alertas são classificados da seguinte forma:

| Dia  | Nível (m) | Alerta                      |
|------|-----------|-----------------------------|
| 1    | 0,8       | ✅ Nível Seguro              |
| 2    | 1,2       | ✅ Nível Seguro              |
| 3    | 1,6       | ✅ Nível Seguro              |
| 4    | 2,1       | ⚠ ALERTA 1 (Risco Moderado) |
| 5    | 2,5       | ⚠ ALERTA 1 (Risco Moderado) |
| 6    | 2,8       | 🚨 ALERTA 2 (Emergência)     |
| 7    | 2,6       | 🚨 ALERTA 2 (Emergência)     |
| 8    | 2,3       | ⚠ ALERTA 1 (Risco Moderado) |
| 9    | 1,9       | ✅ Nível Seguro              |
| 10   | 1,5       | ✅ Nível Seguro              |

### 🔔 Critérios de Alerta

- ✅ **Seguro**: Nível do rio abaixo de **2,0 m**
- ⚠ **Alerta 1 (Risco Moderado)**: Entre **2,0 m** e **2,5 m**
- 🚨 **Alerta 2 (Emergência)**: Acima de **2,5 m**

## 💻 Tecnologias Utilizadas

- Python (modelagem matemática)
- Gráficos de visualização
- GitHub para versionamento
- Documentação científica

## 📦 Dependências

Para executar a simulação e visualização do modelo, certifique-se de ter as seguintes bibliotecas Python instaladas:

```bash
pip install numpy matplotlib
```

### Bibliotecas utilizadas:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```

## 👥 Equipe

Leonardo Da Silva Pinto 564929 <br>
Samuel Enzo D. Monteiro 564391 <br>
Lucas Toledo Cortonezi 563271 <br>
