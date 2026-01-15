AI-Based Public Safety Monitoring & Risk Detection System
Logic-Centric | Algorithm-Focused Project
________________________________________
1. Overview
Crowded public places such as metro stations, markets, festivals, and railway stations are prone to incidents like panic, stampedes, and sudden crowd movement. Manual CCTV monitoring is slow, error-prone, and difficult to scale.
This project presents an AI-based, rule-driven system that analyses crowd-level behaviour from video input to detect abnormal activity and classify public safety risks.
The system strictly follows ethical AI principles by avoiding face recognition, individual tracking, or biometric data usage.
________________________________________
2. Objectives
•	Analyses CCTV or simulated crowd videos
•	Detect abnormal crowd behaviour (motion & density)
•	Classify risks into LOW, MEDIUM, HIGH
•	Generate explainable alerts in near real-time
•	Maintain privacy-preserving crowd analysis
________________________________________
3. Objectives of the Project
The main objectives of this project are:
•	To analyse pre-recorded or simulated CCTV video footage
•	To detect abnormal crowd-level behaviour
•	To classify crowd risk into predefined levels (LOW, MEDIUM, HIGH)
•	To generate explainable, human-readable alerts
•	To design an ethical, privacy-preserving AI system
________________________________________



4. Team Members and Work Distribution
Team Composition
Team Member	Role & Responsibility
Deepak Yadav	Project Lead, System Architecture Design, Main Pipeline Integration, Final Risk Decision Logic
Aaditya Mishra	Motion Analysis Module (Optical Flow), Performance Optimization
Aaditya Yadav	Density Estimation Module, Background Subtraction Logic
Vedant Parab
	Risk Classification Engine, Alert Generation, Documentation Support


	

	
________________________________________

5. Technology Stack
Software Tools
•	Programming Language: Python 
•	IDE: Visual Studio Code (VS Code)
•	Libraries Used:
o	OpenCV
o	NumPy
Hardware
•	CPU-based system
•	No GPU required
Operating System
•	Windows 11
________________________________________


	

	
6. System Architecture
The system follows a modular pipeline-based architecture:
1.	Video Input Module
2.	Motion Analysis Module
3.	Density Estimation Module
4.	Risk Classification Engine
5.	Alert Generation System
Each module is independent, explainable, and easy to modify.
________________________________________
7. Module Description
7.1 Video Input Module
•	Accepts pre-recorded CCTV or simulated crowd video
•	Processes frames sequentially
•	Supports frame skipping for performance optimization
________________________________________
7.2 Motion Analysis Module
Technique Used: Optical Flow 
•	Calculates motion vectors between consecutive frames
•	Computes average motion magnitude
•	Detects sudden acceleration or chaotic movement
Why Optical Flow?
•	Captures collective movement
•	Does not track individuals
•	Efficient and explainable
________________________________________
7.3 Density Estimation Module
Technique Used: Background Subtraction (MOG2)
•	Estimates foreground pixel ratio
•	Represents crowd density level
•	Detects abnormal congestion
This method avoids individual counting and ensures privacy.
________________________________________
7.4 Risk Classification Engine
Approach: Rule-Based Logic (Explainable AI)
Risk Level	Condition
LOW	Normal motion and density

MEDIUM	Moderate motion OR high density
HIGH	High motion AND high density
	
	
	
	

________________________________________
7.5 Alert Generation System
•	Generates console-based alerts
•	Logs alerts to a file
•	Includes timestamp, risk level, and explanation
Example:
CROWD SAFETY ALERT
Time       : 08:33:57
Avg Motion     : 8.46
Avg Density    : 0.59
Risk Level     : MEDIUM
Explanation    : Unusual movement or congestion detected
________________________________________
8. Ethical AI Compliance
1. No face recognition
2. No person identification
3. No individual tracking
4. Only crowd-level behaviour analysis
________________________________________


9. Dataset & Performance
•	Dataset: Pre-recorded / simulated CCTV crowd videos
•	Preprocessing: Frame resize, grayscale conversion
•	Performance: Near real-time on CPU
•	False Alerts: Reduced using averaged decisions
________________________________________
10. Conclusion
This project demonstrates a logic-driven, explainable, and ethical AI system for public safety monitoring. By focusing on collective crowd behaviour, it provides a scalable and privacy-safe solution suitable for real-world deployment.
 
________________________________________
Execution Steps
Step 1: Open Project Directory
Open the project folder in terminal or command prompt:
	cd AI_Crowd_Safety
Step 2: Activate Virtual Environment
Activate the Python virtual environment to ensure correct dependencies are used.
For Windows:
crowd_env\Scripts\activate
For Linux / macOS:
source crowd_env/bin/activate
You should see:
(crowd_env)
in the terminal, confirming the environment is active.

Step 3: Install Required Dependencies
Install project dependencies using the requirements file:
pip install -r requirements.txt
This installs OpenCV and NumPy, which are the only required libraries.
________________________________________
Step 4: Verify Python Environment (Optional but Recommended)
python --version
pip list
Ensure Python runs from crowd_env and required packages are installed.
________________________________________
Step 5: Run the System
Execute the main program:
Python -m src.main
________________________________________
Step 6: Observe Output
•	The system analysis the video input
•	Displays crowd safety alerts in the console
•	Writes alert logs to alerts.log


Sample Output:
CROWD SAFETY ALERT
Time           : 08:31:37
Avg Motion     : 8.46
Avg Density    : 0.59
Risk Level     : MEDIUM
Explanation    : Unusual movement or congestion detected
________________________________________
Step 7: Deactivate Environment (After Execution)
deactivate


