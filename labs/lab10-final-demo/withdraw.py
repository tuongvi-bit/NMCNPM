import mysql.connector, hashlib

def verify_pin(card_no, pin):
    conn = mysql.connector.connect(user="root", password="123456", database="atm_demo")
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    return row and row[0] == hashlib.sha256(pin.encode()).hexdigest()

def withdraw(card_no, amount):
    conn = mysql.connector.connect(user="root", password="123456", database="atm_demo")
    cur = conn.cursor()
    try:
        conn.start_transaction()
        cur.execute("""
            SELECT account_id, balance 
            FROM accounts 
            JOIN cards USING(account_id) 
            WHERE card_no=%s FOR UPDATE
        """, (card_no,))
        account_id, balance = cur.fetchone()

        if balance < amount:
            raise Exception("Insufficient funds")

        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s", (amount, account_id))
        cur.execute("""
            INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after) 
            VALUES(%s,%s,1,'WITHDRAW',%s,%s)
        """, (account_id, card_no, amount, balance - amount))
        conn.commit()
        print("Withdraw success, new balance:", balance - amount)
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    card_no = "1234567890"
    pin = input("Enter PIN: ")
    if verify_pin(card_no, pin):
        withdraw(card_no, 200000)  # rút 200k
    else:
        print("Invalid PIN")
