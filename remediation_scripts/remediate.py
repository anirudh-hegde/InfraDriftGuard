
import os
import subprocess
import logging
from datetime import datetime

LOG_FILE = "remediation.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def remediate():
    try:
        logging.info("🔧 Starting Terraform Remediation")
        terraform_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../terraform"))
        os.chdir(terraform_dir)
        subprocess.run(["terraform", "init"], check=True)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        logging.info("✅ Remediation completed successfully")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Terraform failed: {e}")
    except Exception as ex:
        logging.error(f"❗ Unexpected error: {ex}")

if __name__ == "__main__":
    remediate()
