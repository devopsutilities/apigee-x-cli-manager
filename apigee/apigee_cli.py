from __future__ import annotations
import google_auth

from apigee import apigee_service, instances
import error_checker

import typer

app = typer.Typer()


@app.command()
def get_attachment_list(organization: str = typer.Option(..., "--organization", "-o", help="Apigee Organization")):
    """
    Get list of all Attachments of given Organization
    """
    error_checker.check_if_is_none(organization)
    auth_token = google_auth.get_auth_token()
    instance_name = instances.get_instance_name(auth_token=auth_token, organization=organization)
    attachment_list = apigee_service.get_attachments_list(auth_token=auth_token,
                                                          organization=organization,
                                                          instance=instance_name)

    return attachment_list


@app.command()
def get_attachment(organization: str = typer.Option(..., "--organization", "-o", help="Apigee Organization"),
                   attachment: str = typer.Option(..., "--attachment", "-a", help="Attachment unique name")):
    """
    Get info about a specified Attachment of a given Organization
    """
    error_checker.check_if_is_none(organization, attachment)
    auth_token = google_auth.get_auth_token()
    instance_name = instances.get_instance_name(auth_token=auth_token, organization=organization)
    attachment_found = apigee_service.get_attachment(auth_token=auth_token,
                                                     organization=organization,
                                                     instance=instance_name,
                                                     attachment=attachment)

    return attachment_found


@app.command()
def create_attachments(organization: str = typer.Option(..., "--organization", "-o", help="Apigee Organization"),
                       environments: list[str] = typer.Option(..., "--environment", "-e",
                                                              help="Apigee environments, can be a single element or a list")):
    """
    Receives a list of Environments in input and attaches all those environments to related environment group
    """

    error_checker.check_if_is_none(organization, environments)
    auth_token = google_auth.get_auth_token()
    instance_name = instances.get_instance_name(auth_token=auth_token, organization=organization)

    for environment in environments:
        apigee_service.create_attachment(auth_token=auth_token,
                                         organization=organization,
                                         instance=instance_name,
                                         env=environment)

    print(f"environments {environments} attached SUCCESSFULLY")
    return f"environments {environments} attached SUCCESSFULLY"


@app.command()
def delete_attachments(organization: str = typer.Option(..., "--organization", "-o", help="Apigee Organization"),
                       attachments: list[str] = typer.Option(..., "--attachment", "-a",
                                                             help="Apigee attachments, can be a single element or a list")):
    """
    Receives a list of Attachments of given organization to be detached (deleted)
    """
    error_checker.check_if_is_none(organization, attachments)
    auth_token = google_auth.get_auth_token()
    instance_name = instances.get_instance_name(auth_token=auth_token, organization=organization)

    for attachment in attachments:
        apigee_service.delete_attachment(auth_token=auth_token,
                                         organization=organization,
                                         instance=instance_name,
                                         attachment=attachment)

    print(f"attachments {attachments} deleted SUCCESSFULLY")
    return f"attachments {attachments} deleted SUCCESSFULLY"
