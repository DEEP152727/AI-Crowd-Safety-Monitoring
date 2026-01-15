**AI-Based Public Safety Monitoring & Risk Detection System**

**Logic-Centric \| Algorithm-Focused Project**

**1. Overview**

Crowded public places such as **metro stations, markets, festivals, and
railway stations** are prone to incidents like **panic, stampedes, and
sudden crowd movement**. Manual CCTV monitoring is **slow, error-prone,
and difficult to scale**.

This project presents an **AI-based, rule-driven system** that analyses
**crowd-level behaviour** from video input to detect abnormal activity
and classify **public safety risks**.  
The system strictly follows **ethical AI principles** by avoiding **face
recognition, individual tracking, or biometric data usage**.

**2. Objectives**

- **Analyses CCTV or simulated crowd videos**

- **Detect abnormal crowd behaviour** (motion & density)

- **Classify risks** into **LOW, MEDIUM, HIGH**

- **Generate explainable alerts** in near real-time

- Maintain **privacy-preserving crowd analysis**

**3. Objectives of the Project**

The main objectives of this project are:

- To analyse pre-recorded or simulated CCTV video footage

- To detect abnormal crowd-level behaviour

- To classify crowd risk into predefined levels (LOW, MEDIUM, HIGH)

- To generate explainable, human-readable alerts

- To design an ethical, privacy-preserving AI system

**4. Team Members and Work Distribution**

**Team Composition**

<table>
<colgroup>
<col style="width: 98%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team Member</strong></th>
<th><strong>Role &amp; Responsibility</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Deepak Yadav</strong></td>
<td><strong>Project Lead, System Architecture Design, Main Pipeline
Integration, Final Risk Decision Logic</strong></td>
</tr>
<tr class="even">
<td><strong>Aaditya Mishra</strong></td>
<td><strong>Motion Analysis Module (Optical Flow), Performance
Optimization</strong></td>
</tr>
<tr class="odd">
<td><strong>Aaditya Yadav</strong></td>
<td><strong>Density Estimation Module, Background Subtraction
Logic</strong></td>
</tr>
<tr class="even">
<td><strong>Vedant Parab</strong></td>
<td><p><strong>Risk Classification Engine, Alert Generation,
Documentation Support</strong></p>
<table>
<colgroup>
<col style="width: 94%" />
<col style="width: 5%" />
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
</tbody>
</table></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>5. Technology Stack</strong></p>
<p><strong>Software Tools</strong></p>
<ul>
<li><p><strong>Programming Language: Python</strong></p></li>
<li><p><strong>IDE: Visual Studio Code (VS Code)</strong></p></li>
<li><p><strong>Libraries Used:</strong></p>
<ul>
<li><p><strong>OpenCV</strong></p></li>
<li><p><strong>NumPy</strong></p></li>
</ul></li>
</ul>
<p><strong>Hardware</strong></p>
<ul>
<li><p><strong>CPU-based system</strong></p></li>
<li><p><strong>No GPU required</strong></p></li>
</ul>
<p><strong>Operating System</strong></p>
<ul>
<li><p><strong>Windows 11</strong></p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

|     |
|-----|

|     |     |
|-----|-----|

**6. System Architecture**

**The system follows a modular pipeline-based architecture:**

1.  **Video Input Module**

2.  **Motion Analysis Module**

3.  **Density Estimation Module**

4.  **Risk Classification Engine**

5.  **Alert Generation System**

**Each module is independent, explainable, and easy to modify.**

**7. Module Description**

**7.1 Video Input Module**

- **Accepts pre-recorded CCTV or simulated crowd video**

- **Processes frames sequentially**

- **Supports frame skipping for performance optimization**

**7.2 Motion Analysis Module**

**Technique Used: Optical Flow**

- **Calculates motion vectors between consecutive frames**

- **Computes average motion magnitude**

- **Detects sudden acceleration or chaotic movement**

**Why Optical Flow?**

- **Captures collective movement**

- **Does not track individuals**

- **Efficient and explainable**

**7.3 Density Estimation Module**

**Technique Used: Background Subtraction (MOG2)**

- **Estimates foreground pixel ratio**

- **Represents crowd density level**

- **Detects abnormal congestion**

**This method avoids individual counting and ensures privacy.**

**7.4 Risk Classification Engine**

**Approach: Rule-Based Logic (Explainable AI)**

<table>
<colgroup>
<col style="width: 74%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Risk Level</strong></th>
<th><strong>Condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>LOW</strong></td>
<td><strong>Normal motion and density</strong></td>
</tr>
<tr class="even">
<td><strong>MEDIUM</strong></td>
<td><strong>Moderate motion OR high density</strong></td>
</tr>
<tr class="odd">
<td><strong>HIGH</strong></td>
<td><strong>High motion AND high density</strong></td>
</tr>
</tbody>
</table></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

**7.5 Alert Generation System**

- **Generates console-based alerts**

- **Logs alerts to a file**

- **Includes timestamp, risk level, and explanation**

**Example:**

**CROWD SAFETY ALERT**

> **Time : 08:33:57**
>
> **Avg Motion : 8.46**
>
> **Avg Density : 0.59**
>
> **Risk Level : MEDIUM**
>
> **Explanation : Unusual movement or congestion detected**

**8. Ethical AI Compliance**

> 1**. No face recognition  
> 2. No person identification  
> 3. No individual tracking  
> 4. Only crowd-level behaviour analysis**

**9. Dataset & Performance**

- **Dataset: Pre-recorded / simulated CCTV crowd videos**

- **Preprocessing: Frame resize, grayscale conversion**

- **Performance: Near real-time on CPU**

- **False Alerts: Reduced using averaged decisions**

**10. Conclusion**

> **This project demonstrates a logic-driven, explainable, and ethical
> AI system for public safety monitoring. By focusing on collective
> crowd behaviour, it provides a scalable and privacy-safe solution
> suitable for real-world deployment.**


**Execution Steps**

**Step 1: Open Project Directory**

Open the project folder in terminal or command prompt:

cd AI_Crowd_Safety

**Step 2: Activate Virtual Environment**

Activate the Python virtual environment to ensure correct dependencies
are used.

**For Windows:**

> crowd_env\Scripts\activate

**For Linux / macOS:**

> source crowd_env/bin/activate
>
> You should see:
>
> (crowd_env)
>
> in the terminal, confirming the environment is active.

**Step 3: Install Required Dependencies**

Install project dependencies using the requirements file:

> pip install -r requirements.txt

This installs **OpenCV and NumPy**, which are the only required
libraries.

**Step 4: Verify Python Environment (Optional but Recommended)**

python \--version

> pip list
>
> Ensure Python runs from crowd_env and required packages are installed.

**Step 5: Run the System**

Execute the main program:

> Python -m src.main

**Step 6: Observe Output**

- The system analysis the video input

- Displays **crowd safety alerts** in the console

- Writes alert logs to alerts.log

**Sample Output:**

CROWD SAFETY ALERT

Time : 08:31:37

Avg Motion : 8.46

Avg Density : 0.59

Risk Level : MEDIUM

Explanation : Unusual movement or congestion detected

**Step 7: Deactivate Environment (After Execution)**

deactivate
