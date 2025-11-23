import json, os

DATA_PATH = "accounts.json"

def load_balance():
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump({"balance": 0.0}, f)
    with open(DATA_PATH) as f:
        return json.load(f)["balance"]

def save_balance(bal):
    with open(DATA_PATH, "w") as f:
        json.dump({"balance": bal}, f)

def main():
    bal = load_balance()
    while True:
        print(f"\nBalance: ₹{bal:.2f}")
        cmd = input("Choose: [d]eposit [w]ithdraw [q]uit: ").strip().lower()
        if cmd == 'd':
            amt = float(input("Amount to deposit: "))
            bal += amt
            save_balance(bal)
        elif cmd == 'w':
            amt = float(input("Amount to withdraw: "))
            if amt > bal:
                print("Error: insufficient funds.")
            else:
                bal -= amt
                save_balance(bal)
        elif cmd == 'q':
            break
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()
