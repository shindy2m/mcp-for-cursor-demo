# Cursor IDE Configuration

Tento soubor obsahuje návod pro připojení MCP Demo serveru k Cursor IDE.

## Postup konfigurace

1. **Otevřete Cursor Settings**
   - Stiskněte `Ctrl+,` (Windows/Linux) nebo `Cmd+,` (Mac)
   - Nebo jděte do `File > Preferences > Settings`

2. **Vyhledejte MCP nastavení**
   - Vyhledejte "mcp" v settings
   - Najděte sekci "MCP Servers"

3. **Přidejte konfiguraci**
   Zkopírujte a vložte následující konfiguraci:

```json
{
  "mcpServers": {
    "mcp-demo": {
      "command": "python",
      "args": ["C:/Users/jiri.sindelar/Desktop/Projects/mcp-demo/mcp-demo/src/server.py"],
      "env": {}
    }
  }
}
```

**DŮLEŽITÉ**: Upravte cestu `C:/Users/jiri.sindelar/Desktop/Projects/mcp-demo/mcp-demo/src/server.py` na skutečnou cestu k vašemu projektu.

## Alternativní způsob spuštění

Můžete také použít spouštěcí skript:

```json
{
  "mcpServers": {
    "mcp-demo": {
      "command": "python", 
      "args": ["C:/Users/jiri.sindelar/Desktop/Projects/mcp-demo/mcp-demo/run_server.py"],
      "env": {}
    }
  }
}
```

## Ověření funkčnosti

1. **Restartujte Cursor IDE** po přidání konfigurace
2. **Otevřete nový chat** nebo použijte existující
3. **Zkuste použít nástroje**:
   - "Vypočítej 25 + 17 pomocí kalkulačky"
   - "Zobraz systémové informace"


## Řešení problémů

- **Server se nespouští**: Zkontrolujte, že máte nainstalované všechny závislosti (`pip install -r requirements.txt`)
- **Nesprávná cesta**: Ověřte, že cesta k server.py nebo run_server.py je správná
- **Python není nalezen**: Ujistěte se, že Python je v PATH nebo použijte úplnou cestu k Python interpretu
- **Logs**: Zkontrolujte Output panel v Cursor pro chybové zprávy

## Testování mimo Cursor

Pro testování mimo Cursor můžete spustit:

```bash
python test_server.py
```

Tento test ověří, že všechny nástroje fungují správně.

## Dostupné nástroje

- **calculator**: Základní aritmetické operace
- **get_system_info**: Informace o systému (OS, CPU, paměť, disk)
 