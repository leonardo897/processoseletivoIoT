# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo:** Leonardo de Oliveira Sales Vieira
- **GitHub:** [leonardo897](https://github.com/leonardo897)

---

## 1️⃣ Visão Geral da Solução

O projeto implementa um **semáforo inteligente com suporte à travessia de pedestres**, simulado em um ESP32 via Wokwi utilizando MicroPython.
 
O sistema controla três LEDs (vermelho, amarelo e verde) que representam as fases do semáforo para veículos. Um botão azul permite que pedestres solicitem travessia, alterando o fluxo normal do semáforo. Um buzzer emite um alerta sonoro quando a fase de travessia é iniciada.
 
O usuário interage com o sistema pressionando o botão de pedestre durante a fase verde, o que força uma transição antecipada para amarelo e, em seguida, para vermelho, permitindo a travessia com segurança e sinalização sonora.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O programa é estruturado como uma **máquina de estados não-bloqueante**, com os seguintes estados definidos na classe `TrafficLightState`:
 
- `GREEN` → tráfego fluindo normalmente
- `YELLOW` → transição, atenção
- `RED` → veículos parados (ciclo normal)
- `PEDESTRIAN_CROSSING` → vermelho com travessia ativa e buzzer
O fluxo principal em `run_traffic_light()` executa um loop contínuo que, a cada iteração de 10ms:
 
1. Lê o estado do botão com debounce via classe `ButtonDebounce`
2. Atualiza o buzzer de forma não-bloqueante via classe `SoundAlert`
3. Avalia o estado atual e realiza transições com base em tempo (`ticks_ms`) ou eventos (botão pressionado)
4. Atualiza os LEDs conforme o estado
O uso de `time.ticks_ms()` no lugar de `time.sleep()` garante que nenhuma parte do sistema fique bloqueada aguardando, permitindo leitura contínua do botão e controle preciso do buzzer.

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | ID no diagrama | Pino ESP32 | Função |
|---|---|---|---|
| ESP32 DevKit C v4 | `esp32` | — | Microcontrolador principal |
| LED Vermelho | `red_led` | GPIO 13 | Sinaliza parada para veículos |
| LED Amarelo | `yellow_led` | GPIO 12 | Sinaliza atenção / transição |
| LED Verde | `green_led` | GPIO 14 | Sinaliza tráfego livre |
| Botão (azul) | `pedestrian_button` | GPIO 15 | Solicitação de travessia de pedestre |
| Buzzer | `buzzer1` | GPIO 27 | Alerta sonoro na travessia |

---

## 4️⃣ Decisões Técnicas Relevantes

**Máquina de estados não-bloqueante:** a lógica de temporização usa `time.ticks_diff()` em vez de `time.sleep()`, o que permite que o loop principal continue respondendo a eventos (como o botão) mesmo durante as esperas de cada fase.
 
**Debounce por software:** a classe `ButtonDebounce` detecta apenas a borda de descida do sinal do botão e ignora transições dentro de uma janela de 50ms, evitando leituras duplicadas por ruído mecânico.
 
**Buzzer não-bloqueante:** a classe `SoundAlert` alterna o estado do buzzer em intervalos de 200ms sem usar `sleep`, mantendo o loop principal responsivo durante o alerta sonoro.
 
**Separação de responsabilidades:** hardware, lógica de botão, lógica de som e máquina de estados são tratados em funções e classes separadas, tornando o código mais legível e fácil de manter.
 
**Constantes nomeadas:** todos os valores de temporização e pinos são definidos como constantes no topo do arquivo, facilitando ajustes sem necessidade de procurar valores espalhados pelo código.

---

## 5️⃣ Resultados Obtidos

O sistema funciona corretamente na simulação do Wokwi:
 
- O semáforo cicla automaticamente entre verde (5s), amarelo (2s) e vermelho (4s)
- Ao pressionar o botão durante a fase verde, o ciclo é antecipado e a fase de travessia é ativada com buzzer
- Os LEDs acendem e apagam corretamente em cada transição de estado
- As mensagens de transição são exibidas na serial, incluindo `"Estado inicial: GREEN` que é validado automaticamente pelo Wokwi CLI no pipeline de CI
- O pipeline do GitHub Actions executa com sucesso após o ajuste do timeout para 30 segundos
  

---

## 6️⃣ Comentários Adicionais (Opcional)

Durante o desenvolvimento, o principal desafio foi a configuração do pipeline de CI com o Wokwi CLI:
 
**Texto de validação:** o `expect_text` no `ci.yml` não detectava o print do `main.py`, causando timeout. Resolvido ao fazer com que ele detectasse a segunda mensagem ao invés da primeira.

Limitações da solução:

1. O sistema suporta apenas um semáforo isolado, sem comunicação com outros semáforos — em um cruzamento real seria necessário sincronização entre múltiplos controladores
2. Não há prioridade para veículos de emergência (ambulância, bombeiros), que em sistemas reais acionam o verde imediatamente

Principais aprendizados:

1. A importância de programação não-bloqueante em sistemas embarcados
2. Como estruturar uma máquina de estados em MicroPython
3. O funcionamento do pipeline CI/CD com GitHub Actions integrado ao Wokwi CLI, incluindo como o expect_text funciona como critério de validação

Uma melhoria futura seria adicionar um display para mostrar o tempo restante de cada fase, e suporte a múltiplos botões de pedestre em cruzamentos com mais de uma faixa.


---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
