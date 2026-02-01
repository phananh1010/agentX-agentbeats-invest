# AgentBeats Investment Scenario
Predicting short-term stock price movements offers the potential for significant financial returns, but it is inherently associated with high risk. Incorrect stock selection can lead to substantial opportunity costs, prolonged capital lock-up (“bag holding”), or direct financial losses, particularly in highly volatile or speculative markets.

One common approach to mitigating these risks is systematic analysis of publicly available information, including fundamental indicators, expert opinions, and aggregated market sentiment. With the emergence of agentic systems capable of autonomously querying and synthesizing large volumes of online data, it becomes possible to formalize this process into an automated research pipeline. However, investment information is often noisy, biased, and internally contradictory. Distilling coherent, evidence-supported investment theses from heterogeneous sources remains a non-trivial economic and epistemic problem.

This project develops a benchmarking framework to evaluate the ability of autonomous agents to:

+ Perform structured financial research
+ Filter and reconcile conflicting information
+ Generate economically meaningful arguments
+ And finally, identify stock tickers that exhibit a high probability of significant short-term price appreciation.

The `scenarios/invest` benchmark pairs a purple research agent with a green evaluator to judge whether chosen tickers are likely to rise **30% or more by a target date**. The agent gathers fundamentals from a defined research window; the evaluator fact-checks outcomes in a later verify window and reports pass/fail per ticker.

# Run End to End
- Install deps: `uv sync`
- Provide a Perplexity key (used for search): `cp sample.env .env` then set `PERPLEXITY_API_KEY`
- Run the full pipeline with logs:  
  `uv run agentbeats-run scenarios/invest/scenario.toml --show-logs`
  - Starts both agents from the TOML, waits for them to be ready, sends the assessment, streams logs, and prints the result artifact.
- To change tickers or dates, edit the `[config]` section of `scenarios/invest/scenario.toml` (e.g., `tickers = ["RR", "AAPL"]`) and rerun the same command.
