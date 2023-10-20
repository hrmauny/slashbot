"""
Tests history command
"""
import time
import unittest
from bot_utils import BotTest


class TestSummary(BotTest):
    """
    Test file for history
    """

    def test_summary_command(self):
        """
        Tests the history command
        """
        msg = self.create_text_message('/summary')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/summary'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /history command, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None


if __name__ == '__main__':
    unittest.main()
