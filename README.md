# PTR Record Lookup Script

This Python script reads a list of IP addresses from an input file and performs a PTR (Pointer) record lookup for each IP address using the `socket.gethostbyaddr()` function. It then writes the results, including the IP address and PTR record (if found), to an output file.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- An input file (`ip_list.txt`) containing a list of IP addresses, with each IP address on a separate line.

## Usage

1. Place your list of IP addresses in the `ip_list.txt` file.
2. Run the script using the following command:

```
bash
Copy code
python ptr_lookup.py
```
3. The script will perform PTR record lookups for each IP address and write the results to the `ptr_records.txt` file.

## Output

The script will create an output file named `ptr_records.txt`, which will contain the IP addresses and their corresponding PTR records (if found). If no PTR record is found for an IP address, it will be noted in the output file.

## Error Handling

- If the input file (`ip_list.txt`) is not found, the script will display a "File not found" error.
- If any other error occurs during execution, an error message will be displayed.

Feel free to customize the input file, output file, and error handling as needed for your specific use case.
