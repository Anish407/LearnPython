When psutil actually matters for file workflows
1) Prevent disk-full failures (very common in batch jobs / ML pipelines)

If your job writes big outputs (zips, model checkpoints, parquet, logs), you can check free space before starting.

```python
import psutil

free = psutil.disk_usage("/").free
if free < 5 * 1024**3:  # < 5 GB
    raise RuntimeError("Not enough disk space to start this job")

```
2)Detect and handle memory pressure while reading huge files

If you read large CSV/JSON into memory, you can OOM the box/container. psutil lets you make your code resource-aware.
```python
import psutil

avail = psutil.virtual_memory().available
if avail < 2 * 1024**3:
    print("Low memory — switching to streaming mode")

```