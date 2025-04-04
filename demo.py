def get_credit_rating(mortgages):
    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)
    
    for mortgage in mortgages:
        risk_score = 0
        
        # Loan-to-Value (LTV) Ratio
        ltv = mortgage["loan_amount"] / mortgage["property_value"]
        if ltv > 0.9:
            risk_score += 3
        elif ltv > 0.8:
            risk_score += 2
        elif ltv > 0.7:
            risk_score += 1
        
        # Debt-to-Income (DTI) Ratio
        dti = mortgage["debt_amount"] / mortgage["annual_income"]
        if dti > 0.5:
            risk_score += 3
        elif dti > 0.4:
            risk_score += 2
        elif dti > 0.3:
            risk_score += 1
        
        # Credit Score
        credit_score = mortgage["credit_score"]
        total_credit_score += credit_score
        if credit_score >= 750:
            risk_score -= 2
        elif credit_score >= 700:
            risk_score -= 1
        elif credit_score < 650:
            risk_score += 2
        
        # Loan Type
        if mortgage["loan_type"] == "fixed":
            risk_score -= 1
        elif mortgage["loan_type"] == "adjustable":
            risk_score += 2
        
        # Property Type
        if mortgage["property_type"] == "condo":
            risk_score += 1
        
        total_risk_score += risk_score
    
    # Adjust risk score based on average credit score
    avg_credit_score = total_credit_score / num_mortgages
    if avg_credit_score >= 750:
        total_risk_score -= 2
    elif avg_credit_score >= 700:
        total_risk_score -= 1
    elif avg_credit_score < 650:
        total_risk_score += 2
    
    # Assign credit rating
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 6:
        return "BBB"
    else:
        return "C"

# test_credit_rating.py
import unittest

class TestCreditRating(unittest.TestCase):
    def test_high_credit_score(self):
        mortgages = [{
            "loan_amount": 100000,
            "property_value": 200000,
            "debt_amount": 20000,
            "annual_income": 80000,
            "credit_score": 750,
            "loan_type": "fixed",
            "property_type": "house"
        }]
        self.assertEqual(get_credit_rating(mortgages), "AAA")

    def test_low_credit_score(self):
        mortgages = [{
            "loan_amount": 150000,
            "property_value": 180000,
            "debt_amount": 50000,
            "annual_income": 90000,
            "credit_score": 600,
            "loan_type": "adjustable",
            "property_type": "condo"
        }]
        self.assertEqual(get_credit_rating(mortgages), "C")

    def test_medium_risk(self):
        mortgages = [{
            "loan_amount": 180000,
            "property_value": 200000,
            "debt_amount": 70000,
            "annual_income": 120000,
            "credit_score": 680,
            "loan_type": "fixed",
            "property_type": "house"
        }]
        self.assertEqual(get_credit_rating(mortgages), "BBB")

if __name__ == "__main__":
    unittest.main()


a = "lceo"

for i in itrable:
    