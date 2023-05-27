import subprocess

class Communication:
	def __init__(self, checker, source):
		self.checker = checker
		self.source = source
		self.log = open("./communication.log", "w+")
	
	def eof(self, buffer, end):
		if(buffer.strip() in end):
			self.log.writelines(f"End the communication after receive \'{buffer}\'.\n")
			return True
		return False

	def communicate(self, end, source_first = False):
		checker_process = subprocess.Popen(self.checker, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
		source_process = subprocess.Popen(self.source, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
		
		#Start communation
		self.log.writelines("Start communication:\n\n")

		while True:
			if(source_first): #source go first
				buffer = source_process.stdout.readline().decode()
				source_process.stdout.flush()
				if self.eof(buffer, end) : break
				self.log.writelines(f"Source: {buffer.strip()}\n")
				checker_process.stdin.write(buffer.encode())
				checker_process.stdin.flush()
				source_first ^= True
			else: 
				buffer = checker_process.stdout.readline().decode()
				checker_process.stdout.flush()
				if self.eof(buffer, end) : break
				self.log.writelines(f"Checker: {buffer.strip()}\n")
				source_process.stdin.write(buffer.encode())
				source_process.stdin.flush()
				source_first ^= True
		
		#End communation and kill process
		self.log.writelines("\n")
		checker_process.stdin.close()
		checker_process.stdout.close()
		checker_status = checker_process.wait()
		if checker_status != 0: 
			self.log.writelines("There are some error when kill checker process.")
			raise Exception(checker_status)
		else:
			self.log.writelines("Killed checker process successfully.\n")
		
		source_process.stdin.close()
		source_process.stdout.close()
		source_status = source_process.wait()
		if source_status != 0: 
			self.log.writelines("There are some error when kill source process.")
			raise Exception(source_status)
		else:
			self.log.writelines("Killed source process successfully.")



if __name__ == '__main__': 
	communication = Communication('a.exe', 'b.exe')
	communication.communicate('')