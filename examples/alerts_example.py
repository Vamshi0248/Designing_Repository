"""
Alert Components Usage Examples
"""

from components.alerts import (
    Alert,
    SuccessAlert,
    ErrorAlert,
    WarningAlert,
    InfoAlert,
    AlertGroup
)


def example_basic_alerts():
    """Example: Creating and rendering basic alerts"""
    
    # Create individual alerts
    success = SuccessAlert("Operation completed successfully!")
    error = ErrorAlert("An error occurred. Please try again.")
    warning = WarningAlert("This action cannot be undone.")
    info = InfoAlert("This is an informational message.")
    
    # Render alerts
    print("Basic Alerts:")
    print(success.render())
    print(error.render())
    print(warning.render())
    print(info.render())


def example_dismissible_alerts():
    """Example: Creating dismissible alerts"""
    
    # Create dismissible alerts
    alert = SuccessAlert("Changes saved!", dismissible=True)
    
    # Check if visible
    print(f"Alert visible: {alert.visible}")
    
    # Dismiss the alert
    alert.dismiss()
    print(f"After dismiss: {alert.visible}")
    
    # Render
    print(alert.render())


def example_alert_group():
    """Example: Managing multiple alerts with AlertGroup"""
    
    # Create an alert group
    alerts = AlertGroup()
    
    # Add multiple alerts
    alerts.add_alert(SuccessAlert("File uploaded successfully"))
    alerts.add_alert(InfoAlert("Processing your request..."))
    alerts.add_alert(WarningAlert("Low disk space available"))
    
    # Get visible alerts
    visible = alerts.get_visible_alerts()
    print(f"Visible alerts: {len(visible)}")
    
    # Render all alerts
    rendered = alerts.render()
    for alert in rendered:
        print(alert)
    
    # Dismiss all alerts
    alerts.dismiss_all()
    print(f"After dismiss all: {len(alerts.get_visible_alerts())} visible")


def example_custom_alert():
    """Example: Creating a custom alert"""
    
    # Create custom alert with specific type
    custom = Alert(
        message="Custom alert message",
        alert_type="info",
        dismissible=True
    )
    
    print(custom.render())


if __name__ == "__main__":
    print("=" * 50)
    print("Alert Components Examples")
    print("=" * 50)
    
    print("\n1. Basic Alerts")
    print("-" * 50)
    example_basic_alerts()
    
    print("\n2. Dismissible Alerts")
    print("-" * 50)
    example_dismissible_alerts()
    
    print("\n3. Alert Group")
    print("-" * 50)
    example_alert_group()
    
    print("\n4. Custom Alert")
    print("-" * 50)
    example_custom_alert()
