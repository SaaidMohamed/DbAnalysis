from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


def main():
    print("Hello from dbanalysis!")
    summary_template = """
    Given the information {information} about a person I want you too create:
    1. a short summary.
    2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)


if __name__ == "__main__":
    main()
