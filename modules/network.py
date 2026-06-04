import subprocess

class NetworkTools:
    @staticmethod
    def ping_checker():
        print("\n" + "-"*20)
        print("     NETWORK PING CHECKER    ")
        print("-"*20)

        target = input("Enter Host or IP (e.g., google.com or 8.8.8.8): ").strip()

        if not target:
            print("[-] Hostname cannot be empty!")
            return
        
        print(f"[*] Pinging {target}... Please waite.")

        try:
            response = subprocess.run(
                ["ping", "-n", "1", target], 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL,
                timeout=5
            )
            
            if response.returncode == 0:
                print(f"[+] Success! {target} is UP and reachable. 🔥")
            else:
                print(f"[-] Failed! {target} is DOWN or unreachable. ❌")
                
        except subprocess.TimeoutExpired:
            print("[-] Connection timeout!")
        except Exception as e:
            print(f"[-] An error occurred: {e}")