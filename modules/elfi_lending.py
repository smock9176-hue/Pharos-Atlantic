# ELFi RWA Lending Protocol Implementation

class ELFiLending:
    def __init__(self):
        self.borrowers = []
        self.lenders = []
        self.loans = []

    def add_borrower(self, borrower_id):
        self.borrowers.append(borrower_id)

    def add_lender(self, lender_id):
        self.lenders.append(lender_id)

    def create_loan(self, borrower_id, lender_id, amount):
        if borrower_id not in self.borrowers:
            raise ValueError("Borrower not registered.")
        if lender_id not in self.lenders:
            raise ValueError("Lender not registered.")
        loan = {
            'borrower': borrower_id,
            'lender': lender_id,
            'amount': amount,
        }
        self.loans.append(loan)
        return loan

    def get_loans(self):
        return self.loans

# Example usage:
# elfi = ELFiLending()
# elfi.add_borrower('borrower1')
# elfi.add_lender('lender1')
# loan = elfi.create_loan('borrower1', 'lender1', 1000)
# print(elfi.get_loans())