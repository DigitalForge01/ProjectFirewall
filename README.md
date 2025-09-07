# ProjectFirewall
Python Firewall
A functional, educational software firewall built in Python for monitoring and controlling network traffic. This project provides a hands-on understanding of fundamental network security concepts like packet sniffing, rule-based filtering, and logging.

Features
Packet Filtering: Inspects and filters incoming network packets based on user-defined rules.
Rule Management: Blocks suspicious IP addresses, restricts specific protocols (like ICMP and Telnet), and allows traffic on whitelisted ports.
Logging: Records all blocked and allowed network activities with timestamps for easy review and auditing.
Graphical User Interface (GUI): An intuitive interface built with Tkinter that allows both technical and non-technical users to manage the firewall, view logs in real time, and dynamically add/remove rules.
Background Processes: Utilizes threading to ensure the firewall processes run smoothly in the background while keeping the GUI responsive.

Tools and Technologies
Python: Core programming language.
Scapy: For robust packet sniffing and traffic inspection.
Tkinter: For creating the interactive GUI.
Python Standard Library Logging: For recording all firewall activities.

python main.py
The GUI will launch, allowing you to start and stop the firewall and manage its rules.

Project Structure
main.py: The entry point for the application; initializes the GUI and launches the firewall core.
firewall_core.py: Captures packets and applies rule-based filtering.
rules_manager.py: Manages the security rules for blocking and allowing traffic.
logger.py: Handles all logging functionalities, writing activities to firewall.log.
gui.py: The module that provides the graphical user interface.

Future Enhancements
While this is a simplified prototype, here are some ideas for future development:
Persistent Rule Storage: Save rules to a database or configuration file so they persist across sessions.
Advanced Traffic Analysis: Implement deep packet inspection for more granular control.
Real-time Alerting: Add notifications via email or desktop alerts.
Integration: Connect with an Intrusion Detection System (IDS) for enhanced security.
