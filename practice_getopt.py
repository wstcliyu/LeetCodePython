import sys
import getopt

if __name__ == '__main__':
	opts, args = getopt.getopt(sys.argv[1:], 'hn:w:', ['help', 'name=', 'word='])

	name = 'No Name'
	word = 'Nice to meet you!'

	for key, value in opts:
		if key in ['-h', '--help']:
			print ('A program to say hi')
			print ('Parameters')
			print ('-h\tShow help')
			print ('-n\tYour name')
			print ('-w\tYour word')
			sys.exit(0)
		if key in ['-n', '--name']:
			name = value
		if key in ['-w', '--word']:
			word = value

	print('Hello, my name is {0}. {1}'.format(name, value))