# utils.py

from data_nodes import handle_set, handle_if, handle_merge
from db_nodes import handle_mysql, handle_postgresql, handle_mongodb
from control_nodes import handle_cron, handle_delay
from auth_nodes import handle_http_basic_auth, handle_oauth2
from ai_nodes import handle_openai_completion, handle_huggingface_transformer
from file_nodes import handle_read_file, handle_write_file
from integration_nodes import handle_sendgrid_email, handle_slack_message
from webhook_nodes import handle_webhook_trigger

node_dispatcher = {
    "Set": handle_set,
    "If": handle_if,
    "Merge": handle_merge,
    "MySQL": handle_mysql,
    "PostgreSQL": handle_postgresql,
    "MongoDB": handle_mongodb,
    "Cron": handle_cron,
    "Delay": handle_delay,
    "HTTP Basic Auth": handle_http_basic_auth,
    "OAuth2": handle_oauth2,
    "OpenAI": handle_openai_completion,
    "HuggingFace": handle_huggingface_transformer,
    "Read File": handle_read_file,
    "Write File": handle_write_file,
    "SendGrid": handle_sendgrid_email,
    "Slack": handle_slack_message,
    "Webhook": handle_webhook_trigger
}
