# Documentação do Processo de Desenvolvimento

## Desafios
1. Garantir que o programa lidasse com entradas inválidas, como caracteres não numéricos.
2. Tratar o erro de divisão por zero de forma apropriada.

## Como o Git foi Utilizado
- **Branches**: Cada funcionalidade (operação) foi desenvolvida em uma branch separada:
  - `feature/addition`
  - `feature/subtraction`
  - `feature/multiplication`
  - `feature/division`
- **Commits**: Commits frequentes documentaram o progresso de cada etapa.
- **Merge**: Após concluir e testar cada funcionalidade, ela foi integrada à branch principal (`main`).

## Comandos Úteis do Git Utilizados
- `git branch feature/<funcionalidade>`: Criar branches para cada funcionalidade.
- `git merge`: Integrar funcionalidades na branch principal.
- `git log`: Visualizar o histórico de commits.
