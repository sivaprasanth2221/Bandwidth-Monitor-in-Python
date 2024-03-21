# Network Traffic Monitor

This Python script monitors network traffic statistics using the `psutil` library. It calculates the amount of data received, sent, and the total data transfer during each iteration (1 second interval) and displays the information in megabytes (MB). The script uses the `net_io_counters` function from `psutil` to obtain network I/O statistics.

## How to Use

1. Ensure you have Python and the `psutil` library installed.
2. Clone or download the repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command `python main.py`.
5. The script will continuously monitor and display network traffic statistics until manually stopped.

## Files Included

- `main.py`: The Python script that monitors network traffic.
- `README.md`: This file containing instructions and information about the project.

## Requirements

- Python 3.x
- `psutil` library (`pip install psutil`)

## Additional Notes

- Adjust the `time.sleep` interval in the script to change the monitoring frequency.
- This script provides basic network traffic monitoring and can be extended or modified for specific requirements.

