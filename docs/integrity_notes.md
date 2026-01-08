# Data Integrity Verification

The integrity of the raw datasets is ensured using SHA-256 checksums.

To verify that the raw data files have not been modified, run:

```bash
sha256sum -c docs/checksums.sha256

