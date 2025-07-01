
# InfraDriftGuard

### Automated Infrastructure Drift Detection and Remediation

#### 🔧 Tools Used:
- Terraform (Provisioning)
- AWS Config (Drift Detection)
- Ansible (Remediation)
- Python (Automation)
- GitHub Actions (Scheduled Detection)
- Logstash (Audit Logging)
- Elasticsearch/Kibana (Visualization)

#### 🚀 How to Use:

1. **Terraform**
```bash
cd terraform
terraform init && terraform apply -auto-approve
```

2. **Run Remediation (Terraform-based)**
```bash
cd remediation_scripts
python3 remediate.py
```

3. **Run Remediation (Ansible-based)**
```bash
python3 ansible_remediate.py
```

4. **Enable GitHub Actions for CI Drift Check**

5. **Logstash Integration**
Set up `logstash.conf` to monitor `remediation_scripts/*.log`.

All detection and remediation steps are logged for compliance and reporting.
