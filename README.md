# Atividade de Revisão Python 

**Disciplina:** Desenvolvimento de APIs e Microserviços (DAM)  
**Integrantes:** Anna Julia Higa Farincho, Leticia Macedo, Evelyn Mercês | **Grupo: 4**

**Instituição:** IMPACTA  
**Linguagem:** Python 3.13


---

## Sobre o Projeto

Este repositório apresenta uma coleção abrangente de exercícios práticos em Python, desenvolvidos como atividade de revisão acadêmica. O projeto explora desde conceitos fundamentais da linguagem até integração com APIs externas, oferecendo uma experiência completa de desenvolvimento.

## Visão Geral dos Desafios

O projeto está estruturado em 10 exercícios distintos, cada um abordando aspectos específicos da programação Python:

**Sistemas de Cálculo e Lógica**
- Sistema inteligente de desconto para posto de combustível
- Simulador completo de caixa eletrônico com otimização de notas
- Calculadora acadêmica com sistema de conceitos automatizado

**Aplicações Interativas**
- Corretor automático de provas com análise estatística da turma
- Sistema de pedidos para lanchonete com gestão de cardápio
- Calculadora de progressão salarial com aumentos compostos

**Processamento de Dados**
- Analisador estatístico de sequências numéricas
- Processador de dados com análises avançadas

**Integração com APIs**
- Consultor internacional de países via RestCountries API
- Sistema de cotação de moedas em tempo real
- Identificador geográfico de regiões paulistanas por CEP

## Arquitetura Técnica

```
projeto/
├── README.md              # Documentação principal
├── requirements.txt       # Dependências do projeto  
├── .gitignore            # Configuração Git
└── Atividade/            # Código-fonte dos exercícios
    ├── ex01.py           # Sistema combustível
    ├── ex02.py           # Caixa eletrônico
    ├── ex03.py           # Avaliação acadêmica
    ├── ex04.py           # Corretor de provas
    ├── ex05.py           # Sistema lanchonete
    ├── ex06.py           # Progressão salarial
    ├── ex07.py           # Análise numérica
    ├── ex08.py           # API países
    ├── ex09.py           # API moedas
    └── ex10.py           # Mapeamento CEP
```

## Stack Tecnológica

**Core**
- Python 3.13 com bibliotecas nativas
- Manipulação avançada de estruturas de dados
- Algoritmos de otimização e cálculo

**APIs Integradas**
- **RestCountries API** - Base global de informações geopolíticas
- **ExchangeRate API** - Cotações financeiras em tempo real  
- **ViaCEP API** - Serviço brasileiro de consulta postal

**Bibliotecas**
- `requests` - Cliente HTTP para integração com APIs
- `json` - Parser nativo para dados estruturados

## Destaques de Implementação

**Robustez e Confiabilidade**
- Validação rigorosa de entrada de dados
- Tratamento abrangente de exceções HTTP
- Algoritmos otimizados para performance

**Experiência do Usuário**
- Interfaces intuitivas via terminal
- Feedback claro e informativo
- Fluxos de navegação simplificados

**Qualidade de Código**
- Estrutura modular e reutilizável
- Documentação inline estratégica
- Padrões consistentes de nomenclatura

## Ambiente de Desenvolvimento

**Configuração Inicial**
```bash
# Clonar repositório
git clone <url-do-repositorio>

# Instalar dependências
pip install -r requirements.txt
```

**Execução Individual**
```bash
# Navegar para diretório
cd Atividade/

# Executar exercício específico
python ex01.py
```

## Aplicações Práticas

Este conjunto de exercícios simula cenários reais de desenvolvimento, preparando para:

- **Sistemas Comerciais** - Gestão de vendas e descontos
- **Aplicações Financeiras** - Cálculos monetários e progressões
- **Integrações Corporativas** - Consumo de APIs e processamento de dados
- **Análise de Dados** - Estatísticas e relatórios automatizados
- **Geolocalização** - Mapeamento e identificação regional

## Conceitos Abordados

**Fundamentos**
- Estruturas condicionais complexas
- Loops otimizados e controle de fluxo
- Manipulação avançada de listas e dicionários

**Programação Avançada**
- Consumo e parsing de APIs REST
- Tratamento robusto de exceções
- Algoritmos de otimização numérica

**Integração de Sistemas**
- Comunicação HTTP eficiente
- Processamento de dados JSON
- Validação e sanitização de entrada

---

*Desenvolvido como atividade acadêmica com foco na aplicação prática de conceitos avançados de Python e integração de sistemas.*
