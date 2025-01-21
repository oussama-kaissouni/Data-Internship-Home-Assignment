from src.transform import clean_and_transform
import json

def test_clean_and_transform(tmp_path):
    # Setup
    input_dir = tmp_path / "extracted"
    input_dir.mkdir()
    (input_dir / "job_0.txt").write_text("{\"job_title\": \"Engineer\"}")
    output_dir = tmp_path / "transformed"

    # Test
    clean_and_transform(input_dir, output_dir)
    transformed_file = output_dir / "job_0.json"
    assert transformed_file.exists()

    with transformed_file.open() as f:
        data = json.load(f)
        assert data["job"]["title"] == "Engineer"