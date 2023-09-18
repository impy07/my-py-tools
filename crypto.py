import sys
from ast import literal_eval

def ASCII (msg :str, mode: int):
	out = ''
	if mode:		# Decode
		msg = literal_eval(msg)
		for entry in msg:
			out = f'{out}{chr(int(entry))}'
		
	else:		# Encode
		out = []
		for entry in msg:
			out.append(ord(entry))
	return out
	
	
def HEX (msg: str, mode:int):
	out = ''
	if mode:		# Decode
		out = bytes.fromhex(msg)
	else:		# Encode
		out = msg.encode('utf-8')
		out = out.hex()
	return out
	
	
def main():
	
	ENCDEC = 0		# 0 -> Encrypt;	1 -> Decrypt
	out = ''
	
	msg_ch1 = '''Please, select one of the following:
	1) ASCII		2) HEX'''
	
	msg_ch2 = '''Please, select mode:
	0) Exit		1) Encrypt		2) Decrypt'''
	
	while(1):
		
		print(msg_ch2)
		chose = input()
		match chose:
			case '0':
				sys.exit(0)
			case '1':
				ENCDEC = 0
			case '2':
				ENCDEC = 1
			case other:
				continue
		
		print(msg_ch1)
		chose = input()
		print('Insert input:')
		in_str = input()
		match chose:
			case '1':
				out = ASCII(in_str,ENCDEC)
			case '2':
				out = HEX(in_str,ENCDEC)
			case other:
				continue
		
		print(f'Result:\n{out}\n')
	


if __name__  == '__main__':
	main()