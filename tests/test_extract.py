from src.extract import extract_jobs
import os

def test_extract_jobs(tmp_path):
    # Setup
    csv_path = tmp_path / "jobs.csv"
    csv_path.write_text("context\n{\"job_title\": \"Engineer\"}\n")
    output_dir = tmp_path / "extracted"

    # Test
    extract_jobs(csv_path, output_dir)
    assert os.listdir(output_dir) == ["job_0.txt"]
