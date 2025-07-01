
import subprocess
import logging
import os
from datetime import datetime

logging.basicConfig(filename='ansible_remediation.log', level=logging.INFO, format="%(asctime)s - %(message)s")

def run_ansible():
    try:
        logging.info("🔧 Running Ansible Remediation")
        playbook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ansible/playbook.yml"))
        subprocess.run(["ansible-playbook", playbook_path], check=True)
        logging.info("✅ Ansible remediation completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Ansible failed: {e}")

if __name__ == "__main__":
    run_ansible()
