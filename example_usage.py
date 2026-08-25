from client import ChainOfThoughtDeliberativeReasoningVerifierClient

def main():
    client = ChainOfThoughtDeliberativeReasoningVerifierClient()
    res = client.solve_deliberative_reasoning_problem('Compute the asymptotic complexity of quantum state tomography with randomized Pauli measurements', 8192)
    print('Deliberation: ' + res['deliberation_session_id'] + ' (' + str(res['allocated_thinking_tokens']) + ' tokens)')
    print('Verification Steps: ' + str(res['intermediate_verification_steps_count']) + ' (Backtracks: ' + str(res['backtrack_and_correction_branches']) + ')')
    print('Soundness: ' + str(res['formal_mathematical_soundness_score_pct']) + '% | Verified: ' + str(res['final_concise_solution_verified']))

if __name__ == '__main__':
    main()
