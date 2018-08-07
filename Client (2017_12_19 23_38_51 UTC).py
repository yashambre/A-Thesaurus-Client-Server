#Name: Yash Bhushan Ambre
#Login_ID:yxa5797
#UTA_ID: 1001535797
#Source code:(https://wiki.python.org/moin/TcpCommunication)
#GUI: http://easygui.sourceforge.net/tutorial.html
#CLIENT SIDE

import socket  													      #import socket module	
from easygui import msgbox, multenterbox                              #invoke easygui with functions msgbox & multenterbox for GUI
    
TCP_IP = '127.0.0.1'                                                  #Local host IP address
TCP_PORT = 5005                                                       #Used to connect with the same port as the server
BUFFER_SIZE = 1024                                                    #The maximum number of bytes that can be received 

fieldNames = ["WORD"]                                                 #Displays a Popup to enter the input word. (GUI code)
fieldValues = multenterbox(msg='Enter the word', title='THESAURUS',   #The input word along with popup details is stored in the variable fieldValues  
			 fields=(fieldNames))                                     #multenterbox is used to show enterboxes on a single screen

   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 #Creates an INET and STREAMing socket
s.connect((TCP_IP, TCP_PORT))                                         #Connects to the IP:'127.0.0.1 and TCP_PORT:'5005'
s.send(fieldValues[0].encode())                                       #Sends the input word with fieldValues as a list to the server with encoding
key = s.recv(BUFFER_SIZE).decode()                                    #Receives the Synonym and stores it in 'key'
s.close()                                                             #Closes the connection with the server
   
print ("Synonym:",key)                                                #Prints the desired synonym of the input word
msgbox(msg=(key), title = "Synonym")                                  #Displays the popup with the string

