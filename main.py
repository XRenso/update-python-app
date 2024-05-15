class program_status:
    def __init__(self):
        self.version = 'v1.0.3'
        self.author = 'XRenso'
        self.name = 'Small Logic'



def main():
    print('Ha')

program = program_status()

def run():
    main()
    print(program.author)
    print(program.version)
    input()


run()