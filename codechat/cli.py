import argparse
import os
from codechat.code_loader import load_codebase
from codechat.llm_client import analyze_code

def main():
    parser = argparse.ArgumentParser(
        prog="codechat",
        description="🤖 CodeChat: Ask AI about your codebase",
        epilog="Example: codechat /path/to/codebase -q 'What does this code do?'",
        formatter_class=argparse.RawTextHelpFormatter,
        usage="%(prog)s path -q [question]",
    )
    parser.add_argument("path", help="Path to the root of the codebase")
    parser.add_argument("-q", "--question", help="Question or prompt about the codebase")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("❌ Path does not exist.")
        return

    print("📦 Loading codebase...")
    code = load_codebase(args.path)
    print(f"✅ Loaded {len(code)} code files.")

    if args.question:
        # Single-question mode
        result = analyze_code(code, args.question)
        print(f"\n💬 Answer:\n{result}")
    else:
        # Interactive chat mode
        print("\n💬 Interactive mode. Type 'exit' or 'quit' to leave.")
        while True:
            question = input("\n❓ You > ").strip()
            if question.lower() in ("exit", "quit"):
                print("👋 Goodbye!")
                break
            if not question:
                continue
            result = analyze_code(code, question)
            print(f"\n💬 Answer >\n{result}")
