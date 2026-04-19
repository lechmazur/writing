# API Documentation (Partial Refresh)

This document captures key public interfaces for recently updated scripts. For full project context, see `PROJECT_DOCUMENTATION.md` and `PIPELINES.md`.

---

## Module: run_poor_writing_analysis.py

Run the poor‑writing analyzer LLM over prepared prompt packets.

Inputs:
- Prompt files: `/mnt/r/writing2-data/for_poor_writing/<student>/analyze_story_*.txt`

Outputs:
- Raw responses: `/mnt/r/writing2-data/poor_writing_raw/<analyzer>/<student>/<story_fname>.txt`
- Log CSV: `/mnt/r/writing2/data/poor_writing_run_log.csv` (append)

Usage example:
```bash
python run_poor_writing_analysis.py -p 8040 --analyzer gpt-5-low --workers 24 --skip-existing
```

Requires an OpenAI‑compatible proxy at `http://localhost:<port>/v1/`. The SDK demands an API key but the proxy may ignore it.

### Constants
- `BASE: Path` → `/mnt/r/writing2`
- `PROMPT_ROOT: Path` → `/mnt/r/writing2-data/for_poor_writing`
- `RAW_ROOT: Path` → `/mnt/r/writing2-data/poor_writing_raw`
- `LOG_CSV: Path` → `BASE/data/poor_writing_run_log.csv`
- `DEFAULT_ANALYZER: str` → `"gpt-5-low"`
- `DEFAULT_PORT: int` → `8040`
- `DEFAULT_WORKERS: int` → `24`

### Functions

`_iter_students(selected: Iterable[str] | None) -> List[str]`
- Return the list of student ids to process. If `selected` is given, it is filtered to those present under `PROMPT_ROOT`; otherwise returns all subdirectories.

`_story_name_from_prompt(prompt_name: str) -> str`
- Map analyzer prompt basenames like `analyze_story_wc_123.txt` to output story names like `story_wc_123.txt` (others unchanged).

`_create_client(port: int) -> OpenAI`
- Create an OpenAI SDK client pointed at the local proxy with long timeouts suitable for large/slow responses.

`_append_log(row: List[str]) -> None`
- Append a CSV row to the run log, creating the file with a header if needed. Schema: `timestamp,analyzer,student,prompt_path,raw_path,status`.

`_process_one(analyzer: str, prompt_path: Path, raw_out: Path, port: int) -> None`
- Run one analyzer call; on success write `raw_out` and log `OK`, else log `ERROR <exc>`.

`_gather_tasks(analyzer: str, students: List[str], skip_existing: bool) -> List[Tuple[str, Path, Path]]`
- Build the task list by scanning `PROMPT_ROOT/<student>` for `analyze_story_*.txt`, mapping to `RAW_ROOT/<analyzer>/<student>/...`. Skips existing outputs if requested.

`run_jobs(analyzer: str, students: List[str], port: int, workers: int, skip_existing: bool) -> None`
- Execute analyzer calls in parallel with `ProcessPoolExecutor`. Prints pending count, progress every 50 completions, and start/end/duration.

`parse_args() -> argparse.Namespace`
- Parse CLI flags: `port`, `analyzer`, `students` (comma‑sep string), `workers`, `skip_existing`.
