#import library
import socket

def Main():
	#pendefinisian host dan port
	host = "127.0.0.1"
	port = 5000
	
	#pemanggilan fungsi connect pada library socket
	s = socket.socket()
	s.connect((host,port))
	
	#game telah dimulai, meminta input nama player atau client
	message = input("Enter your name : ")
	s.send(message.encode('utf-8'))

	#loop game
	while message!='q':
		user_input = input("Enter r-Rock , s-Scissor , p-Paper ")
		s.send(user_input.encode("utf-8"))
		data = s.recv(1024).decode('utf-8')
		print("Recieved dom Server : "+data)

	#tutup koneksi	
	s.close()

if __name__=='__main__':
	Main()