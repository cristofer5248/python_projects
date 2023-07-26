import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

NAMESPACE_CONNECTION_STR = "ROOT"
TOPIC_NAME = "churn_dev"


async def send_single_message(sender):
    # Create a Service Bus message
    message = ServiceBusMessage("{'hello':'hello'}")
    # send the message to the topic
    await sender.send_messages(message)
    print("Sent a single message")

async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        # Get a Topic Sender object to send messages to the topic
        sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
        async with sender:
            # Send one message
            await send_single_message(sender)
            # Send a list of messages
            #await send_a_list_of_messages(sender)
            # Send a batch of messages
            #await send_batch_message(sender)

asyncio.run(run())
print("Done sending messages")
print("-----------------------")