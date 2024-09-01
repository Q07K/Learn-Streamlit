from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import (
    RunnableWithMessageHistory,
    ConfigurableFieldSpec,
)


PERSONA = """
# Assistant Role
**Name:** 이혜지

## Appearance

- **Age:** 14
- **Height:** 156cm
- **Weight:** 55kg
- **Hair:** Long, black hair worn in a practical braid
- **Eyes:** Piercing hazel eyes that reflect the sea's depths
- **nationality:** Korean

## Personality

- **Cute:** She is so bright and everything she does is cute.
- **Friendly:** She becomes friendly with many people easily, and when she does, she shows even more intimacy by speaking informally.
- **Chat:** I've known you for a long time and am a very close friend.
"""

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", PERSONA),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)


def get_session_history(
    session_id: str, store: dict
) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


def generate(user_input: str, store: dict, api_key: str) -> str:
    LLM = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=api_key,
        temperature=0,
        max_output_tokens=1000,
    )
    CHAIN = PROMPT | LLM

    CHAIN = RunnableWithMessageHistory(
        CHAIN,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="session_id",
                annotation=str,
            ),
            ConfigurableFieldSpec(
                id="store",
                annotation=dict,
            ),
        ],
    )
    result = CHAIN.stream(
        {"input": user_input},
        config={"configurable": {"session_id": "abc123", "store": store}},
    )

    yield result


def message_parser(messages: list) -> dict[str, str]:
    result = []
    for idx in range(0, len(messages), 2):
        message = {
            "user": messages[idx].content,
            "ai": messages[idx + 1].content,
        }
        result.append(message)
    return result


if __name__ == "__main__":
    STORE = {}
    print(generate("안녕", STORE))
    print(generate("반가워", STORE))
    print(generate("대화 히스토리 요약", STORE))
    print(STORE)
