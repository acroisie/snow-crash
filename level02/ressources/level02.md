# SnowCrash Level02 Guide
This guide will walk you through the process of finding the password for the `flag02` user.

## Procedure:

1. **Examine your environment using Unix commands.**
   
   - `id` : Shows user and group identities that you have. 
   - `pwd` : Displays the current directory you are in.
   - `ls -la` : Lists files and their permissions in the current directory.
  
2. **After executing `ls -la`, you should notice a file called 'level02.pcap'.**

   - The pcap file contains network traffic data packets that have been previously captured.
   - It is a raw data file that needs to be analyzed. 

3. **Copy pcap file to your local machine via scp.**
    
   ```bash
   scp -P 4242 level02@XXX.XXX.XX.XX:~/level02.pcap ~/. 
   ```
   This command copies the level02.pcap file from the remote machine to your personal directory on your local machine via scp (secure copy).

4. **Set up a Python virtual environment and install the necessary library**
   
    ```bash
    python3 -m venv myenv              # create a virtual environment
    source myenv/bin/activate          # activate the environment
    pip install -r requirements.txt    # install required packages
    ```

5. **Use a Python script with Scapy library to analyze pcap file and extract the useful data (user inputs).**
   
   - Run a script similar to:
   ```python
   from scapy.all import *
   
    def analyze_pcap(file_name):
     packets = rdpcap(file_name)
     for i, packet in enumerate(packets):
     print(i, packet.sprintf("{Raw:%Raw.load%\n}"))

    analyze_pcap('level02.pcap')
    ```
    - This script displays the raw payload of each packet, which is what was actually transmitted over the network. This could include the password you're looking for.

6. **The password could be hidden among the characters displayed by the script. For instance, '\x7f' represents the 'Delete' key.**

7. **Decipher the password from the output data.**

    We get packets containing the following characters: f t _ w a n d r '\x7f' '\x7f' '\x7f' N D R e L '\x7f' L 0 L

    In this context, '\x7f' corresponds to a keypress of the delete key. By deleting each character that precedes '\x7f,' the password is revealed: `ft_waNDReL0L`