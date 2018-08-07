#Name: Yash Bhushan Ambre
#Login_ID:yxa5797
#UTA_ID: 1001535797
#Source code:(https://wiki.python.org/moin/TcpCommunication)
#GUI: http://easygui.sourceforge.net/tutorial.html
#SERVER SIDE
    
import socket                                                             #import socket module	
from easygui import msgbox, multenterbox                                  #invoke easygui with functions msgbox & multenterbox for GUI
    
TCP_IP = '127.0.0.1'                                                      #Local host IP address for client server connection
TCP_PORT = 5005                                                           #Used to connect with the same port as the client
BUFFER_SIZE = 20  # Normally 1024, but we want fast response,The maximum number of bytes that can be received
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                     #Creates an INET and STREAMing socket
s.bind((TCP_IP, TCP_PORT))                                                #Binds to the port of the client
s.listen(1)                                                               #opens the connection and waits for the client
  
                                                                          #Creates a dictioanry which consists an array 
dict1 = {'Come':'advance,approach',                                       #of all the words with their synonyms
		'Go':'depart, disappear, fade, move, proceed, recede, travel', 
		'Run':'dash, escape, elope, flee, hasten, hurry, race, rush, speed, sprint', 
		'Hurry':'rush, run, speed, race, hasten, urge, accelerate, bustle', 
		'Hide':'conceal, cover, mask, cloak, camouflage, screen, shroud, veil', 
		'Move':'plod, go, creep, crawl, inch, poke, drag, toddle, shuffle, trot, dawdle',
		'Destroy':'ruin, demolish, raze, waste, kill, slay, end, extinguish',
		'Kill':'slay, execute, assassinate, murder, destroy, cancel, abolish',
		'Decide':'determine, settle, choose, resolve',
		'Help':'aid, assist, support, encourage, back, wait on, attend'}

  #print ('Connection address:', addr)
while 1:
	conn, addr = s.accept()                                              #Accepts the connection from the client side
	data = conn.recv(BUFFER_SIZE).decode()                               #Stores the input word into the variable data 
	if not data: break                                                   #Breaks the condition if theres no data 
	print ("received data:", data)
	msgbox(msg=(data), title = "Requested word from client")          #Displays a popup which shows the requested word from the client to the server
	for key in dict1:                                                 #Opens a for loop which checks the key value in the array 'dict1'
		if data==key:                                                 #Compares the key values from 'dict1' with the input word stored in 'data'
			wr=dict1[key]                                             #The desired synonym is then stored in the variable 'wr'
	#print (wr)
	conn.send(wr.encode())                                            #Sends the synonym to the client with encoding 
conn.close()                                                          #terminates the connection

