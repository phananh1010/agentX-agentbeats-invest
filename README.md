# Invest Scenario (AgentBeats)

The `scenarios/invest` benchmark pairs a purple research agent with a green evaluator to judge whether chosen tickers are likely to rise **30% or more by a target date**. The agent gathers fundamentals from a defined research window; the evaluator fact-checks outcomes in a later verify window and reports pass/fail per ticker.

## Run End to End
- Install deps: `uv sync`
- Provide a Perplexity key (used for search): `cp sample.env .env` then set `PERPLEXITY_API_KEY`
- Run the full pipeline with logs:  
  `uv run agentbeats-run scenarios/invest/scenario.toml --show-logs`
  - Starts both agents from the TOML, waits for them to be ready, sends the assessment, streams logs, and prints the result artifact.
- To change tickers or dates, edit the `[config]` section of `scenarios/invest/scenario.toml` (e.g., `tickers = ["RR", "AAPL"]`) and rerun the same command.
