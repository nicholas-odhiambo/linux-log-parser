#!/usr/bin/env python3

def read_logfile(filepath):
    try: 
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            lines =[line.strip() for line in file if line.strip()]
        print(f"Successfully read {len(lines)} lines from {filepath}")
        return lines
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        return[]
    except PermissionError:
        print(f"Error: Permission denied - {filepath}")
        return []
    except Exception as e: 
        print(f"Error reading file {filepath}: {e}")
        return []
    

## for testing 
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        lines = read_logfile(sys.argv[1])
        print(f"First 5 lines:")
        for line in lines[:5]:
            print(line)
        else:
            print("Usage: python parser.py <logfile>")










