from experiment import experiment

def main():
    for n in range (1000, 100001, 1000):
        for k in range(0, 1):
            exp = experiment(n)
            Bn, Un, Cn, Dn = exp.run()
            print(f"n: {n}, Bn: {Bn}, Un: {Un}, Cn: {Cn}, Dn: {Dn}")
        
        
if __name__ == "__main__":
    main()