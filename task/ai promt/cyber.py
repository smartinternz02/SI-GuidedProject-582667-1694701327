import datetime


# Function to generate a timestamp
def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Function to generate a cybersecurity incident report
def generate_incident_report():
    incident_date = get_timestamp()
    report_title = input("Enter the title of the incident report: ")
    description = input("Enter a description of the incident: ")
    affected_systems = input("Enter the affected systems or assets: ")
    impact = input("Enter the impact of the incident: ")
    actions_taken = input("Enter the actions taken to address the incident: ")

    # Create and format the incident report
    incident_report = f"Incident Date: {incident_date}\n"
    incident_report += f"Title: {report_title}\n"
    incident_report += f"Description: {description}\n"
    incident_report += f"Affected Systems/Assets: {affected_systems}\n"
    incident_report += f"Impact: {impact}\n"
    incident_report += f"Actions Taken: {actions_taken}\n"

    # Save the incident report to a file
    with open("incident_report.txt", "w") as file:
        file.write(incident_report)

    print("Incident report generated and saved as 'incident_report.txt'.")


# Main program
if __name__ == "__main__":
    generate_incident_report()
