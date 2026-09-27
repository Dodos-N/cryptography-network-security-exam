# Network Traffic Filtering Test Log
 
**Target Service:** Student Records Server (Port 443 / HTTPS)  
**Server IP:** `10.0.0.100`

---

## Network Architecture Setup
* **Staff Network Subnet:** `192.168.10.0/24`
* **Guest Network Subnet:** `192.168.20.0/24`
* **External Network Subnet:** `172.16.0.0/16`

---

## Execution Logs & Verification Matrix

### Test 1: Permitted Access — Staff Network (Task 3b)
* **Source Host:** Staff Workstation (`192.168.10.15`)
* **Command Executed:**
  ```bash
  nc -zv -w 3 10.0.0.100 443
  ```
  
