class program_status:
    def __init__(self):
        self.author = 'XRenso'
        self.name = 'Small Logic'
        self.version = open('version.txt','r').readline().strip()



def main():
    print('Ha')

program = program_status()

def run():
    main()
    print(program.author)
    print(program.version)
    input()


run()