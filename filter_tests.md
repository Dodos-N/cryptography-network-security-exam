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

 * **Expected Outcome:** Connection allowed / port open.
   
* **Actual Command Output:**
  Connection to 10.0.0.100 443 port [tcp/https] succeeded!
* **Status: PASSED**

* **Test 2: Blocked Access — Guest Network (Task 3a)**
* **Source Host:** Guest Laptop (192.168.20.50)

* **Command Executed:**
  ```Bash
  nc -zv -w 3 10.0.0.100 443
  ```
  
* **Expected Outcome:** Connection dropped / timeout.

* **Actual Command Output:**

  nc: connect to 10.0.0.100 port 443 (tcp) timed out: Operation now in progress
* **Status: PASSED**

* **Test 3: Blocked Access — Unfamiliar External IP (Task 3c)**
* **Source Host:** External Machine (172.16.0.88)

* **Command Executed:**
  ```Bash
  curl --connect-timeout 3 [https://10.0.0.100](https://10.0.0.100)
  ```

* **Expected Outcome:** Connection dropped / timeout.

* **Actual Command Output:**

  curl: (28) Failed to connect to 10.0.0.100 port 443 after 3001 ms: Could not connect
* **Status: PASSED**
