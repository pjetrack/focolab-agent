"""Agente experimental determinístico. Sem APIs externas ou custos."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import json

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)
now = datetime.now(ZoneInfo("America/Sao_Paulo"))
if not (now.year == 2026 and now.month == 10 and now.day == 22 and 16 <= now.hour < 18):
    print("Fora da janela autorizada: nenhuma ação realizada.")
    raise SystemExit(0)

state_path = OUT / "state.json"
state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {"completed": []}
steps = {
    "01-proposta-de-valor.md": "# FocoLab — proposta de valor\nPúblico: estudantes que querem planejar os estudos.\nBenefício: clareza nas prioridades e revisões.\nNão prometer aprovação ou resultados não comprovados.\n",
    "02-kit-produto.md": "# Kit FocoLab\nPreparar planner semanal, quadro de prioridades, calendário de revisão e guia de uso.\nAinda não disponível para compra.\n",
    "03-copy-comercial.md": "# Apresentação comercial\nTítulo: Faça seu plano de estudos sair do papel.\nDescrição: Ferramentas digitais simples para planejar e acompanhar sua rotina.\nCTA: Experimente o planejador gratuito.\n",
    "04-checklist.md": "# Pendências antes de vender\n- [ ] Finalizar arquivos\n- [ ] Configurar checkout e entrega\n- [ ] Revisar termos e políticas\n- [ ] Testar uma compra com aprovação\n",
    "05-relatorio.md": "# Relatório de operação\nExecutor restrito a 22/10/2026 até 18h (São Paulo). Sem custos, anúncios ou acesso a contas financeiras. Não integra ao Floot automaticamente.\n"
}
for name, content in steps.items():
    if name not in state["completed"]:
        (OUT/name).write_text(content, encoding="utf-8")
        state["completed"].append(name)
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Criado:", name)
        break
else:
    print("Todas as tarefas predefinidas foram concluídas.")
