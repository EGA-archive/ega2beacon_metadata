# ega2beacon_metadata

This software will convert EGA metadata to BFF

## What it does
- Connects to a PostgreSQL metadata store.
- Fetches EGA XML (e.g., `analysis` records).
- Parses key accessions (e.g., `STUDY_REF`, `SAMPLE_REF`).
- Stages values into the Beacon v2 Models (XLSX) — on the path to BFF JSON export.

## Status
`alpha` — parsing and XLSX write are prototyped; full BFF export pending.

## Requirements
- Python 3.9+
- `psycopg2`, `PyYAML`, `openpyxl`
- Access to your EGA-derived PostgreSQL with XML payloads

```bash
pip install psycopg2-binary PyYAML openpyxl
```

## Quick start
1. Create `config/config.yml`:
   ```yaml
   plsql:
     host: your-host
     port: 5432
     dbname: your-db
     user: your-user
     password: your-pass
   ```
2. Place the Beacon Models template (XLSX) somewhere accessible and note its path.
3. Run:
   ```bash
   python ega2beacon.py
   ```

## Configuration
- DB settings come from `config/config.yml`.
- Update SQL in `get_metadata_egapro()` to match your schema/IDs.
- Update `write_metadata_beacon()` with your XLSX template path and output path.

## Usage notes
- The demo query uses a hardcoded `ega_stable_id`; switch to parameters/batch processing for real runs.
- Use explicit projections and robust XML parsing for production.
- Never commit credentials.

## Roadmap
- Implement full XML → Beacon Models mapping (biosamples, individuals, analyses, runs, datasets).
- Add BFF JSON writer + validation.
- CLI (`argparse`) for IDs, ranges, batch size, and template/output paths.
- Tests for XML fixtures and template headers.
