from transfer_money import transfer_money

class SendtoMtn(transfer_money):

    def __int__(self, recipient_number, amount, reference):
        self.recipient_number = recipient_number
        self.amount = amount
        self.reference = reference
        self.balance = balance

    def perform_transaction(self):
        if self.amount < self.balance
        return f"Amount of {self.amount} sent to account number {recipient_numbe        r}. Current balance is" + self.balance - self.amount

        else:
            return f"Insufficient balance of {self.balance} to make transaction"
