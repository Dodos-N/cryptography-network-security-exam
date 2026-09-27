# Risk Assessment

## Project: Cryptography and Network Security

### 1. Introduction

The polytechnic institute stores student records on a central server and
transfers files between two campuses. The security review identified weak
staff passwords, outdated software, unencrypted file transfers, guest network
access to the records server, and repeated attempts to reach the server from
an unfamiliar external address.

This risk assessment identifies the main assets, vulnerabilities, possible
consequences, risk levels, and recommended security controls.

---

## 2. Assets

| No. | Asset | Description |
|-----|-------|-------------|
| 1 | Student Records Server | Central server that stores student records and other important academic information. |
| 2 | Student Record Files | Digital files containing student information that are transferred between the two campuses. |
| 3 | Network Infrastructure | The network, firewall, and communication services used to provide access to the student records server. |

---

## 3. Vulnerabilities and Possible Consequences

| No. | Vulnerability | Possible Consequence |
|-----|---------------|----------------------|
| 1 | Weak staff passwords | Attackers may guess or compromise staff accounts and gain unauthorized access to student records. This could result in data disclosure or unauthorized modification. |
| 2 | Unencrypted file transfers | Student records transferred between campuses may be intercepted by unauthorized users, resulting in exposure of confidential information. |
| 3 | Guest network access to the records server | Unauthorized users on the guest network may reach the student records server, increasing the risk of unauthorized access, data theft, or disruption of services. |

---

## 4. Risk Ranking

The risks are ranked according to their estimated likelihood and potential
impact on the confidentiality, integrity, and availability of the institute's
systems and student records.

| Rank | Risk | Likelihood | Impact | Risk Level | Reason |
|------|------|------------|--------|------------|--------|
| 1 | Guest network access to the records server | High | High | High | The records server contains sensitive student information, and allowing guest network access creates a direct opportunity for unauthorized users to attempt access. |
| 2 | Weak staff passwords | High | High | High | Weak passwords can be easier to guess or compromise, potentially allowing an attacker to access systems using a legitimate staff account. |
| 3 | Unencrypted file transfers | Medium | High | High | Data transferred without encryption may be intercepted, exposing confidential student information during transmission. |

---

## 5. Recommended Security Controls

| Risk | Recommended Control | Purpose |
|------|---------------------|---------|
| Guest network access to the records server | Configure firewall rules to block guest network access to the student records server while permitting authorized staff access to the required service. | Prevent unauthorized network access to the records server. |
| Weak staff passwords | Enforce a strong password policy requiring sufficiently complex passwords and secure authentication practices. | Reduce the likelihood of unauthorized access through compromised or easily guessed passwords. |
| Unencrypted file transfers | Use encrypted communication for file transfers, such as a secure transfer service approved for the laboratory environment. | Protect student records from interception while being transferred between campuses. |

---

## 6. Conclusion

The assessment identifies three important security risks affecting the
institute's student records and network environment. The most important
controls are to restrict unauthorized network access, strengthen staff
authentication, and protect files during transmission.

These controls will support the confidentiality, integrity, and availability
of student records and provide a foundation for the encryption and firewall
implementation carried out in the next stages of the project.
