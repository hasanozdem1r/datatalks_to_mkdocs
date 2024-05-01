import pandas as pd


def json_to_df(json_data) -> pd.DataFrame:
    message_data = []
    messages = json_data.get("messages")
    if len(json_data.get("messages")) > 0:
        for message in messages:
            user = message.get("user")
            message_type = message.get("type")
            message_subtype = True if message.get("subtype") else False
            message_id = message.get("client_msg_id")
            message_text = message.get("text")
            message_data.append(
                {
                    "slack_user": user,
                    "slack_message_type": message_type,
                    "slack_message_subtype": message_subtype,
                    "slack_message_id": message_id,
                    "slack_message": message_text,
                }
            )
        return pd.DataFrame(
            message_data,
            columns=[
                "slack_user",
                "slack_message_type",
                "slack_message_subtype",
                "slack_message_id",
                "slack_message",
            ],
        )
    raise ValueError("Given JSON data is invalid!!!")
