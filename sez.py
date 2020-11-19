# STOP AND WAIT ARQ 
# Reg. No. - 19BCE2236

from time import sleep
nof = int(input("Number of frames to be sent: "))
rtt = float(input("Round trip time: "))
str1 = '01'
buffer1 = []
x = 0
for i in range(nof):
	buffer1.append(str1[x])
	x += 1
	if x == len(str1):
		x = 0

temp = 0
for i in range(1, nof + 1 , 1):
	sleep(rtt)
	print("Sender: Frame " + str(i) + " with sequence number " + str(buffer1[temp]) + " has been sent. "); sleep(rtt)
	j = input("Enter 'a' if Frame successfully received and acknowledgemnt also received by sender" + str('\n') + 
		"Enter 'b' if frame is lost" + str('\n') + 
		"Enter 'c' if frame is received but acknowledgement is lost: " + str('\n'))
	if j == 'a':
		print("Receiver: Frame " + str(i) + " with sequence number " + str(buffer1[temp]) + " has been received and acknowledgement has been sent.")
		print("Sender: Ack " + str(buffer1[temp]) + " has been received by sender.")
	elif j == 'c':
		print("Receiver: Frame " + str(i) + " with sequence number " + str(buffer1[temp]) + " has been received and acknowledgement has been sent.")
		print("Sender: Ack " + str(buffer1[temp]) + " is lost, resending frame " + str(i) + " with sequence number " + str(buffer1[temp]))
		print("Receiver: Resending " + str(buffer1[temp]) + " and discarding frame " + str(i))
		print("Sender: Ack " + str(buffer1[temp]) + " has been received by sender.")
	elif j == 'b':
		print("Receiver: Frame " + str(i) + " with sequence number " + str(buffer1[temp]) + " is lost.")
		print("Sender: Ack " + str(buffer1[temp]) + " is lost, resending frame " + str(i) + " with sequence number " + str(buffer1[temp]))
		print("Receiver: Frame " + str(i) + " with sequence number " + str(buffer1[temp]) + " has been received and acknowledgement has been sent.")
		print("Sender: Ack " + str(buffer1[temp]) + " has been received by sender.")
	else: pass
	temp += 1




