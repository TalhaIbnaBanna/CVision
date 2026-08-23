"""Debug: simulate what the pipeline does and check key matching."""
import sys
import os
from pathlib import Path

# Add project root to sys.path so it can find the 'modules' package robustly
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.parser import extract_markdown_from_pdf, extract_candidate_metadata

folder = PROJECT_ROOT / "assets" / "input_and_output" / "sample_resumes"
filenames = []
for pdf in sorted(folder.glob("*.pdf")):
    fn = pdf.name
    display_name = Path(fn).stem.replace("_", " ").replace("-", " ").title()
    filenames.append((fn, display_name))
    print(f"filename: {fn!r}")
    print(f"  display_name (CandidateRecord.name): {display_name!r}")
    print(f"  cand_name from results_df row would be: (same as display_name)")
    print()
