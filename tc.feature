# contents of tc.feature

Feature: System entity module test code
    Scenario Outline: Test case
        Given input_sentence is {now_input}

        When starting module
        
        Then entity_name is {result_entity_name}
        And value is {result_value}
        And start_idx is {result_start_idx}
        And end_idx is {result_end_idx}
        And get_tagged_sentence is {result_tagged_sentence}

        Examples:
        | 2022년 9월 22일 사수자리 운세 알려줘 | @sys.date, @sys.fortune.starsign | 2022-9-22 00:00:00, 사수자리 | 0, 13 | 11, 16 | @sys.date @sys.fortune.starsign 운세 알려줘 |
    