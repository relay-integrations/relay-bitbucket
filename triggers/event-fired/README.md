# bitbucket-trigger-event-fired

This trigger fires when an event from Bitbucket is received. 

The payload will be wrapped in an additional map called `event_payload` and
needs to be unwrapped at the step level in order to use it; see the example below.

For more details about the specific event payloads, check out the [documentation](https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/). 

## Setup Instructions

1. From Bitbucket, open the repository where you want to add the webhook.
2. Click the **Settings** link on the left side.
3. From the links on the **Settings** page, click the **Webhooks** link.
4. Click the **Add webhook** button to create a webhook for the repository. 
5. On the **Add new webhook**page, enter a **Title** with a short description.
6. Copy the **URL** from the Relay trigger 
7. Enter that URL into the **URL** field.
8. If necessary, update the **Triggers** field. By default, the trigger for the webhook is a repository push, as demonstrated by the **Repository push** field. If you want additional or different actions to trigger the webhook, click **Choose from a full list of triggers**. You will see a list of all the event types that can trigger the webhook.
10. After you entered all the necessary information for your webhook, click **Save**.

For more details about setting up webhooks, check out the [documentation](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/).

## Example Usage

```yaml
parameters:
  event_payload:
    description: "The full json payload from the incoming Bitbucket event"
triggers:
  - name: bitbucket-event
    source:
      type: webhook
      image: relaysh/bitbucket-trigger-event-fired
    binding:
      parameters:
        event_payload: !Data event_payload
steps:
  - name: dump-payload
    image: relaysh/core
    spec:
      event_payload: !Parameter event_payload
    input:
      - mkdir -p /bitbucket/workflow
      - "ni get | jq .event_payload > /bitbucket/workflow/event.json"
      - cat /bitbucket/workflow/event.json
```
