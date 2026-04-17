class ReferralSystem:
    def __init__(self):
        self.referrals = {}
    
    def add_referral(self, referrer_id, referred_id):
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_id)
        
    def get_referrals(self, referrer_id):
        return self.referrals.get(referrer_id, [])
    
    def total_referrals(self, referrer_id):
        return len(self.get_referrals(referrer_id))

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    referral_system.add_referral('user1', 'user2')
    print(f"Referrals for user1: {referral_system.get_referrals('user1')}")
    print(f"Total referrals for user1: {referral_system.total_referrals('user1')}")
