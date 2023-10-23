import time

import apigee.attachments
import constants


def get_attachments_list(auth_token: str, organization: str, instance: str):
    return apigee.attachments.get_attachment_list(
        auth_token=auth_token,
        organization=organization,
        instance=instance
    )


def get_attachment(auth_token: str, organization: str, instance: str, attachment: str):
    return apigee.attachments.get_attachment(
        auth_token=auth_token,
        organization=organization,
        instance=instance,
        attachment=attachment
    )


def create_attachment(auth_token: str, organization: str, instance: str, env: str):
    response = apigee.attachments.create_attachment(
        auth_token=auth_token,
        organization=organization,
        instance=instance,
        env=env)

    print(f"created object {response}")
    attachment_name = response.get("metadata").get("targetResourceName").split("attachments/", 1)[1]
    print(f"New attachment name found: {attachment_name}")

    is_created = False
    new_att = {}

    while not is_created:
        time.sleep(constants.RETRY_TIMEOUT)
        new_att = apigee.attachments.get_attachment(
            auth_token=auth_token,
            organization=organization,
            instance=instance,
            attachment=attachment_name
        )
        try:
            new_att.get("error").get("code") == 404
            print(f"Attachment not yet created. Waiting a little more to proceed..")
        except AttributeError:
            is_created = True

    print(f"env {env} with name {new_att.get('name')} attached SUCCESSFULLY")
    return new_att


def delete_attachment(auth_token: str, organization: str, instance: str, attachment: str):
    response = apigee.attachments.delete_attachment(
        auth_token=auth_token,
        organization=organization,
        instance=instance,
        attachment=attachment)

    time.sleep(constants.DELETE_ATTACHMENT_TIMEOUT)
    print(f"attachment {attachment} deleted SUCCESSFULLY")
    return response
