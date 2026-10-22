# FocoLab Agent

Executor experimental para o projeto FocoLab — loja de produtividade.

- Opera apenas em **22/10/2026 entre 16h e 18h (America/Sao_Paulo)**; cada execução verifica a data e o horário.
- Um arquivo de planejamento é criado por execução até completar cinco tarefas.
- As ações são executadas em sequência, imediatamente após o término da anterior, em uma única execução GitHub Actions. Não há cron.
- Sem IA deliberativa, APIs externas, acesso ao Floot, pagamentos, fornecedores, campanhas ou decisões financeiras.
- Custos: sem serviços pagos configurados; uso sujeito às políticas de limites do GitHub Actions.

## Ativação
Abrir Actions > FocoLab - executor por conclusão > Run workflow. Conferir os registros e os arquivos `output/`.
O agendamento também depende das configurações do GitHub Actions.
