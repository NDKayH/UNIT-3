# Quiz 042


## Paper Solution
![IMG_4787](https://github.com/user-attachments/assets/c84ead88-25a5-4324-8a59-ca91fb9fddd0)



## Code
```.py

#quiz_042.py
from secure_password import check_password as check_hash
from passlib.context import CryptContext
from my_lib import DatabaseManager

x = DatabaseManager('bitcoin_exchange.db')
result  = x.search("SELECT * FROM ledger")
x.close()

for row in result:
    #(3, 254, 920, 'hash here')
    id, send_id, rece_id, amount, signature = row
    string_hash = f"id {id},sender_id {send_id},reciever_id {rece_id},amount {amount}"
    print(signature)
    if check_hash(signature, string_hash):
        #tx matches
        print("TX is Correct")
    else:
        #tx is wrong
        print("TX is Wrong")

```

## Proof of work
![image](https://github.com/user-attachments/assets/e467268b-f4f4-4f72-a262-f60c13474476)
