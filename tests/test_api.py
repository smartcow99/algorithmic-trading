import unittest
from trading.rest_api import get_accounts

class TestAccountsAPI(unittest.TestCase):
    def test_get_accounts(self):
        """전체 계좌 조회 테스트"""
        accounts = get_accounts()

        # 응답이 None이 아닌지 확인
        self.assertIsNotNone(accounts, "API 응답이 None입니다.")

        # 응답이 리스트인지 확인
        self.assertIsInstance(accounts, list, "응답이 리스트 형식이 아닙니다.")

        # 리스트가 비어있지 않은지 확인
        self.assertGreater(len(accounts), 0, "응답 리스트가 비어 있습니다.")

        # 리스트 항목 검사 (예: 첫 번째 항목의 필드 확인)
        account = accounts[0]  # 첫 번째 항목
        self.assertIn('currency', account, "항목에 'currency' 필드가 없습니다.")
        self.assertIn('balance', account, "항목에 'balance' 필드가 없습니다.")

if __name__ == "__main__":
    unittest.main()
